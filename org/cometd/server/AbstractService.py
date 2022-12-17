def ():
    '''returns AbstractService\n\n
    (final BayeuxServer bayeux, final String name)\n
    (final BayeuxServer bayeux, final String name, final int maxThreads)\n
    '''
def getBayeux():
    '''returns BayeuxServer\n\n
    getBayeux()\n
    '''
def getLocalSession():
    '''returns LocalSession\n\n
    getLocalSession()\n
    '''
def getServerSession():
    '''returns ServerSession\n\n
    getServerSession()\n
    '''
def getThreadPool():
    '''returns ThreadPool\n\n
    getThreadPool()\n
    '''
def setThreadPool():
    '''returns None\n\n
    setThreadPool(final ThreadPool pool)\n
    '''
def isSeeOwnPublishes():
    '''returns boolean\n\n
    isSeeOwnPublishes()\n
    '''
def setSeeOwnPublishes():
    '''returns None\n\n
    setSeeOwnPublishes(final boolean own)\n
    '''
def onMessage():
    '''returns boolean\n\n
    onMessage(final ServerSession from, final ServerChannel channel, final ServerMessage.Mutable message)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
