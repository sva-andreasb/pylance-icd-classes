TADDM = "int  1"
OAL = "int  2"
def ApiFactory():
'''public ApiFactory(final int type)
'''
pass
def getInstance():
'''public static synchronized ApiFactory getInstance()
'''
pass
def getApiConnection():
'''public ApiConnection getApiConnection(final String host, final int port, final String trustStoreLocation, final boolean useSSL)
public ApiConnection getApiConnection()
'''
pass
def getSession():
'''public ApiSession getSession(final ApiConnection conn, final String user, final String password, final long version)
public ApiSession getSession(final ApiConnection conn, final long sessionId, final long version)
public ApiSession getSession(final ApiConnection conn, final Principal p, final long version)
'''
pass
def postProcess():
'''public void postProcess()
'''
pass