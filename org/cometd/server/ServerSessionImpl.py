def getUserAgent():
    '''returns String\n\n
    getUserAgent()\n
    '''
def setUserAgent():
    '''returns None\n\n
    setUserAgent(final String userAgent)\n
    '''
def getSubscriptions():
    '''returns Set<ServerChannel>\n\n
    getSubscriptions()\n
    '''
def addExtension():
    '''returns None\n\n
    addExtension(final ServerSession.Extension extension)\n
    '''
def removeExtension():
    '''returns None\n\n
    removeExtension(final ServerSession.Extension extension)\n
    '''
def batch():
    '''returns None\n\n
    batch(final Runnable batch)\n
    '''
def deliver():
    '''returns None\n\n
    deliver(final Session from, final ServerMessage.Mutable message)\n
    deliver(final Session from, final String channelId, final Object data, final String id)\n
    '''
def expired():
    '''returns None\n\n
    expired()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def endBatch():
    '''returns boolean\n\n
    endBatch()\n
    '''
def getLocalSession():
    '''returns LocalSession\n\n
    getLocalSession()\n
    '''
def isLocalSession():
    '''returns boolean\n\n
    isLocalSession()\n
    '''
def startBatch():
    '''returns None\n\n
    startBatch()\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final ServerSession.ServerSessionListener listener)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getLock():
    '''returns Object\n\n
    getLock()\n
    '''
def getQueue():
    '''returns Queue<ServerMessage>\n\n
    getQueue()\n
    '''
def isQueueEmpty():
    '''returns boolean\n\n
    isQueueEmpty()\n
    '''
def replaceQueue():
    '''returns None\n\n
    replaceQueue(final List<ServerMessage> queue)\n
    '''
def takeQueue():
    '''returns List<ServerMessage>\n\n
    takeQueue()\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final ServerSession.ServerSessionListener listener)\n
    '''
def setScheduler():
    '''returns None\n\n
    setScheduler(final AbstractServerTransport.Scheduler newScheduler)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def flushLazy():
    '''returns None\n\n
    flushLazy()\n
    '''
def cancelSchedule():
    '''returns None\n\n
    cancelSchedule()\n
    '''
def cancelIntervalTimeout():
    '''returns None\n\n
    cancelIntervalTimeout()\n
    '''
def startIntervalTimeout():
    '''returns None\n\n
    startIntervalTimeout(final long defaultInterval)\n
    '''
def getAttribute():
    '''returns Object\n\n
    getAttribute(final String name)\n
    '''
def getAttributeNames():
    '''returns Set<String>\n\n
    getAttributeNames()\n
    '''
def removeAttribute():
    '''returns Object\n\n
    removeAttribute(final String name)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final String name, final Object value)\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def isHandshook():
    '''returns boolean\n\n
    isHandshook()\n
    '''
def reAdvise():
    '''returns None\n\n
    reAdvise()\n
    '''
def getTimeout():
    '''returns long\n\n
    getTimeout()\n
    '''
def getInterval():
    '''returns long\n\n
    getInterval()\n
    '''
def setTimeout():
    '''returns None\n\n
    setTimeout(final long timeoutMS)\n
    '''
def setInterval():
    '''returns None\n\n
    setInterval(final long intervalMS)\n
    '''
def setMetaConnectDeliveryOnly():
    '''returns None\n\n
    setMetaConnectDeliveryOnly(final boolean meta)\n
    '''
def isMetaConnectDeliveryOnly():
    '''returns boolean\n\n
    isMetaConnectDeliveryOnly()\n
    '''
def calculateTimeout():
    '''returns long\n\n
    calculateTimeout(final long defaultTimeout)\n
    '''
def calculateInterval():
    '''returns long\n\n
    calculateInterval(final long defaultInterval)\n
    '''
def updateTransientTimeout():
    '''returns None\n\n
    updateTransientTimeout(final long timeout)\n
    '''
def updateTransientInterval():
    '''returns None\n\n
    updateTransientInterval(final long interval)\n
    '''
