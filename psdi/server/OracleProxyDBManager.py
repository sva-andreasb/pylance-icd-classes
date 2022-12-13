MODEUSERNAME = "int  1"
MODEUSERNAMEPASSWORD = "int  2"
MODEDN = "int  3"
MODECERTIFICATE = "int  4"
ORADBPROXYMODE = "String  ORADBPROXYMODE""
def OracleProxyDBManager():
'''public OracleProxyDBManager()
'''
pass
def configure():
'''public void configure(final Properties properties)
'''
pass
def init():
'''public boolean init()
'''
pass
def destroy():
'''public synchronized void destroy()
'''
pass
def getConnectionDetail():
'''public Connection getConnectionDetail(final ConnectionKey conKey)
'''
pass
def freeConnectionDetail():
'''public void freeConnectionDetail(final ConnectionKey conKey)
'''
pass
def getSystemConnection():
'''public synchronized Connection getSystemConnection()
'''
pass
def getSequenceConnection():
'''public synchronized Connection getSequenceConnection()
'''
pass
def getNewConnectionPool():
'''public OracleOCIConnectionPool getNewConnectionPool(final String url, final String userName, final String password)
'''
pass
def getProxyConnection():
'''public ConRef getProxyConnection(final OracleOCIConnectionPool pool, final Object certi)
'''
pass
def getDBAuthenticationType():
'''public int getDBAuthenticationType()
'''
pass
def getCredentialHandler():
'''public DBCredentialHandler getCredentialHandler()
'''
pass
def run():
'''public void run()
public void run()
'''
pass
def getRetryConnectionPool():
'''public OracleOCIConnectionPool getRetryConnectionPool()
'''
pass
