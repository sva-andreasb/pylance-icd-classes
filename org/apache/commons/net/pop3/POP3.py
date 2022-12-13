DEFAULT_PORT = "int  110"
DISCONNECTED_STATE = "int  -1"
AUTHORIZATION_STATE = "int  0"
TRANSACTION_STATE = "int  1"
UPDATE_STATE = "int  2"
def POP3():
'''public POP3()
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
def setState():
'''public void setState(final int state)
'''
pass
def getState():
'''public int getState()
'''
pass
def getAdditionalReply():
'''public void getAdditionalReply()
'''
pass
def disconnect():
'''public void disconnect()
'''
pass
def sendCommand():
'''public int sendCommand(final String command, final String args)
public int sendCommand(final String command)
public int sendCommand(final int command, final String args)
public int sendCommand(final int command)
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
