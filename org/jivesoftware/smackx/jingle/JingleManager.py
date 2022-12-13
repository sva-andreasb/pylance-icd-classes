def getThreadPool():
    '''public static ExecutorService getThreadPool()
    '''
def getInstanceFor():
    '''public static synchronized JingleManager getInstanceFor(final XMPPConnection connection)
    '''
def handleIQRequest():
    '''public IQ handleIQRequest(final IQ iqRequest)
    '''
def registerDescriptionHandler():
    '''public JingleHandler registerDescriptionHandler(final String namespace, final JingleHandler handler)
    '''
def registerJingleSessionHandler():
    '''public JingleSessionHandler registerJingleSessionHandler(final FullJid otherJid, final String sessionId, final JingleSessionHandler sessionHandler)
    '''
def unregisterJingleSessionHandler():
    '''public JingleSessionHandler unregisterJingleSessionHandler(final FullJid otherJid, final String sessionId, final JingleSessionHandler sessionHandler)
    '''
def randomId():
    '''public static String randomId()
    '''
