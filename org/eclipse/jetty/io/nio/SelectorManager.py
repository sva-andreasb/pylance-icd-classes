def ():
    '''returns ChannelAndAttachment\n\n
    ()\n
    (final SelectableChannel channel, final Object attachment)\n
    '''
def setMaxIdleTime():
    '''returns None\n\n
    setMaxIdleTime(final long maxIdleTime)\n
    '''
def setSelectSets():
    '''returns None\n\n
    setSelectSets(final int selectSets)\n
    '''
def getMaxIdleTime():
    '''returns long\n\n
    getMaxIdleTime()\n
    '''
def getSelectSets():
    '''returns int\n\n
    getSelectSets()\n
    '''
def getSelectSet():
    '''returns SelectSet\n\n
    getSelectSet(final int i)\n
    '''
def register():
    '''returns None\n\n
    register(final SocketChannel channel, final Object att)\n
    register(final SocketChannel channel)\n
    register(final ServerSocketChannel acceptChannel)\n
    '''
def getSelectorPriorityDelta():
    '''returns int\n\n
    getSelectorPriorityDelta()\n
    '''
def setSelectorPriorityDelta():
    '''returns None\n\n
    setSelectorPriorityDelta(final int delta)\n
    '''
def getLowResourcesConnections():
    '''returns long\n\n
    getLowResourcesConnections()\n
    '''
def setLowResourcesConnections():
    '''returns None\n\n
    setLowResourcesConnections(final long lowResourcesConnections)\n
    '''
def getLowResourcesMaxIdleTime():
    '''returns long\n\n
    getLowResourcesMaxIdleTime()\n
    '''
def setLowResourcesMaxIdleTime():
    '''returns None\n\n
    setLowResourcesMaxIdleTime(final long lowResourcesMaxIdleTime)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def dump():
    '''returns None\n\n
    dump()\n
    dump(final Appendable out, final String indent)\n
    dump()\n
    dump(final Appendable out, final String indent)\n
    '''
def isDeferringInterestedOps0():
    '''returns boolean\n\n
    isDeferringInterestedOps0()\n
    '''
def setDeferringInterestedOps0():
    '''returns None\n\n
    setDeferringInterestedOps0(final boolean deferringInterestedOps0)\n
    '''
def addChange():
    '''returns None\n\n
    addChange(final Object change)\n
    addChange(final SelectableChannel channel, final Object att)\n
    '''
def doSelect():
    '''returns None\n\n
    doSelect()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getManager():
    '''returns SelectorManager\n\n
    getManager()\n
    '''
def getNow():
    '''returns long\n\n
    getNow()\n
    '''
def scheduleTimeout():
    '''returns None\n\n
    scheduleTimeout(final Timeout.Task task, final long timeoutMs)\n
    '''
def cancelTimeout():
    '''returns None\n\n
    cancelTimeout(final Timeout.Task task)\n
    '''
def wakeup():
    '''returns None\n\n
    wakeup()\n
    '''
def destroyEndPoint():
    '''returns None\n\n
    destroyEndPoint(final SelectChannelEndPoint endp)\n
    '''
def dumpKeyState():
    '''returns None\n\n
    dumpKeyState(final List<Object> dumpto)\n
    '''
