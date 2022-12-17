def ():
    '''returns FixedRateTracker\n\n
    ()\n
    (final String id, final int type, final int maxRequestsPerSecond)\n
    (final String id, final int type, final int numRecentRequestsTracked)\n
    '''
def init():
    '''returns None\n\n
    init(final FilterConfig filterConfig)\n
    '''
def onComplete():
    '''returns None\n\n
    onComplete(final Continuation continuation)\n
    '''
def onTimeout():
    '''returns None\n\n
    onTimeout(final Continuation continuation)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def doFilter():
    '''returns None\n\n
    doFilter(final ServletRequest request, final ServletResponse response, final FilterChain filterchain)\n
    '''
def expired():
    '''returns None\n\n
    expired()\n
    expired()\n
    '''
def getRateTracker():
    '''returns RateTracker\n\n
    getRateTracker(final ServletRequest request)\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def getMaxRequestsPerSec():
    '''returns int\n\n
    getMaxRequestsPerSec()\n
    '''
def setMaxRequestsPerSec():
    '''returns None\n\n
    setMaxRequestsPerSec(final int value)\n
    '''
def getDelayMs():
    '''returns long\n\n
    getDelayMs()\n
    '''
def setDelayMs():
    '''returns None\n\n
    setDelayMs(final long value)\n
    '''
def getMaxWaitMs():
    '''returns long\n\n
    getMaxWaitMs()\n
    '''
def setMaxWaitMs():
    '''returns None\n\n
    setMaxWaitMs(final long value)\n
    '''
def getThrottledRequests():
    '''returns int\n\n
    getThrottledRequests()\n
    '''
def setThrottledRequests():
    '''returns None\n\n
    setThrottledRequests(final int value)\n
    '''
def getThrottleMs():
    '''returns long\n\n
    getThrottleMs()\n
    '''
def setThrottleMs():
    '''returns None\n\n
    setThrottleMs(final long value)\n
    '''
def getMaxRequestMs():
    '''returns long\n\n
    getMaxRequestMs()\n
    '''
def setMaxRequestMs():
    '''returns None\n\n
    setMaxRequestMs(final long value)\n
    '''
def getMaxIdleTrackerMs():
    '''returns long\n\n
    getMaxIdleTrackerMs()\n
    '''
def setMaxIdleTrackerMs():
    '''returns None\n\n
    setMaxIdleTrackerMs(final long value)\n
    '''
def isInsertHeaders():
    '''returns boolean\n\n
    isInsertHeaders()\n
    '''
def setInsertHeaders():
    '''returns None\n\n
    setInsertHeaders(final boolean value)\n
    '''
def isTrackSessions():
    '''returns boolean\n\n
    isTrackSessions()\n
    '''
def setTrackSessions():
    '''returns None\n\n
    setTrackSessions(final boolean value)\n
    '''
def isRemotePort():
    '''returns boolean\n\n
    isRemotePort()\n
    '''
def setRemotePort():
    '''returns None\n\n
    setRemotePort(final boolean value)\n
    '''
def getWhitelist():
    '''returns String\n\n
    getWhitelist()\n
    '''
def setWhitelist():
    '''returns None\n\n
    setWhitelist(final String value)\n
    '''
def isRateExceeded():
    '''returns boolean\n\n
    isRateExceeded(final long now)\n
    isRateExceeded(final long now)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def valueBound():
    '''returns None\n\n
    valueBound(final HttpSessionBindingEvent event)\n
    '''
def valueUnbound():
    '''returns None\n\n
    valueUnbound(final HttpSessionBindingEvent event)\n
    '''
def sessionWillPassivate():
    '''returns None\n\n
    sessionWillPassivate(final HttpSessionEvent se)\n
    '''
def sessionDidActivate():
    '''returns None\n\n
    sessionDidActivate(final HttpSessionEvent se)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
