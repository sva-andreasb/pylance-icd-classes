def AbstractService():
'''public AbstractService(final BayeuxServer bayeux, final String name)
public AbstractService(final BayeuxServer bayeux, final String name, final int maxThreads)
'''
pass
def getBayeux():
'''public BayeuxServer getBayeux()
'''
pass
def getLocalSession():
'''public LocalSession getLocalSession()
'''
pass
def getServerSession():
'''public ServerSession getServerSession()
'''
pass
def getThreadPool():
'''public ThreadPool getThreadPool()
'''
pass
def setThreadPool():
'''public void setThreadPool(final ThreadPool pool)
'''
pass
def isSeeOwnPublishes():
'''public boolean isSeeOwnPublishes()
'''
pass
def setSeeOwnPublishes():
'''public void setSeeOwnPublishes(final boolean own)
'''
pass
def onMessage():
'''public boolean onMessage(final ServerSession from, final ServerChannel channel, final ServerMessage.Mutable message)
'''
pass
def run():
'''public void run()
'''
pass
