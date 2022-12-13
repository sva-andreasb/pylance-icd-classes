def DoSFilter():
    '''public DoSFilter()
    '''
def init():
    '''public void init(final FilterConfig filterConfig)
    '''
def onComplete():
    '''public void onComplete(final Continuation continuation)
    '''
def onTimeout():
    '''public void onTimeout(final Continuation continuation)
    '''
def run():
    '''public void run()
    '''
def doFilter():
    '''public void doFilter(final ServletRequest request, final ServletResponse response, final FilterChain filterchain)
    '''
def expired():
    '''public void expired()
    public void expired()
    '''
def getRateTracker():
    '''public RateTracker getRateTracker(final ServletRequest request)
    '''
def destroy():
    '''public void destroy()
    '''
def getMaxRequestsPerSec():
    '''public int getMaxRequestsPerSec()
    '''
def setMaxRequestsPerSec():
    '''public void setMaxRequestsPerSec(final int value)
    '''
def getDelayMs():
    '''public long getDelayMs()
    '''
def setDelayMs():
    '''public void setDelayMs(final long value)
    '''
def getMaxWaitMs():
    '''public long getMaxWaitMs()
    '''
def setMaxWaitMs():
    '''public void setMaxWaitMs(final long value)
    '''
def getThrottledRequests():
    '''public int getThrottledRequests()
    '''
def setThrottledRequests():
    '''public void setThrottledRequests(final int value)
    '''
def getThrottleMs():
    '''public long getThrottleMs()
    '''
def setThrottleMs():
    '''public void setThrottleMs(final long value)
    '''
def getMaxRequestMs():
    '''public long getMaxRequestMs()
    '''
def setMaxRequestMs():
    '''public void setMaxRequestMs(final long value)
    '''
def getMaxIdleTrackerMs():
    '''public long getMaxIdleTrackerMs()
    '''
def setMaxIdleTrackerMs():
    '''public void setMaxIdleTrackerMs(final long value)
    '''
def isInsertHeaders():
    '''public boolean isInsertHeaders()
    '''
def setInsertHeaders():
    '''public void setInsertHeaders(final boolean value)
    '''
def isTrackSessions():
    '''public boolean isTrackSessions()
    '''
def setTrackSessions():
    '''public void setTrackSessions(final boolean value)
    '''
def isRemotePort():
    '''public boolean isRemotePort()
    '''
def setRemotePort():
    '''public void setRemotePort(final boolean value)
    '''
def getWhitelist():
    '''public String getWhitelist()
    '''
def setWhitelist():
    '''public void setWhitelist(final String value)
    '''
def RateTracker():
    '''public RateTracker(final String id, final int type, final int maxRequestsPerSecond)
    '''
def isRateExceeded():
    '''public boolean isRateExceeded(final long now)
    public boolean isRateExceeded(final long now)
    '''
def getId():
    '''public String getId()
    '''
def getType():
    '''public int getType()
    '''
def valueBound():
    '''public void valueBound(final HttpSessionBindingEvent event)
    '''
def valueUnbound():
    '''public void valueUnbound(final HttpSessionBindingEvent event)
    '''
def sessionWillPassivate():
    '''public void sessionWillPassivate(final HttpSessionEvent se)
    '''
def sessionDidActivate():
    '''public void sessionDidActivate(final HttpSessionEvent se)
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def FixedRateTracker():
    '''public FixedRateTracker(final String id, final int type, final int numRecentRequestsTracked)
    '''
