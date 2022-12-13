def isLoggedIn():
'''public boolean isLoggedIn()
'''
pass
def getLoginInfo():
'''public STUserInstance getLoginInfo()
'''
pass
def getPrivacyMode():
'''public short getPrivacyMode()
'''
pass
def getIp():
'''public InetAddress getIp()
'''
pass
def getServerPovIp():
'''public InetAddress getServerPovIp()
'''
pass
def getConnectionInfo():
'''public synchronized ConnectionInfo getConnectionInfo()
'''
pass
def setIp():
'''public void setIp(final InetAddress ip)
'''
pass
def setLocation():
'''public void setLocation(final String location)
'''
pass
def getStatus():
'''public STUserStatus getStatus()
'''
pass
def getPrivacyList():
'''public STPrivacyList getPrivacyList()
'''
pass
def getServerVersion():
'''public int getServerVersion()
'''
pass
def isGroupPrivacySupported():
'''public boolean isGroupPrivacySupported()
'''
pass
def setAutoRelogin():
'''public void setAutoRelogin(final boolean autoRelogin)
'''
pass
def getAutoRelogin():
'''public boolean getAutoRelogin()
'''
pass
def setLoginType():
'''public void setLoginType(final short loginType)
'''
pass
def setLoginStatus():
'''public void setLoginStatus(final boolean forceChangeStatus, final STUserStatus userStatusOnLogin)
'''
pass
def getLoginType():
'''public short getLoginType()
'''
pass
def getHost():
'''public String getHost()
'''
pass
def getConnectingServer():
'''public STServer getConnectingServer()
'''
pass
def getConnectionHandler():
'''public ConnectionHandler getConnectionHandler()
'''
pass
def getKernelName():
'''public String getKernelName()
'''
pass
def getLocalAddress():
'''public InetAddress getLocalAddress()
'''
pass
def loginByPassword():
'''public synchronized boolean loginByPassword(final String s, final String s2, final String str, final String s3)
'''
pass
def loginByToken():
'''public synchronized boolean loginByToken(final String s, final String s2, final String str, final String s3)
'''
pass
def loginAsAnon():
'''public synchronized boolean loginAsAnon(final String s, String s2, final String s3)
'''
pass
def loginAsServerApp():
'''public synchronized boolean loginAsServerApp(final String s, final short n, final String s2, final int[] array)
'''
pass
def login():
'''public final synchronized boolean login(final String s, final String s2, final VpkAuthInfo vpkAuthInfo, final String s3, final boolean b)
'''
pass
def reconnect():
'''public final synchronized boolean reconnect()
'''
pass
def logout():
'''public synchronized boolean logout()
public final synchronized boolean logout(final int n)
'''
pass
def setPrivacyMode():
'''public final synchronized boolean setPrivacyMode(final short n)
'''
pass
def setPrivacyList():
'''public final synchronized boolean setPrivacyList(final STPrivacyList list)
'''
pass
def setUserStatus():
'''public final synchronized boolean setUserStatus(final STUserStatus stUserStatus)
'''
pass
def setUserName():
'''public final synchronized boolean setUserName(final String s)
'''
pass
def senseService():
'''public final synchronized boolean senseService(final int n)
'''
pass
def createChannel():
'''public final synchronized boolean createChannel(final int value, STId stId, final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final int n4, final byte b, final STUserInstance stUserInstance)
'''
pass
def acceptChannel():
'''public final synchronized boolean acceptChannel(final int value, final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STUserInstance stUserInstance, final byte priority, final STUserInstance stUserInstance2)
'''
pass
def destroyChannel():
'''public final synchronized boolean destroyChannel(int value, final int n, final byte[] array)
'''
pass
def sendOnChannel():
'''public final synchronized boolean sendOnChannel(final int value, final short n, byte[] encrypt, final boolean b)
'''
pass
def multiSendOnChannel():
'''public final synchronized boolean multiSendOnChannel(final int[] array, final short n, final byte[] array2, final boolean b)
'''
pass
def sendTo():
'''public final synchronized boolean sendTo(final int n, final STId stId, final int n2, final int n3, final int n4, final short n5, final byte[] array)
'''
pass
def denySend():
'''public final synchronized boolean denySend(final int n, final STId stId, final int n2)
'''
pass
def queryCommunities():
'''public boolean queryCommunities()
'''
pass
def adminMsg():
'''public boolean adminMsg(final String s)
'''
pass
def sendMultiCastMsg():
'''public boolean sendMultiCastMsg(final STObject[] array, final short n, final byte[] array2)
'''
pass
def setConnectivity():
'''public boolean setConnectivity(final Connection[] connectionsToTry)
'''
pass
def setKeepAliveRate():
'''public synchronized void setKeepAliveRate(final long n)
'''
pass
def serviceUp():
'''public synchronized void serviceUp(final int[] array)
'''
pass
def serviceDown():
'''public synchronized void serviceDown(final int[] array)
'''
pass
def onConnected():
'''public void onConnected(final ConnectionHandler connectionHandler)
'''
pass
def onConnectFailed():
'''public void onConnectFailed(final ConnectionHandler connectionHandler)
'''
pass
def onProtocolErrorOccured():
'''public void onProtocolErrorOccured(final ConnectionHandler connectionHandler)
'''
pass
def onConnectionClosed():
'''public synchronized void onConnectionClosed(final int n, final ConnectionHandler connectionHandler)
'''
pass
def onReceive():
'''public void onReceive(final VpkMsgIn vpkMsgIn)
'''
pass
