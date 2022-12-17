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
    '''returns byte[]\n\n
    getData()\n
    '''
def getReason():
    '''returns int\n\n
    getReason()\n
    '''
def getDestroyData():
    '''returns byte[]\n\n
    getDestroyData()\n
    '''
def getMessageType():
    '''returns short\n\n
    getMessageType()\n
    '''
def isEncrypted():
    '''returns boolean\n\n
    isEncrypted()\n
    '''
def getChannel():
    '''returns Channel\n\n
    getChannel()\n
    '''
def getPriority():
    '''returns byte\n\n
    getPriority()\n
    '''
def getCreator():
    '''returns STUserInstance\n\n
    getCreator()\n
    '''
def getAccpetor():
    '''returns STUserInstance\n\n
    getAccpetor()\n
    '''
def getToUser():
    '''returns STUser\n\n
    getToUser()\n
    '''
