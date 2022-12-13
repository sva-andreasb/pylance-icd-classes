def STBase():
    '''    public STBase(final STSession stSession)
    '''
def addLoginListener():
    '''    public synchronized void addLoginListener(final LoginListener obj)
    '''
def removeLoginListener():
    '''    public synchronized void removeLoginListener(final LoginListener obj)
    '''
def addOTMServiceListener():
    '''    public synchronized void addOTMServiceListener(final OTMServiceListener obj)
    '''
def removeOTMServiceListener():
    '''    public synchronized void removeOTMServiceListener(final OTMServiceListener obj)
    '''
def addAdminMsgListener():
    '''    public synchronized void addAdminMsgListener(final AdminMsgListener obj)
    '''
def removeAdminMsgListener():
    '''    public synchronized void removeAdminMsgListener(final AdminMsgListener obj)
    '''
def addMultiCastListener():
    '''    public synchronized void addMultiCastListener(final MultiCastListener obj)
    '''
def removeMultiCastListener():
    '''    public synchronized void removeMultiCastListener(final MultiCastListener obj)
    '''
def addServiceListener():
    '''    public synchronized void addServiceListener(final ServiceListener obj)
    '''
def removeServiceListener():
    '''    public synchronized void removeServiceListener(final ServiceListener obj)
    '''
def addChannelServiceListener():
    '''    public synchronized void addChannelServiceListener(final ChannelServiceListener obj)
    '''
def removeChannelServiceListener():
    '''    public synchronized void removeChannelServiceListener(final ChannelServiceListener obj)
    '''
def addMultiChannelEventListener():
    '''    public void addMultiChannelEventListener(final MultiChannelEventListener obj)
    '''
def removeMultiChannelEventListener():
    '''    public void removeMultiChannelEventListener(final MultiChannelEventListener obj)
    '''
def isLoggedIn():
    '''    public boolean isLoggedIn()
    '''
def setLoginType():
    '''    public void setLoginType(final short loginType)
    '''
def getLoginType():
    '''    public short getLoginType()
    '''
def getConnectionInfo():
    '''    public ConnectionInfo getConnectionInfo()
    '''
def getConnectionHandler():
    '''    public ConnectionHandler getConnectionHandler()
    '''
def setConnectivity():
    '''    public void setConnectivity(final Connection[] connectivity)
    '''
def setKeepAliveRate():
    '''    public void setKeepAliveRate(final long keepAliveRate)
    '''
def getLogin():
    '''    public Login getLogin()
    '''
def setLoginStatus():
    '''    public void setLoginStatus(final boolean b, final STUserStatus stUserStatus)
    '''
def loginByPassword():
    '''    public void loginByPassword(final String s, final String s2, final String s3)
    public void loginByPassword(final String s, final String s2, final String s3, final String s4)
    public void loginByPassword(final String s, final String s2, final String s3, final String s4, final InetAddress inetAddress, final String s5)
    public void loginByPassword(final String s, final String s2, final ServerAppService serverAppService, final InetAddress inetAddress)
    public void loginByPassword(final String s, final String s2, final String s3, final ServerAppService serverAppService, final InetAddress inetAddress)
    public void loginByPassword(final String s, final String s2, final String s3, final ServerAppService serverAppService, final InetAddress inetAddress, final String s4)
    '''
def loginByToken():
    '''    public void loginByToken(final String s, final String s2, final String s3)
    public void loginByToken(final String s, final String s2, final String s3, final String s4)
    public void loginByToken(final String s, final String s2, final String s3, final String s4, final InetAddress inetAddress, final String s5)
    public void loginByToken(final String s, final String s2, final ServerAppService serverAppService, final InetAddress inetAddress)
    public void loginByToken(final String s, final String s2, final String s3, final ServerAppService serverAppService, final InetAddress inetAddress, final String s4)
    '''
def loginAsAnon():
    '''    public void loginAsAnon(final String s, final String s2)
    public void loginAsAnon(final String s, final String s2, final String s3)
    public void loginAsAnon(final String s, final String s2, final String s3, final InetAddress inetAddress, final String s4)
    public void loginAsAnon(final String s, final ServerAppService serverAppService, final InetAddress inetAddress)
    public void loginAsAnon(final String s, final ServerAppService serverAppService, final String s2, final InetAddress inetAddress, final String s3)
    '''
def loginAsServerApp():
    '''    public void loginAsServerApp(final String s, final short n, final String s2, final int[] array)
    '''
def logout():
    '''    public void logout()
    '''
def senseService():
    '''    public void senseService(final int n)
    '''
def sendOTM():
    '''    public void sendOTM(final int value, final STId stId, final int n, final int n2, final int n3, final short n4, final byte[] array)
    '''
def denyOTM():
    '''    public void denyOTM(final int value, final STId stId, final int n)
    '''
def serviceUp():
    '''    public void serviceUp(final int[] array)
    '''
def serviceDown():
    '''    public void serviceDown(final int[] array)
    '''
def sendMultiCast():
    '''    public void sendMultiCast(final STObject[] array, final short n, final byte[] array2)
    '''
def sendOnChannels():
    '''    public void sendOnChannels(final Channel[] array, final short n, final byte[] array2, final boolean b)
    '''
def createChannel():
    '''    public Channel createChannel(final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STId stId)
    public Channel createChannel(final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STId stId, final STUserInstance stUserInstance)
    public Channel createChannel(final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STId stId, byte b)
    public Channel createChannel(final int n, final int n2, final int n3, final EncLevel encLevel, final byte[] array, final STId stId, byte b, final STUserInstance stUserInstance)
    '''
def adminMsg():
    '''    public void adminMsg(final String s)
    '''
def enableAutomaticReconnect():
    '''    public void enableAutomaticReconnect(final int n, final long n2)
    '''
def disableAutomaticReconnect():
    '''    public void disableAutomaticReconnect()
    '''
def createAwarenessPermissionManager():
    '''    public AwarenessPermissionManager createAwarenessPermissionManager()
    '''
def getServerPovIp():
    '''    public InetAddress getServerPovIp()
    '''
