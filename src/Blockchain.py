from Block import Block
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from ProofOfStake import ProofOfStake

class Blockchain():
    
    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountModel = AccountModel()
        self.pos = ProofOfStake()
        
    def addBlock(self, block):
        self.executeTransactions(block.transactions)
        self.blocks.append(block)
        
    def toJson(self):
        data = {}
        jsonBlocks = []
        for block in self.blocks:
            jsonBlocks.append(block.toJson())
        data['blocks'] = jsonBlocks
        return data
    
    def blockCountValid(self, block):
        return self.blocks[-1].blockCount == block.blockCount -1
        
    def lastBlockHashValid(self, block):
        latestBlockchainBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        return latestBlockchainBlockHash == block.lastHash
    
    def getConveredTransactionSet(self, transactions):
        coveredTransactions = []
        for transaction in transactions:
            if self.transactionCovered(transaction):
                coveredTransactions.append(transaction)
            else:
                print(f'Transaction {transaction.id} is not covered by sender')
        return coveredTransactions
    
    def transactionCovered(self, transaction):   
        senderBalance = self.accountModel.getBalance(transaction.senderPublicKey)
        return transaction.type == 'EXCHANGE' or senderBalance >= transaction.amount
    
    def executeTransactions(self, transactions):
        for transaction in transactions:
            self.executeTransaction(transaction)
    
    def executeTransaction(self, transaction):
        if transaction.type == 'STAKE':
            sender = transaction.senderPublicKey
            receiver = transaction.receiverPublicKey
            if sender == receiver:
                amount = transaction.amount
                self.pos.update(sender, amount)
                self.accountModel.updateBalance(sender, -amount)
        else:
            sender = transaction.senderPublicKey
            receiver = transaction.receiverPublicKey
            amount = transaction.amount
            self.accountModel.updateBalance(sender, -amount)
            self.accountModel.updateBalance(receiver, amount)
        
    def nextForger(self):
        lastBlockHash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        nextForger = self.pos.forger(lastBlockHash)
        return nextForger
    
    def createBlock(self, transactionFromPool, forgerWallet):
        converedTransactions = self.getConveredTransactionSet(transactionFromPool)
        self.executeTransactions(converedTransactions)
        newBlock = forgerWallet.createBlock(converedTransactions, BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest(), len(self.blocks))
        self.blocks.append(newBlock)
        return newBlock

    def transactionExists(self, transaction):
        for block in self.blocks:
            for blockTransaction in block.transactions:
                if transaction.equals(blockTransaction):
                    return True
        return False                                                                                                                 
        
    def forgerValid(self, block):
        forgerPublicKey = self.pos.forger(block.lastHash)
        proposedBlockForger = block.forger
        return forgerPublicKey == proposedBlockForger
    
    def transactionsValid(self, transactions):
        coveredTransactions = self.getConveredTransactionSet(transactions)
        return len(coveredTransactions) == len(transactions)
            
    