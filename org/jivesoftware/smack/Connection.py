def getServiceName():
    '''public String getServiceName()
    '''
def getHost():
    '''public String getHost()
    '''
def getPort():
    '''public int getPort()
    '''
def login():
    '''public void login(final String username, final String password)
    '''
def getAccountManager():
    '''public AccountManager getAccountManager()
    '''
def getChatManager():
    '''public synchronized ChatManager getChatManager()
    '''
def getSASLAuthentication():
    '''public SASLAuthentication getSASLAuthentication()
    '''
def disconnect():
    '''public void disconnect()
    '''
def addConnectionCreationListener():
    '''public static void addConnectionCreationListener(final ConnectionCreationListener connectionCreationListener)
    '''
def removeConnectionCreationListener():
    '''public static void removeConnectionCreationListener(final ConnectionCreationListener connectionCreationListener)
    '''
def addConnectionListener():
    '''public void addConnectionListener(final ConnectionListener connectionListener)
    '''
def removeConnectionListener():
    '''public void removeConnectionListener(final ConnectionListener connectionListener)
    '''
def createPacketCollector():
    '''public PacketCollector createPacketCollector(final PacketFilter packetFilter)
    '''
def addPacketListener():
    '''public void addPacketListener(final PacketListener packetListener, final PacketFilter packetFilter)
    '''
def removePacketListener():
    '''public void removePacketListener(final PacketListener packetListener)
    '''
def addPacketSendingListener():
    '''public void addPacketSendingListener(final PacketListener packetListener, final PacketFilter packetFilter)
    '''
def removePacketSendingListener():
    '''public void removePacketSendingListener(final PacketListener packetListener)
    '''
def addPacketInterceptor():
    '''public void addPacketInterceptor(final PacketInterceptor packetInterceptor, final PacketFilter packetFilter)
    '''
def removePacketInterceptor():
    '''public void removePacketInterceptor(final PacketInterceptor packetInterceptor)
    '''
def ListenerWrapper():
    '''public ListenerWrapper(final PacketListener packetListener, final PacketFilter packetFilter)
    '''
def notifyListener():
    '''public void notifyListener(final Packet packet)
    public void notifyListener(final Packet packet)
    '''
def InterceptorWrapper():
    '''public InterceptorWrapper(final PacketInterceptor packetInterceptor, final PacketFilter packetFilter)
    '''
def equals():
    '''public boolean equals(final Object object)
    '''
