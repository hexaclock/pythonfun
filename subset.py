def subset(target,list):
	if (list == []):
		return []
	elif (list[0] - target > 0):
		return subset(target-list[0],list[1:])
	elif (list[0] - target < 0):
		return subset(list[1:])
	elif (list[0] - target == 0):
		return True
	return False