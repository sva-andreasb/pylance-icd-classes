DEFAULT_PORT = "int  110"
DISCONNECTED_STATE = "int  -1"
AUTHORIZATION_STATE = "int  0"
TRANSACTION_STATE = "int  1"
UPDATE_STATE = "int  2"
def POP3():
    '''    public POP3()
    '''
def addProtocolCommandListener():
    '''    public void addProtocolCommandListener(final ProtocolCommandListener listener)
    '''
def removeProtocolCommandistener():
    '''    public void removeProtocolCommandistener(final ProtocolCommandListener listener)
    '''
def setState():
    '''    public void setState(final int state)
    '''
def getState():
    '''    public int getState()
    '''
def getAdditionalReply():
    '''    public void getAdditionalReply()
    '''
def disconnect():
    '''    public void disconnect()
    '''
def sendCommand():
    '''    public int sendCommand(final String command, final String args)
    public int sendCommand(final String command)
    public int sendCommand(final int command, final String args)
    public int sendCommand(final int command)
    '''
def getReplyStrings():
    '''    public String[] getReplyStrings()
    '''
def getReplyString():
    '''    public String getReplyString()
    '''
