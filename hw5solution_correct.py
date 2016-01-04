import turtle

memo={}

def svTree(trunkLength, levels):
        if (levels <= 1):
            return
        else:
            turtle.forward(trunkLength)
            turtle.right(45)
            svTree(trunkLength/2,levels-1)
            turtle.left(90)
            svTree(trunkLength/2,levels-1)
            turtle.right(45)
            turtle.forward(-1*trunkLength)
            return

def fastFib(N):
        if N==0 or N==1:
                return N
        elif memo.has_key(N):
                return memo[N]
        else:
                fibber = (fastFib(N-1) + fastFib(N-2))
                memo[N] = fibber
                return fibber
