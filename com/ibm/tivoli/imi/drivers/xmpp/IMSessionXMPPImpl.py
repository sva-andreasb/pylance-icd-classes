def IMSessionXMPPImpl():
    '''    public IMSessionXMPPImpl()
    '''
def configure():
    '''    public void configure(final Properties properties)
    '''
def getServerHostName():
    '''    public String getServerHostName()
    '''
def getServerPort():
    '''    public int getServerPort()
    '''
def getServiceName():
    '''    public String getServiceName()
    '''
def getSessionName():
    '''    public String getSessionName()
    '''
def getUserId():
    '''    public String getUserId()
    '''
def getUserPassword():
    '''    public String getUserPassword()
    '''
def getIMUser():
    '''    public IMUser getIMUser()
    '''
def open():
    '''    public void open()
    '''
def changeUserStatus():
    '''    public void changeUserStatus(final IMUser.IMUserStatus imUserStatus)
    '''
def close():
    '''    public void close()
    '''
def isOpened():
    '''    public boolean isOpened()
    '''
def createResolveHandler():
    '''    public IMResolveHandler createResolveHandler(final boolean b, final boolean b2)
    '''
def createUserStatusHandler():
    '''    public IMUserStatusHandler createUserStatusHandler()
    '''
def createMessageHandler():
    '''    public IMMessageHandler createMessageHandler(final IMUser imUser)
    '''
def resolve():
    '''    public IMResolveEvent resolve(final String s, final boolean b, final boolean b2)
    public IMUser resolve(final String s)
    '''
def getDefaultConnectionTimeout():
    '''    public long getDefaultConnectionTimeout()
    '''
def setConnectionTimeout():
    '''    public void setConnectionTimeout(final long connectionTimeout)
    '''
def getConnectionTimeout():
    '''    public long getConnectionTimeout()
    '''
def getDefaultResolveTimeout():
    '''    public long getDefaultResolveTimeout()
    '''
def setResolveTimeout():
    '''    public synchronized void setResolveTimeout(final long resolveTimeout)
    '''
def getResolveTimeout():
    '''    public synchronized long getResolveTimeout()
    '''
def registerIMSingleListener():
    '''    public void registerIMSingleListener(final IMSingleListener imSingleListener)
    '''
def removeIMSingleListener():
    '''    public void removeIMSingleListener(final IMSingleListener imSingleListener)
    '''
def removeMessageHandlerList():
    '''    public void removeMessageHandlerList(final String anObject)
    '''
def run():
    '''    public void run()
    '''
