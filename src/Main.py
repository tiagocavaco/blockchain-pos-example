# To be installed:
# set CL=-FI"C:\Program Files (x86)\Microsoft Visual Studio\2019\Enterprise\VC\Tools\MSVC\14.29.30133\include\stdint.h"
# pycrypto: pip install pycrypto
# p2pnetwork: pip install p2pnetwork
# jsonpickle: pip install jsonpickle
# Flask: pip install Flask
# Flask-Classful: pip install Flask-Classful


from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
from Blockchain import Blockchain
from BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
import pprint
from Node import Node
import sys

if __name__ == '__main__':
    
    ip = sys.argv[1]
    port = int(sys.argv[2])
    apiPort = int(sys.argv[3])
    keyFile = None
    if len(sys.argv) > 4:
        keyFile = sys.argv[4]
    
    print(keyFile)
    
    node = Node(ip, port, keyFile)
    node.startP2P()
    node.startAPI(apiPort)
    
    # if port == 10002:
    #     node.p2p.connect_with_node('localhost', 10001)
    
    # blockchain = Blockchain()
    # pool = TransactionPool()
    
    # alice = Wallet()
    # bob = Wallet()
    # exchange = Wallet()
    # forger = Wallet()
    
    # exchangeTransaction = exchange.createTransaction(alice.publicKeyString(), 10, 'EXCHANGE')
    
    # if not pool.transactionExists(exchangeTransaction):
    #     pool.addTransaction(exchangeTransaction)
        
    # coveredTransactions = blockchain.getConveredTransactionSet(pool.transactions)
    # lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    # blockCount = blockchain.blocks[-1].blockCount + 1
    # blockOne = forger.createBlock(coveredTransactions, lastHash, blockCount)
    # blockchain.addBlock(blockOne)
    # pool.removeFromPool(blockOne.transactions)
    
    # transaction = alice.createTransaction(bob.publicKeyString(), 5, 'TRANSFER')
    
    # if not pool.transactionExists(transaction):
    #     pool.addTransaction(transaction)
        
    # coveredTransactions = blockchain.getConveredTransactionSet(pool.transactions)
    # lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    # blockCount = blockchain.blocks[-1].blockCount + 1
    # blockTwo = forger.createBlock(coveredTransactions, lastHash, blockCount)
    # blockchain.addBlock(blockTwo)
    # pool.removeFromPool(blockTwo.transactions)
    
    # pprint.pprint(blockchain.toJson())
    
    # wallet = Wallet()
    # accountModel = AccountModel()
    
    # accountModel.updateBalance(wallet.publicKeyString(), 10)
    # accountModel.updateBalance(wallet.publicKeyString(), -5)

    # print(accountModel.balances)
    
    # sender = 'sender'
    # receiver = 'receiver'
    # amount = 1
    # type = 'TRANSFER'
    
    # wallet = Wallet()
    # fraudlendWallet = Wallet()
    # pool = TransactionPool()
    
    # transaction = wallet.createTransaction(receiver, amount, type)
    
    # if pool.transactionExists(transaction) == False:
    #     pool.addTransaction(transaction)

    # blockchain = Blockchain()
    
    # lastHash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
    # blockCount = blockchain.blocks[-1].blockCount + 1
    # block = wallet.createBlock(pool.transactions, lastHash, blockCount)

    # if not blockchain.lastBlockHashValid(block):
    #     print('lastBlockHash is not valid')
        
    # if not blockchain.blockCountValid(block):
    #     print('blockCount is not valid')

    # if blockchain.lastBlockHashValid(block) and blockchain.blockCountValid(block):
    #     blockchain.addBlock(block)

    # pprint.pprint(blockchain.toJson())
    # pprint.pprint(blockchain.toJson())
    
    # signatureValid = Wallet.signatureValid(block.payload(), block.signature, wallet.publicKeyString())
    # pprint.pprint(signatureValid)

    
    

    