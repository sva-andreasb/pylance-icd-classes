NAMESPACE = "String  \"urn:xmpp:bob\""
def getInstanceFor():
    '''public static synchronized BoBManager getInstanceFor(final XMPPConnection connection)
    '''
def handleIQRequest():
    '''public IQ handleIQRequest(final IQ iqRequest)
    '''
def isSupportedByServer():
    '''public boolean isSupportedByServer()
    '''
def requestBoB():
    '''public BoBData requestBoB(final Jid to, final BoBHash bobHash)
    '''
def addBoB():
    '''public BoBInfo addBoB(final BoBData bobData)
    '''
def removeBoB():
    '''public BoBInfo removeBoB(final BoBHash bobHash)
    '''
def connectionCreated():
    '''public void connectionCreated(final XMPPConnection connection)
    '''
