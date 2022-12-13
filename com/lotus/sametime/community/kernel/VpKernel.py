def isLoggedIn():
    '''public boolean isLoggedIn()
    '''
def getLoginInfo():
    '''public STUserInstance getLoginInfo()
    '''
def getPrivacyMode():
    '''public short getPrivacyMode()
    '''
def getIp():
    '''public InetAddress getIp()
    '''
def getServerPovIp():
    '''public InetAddress getServerPovIp()
    '''
def getConnectionInfo():
    '''public synchronized ConnectionInfo getConnectionInfo()
    '''
def setIp():
    '''public void setIp(final InetAddress ip)
    '''
def setLocation():
    '''public void setLocation(final String location)
    '''
def getStatus():
    '''public STUserStatus getStatus()
    '''
def getPrivacyList():
    '''public STPrivacyList getPrivacyList()
    '''
def getServerVersion():
    '''public int getServerVersion()
    '''
def isGroupPrivacySupported():
    '''public boolean isGroupPrivacySupported()
    '''
def setAutoRelogin():
    '''public void setAutoRelogin(final boolean autoRelogin)
    '''
def getAutoRelogin():
    '''public boolean getAutoRelogin()
    '''
def setLoginType():
    '''public void setLoginType(final short loginType)
    '''
def setLoginStatus():
    '''public void setLoginStatus(final boolean forceChangeStatus, final STUserStatus userStatusOnLogin)
    '''
def getLoginType():
    '''public short getLoginType()
    '''
def getHost():
    '''public String getHost()
    '''
def getConnectingServer():
    '''public STServer getConnectingServer()
    '''
def getConnectionHandler():
    '''public ConnectionHandler getConnectionHandler()
    '''
def getKernelName():
    '''public String getKernelName()
    '''
def getLocalAddress():
    '''public InetAddress getLocalAddress()
    '''
def loginByPassword():
    '''public synchronized boolean loginByPassword(final String s, final String s2, final String str, final String s3)
    '''
def loginByToken():
    '''public synchronized boolean loginByToken(final String s, final String s2, final String str, final String s3)
    '''
def loginAsAnon():
    '''public synchronized boolean loginAsAnon(final String s, String s2, final String s3)
    '''
def loginAsServerApp():
    '''public synchronized boolean loginAsServerApp(final String s, final short n, final String s2, final int[] array)
    '''
def login():
    '''public final synchronized boolean login(final String s, final String s2, final VpkAuthInfo vpkAuthInfo, final String s3, final boolean b)
    '''
def reconnect():
    '''public final synchronized boolean reconnect()
    '''
def logout():
    '''public synchronized boolean logout()
    public final synchronized boolean logout(final int n)
    '''
def setPrivacyMode():
    '''public final synchronized boolean setPrivacyMode(final short n)
    '''
def setPrivacyList():
    '''public final synchronized boolean setPrivacyList(final STPrivacyList list)
    '''
def setUserStatus():
    '''public final synchronized boolean setUserStatus(final STUserStatus stUserStatus)
    '''
def setUserName():
    '''public final synchronized boolean setUserName(final String s)
    '''
def senseService():
    '''public final synchronized boolean senseService(final int n)
    '''
def createChannel():
    '''public final synchronized boolean createChannel(final int value, STId stId, final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final int n4, final byte b, final STUserInstance stUserInstance)
    '''
def acceptChannel():
    '''public final synchronized boolean acceptChannel(final int value, final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STUserInstance stUserInstance, final byte priority, final STUserInstance stUserInstance2)
    '''
def destroyChannel():
    '''public final synchronized boolean destroyChannel(int value, final int n, final byte[] array)
    '''
def sendOnChannel():
    '''public final synchronized boolean sendOnChannel(final int value, final short n, byte[] encrypt, final boolean b)
    '''
def multiSendOnChannel():
    '''public final synchronized boolean multiSendOnChannel(final int[] array, final short n, final byte[] array2, final boolean b)
    '''
def sendTo():
    '''public final synchronized boolean sendTo(final int n, final STId stId, final int n2, final int n3, final int n4, final short n5, final byte[] array)
    '''
def denySend():
    '''public final synchronized boolean denySend(final int n, final STId stId, final int n2)
    '''
def queryCommunities():
    '''public boolean queryCommunities()
    '''
def adminMsg():
    '''public boolean adminMsg(final String s)
    '''
def sendMultiCastMsg():
    '''public boolean sendMultiCastMsg(final STObject[] array, final short n, final byte[] array2)
    '''
def setConnectivity():
    '''public boolean setConnectivity(final Connection[] connectionsToTry)
    '''
def setKeepAliveRate():
    '''public synchronized void setKeepAliveRate(final long n)
    '''
def serviceUp():
    '''public synchronized void serviceUp(final int[] array)
    '''
def serviceDown():
    '''public synchronized void serviceDown(final int[] array)
    '''
def onConnected():
    '''public void onConnected(final ConnectionHandler connectionHandler)
    '''
def onConnectFailed():
    '''public void onConnectFailed(final ConnectionHandler connectionHandler)
    '''
def onProtocolErrorOccured():
    '''public void onProtocolErrorOccured(final ConnectionHandler connectionHandler)
    '''
def onConnectionClosed():
    '''public synchronized void onConnectionClosed(final int n, final ConnectionHandler connectionHandler)
    '''
def onReceive():
    '''public void onReceive(final VpkMsgIn vpkMsgIn)
    '''
