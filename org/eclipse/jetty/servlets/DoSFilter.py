def DoSFilter():
'''public DoSFilter()
'''
pass
def init():
'''public void init(final FilterConfig filterConfig)
'''
pass
def onComplete():
'''public void onComplete(final Continuation continuation)
'''
pass
def onTimeout():
'''public void onTimeout(final Continuation continuation)
'''
pass
def run():
'''public void run()
'''
pass
def doFilter():
'''public void doFilter(final ServletRequest request, final ServletResponse response, final FilterChain filterchain)
'''
pass
def expired():
'''public void expired()
public void expired()
'''
pass
def getRateTracker():
'''public RateTracker getRateTracker(final ServletRequest request)
'''
pass
def destroy():
'''public void destroy()
'''
pass
def getMaxRequestsPerSec():
'''public int getMaxRequestsPerSec()
'''
pass
def setMaxRequestsPerSec():
'''public void setMaxRequestsPerSec(final int value)
'''
pass
def getDelayMs():
'''public long getDelayMs()
'''
pass
def setDelayMs():
'''public void setDelayMs(final long value)
'''
pass
def getMaxWaitMs():
'''public long getMaxWaitMs()
'''
pass
def setMaxWaitMs():
'''public void setMaxWaitMs(final long value)
'''
pass
def getThrottledRequests():
'''public int getThrottledRequests()
'''
pass
def setThrottledRequests():
'''public void setThrottledRequests(final int value)
'''
pass
def getThrottleMs():
'''public long getThrottleMs()
'''
pass
def setThrottleMs():
'''public void setThrottleMs(final long value)
'''
pass
def getMaxRequestMs():
'''public long getMaxRequestMs()
'''
pass
def setMaxRequestMs():
'''public void setMaxRequestMs(final long value)
'''
pass
def getMaxIdleTrackerMs():
'''public long getMaxIdleTrackerMs()
'''
pass
def setMaxIdleTrackerMs():
'''public void setMaxIdleTrackerMs(final long value)
'''
pass
def isInsertHeaders():
'''public boolean isInsertHeaders()
'''
pass
def setInsertHeaders():
'''public void setInsertHeaders(final boolean value)
'''
pass
def isTrackSessions():
'''public boolean isTrackSessions()
'''
pass
def setTrackSessions():
'''public void setTrackSessions(final boolean value)
'''
pass
def isRemotePort():
'''public boolean isRemotePort()
'''
pass
def setRemotePort():
'''public void setRemotePort(final boolean value)
'''
pass
def getWhitelist():
'''public String getWhitelist()
'''
pass
def setWhitelist():
'''public void setWhitelist(final String value)
'''
pass
def RateTracker():
'''public RateTracker(final String id, final int type, final int maxRequestsPerSecond)
'''
pass
def isRateExceeded():
'''public boolean isRateExceeded(final long now)
public boolean isRateExceeded(final long now)
'''
pass
def getId():
'''public String getId()
'''
pass
def getType():
'''public int getType()
'''
pass
def valueBound():
'''public void valueBound(final HttpSessionBindingEvent event)
'''
pass
def valueUnbound():
'''public void valueUnbound(final HttpSessionBindingEvent event)
'''
pass
def sessionWillPassivate():
'''public void sessionWillPassivate(final HttpSessionEvent se)
'''
pass
def sessionDidActivate():
'''public void sessionDidActivate(final HttpSessionEvent se)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def FixedRateTracker():
'''public FixedRateTracker(final String id, final int type, final int numRecentRequestsTracked)
'''
pass
