PREEMPTIVE_PROPERTY = "String  httpclient.authentication.preemptive""
PREEMPTIVE_DEFAULT = "String  false""
def HttpState():
'''public HttpState()
'''
pass
def addCookie():
'''public synchronized void addCookie(final Cookie cookie)
'''
pass
def addCookies():
'''public synchronized void addCookies(final Cookie[] cookies)
'''
pass
def getCookies():
'''public synchronized Cookie[] getCookies()
public synchronized Cookie[] getCookies(final String domain, final int port, final String path, final boolean secure)
'''
pass
def purgeExpiredCookies():
'''public synchronized boolean purgeExpiredCookies()
public synchronized boolean purgeExpiredCookies(final Date date)
'''
pass
def getCookiePolicy():
'''public int getCookiePolicy()
'''
pass
def setAuthenticationPreemptive():
'''public void setAuthenticationPreemptive(final boolean value)
'''
pass
def isAuthenticationPreemptive():
'''public boolean isAuthenticationPreemptive()
'''
pass
def setCookiePolicy():
'''public void setCookiePolicy(final int policy)
'''
pass
def setCredentials():
'''public synchronized void setCredentials(final String realm, final String host, final Credentials credentials)
public synchronized void setCredentials(final AuthScope authscope, final Credentials credentials)
'''
pass
def getCredentials():
'''public synchronized Credentials getCredentials(final String realm, final String host)
public synchronized Credentials getCredentials(final AuthScope authscope)
'''
pass
def setProxyCredentials():
'''public synchronized void setProxyCredentials(final String realm, final String proxyHost, final Credentials credentials)
public synchronized void setProxyCredentials(final AuthScope authscope, final Credentials credentials)
'''
pass
def getProxyCredentials():
'''public synchronized Credentials getProxyCredentials(final String realm, final String proxyHost)
public synchronized Credentials getProxyCredentials(final AuthScope authscope)
'''
pass
def toString():
'''public synchronized String toString()
'''
pass
def clearCredentials():
'''public void clearCredentials()
'''
pass
def clearProxyCredentials():
'''public void clearProxyCredentials()
'''
pass
def clearCookies():
'''public synchronized void clearCookies()
'''
pass
def clear():
'''public void clear()
'''
pass
