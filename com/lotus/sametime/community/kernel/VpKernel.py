def isLoggedIn():
    '''returns boolean\n\n
    isLoggedIn()\n
    '''
def getLoginInfo():
    '''returns STUserInstance\n\n
    getLoginInfo()\n
    '''
def getPrivacyMode():
    '''returns short\n\n
    getPrivacyMode()\n
    '''
def getIp():
    '''returns InetAddress\n\n
    getIp()\n
    '''
def getServerPovIp():
    '''returns InetAddress\n\n
    getServerPovIp()\n
    '''
def setIp():
    '''returns None\n\n
    setIp(final InetAddress ip)\n
    '''
def setLocation():
    '''returns None\n\n
    setLocation(final String location)\n
    '''
def getStatus():
    '''returns STUserStatus\n\n
    getStatus()\n
    '''
def getPrivacyList():
    '''returns STPrivacyList\n\n
    getPrivacyList()\n
    '''
def getServerVersion():
    '''returns int\n\n
    getServerVersion()\n
    '''
def isGroupPrivacySupported():
    '''returns boolean\n\n
    isGroupPrivacySupported()\n
    '''
def setAutoRelogin():
    '''returns None\n\n
    setAutoRelogin(final boolean autoRelogin)\n
    '''
def getAutoRelogin():
    '''returns boolean\n\n
    getAutoRelogin()\n
    '''
def setLoginType():
    '''returns None\n\n
    setLoginType(final short loginType)\n
    '''
def setLoginStatus():
    '''returns None\n\n
    setLoginStatus(final boolean forceChangeStatus, final STUserStatus userStatusOnLogin)\n
    '''
def getLoginType():
    '''returns short\n\n
    getLoginType()\n
    '''
def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def getConnectingServer():
    '''returns STServer\n\n
    getConnectingServer()\n
    '''
def getConnectionHandler():
    '''returns ConnectionHandler\n\n
    getConnectionHandler()\n
    '''
def getKernelName():
    '''returns String\n\n
    getKernelName()\n
    '''
def getLocalAddress():
    '''returns InetAddress\n\n
    getLocalAddress()\n
    '''
def queryCommunities():
    '''returns boolean\n\n
    queryCommunities()\n
    '''
def adminMsg():
    '''returns boolean\n\n
    adminMsg(final String s)\n
    '''
def sendMultiCastMsg():
    '''returns boolean\n\n
    sendMultiCastMsg(final STObject[] array, final short n, final byte[] array2)\n
    '''
def setConnectivity():
    '''returns boolean\n\n
    setConnectivity(final Connection[] connectionsToTry)\n
    '''
def onConnected():
    '''returns None\n\n
    onConnected(final ConnectionHandler connectionHandler)\n
    '''
def onConnectFailed():
    '''returns None\n\n
    onConnectFailed(final ConnectionHandler connectionHandler)\n
    '''
def onProtocolErrorOccured():
    '''returns None\n\n
    onProtocolErrorOccured(final ConnectionHandler connectionHandler)\n
    '''
def onReceive():
    '''returns None\n\n
    onReceive(final VpkMsgIn vpkMsgIn)\n
    '''
