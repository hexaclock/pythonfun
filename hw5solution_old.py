import turtle

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
        return True
