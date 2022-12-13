DEFAULT_PORT = "int  25"
def SMTP():
'''public SMTP()
'''
pass
def addProtocolCommandListener():
'''public void addProtocolCommandListener(final ProtocolCommandListener listener)
'''
pass
def removeProtocolCommandistener():
'''public void removeProtocolCommandistener(final ProtocolCommandListener listener)
'''
pass
def disconnect():
'''public void disconnect()
'''
pass
def sendCommand():
'''public int sendCommand(final String command, final String args)
public int sendCommand(final int command, final String args)
public int sendCommand(final String command)
public int sendCommand(final int command)
'''
pass
def getReplyCode():
'''public int getReplyCode()
'''
pass
def getReply():
'''public int getReply()
'''
pass
def getReplyStrings():
'''public String[] getReplyStrings()
'''
pass
def getReplyString():
'''public String getReplyString()
'''
pass
def helo():
'''public int helo(final String hostname)
'''
pass
def mail():
'''public int mail(final String reversePath)
'''
pass
def rcpt():
'''public int rcpt(final String forwardPath)
'''
pass
def data():
'''public int data()
'''
pass
def send():
'''public int send(final String reversePath)
'''
pass
def soml():
'''public int soml(final String reversePath)
'''
pass
def saml():
'''public int saml(final String reversePath)
'''
pass
def rset():
'''public int rset()
'''
pass
def vrfy():
'''public int vrfy(final String user)
'''
pass
def expn():
'''public int expn(final String name)
'''
pass
def help():
'''public int help()
public int help(final String command)
'''
pass
def noop():
'''public int noop()
'''
pass
def turn():
'''public int turn()
'''
pass
def quit():
'''public int quit()
'''
pass
