CONNECTION_MANAGER_TIMEOUT = "String  http.connection-manager.timeout""
CONNECTION_MANAGER_CLASS = "String  http.connection-manager.class""
PREEMPTIVE_AUTHENTICATION = "String  http.authentication.preemptive""
REJECT_RELATIVE_REDIRECT = "String  http.protocol.reject-relative-redirect""
MAX_REDIRECTS = "String  http.protocol.max-redirects""
ALLOW_CIRCULAR_REDIRECTS = "String  http.protocol.allow-circular-redirects""
def HttpClientParams():
'''public HttpClientParams()
public HttpClientParams(final HttpParams defaults)
'''
pass
def getConnectionManagerTimeout():
'''public long getConnectionManagerTimeout()
'''
pass
def setConnectionManagerTimeout():
'''public void setConnectionManagerTimeout(final long timeout)
'''
pass
def getConnectionManagerClass():
'''public Class getConnectionManagerClass()
'''
pass
def setConnectionManagerClass():
'''public void setConnectionManagerClass(final Class clazz)
'''
pass
def isAuthenticationPreemptive():
'''public boolean isAuthenticationPreemptive()
'''
pass
def setAuthenticationPreemptive():
'''public void setAuthenticationPreemptive(final boolean value)
'''
pass
def makeStrict():
'''public void makeStrict()
'''
pass
def makeLenient():
'''public void makeLenient()
'''
pass
