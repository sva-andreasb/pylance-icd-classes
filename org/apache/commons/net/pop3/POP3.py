DEFAULT_PORT = "int  110"
DISCONNECTED_STATE = "int  -1"
AUTHORIZATION_STATE = "int  0"
TRANSACTION_STATE = "int  1"
UPDATE_STATE = "int  2"
def ():
    '''returns POP3\n\n
    ()\n
    '''
def addProtocolCommandListener():
    '''returns None\n\n
    addProtocolCommandListener(final ProtocolCommandListener listener)\n
    '''
def removeProtocolCommandistener():
    '''returns None\n\n
    removeProtocolCommandistener(final ProtocolCommandListener listener)\n
    '''
def setState():
    '''returns None\n\n
    setState(final int state)\n
    '''
def getState():
    '''returns int\n\n
    getState()\n
    '''
def getAdditionalReply():
    '''returns None\n\n
    getAdditionalReply()\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def sendCommand():
    '''returns int\n\n
    sendCommand(final String command, final String args)\n
    sendCommand(final String command)\n
    sendCommand(final int command, final String args)\n
    sendCommand(final int command)\n
    '''
def getReplyStrings():
    '''returns String[]\n\n
    getReplyStrings()\n
    '''
def getReplyString():
    '''returns String\n\n
    getReplyString()\n
    '''
