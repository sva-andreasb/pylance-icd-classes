def ApiSessionImpl():
'''public ApiSessionImpl()
'''
pass
def getSession():
'''public static ApiSession getSession(final ApiConnection conn, final String user, final String password, final long version)
public static ApiSession getSession(final ApiConnection conn, final long sessionId, final long version)
public static ApiSession getSession(final ApiConnection conn, final Principal p, final long version)
'''
pass
def init():
'''public void init(final long version, final ApiConnection conn, final long sessionId)
public void init(final long version, final ApiConnection conn, final String user, final String password)
public void init(final long version, final ApiConnection conn, final Principal p)
'''
pass
def copy():
'''public ApiSession copy(final long version)
'''
pass
def close():
'''public void close()
'''
pass
def release():
'''public void release()
'''
pass
def closeAll():
'''public static void closeAll()
'''
pass
def getSessionId():
'''public String getSessionId()
'''
pass
def getConnection():
'''public ApiConnection getConnection()
'''
pass
def setSessionTimeout():
'''public void setSessionTimeout(final int seconds)
'''
pass
def getSessionTimeout():
'''public int getSessionTimeout()
'''
pass
def createDataApi():
'''public DataApi createDataApi()
'''
pass
def createPresentationApi():
'''public PresentationApi createPresentationApi()
'''
pass
def createCMDBApi():
'''public CMDBApi createCMDBApi()
'''
pass
def createControlApi():
'''public ControlApi createControlApi()
'''
pass
def createNamingApi():
'''public NamingUtilityApi createNamingApi()
'''
pass
def createCompatibilityApi():
'''public CompatibilityApi createCompatibilityApi()
'''
pass
def createEDM():
'''public EDMInterface createEDM()
'''
pass
def createAuthorizationManagerApi():
'''public AuthorizationManagerApi createAuthorizationManagerApi()
'''
pass
def getVersion():
'''public long getVersion()
'''
pass
def toString():
'''public String toString()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
def getUser():
'''public String getUser()
'''
pass
def getPrincipal():
'''public ApiPrincipal getPrincipal()
'''
pass
def getFingerPrint():
'''public long getFingerPrint()
'''
pass
def setLocale():
'''public void setLocale(final Locale locale)
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def setApiServer():
'''public void setApiServer(final Object apiServer)
'''
pass
def getApiServer():
'''public Object getApiServer()
'''
pass
