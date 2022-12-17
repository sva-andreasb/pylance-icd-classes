def ():
    '''returns STBase\n\n
    (final STSession stSession)\n
    '''
def addMultiChannelEventListener():
    '''returns None\n\n
    addMultiChannelEventListener(final MultiChannelEventListener obj)\n
    '''
def removeMultiChannelEventListener():
    '''returns None\n\n
    removeMultiChannelEventListener(final MultiChannelEventListener obj)\n
    '''
def isLoggedIn():
    '''returns boolean\n\n
    isLoggedIn()\n
    '''
def setLoginType():
    '''returns None\n\n
    setLoginType(final short loginType)\n
    '''
def getLoginType():
    '''returns short\n\n
    getLoginType()\n
    '''
def getConnectionInfo():
    '''returns ConnectionInfo\n\n
    getConnectionInfo()\n
    '''
def getConnectionHandler():
    '''returns ConnectionHandler\n\n
    getConnectionHandler()\n
    '''
def setConnectivity():
    '''returns None\n\n
    setConnectivity(final Connection[] connectivity)\n
    '''
def setKeepAliveRate():
    '''returns None\n\n
    setKeepAliveRate(final long keepAliveRate)\n
    '''
def getLogin():
    '''returns Login\n\n
    getLogin()\n
    '''
def setLoginStatus():
    '''returns None\n\n
    setLoginStatus(final boolean b, final STUserStatus stUserStatus)\n
    '''
def loginByPassword():
    '''returns None\n\n
    loginByPassword(final String s, final String s2, final String s3)\n
    loginByPassword(final String s, final String s2, final String s3, final String s4)\n
    loginByPassword(final String s, final String s2, final String s3, final String s4, final InetAddress inetAddress, final String s5)\n
    loginByPassword(final String s, final String s2, final ServerAppService serverAppService, final InetAddress inetAddress)\n
    loginByPassword(final String s, final String s2, final String s3, final ServerAppService serverAppService, final InetAddress inetAddress)\n
    loginByPassword(final String s, final String s2, final String s3, final ServerAppService serverAppService, final InetAddress inetAddress, final String s4)\n
    '''
def loginByToken():
    '''returns None\n\n
    loginByToken(final String s, final String s2, final String s3)\n
    loginByToken(final String s, final String s2, final String s3, final String s4)\n
    loginByToken(final String s, final String s2, final String s3, final String s4, final InetAddress inetAddress, final String s5)\n
    loginByToken(final String s, final String s2, final ServerAppService serverAppService, final InetAddress inetAddress)\n
    loginByToken(final String s, final String s2, final String s3, final ServerAppService serverAppService, final InetAddress inetAddress, final String s4)\n
    '''
def loginAsAnon():
    '''returns None\n\n
    loginAsAnon(final String s, final String s2)\n
    loginAsAnon(final String s, final String s2, final String s3)\n
    loginAsAnon(final String s, final String s2, final String s3, final InetAddress inetAddress, final String s4)\n
    loginAsAnon(final String s, final ServerAppService serverAppService, final InetAddress inetAddress)\n
    loginAsAnon(final String s, final ServerAppService serverAppService, final String s2, final InetAddress inetAddress, final String s3)\n
    '''
def loginAsServerApp():
    '''returns None\n\n
    loginAsServerApp(final String s, final short n, final String s2, final int[] array)\n
    '''
def logout():
    '''returns None\n\n
    logout()\n
    '''
def senseService():
    '''returns None\n\n
    senseService(final int n)\n
    '''
def sendOTM():
    '''returns None\n\n
    sendOTM(final int value, final STId stId, final int n, final int n2, final int n3, final short n4, final byte[] array)\n
    '''
def denyOTM():
    '''returns None\n\n
    denyOTM(final int value, final STId stId, final int n)\n
    '''
def serviceUp():
    '''returns None\n\n
    serviceUp(final int[] array)\n
    '''
def serviceDown():
    '''returns None\n\n
    serviceDown(final int[] array)\n
    '''
def sendMultiCast():
    '''returns None\n\n
    sendMultiCast(final STObject[] array, final short n, final byte[] array2)\n
    '''
def sendOnChannels():
    '''returns None\n\n
    sendOnChannels(final Channel[] array, final short n, final byte[] array2, final boolean b)\n
    '''
def createChannel():
    '''returns Channel\n\n
    createChannel(final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STId stId)\n
    createChannel(final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STId stId, final STUserInstance stUserInstance)\n
    createChannel(final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STId stId, byte b)\n
    createChannel(final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STId stId, byte b, final STUserInstance stUserInstance)\n
    '''
def adminMsg():
    '''returns None\n\n
    adminMsg(final String s)\n
    '''
def enableAutomaticReconnect():
    '''returns None\n\n
    enableAutomaticReconnect(final int n, final long n2)\n
    '''
def disableAutomaticReconnect():
    '''returns None\n\n
    disableAutomaticReconnect()\n
    '''
def createAwarenessPermissionManager():
    '''returns AwarenessPermissionManager\n\n
    createAwarenessPermissionManager()\n
    '''
def getServerPovIp():
    '''returns InetAddress\n\n
    getServerPovIp()\n
    '''
