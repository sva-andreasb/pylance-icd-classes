DEFAULT_PORT = "int  25"
def SMTP():
    '''    public SMTP()
    '''
def addProtocolCommandListener():
    '''    public void addProtocolCommandListener(final ProtocolCommandListener listener)
    '''
def removeProtocolCommandistener():
    '''    public void removeProtocolCommandistener(final ProtocolCommandListener listener)
    '''
def disconnect():
    '''    public void disconnect()
    '''
def sendCommand():
    '''    public int sendCommand(final String command, final String args)
    public int sendCommand(final int command, final String args)
    public int sendCommand(final String command)
    public int sendCommand(final int command)
    '''
def getReplyCode():
    '''    public int getReplyCode()
    '''
def getReply():
    '''    public int getReply()
    '''
def getReplyStrings():
    '''    public String[] getReplyStrings()
    '''
def getReplyString():
    '''    public String getReplyString()
    '''
def helo():
    '''    public int helo(final String hostname)
    '''
def mail():
    '''    public int mail(final String reversePath)
    '''
def rcpt():
    '''    public int rcpt(final String forwardPath)
    '''
def data():
    '''    public int data()
    '''
def send():
    '''    public int send(final String reversePath)
    '''
def soml():
    '''    public int soml(final String reversePath)
    '''
def saml():
    '''    public int saml(final String reversePath)
    '''
def rset():
    '''    public int rset()
    '''
def vrfy():
    '''    public int vrfy(final String user)
    '''
def expn():
    '''    public int expn(final String name)
    '''
def help():
    '''    public int help()
    public int help(final String command)
    '''
def noop():
    '''    public int noop()
    '''
def turn():
    '''    public int turn()
    '''
def quit():
    '''    public int quit()
    '''
