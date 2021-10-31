def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
	yourMin = -1
	yourMax = 21
	if yourLeft < yourRight:
		yourMin = yourLeft
		yourMax = yourRight
	else:
		yourMin = yourRight
		yourMax = yourLeft
	friendsMin = -1
	friendsMax = 21
	if friendsLeft < friendsRight:
		friendsMin = friendsLeft
		friendsMax = friendsRight
	else:
		friendsMin = friendsRight
		friendsMax = friendsLeft
	if (yourMin == friendsMin and yourMax == friendsMax) or (yourMin == friendsMax and yourMax == friendsMin):
		return True
	else:
		return False
