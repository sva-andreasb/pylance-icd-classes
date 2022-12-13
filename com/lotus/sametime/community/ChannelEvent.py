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
def getReason():
    '''public int getReason()
    '''
def getDestroyData():
    '''public byte[] getDestroyData()
    '''
def getMessageType():
    '''public short getMessageType()
    '''
def isEncrypted():
    '''public boolean isEncrypted()
    '''
def getChannel():
    '''public Channel getChannel()
    '''
def getPriority():
    '''public byte getPriority()
    '''
def getCreator():
    '''public STUserInstance getCreator()
    '''
def getAccpetor():
    '''public STUserInstance getAccpetor()
    '''
def getToUser():
    '''public STUser getToUser()
    '''
