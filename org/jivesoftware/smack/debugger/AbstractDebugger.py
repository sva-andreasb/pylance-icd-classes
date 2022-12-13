def AbstractDebugger():
'''public AbstractDebugger(final XMPPConnection connection)
'''
pass
def read():
'''public void read(final String str)
'''
pass
def write():
'''public void write(final String str)
'''
pass
def connected():
'''public void connected(final XMPPConnection connection)
'''
pass
def authenticated():
'''public void authenticated(final XMPPConnection connection, final boolean resumed)
'''
pass
def connectionClosed():
'''public void connectionClosed()
'''
pass
def connectionClosedOnError():
'''public void connectionClosedOnError(final Exception e)
'''
pass
def reconnectionFailed():
'''public void reconnectionFailed(final Exception e)
'''
pass
def reconnectingIn():
'''public void reconnectingIn(final int seconds)
'''
pass
def newConnectionReader():
'''public Reader newConnectionReader(final Reader newReader)
'''
pass
def newConnectionWriter():
'''public Writer newConnectionWriter(final Writer newWriter)
'''
pass
def userHasLogged():
'''public void userHasLogged(final EntityFullJid user)
'''
pass
def onIncomingStreamElement():
'''public void onIncomingStreamElement(final TopLevelStreamElement streamElement)
'''
pass
def onOutgoingStreamElement():
'''public void onOutgoingStreamElement(final TopLevelStreamElement streamElement)
'''
pass
