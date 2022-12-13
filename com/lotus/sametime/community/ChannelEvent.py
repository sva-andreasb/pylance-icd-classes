CREATE_CHANNEL = "int  1"
DESTROY_CHANNEL = "int  2"
SEND_ON_CHANNEL = "int  3"
ACCEPT_CHANNEL = "int  4"
SEND_ON_MULTI_CHANNEL = "int  5"
CHANNEL_CREATED = "int  -2147483647"
CHANNEL_ACCEPTED = "int  -2147483646"
CHANNEL_DESTROYED = "int  -2147483645"
CHANNEL_SENT = "int  -2147483644"
MULTI_CHANNEL_SENT = "int  -2147483643"
def getData():
'''public byte[] getData()
'''
pass
def getReason():
'''public int getReason()
'''
pass
def getDestroyData():
'''public byte[] getDestroyData()
'''
pass
def getMessageType():
'''public short getMessageType()
'''
pass
def isEncrypted():
'''public boolean isEncrypted()
'''
pass
def getChannel():
'''public Channel getChannel()
'''
pass
def getPriority():
'''public byte getPriority()
'''
pass
def getCreator():
'''public STUserInstance getCreator()
'''
pass
def getAccpetor():
'''public STUserInstance getAccpetor()
'''
pass
def getToUser():
'''public STUser getToUser()
'''
pass
