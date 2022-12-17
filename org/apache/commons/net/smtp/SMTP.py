DEFAULT_PORT = "int  25"
def ():
    '''returns SMTP\n\n
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
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def sendCommand():
    '''returns int\n\n
    sendCommand(final String command, final String args)\n
    sendCommand(final int command, final String args)\n
    sendCommand(final String command)\n
    sendCommand(final int command)\n
    '''
def getReplyCode():
    '''returns int\n\n
    getReplyCode()\n
    '''
def getReply():
    '''returns int\n\n
    getReply()\n
    '''
def getReplyStrings():
    '''returns String[]\n\n
    getReplyStrings()\n
    '''
def getReplyString():
    '''returns String\n\n
    getReplyString()\n
    '''
def helo():
    '''returns int\n\n
    helo(final String hostname)\n
    '''
def mail():
    '''returns int\n\n
    mail(final String reversePath)\n
    '''
def rcpt():
    '''returns int\n\n
    rcpt(final String forwardPath)\n
    '''
def data():
    '''returns int\n\n
    data()\n
    '''
def send():
    '''returns int\n\n
    send(final String reversePath)\n
    '''
def soml():
    '''returns int\n\n
    soml(final String reversePath)\n
    '''
def saml():
    '''returns int\n\n
    saml(final String reversePath)\n
    '''
def rset():
    '''returns int\n\n
    rset()\n
    '''
def vrfy():
    '''returns int\n\n
    vrfy(final String user)\n
    '''
def expn():
    '''returns int\n\n
    expn(final String name)\n
    '''
def help():
    '''returns int\n\n
    help()\n
    help(final String command)\n
    '''
def noop():
    '''returns int\n\n
    noop()\n
    '''
def turn():
    '''returns int\n\n
    turn()\n
    '''
def quit():
    '''returns int\n\n
    quit()\n
    '''
