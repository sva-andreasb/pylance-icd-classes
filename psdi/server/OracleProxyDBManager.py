MODEUSERNAME = "int  1"
MODEUSERNAMEPASSWORD = "int  2"
MODEDN = "int  3"
MODECERTIFICATE = "int  4"
ORADBPROXYMODE = "String  \"ORADBPROXYMODE\""
def OracleProxyDBManager():
    '''    public OracleProxyDBManager()
    '''
def configure():
    '''    public void configure(final Properties properties)
    '''
def init():
    '''    public boolean init()
    '''
def destroy():
    '''    public synchronized void destroy()
    '''
def getConnectionDetail():
    '''    public Connection getConnectionDetail(final ConnectionKey conKey)
    '''
def freeConnectionDetail():
    '''    public void freeConnectionDetail(final ConnectionKey conKey)
    '''
def getSystemConnection():
    '''    public synchronized Connection getSystemConnection()
    '''
def getSequenceConnection():
    '''    public synchronized Connection getSequenceConnection()
    '''
def getNewConnectionPool():
    '''    public OracleOCIConnectionPool getNewConnectionPool(final String url, final String userName, final String password)
    '''
def getProxyConnection():
    '''    public ConRef getProxyConnection(final OracleOCIConnectionPool pool, final Object certi)
    '''
def getDBAuthenticationType():
    '''    public int getDBAuthenticationType()
    '''
def getCredentialHandler():
    '''    public DBCredentialHandler getCredentialHandler()
    '''
def run():
    '''    public void run()
    public void run()
    '''
def getRetryConnectionPool():
    '''    public OracleOCIConnectionPool getRetryConnectionPool()
    '''
