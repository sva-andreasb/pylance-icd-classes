def ():
    '''returns HealthMonitorManagerImpl\n\n
    ()\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final Object config)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def stop():
    '''returns None\n\n
    stop()\n
    '''
def addMonitoringEndPoints():
    '''returns None\n\n
    addMonitoringEndPoints(final CFEndPoint[] cfEPs, final EndPoint[] eps, final long timeout)\n
    '''
def removeMonitoringEndPoints():
    '''returns None\n\n
    removeMonitoringEndPoints(final CFEndPoint[] cfEPs, final EndPoint[] eps)\n
    '''
def startMonitorEndPoints():
    '''returns None\n\n
    startMonitorEndPoints(final ChannelTargetImpl channelTarget, final CFEndPointCriteria criteria, final long timeout)\n
    '''
def stopMonitorEndPoints():
    '''returns None\n\n
    stopMonitorEndPoints(final ChannelTargetImpl channelTarget, final CFEndPointCriteria criteria)\n
    '''
def startMonitor():
    '''returns None\n\n
    startMonitor(final ChannelTarget channelTarget)\n
    startMonitor(final Identity clusterIdentity, final CFEndPointCriteria cfEndPointCriteria)\n
    startMonitor(final Identity memberIdentity)\n
    startMonitor(final ChannelTarget channelTarget, long timeout)\n
    startMonitor(final Identity clusterIdentity, final CFEndPointCriteria cfEndPointCriteria, long timeout)\n
    startMonitor(final Identity memberIdentity, long timeout)\n
    '''
def stopMonitor():
    '''returns None\n\n
    stopMonitor(final ChannelTarget channelTarget)\n
    stopMonitor(final Identity clusterIdentity, final CFEndPointCriteria cfEndPointCriteria)\n
    stopMonitor(final Identity memberIdentity)\n
    '''
def registerMonitorAdvisor():
    '''returns None\n\n
    registerMonitorAdvisor(final Class monitorAdvisor)\n
    '''
def deregisterMonitorAdvisor():
    '''returns None\n\n
    deregisterMonitorAdvisor(final Class monitorAdvisor)\n
    '''
def getRegisteredMonitorAdvisors():
    '''returns Class[]\n\n
    getRegisteredMonitorAdvisors()\n
    '''
def getActiveMonitorAdvisorsSize():
    '''returns int\n\n
    getActiveMonitorAdvisorsSize()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def getEndPoint():
    '''returns EndPoint\n\n
    getEndPoint()\n
    '''
def getCFEndPoint():
    '''returns CFEndPoint\n\n
    getCFEndPoint()\n
    '''
def getTestCount():
    '''returns int\n\n
    getTestCount()\n
    '''
def getTimeout():
    '''returns long\n\n
    getTimeout()\n
    '''
def getLastAdvice():
    '''returns int\n\n
    getLastAdvice()\n
    '''
def getStateChangedTimeStamp():
    '''returns long\n\n
    getStateChangedTimeStamp()\n
    '''
def getLastAccessedTimeStamp():
    '''returns long\n\n
    getLastAccessedTimeStamp()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object cmd)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
