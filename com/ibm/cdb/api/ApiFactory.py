TADDM = "int  1"
OAL = "int  2"
def ():
    '''returns ApiFactory\n\n
    (final int type)\n
    '''
def getApiConnection():
    '''returns ApiConnection\n\n
    getApiConnection(final String host, final int port, final String trustStoreLocation, final boolean useSSL)\n
    getApiConnection()\n
    '''
def getSession():
    '''returns ApiSession\n\n
    getSession(final ApiConnection conn, final String user, final String password, final long version)\n
    getSession(final ApiConnection conn, final long sessionId, final long version)\n
    getSession(final ApiConnection conn, final Principal p, final long version)\n
    '''
def postProcess():
    '''returns None\n\n
    postProcess()\n
    '''
