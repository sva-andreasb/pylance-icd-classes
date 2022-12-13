def getUserAgent():
'''public String getUserAgent()
'''
pass
def setUserAgent():
'''public void setUserAgent(final String userAgent)
'''
pass
def getSubscriptions():
'''public Set<ServerChannel> getSubscriptions()
'''
pass
def addExtension():
'''public void addExtension(final ServerSession.Extension extension)
'''
pass
def removeExtension():
'''public void removeExtension(final ServerSession.Extension extension)
'''
pass
def batch():
'''public void batch(final Runnable batch)
'''
pass
def deliver():
'''public void deliver(final Session from, final ServerMessage.Mutable message)
public void deliver(final Session from, final String channelId, final Object data, final String id)
'''
pass
def expired():
'''public void expired()
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def disconnect():
'''public void disconnect()
'''
pass
def endBatch():
'''public boolean endBatch()
'''
pass
def getLocalSession():
'''public LocalSession getLocalSession()
'''
pass
def isLocalSession():
'''public boolean isLocalSession()
'''
pass
def startBatch():
'''public void startBatch()
'''
pass
def addListener():
'''public void addListener(final ServerSession.ServerSessionListener listener)
'''
pass
def getId():
'''public String getId()
'''
pass
def getLock():
'''public Object getLock()
'''
pass
def getQueue():
'''public Queue<ServerMessage> getQueue()
'''
pass
def isQueueEmpty():
'''public boolean isQueueEmpty()
'''
pass
def replaceQueue():
'''public void replaceQueue(final List<ServerMessage> queue)
'''
pass
def takeQueue():
'''public List<ServerMessage> takeQueue()
'''
pass
def removeListener():
'''public void removeListener(final ServerSession.ServerSessionListener listener)
'''
pass
def setScheduler():
'''public void setScheduler(final AbstractServerTransport.Scheduler newScheduler)
'''
pass
def flush():
'''public void flush()
'''
pass
def flushLazy():
'''public void flushLazy()
'''
pass
def cancelSchedule():
'''public void cancelSchedule()
'''
pass
def cancelIntervalTimeout():
'''public void cancelIntervalTimeout()
'''
pass
def startIntervalTimeout():
'''public void startIntervalTimeout(final long defaultInterval)
'''
pass
def getAttribute():
'''public Object getAttribute(final String name)
'''
pass
def getAttributeNames():
'''public Set<String> getAttributeNames()
'''
pass
def removeAttribute():
'''public Object removeAttribute(final String name)
'''
pass
def setAttribute():
'''public void setAttribute(final String name, final Object value)
'''
pass
def isConnected():
'''public boolean isConnected()
'''
pass
def isHandshook():
'''public boolean isHandshook()
'''
pass
def reAdvise():
'''public void reAdvise()
'''
pass
def takeAdvice():
'''public Map<String, Object> takeAdvice()
'''
pass
def getTimeout():
'''public long getTimeout()
'''
pass
def getInterval():
'''public long getInterval()
'''
pass
def setTimeout():
'''public void setTimeout(final long timeoutMS)
'''
pass
def setInterval():
'''public void setInterval(final long intervalMS)
'''
pass
def setMetaConnectDeliveryOnly():
'''public void setMetaConnectDeliveryOnly(final boolean meta)
'''
pass
def isMetaConnectDeliveryOnly():
'''public boolean isMetaConnectDeliveryOnly()
'''
pass
def calculateTimeout():
'''public long calculateTimeout(final long defaultTimeout)
'''
pass
def calculateInterval():
'''public long calculateInterval(final long defaultInterval)
'''
pass
def updateTransientTimeout():
'''public void updateTransientTimeout(final long timeout)
'''
pass
def updateTransientInterval():
'''public void updateTransientInterval(final long interval)
'''
pass
