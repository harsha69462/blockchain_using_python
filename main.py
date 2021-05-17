from chain import Chain

chain = Chain(20)

i = 0

while(True):
    data = input("Add to chain: ")
    chain.pool_add(data)
    chain.mine()
    print(chain.blocks[i])
    i += 1
