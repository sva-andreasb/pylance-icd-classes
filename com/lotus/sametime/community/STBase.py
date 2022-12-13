def STBase():
'''public STBase(final STSession stSession)
'''
pass
def addLoginListener():
'''public synchronized void addLoginListener(final LoginListener obj)
'''
pass
def removeLoginListener():
'''public synchronized void removeLoginListener(final LoginListener obj)
'''
pass
def addOTMServiceListener():
'''public synchronized void addOTMServiceListener(final OTMServiceListener obj)
'''
pass
def removeOTMServiceListener():
'''public synchronized void removeOTMServiceListener(final OTMServiceListener obj)
'''
pass
def addAdminMsgListener():
'''public synchronized void addAdminMsgListener(final AdminMsgListener obj)
'''
pass
def removeAdminMsgListener():
'''public synchronized void removeAdminMsgListener(final AdminMsgListener obj)
'''
pass
def addMultiCastListener():
'''public synchronized void addMultiCastListener(final MultiCastListener obj)
'''
pass
def removeMultiCastListener():
'''public synchronized void removeMultiCastListener(final MultiCastListener obj)
'''
pass
def addServiceListener():
'''public synchronized void addServiceListener(final ServiceListener obj)
'''
pass
def removeServiceListener():
'''public synchronized void removeServiceListener(final ServiceListener obj)
'''
pass
def addChannelServiceListener():
'''public synchronized void addChannelServiceListener(final ChannelServiceListener obj)
'''
pass
def removeChannelServiceListener():
'''public synchronized void removeChannelServiceListener(final ChannelServiceListener obj)
'''
pass
def addMultiChannelEventListener():
'''public void addMultiChannelEventListener(final MultiChannelEventListener obj)
'''
pass
def removeMultiChannelEventListener():
'''public void removeMultiChannelEventListener(final MultiChannelEventListener obj)
'''
pass
def isLoggedIn():
'''public boolean isLoggedIn()
'''
pass
def setLoginType():
'''public void setLoginType(final short loginType)
'''
pass
def getLoginType():
'''public short getLoginType()
'''
pass
def getConnectionInfo():
'''public ConnectionInfo getConnectionInfo()
'''
pass
def getConnectionHandler():
'''public ConnectionHandler getConnectionHandler()
'''
pass
def setConnectivity():
'''public void setConnectivity(final Connection[] connectivity)
'''
pass
def setKeepAliveRate():
'''public void setKeepAliveRate(final long keepAliveRate)
'''
pass
def getLogin():
'''public Login getLogin()
'''
pass
def setLoginStatus():
'''public void setLoginStatus(final boolean b, final STUserStatus stUserStatus)
'''
pass
def loginByPassword():
'''public void loginByPassword(final String s, final String s2, final String s3)
public void loginByPassword(final String s, final String s2, final String s3, final String s4)
public void loginByPassword(final String s, final String s2, final String s3, final String s4, final InetAddress inetAddress, final String s5)
public void loginByPassword(final String s, final String s2, final ServerAppService serverAppService, final InetAddress inetAddress)
public void loginByPassword(final String s, final String s2, final String s3, final ServerAppService serverAppService, final InetAddress inetAddress)
public void loginByPassword(final String s, final String s2, final String s3, final ServerAppService serverAppService, final InetAddress inetAddress, final String s4)
'''
pass
def loginByToken():
'''public void loginByToken(final String s, final String s2, final String s3)
public void loginByToken(final String s, final String s2, final String s3, final String s4)
public void loginByToken(final String s, final String s2, final String s3, final String s4, final InetAddress inetAddress, final String s5)
public void loginByToken(final String s, final String s2, final ServerAppService serverAppService, final InetAddress inetAddress)
public void loginByToken(final String s, final String s2, final String s3, final ServerAppService serverAppService, final InetAddress inetAddress, final String s4)
'''
pass
def loginAsAnon():
'''public void loginAsAnon(final String s, final String s2)
public void loginAsAnon(final String s, final String s2, final String s3)
public void loginAsAnon(final String s, final String s2, final String s3, final InetAddress inetAddress, final String s4)
public void loginAsAnon(final String s, final ServerAppService serverAppService, final InetAddress inetAddress)
public void loginAsAnon(final String s, final ServerAppService serverAppService, final String s2, final InetAddress inetAddress, final String s3)
'''
pass
def loginAsServerApp():
'''public void loginAsServerApp(final String s, final short n, final String s2, final int[] array)
'''
pass
def logout():
'''public void logout()
'''
pass
def senseService():
'''public void senseService(final int n)
'''
pass
def sendOTM():
'''public void sendOTM(final int value, final STId stId, final int n, final int n2, final int n3, final short n4, final byte[] array)
'''
pass
def denyOTM():
'''public void denyOTM(final int value, final STId stId, final int n)
'''
pass
def serviceUp():
'''public void serviceUp(final int[] array)
'''
pass
def serviceDown():
'''public void serviceDown(final int[] array)
'''
pass
def sendMultiCast():
'''public void sendMultiCast(final STObject[] array, final short n, final byte[] array2)
'''
pass
def sendOnChannels():
'''public void sendOnChannels(final Channel[] array, final short n, final byte[] array2, final boolean b)
'''
pass
def createChannel():
'''public Channel createChannel(final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STId stId)
public Channel createChannel(final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STId stId, final STUserInstance stUserInstance)
public Channel createChannel(final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STId stId, byte b)
public Channel createChannel(final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STId stId, byte b, final STUserInstance stUserInstance)
'''
pass
def adminMsg():
'''public void adminMsg(final String s)
'''
pass
def enableAutomaticReconnect():
'''public void enableAutomaticReconnect(final int n, final long n2)
'''
pass
def disableAutomaticReconnect():
'''public void disableAutomaticReconnect()
'''
pass
def createAwarenessPermissionManager():
'''public AwarenessPermissionManager createAwarenessPermissionManager()
'''
pass
def getServerPovIp():
'''public InetAddress getServerPovIp()
'''
pass
