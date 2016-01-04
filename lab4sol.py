def giveChange(amount,coins):
	if (coins==[]):
		return float("inf")
	else:
		if (amount-coins[0] > 0):
			useIt = 1 + giveChange(amount-coins[0],coins)
			loseIt = giveChange(amount,coins[1:])
			return min(useIt,loseIt)
		elif (amount-coins[0] < 0):
			return giveChange(amount,coins[1:])
		elif (amount-coins[0] == 0):
			return 1
		else:
			return float("inf")