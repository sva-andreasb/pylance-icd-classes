CONNECTION_MANAGER_TIMEOUT = "String  \"http.connection-manager.timeout\""
CONNECTION_MANAGER_CLASS = "String  \"http.connection-manager.class\""
PREEMPTIVE_AUTHENTICATION = "String  \"http.authentication.preemptive\""
REJECT_RELATIVE_REDIRECT = "String  \"http.protocol.reject-relative-redirect\""
MAX_REDIRECTS = "String  \"http.protocol.max-redirects\""
ALLOW_CIRCULAR_REDIRECTS = "String  \"http.protocol.allow-circular-redirects\""
def ():
    '''returns HttpClientParams\n\n
    ()\n
    (final HttpParams defaults)\n
    '''
def getConnectionManagerTimeout():
    '''returns long\n\n
    getConnectionManagerTimeout()\n
    '''
def setConnectionManagerTimeout():
    '''returns None\n\n
    setConnectionManagerTimeout(final long timeout)\n
    '''
def getConnectionManagerClass():
    '''returns Class\n\n
    getConnectionManagerClass()\n
    '''
def setConnectionManagerClass():
    '''returns None\n\n
    setConnectionManagerClass(final Class clazz)\n
    '''
def isAuthenticationPreemptive():
    '''returns boolean\n\n
    isAuthenticationPreemptive()\n
    '''
def setAuthenticationPreemptive():
    '''returns None\n\n
    setAuthenticationPreemptive(final boolean value)\n
    '''
def makeStrict():
    '''returns None\n\n
    makeStrict()\n
    '''
def makeLenient():
    '''returns None\n\n
    makeLenient()\n
    '''
