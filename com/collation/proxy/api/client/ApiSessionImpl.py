def ApiSessionImpl():
    '''public ApiSessionImpl()
    '''
def getSession():
    '''public static ApiSession getSession(final ApiConnection conn, final String user, final String password, final long version)
    public static ApiSession getSession(final ApiConnection conn, final long sessionId, final long version)
    public static ApiSession getSession(final ApiConnection conn, final Principal p, final long version)
    '''
def init():
    '''public void init(final long version, final ApiConnection conn, final long sessionId)
    public void init(final long version, final ApiConnection conn, final String user, final String password)
    public void init(final long version, final ApiConnection conn, final Principal p)
    '''
def copy():
    '''public ApiSession copy(final long version)
    '''
def close():
    '''public void close()
    '''
def release():
    '''public void release()
    '''
def closeAll():
    '''public static void closeAll()
    '''
def getSessionId():
    '''public String getSessionId()
    '''
def getConnection():
    '''public ApiConnection getConnection()
    '''
def setSessionTimeout():
    '''public void setSessionTimeout(final int seconds)
    '''
def getSessionTimeout():
    '''public int getSessionTimeout()
    '''
def createDataApi():
    '''public DataApi createDataApi()
    '''
def createPresentationApi():
    '''public PresentationApi createPresentationApi()
    '''
def createCMDBApi():
    '''public CMDBApi createCMDBApi()
    '''
def createControlApi():
    '''public ControlApi createControlApi()
    '''
def createNamingApi():
    '''public NamingUtilityApi createNamingApi()
    '''
def createCompatibilityApi():
    '''public CompatibilityApi createCompatibilityApi()
    '''
def createEDM():
    '''public EDMInterface createEDM()
    '''
def createAuthorizationManagerApi():
    '''public AuthorizationManagerApi createAuthorizationManagerApi()
    '''
def getVersion():
    '''public long getVersion()
    '''
def toString():
    '''public String toString()
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object obj)
    '''
def getUser():
    '''public String getUser()
    '''
def getPrincipal():
    '''public ApiPrincipal getPrincipal()
    '''
def getFingerPrint():
    '''public long getFingerPrint()
    '''
def setLocale():
    '''public void setLocale(final Locale locale)
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def setApiServer():
    '''public void setApiServer(final Object apiServer)
    '''
def getApiServer():
    '''public Object getApiServer()
    '''
