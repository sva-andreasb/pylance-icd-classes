PREEMPTIVE_PROPERTY = "String  \"httpclient.authentication.preemptive\""
PREEMPTIVE_DEFAULT = "String  \"false\""
def HttpState():
    '''public HttpState()
    '''
def addCookie():
    '''public synchronized void addCookie(final Cookie cookie)
    '''
def addCookies():
    '''public synchronized void addCookies(final Cookie[] cookies)
    '''
def getCookies():
    '''public synchronized Cookie[] getCookies()
    public synchronized Cookie[] getCookies(final String domain, final int port, final String path, final boolean secure)
    '''
def purgeExpiredCookies():
    '''public synchronized boolean purgeExpiredCookies()
    public synchronized boolean purgeExpiredCookies(final Date date)
    '''
def getCookiePolicy():
    '''public int getCookiePolicy()
    '''
def setAuthenticationPreemptive():
    '''public void setAuthenticationPreemptive(final boolean value)
    '''
def isAuthenticationPreemptive():
    '''public boolean isAuthenticationPreemptive()
    '''
def setCookiePolicy():
    '''public void setCookiePolicy(final int policy)
    '''
def setCredentials():
    '''public synchronized void setCredentials(final String realm, final String host, final Credentials credentials)
    public synchronized void setCredentials(final AuthScope authscope, final Credentials credentials)
    '''
def getCredentials():
    '''public synchronized Credentials getCredentials(final String realm, final String host)
    public synchronized Credentials getCredentials(final AuthScope authscope)
    '''
def setProxyCredentials():
    '''public synchronized void setProxyCredentials(final String realm, final String proxyHost, final Credentials credentials)
    public synchronized void setProxyCredentials(final AuthScope authscope, final Credentials credentials)
    '''
def getProxyCredentials():
    '''public synchronized Credentials getProxyCredentials(final String realm, final String proxyHost)
    public synchronized Credentials getProxyCredentials(final AuthScope authscope)
    '''
def toString():
    '''public synchronized String toString()
    '''
def clearCredentials():
    '''public void clearCredentials()
    '''
def clearProxyCredentials():
    '''public void clearProxyCredentials()
    '''
def clearCookies():
    '''public synchronized void clearCookies()
    '''
def clear():
    '''public void clear()
    '''
