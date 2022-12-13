def getUserAgent():
    '''    public String getUserAgent()
    '''
def setUserAgent():
    '''    public void setUserAgent(final String userAgent)
    '''
def getSubscriptions():
    '''    public Set<ServerChannel> getSubscriptions()
    '''
def addExtension():
    '''    public void addExtension(final ServerSession.Extension extension)
    '''
def removeExtension():
    '''    public void removeExtension(final ServerSession.Extension extension)
    '''
def batch():
    '''    public void batch(final Runnable batch)
    '''
def deliver():
    '''    public void deliver(final Session from, final ServerMessage.Mutable message)
    public void deliver(final Session from, final String channelId, final Object data, final String id)
    '''
def expired():
    '''    public void expired()
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def disconnect():
    '''    public void disconnect()
    '''
def endBatch():
    '''    public boolean endBatch()
    '''
def getLocalSession():
    '''    public LocalSession getLocalSession()
    '''
def isLocalSession():
    '''    public boolean isLocalSession()
    '''
def startBatch():
    '''    public void startBatch()
    '''
def addListener():
    '''    public void addListener(final ServerSession.ServerSessionListener listener)
    '''
def getId():
    '''    public String getId()
    '''
def getLock():
    '''    public Object getLock()
    '''
def getQueue():
    '''    public Queue<ServerMessage> getQueue()
    '''
def isQueueEmpty():
    '''    public boolean isQueueEmpty()
    '''
def replaceQueue():
    '''    public void replaceQueue(final List<ServerMessage> queue)
    '''
def takeQueue():
    '''    public List<ServerMessage> takeQueue()
    '''
def removeListener():
    '''    public void removeListener(final ServerSession.ServerSessionListener listener)
    '''
def setScheduler():
    '''    public void setScheduler(final AbstractServerTransport.Scheduler newScheduler)
    '''
def flush():
    '''    public void flush()
    '''
def flushLazy():
    '''    public void flushLazy()
    '''
def cancelSchedule():
    '''    public void cancelSchedule()
    '''
def cancelIntervalTimeout():
    '''    public void cancelIntervalTimeout()
    '''
def startIntervalTimeout():
    '''    public void startIntervalTimeout(final long defaultInterval)
    '''
def getAttribute():
    '''    public Object getAttribute(final String name)
    '''
def getAttributeNames():
    '''    public Set<String> getAttributeNames()
    '''
def removeAttribute():
    '''    public Object removeAttribute(final String name)
    '''
def setAttribute():
    '''    public void setAttribute(final String name, final Object value)
    '''
def isConnected():
    '''    public boolean isConnected()
    '''
def isHandshook():
    '''    public boolean isHandshook()
    '''
def reAdvise():
    '''    public void reAdvise()
    '''
def takeAdvice():
    '''    public Map<String, Object> takeAdvice()
    '''
def getTimeout():
    '''    public long getTimeout()
    '''
def getInterval():
    '''    public long getInterval()
    '''
def setTimeout():
    '''    public void setTimeout(final long timeoutMS)
    '''
def setInterval():
    '''    public void setInterval(final long intervalMS)
    '''
def setMetaConnectDeliveryOnly():
    '''    public void setMetaConnectDeliveryOnly(final boolean meta)
    '''
def isMetaConnectDeliveryOnly():
    '''    public boolean isMetaConnectDeliveryOnly()
    '''
def calculateTimeout():
    '''    public long calculateTimeout(final long defaultTimeout)
    '''
def calculateInterval():
    '''    public long calculateInterval(final long defaultInterval)
    '''
def updateTransientTimeout():
    '''    public void updateTransientTimeout(final long timeout)
    '''
def updateTransientInterval():
    '''    public void updateTransientInterval(final long interval)
    '''
