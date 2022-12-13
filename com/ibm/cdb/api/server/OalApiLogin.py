def OalApiLogin():
    '''    public OalApiLogin()
    public OalApiLogin(final String user, final String pass, final ApiPrincipal pr, final String clientIp, final long verison)
    '''
def init():
    '''    public void init(final long sess, final long version)
    public void init(final ApiPrincipal pr, final String user, final String pass, final String clientIp, final long verison)
    '''
def checkSessionId():
    '''    public ApiLoginInterface checkSessionId(final String sessionId)
    '''
def getTopoMgr():
    '''    public TopologyManager getTopoMgr(final TopologyManagerFactory tmf)
    public TopologyManager getTopoMgr()
    '''
def getSessionId():
    '''    public long getSessionId()
    '''
def getSession():
    '''    public SessionContext getSession()
    '''
def getUser():
    '''    public String getUser()
    '''
def logout():
    '''    public void logout()
    '''
def checkPermission():
    '''    public SessionContext checkPermission(final int type)
    '''
def ping():
    '''    public static boolean ping()
    '''
def getTxTimer():
    '''    public Timer getTxTimer()
    '''
def setTxTimer():
    '''    public void setTxTimer(final Timer t)
    '''
def getVersion():
    '''    public long getVersion()
    '''
