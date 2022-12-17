def ():
    '''returns OalApiLogin\n\n
    ()\n
    (final String user, final String pass, final ApiPrincipal pr, final String clientIp, final long verison)\n
    '''
def init():
    '''returns None\n\n
    init(final long sess, final long version)\n
    init(final ApiPrincipal pr, final String user, final String pass, final String clientIp, final long verison)\n
    '''
def checkSessionId():
    '''returns ApiLoginInterface\n\n
    checkSessionId(final String sessionId)\n
    '''
def getTopoMgr():
    '''returns TopologyManager\n\n
    getTopoMgr(final TopologyManagerFactory tmf)\n
    getTopoMgr()\n
    '''
def getSessionId():
    '''returns long\n\n
    getSessionId()\n
    '''
def getSession():
    '''returns SessionContext\n\n
    getSession()\n
    '''
def getUser():
    '''returns String\n\n
    getUser()\n
    '''
def logout():
    '''returns None\n\n
    logout()\n
    '''
def checkPermission():
    '''returns SessionContext\n\n
    checkPermission(final int type)\n
    '''
def getTxTimer():
    '''returns Timer\n\n
    getTxTimer()\n
    '''
def setTxTimer():
    '''returns None\n\n
    setTxTimer(final Timer t)\n
    '''
def getVersion():
    '''returns long\n\n
    getVersion()\n
    '''
