import random
#Setting random seed for reproducibility of code
random.seed(4)


Russell2000 = 2000
Ftse100 = 100


def stockSelection(index):
    
    stockCount = []

    while len(stockCount)<6:
        
        stock = random.randint(1,index)
        stockCount.append(stock)

    print(stockCount)

    return stockCount


stockSelection(Russell2000)
stockSelection(Ftse100)