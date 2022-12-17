MODEUSERNAME = "int  1"
MODEUSERNAMEPASSWORD = "int  2"
MODEDN = "int  3"
MODECERTIFICATE = "int  4"
ORADBPROXYMODE = "String  \"ORADBPROXYMODE\""
def ():
    '''returns OracleProxyDBManager\n\n
    ()\n
    '''
def configure():
    '''returns None\n\n
    configure(final Properties properties)\n
    '''
def init():
    '''returns boolean\n\n
    init()\n
    '''
def getConnectionDetail():
    '''returns Connection\n\n
    getConnectionDetail(final ConnectionKey conKey)\n
    '''
def freeConnectionDetail():
    '''returns None\n\n
    freeConnectionDetail(final ConnectionKey conKey)\n
    '''
def getNewConnectionPool():
    '''returns OracleOCIConnectionPool\n\n
    getNewConnectionPool(final String url, final String userName, final String password)\n
    '''
def getProxyConnection():
    '''returns ConRef\n\n
    getProxyConnection(final OracleOCIConnectionPool pool, final Object certi)\n
    '''
def getDBAuthenticationType():
    '''returns int\n\n
    getDBAuthenticationType()\n
    '''
def getCredentialHandler():
    '''returns DBCredentialHandler\n\n
    getCredentialHandler()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    '''
def getRetryConnectionPool():
    '''returns OracleOCIConnectionPool\n\n
    getRetryConnectionPool()\n
    '''
