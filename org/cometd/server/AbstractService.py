def AbstractService():
    '''public AbstractService(final BayeuxServer bayeux, final String name)
    public AbstractService(final BayeuxServer bayeux, final String name, final int maxThreads)
    '''
def getBayeux():
    '''public BayeuxServer getBayeux()
    '''
def getLocalSession():
    '''public LocalSession getLocalSession()
    '''
def getServerSession():
    '''public ServerSession getServerSession()
    '''
def getThreadPool():
    '''public ThreadPool getThreadPool()
    '''
def setThreadPool():
    '''public void setThreadPool(final ThreadPool pool)
    '''
def isSeeOwnPublishes():
    '''public boolean isSeeOwnPublishes()
    '''
def setSeeOwnPublishes():
    '''public void setSeeOwnPublishes(final boolean own)
    '''
def onMessage():
    '''public boolean onMessage(final ServerSession from, final ServerChannel channel, final ServerMessage.Mutable message)
    '''
def run():
    '''public void run()
    '''
