def XMPPConnection():
    '''    public XMPPConnection(final String serviceName, final CallbackHandler callbackHandler)
    public XMPPConnection(final String serviceName)
    public XMPPConnection(final ConnectionConfiguration config)
    public XMPPConnection(final ConnectionConfiguration config, final CallbackHandler callbackHandler)
    '''
def getConnectionID():
    '''    public String getConnectionID()
    '''
def getUser():
    '''    public String getUser()
    '''
def login():
    '''    public synchronized void login(String username, final String password, final String resource)
    '''
def loginAnonymously():
    '''    public synchronized void loginAnonymously()
    '''
def getRoster():
    '''    public Roster getRoster()
    '''
def isConnected():
    '''    public boolean isConnected()
    '''
def isSecureConnection():
    '''    public boolean isSecureConnection()
    '''
def isAuthenticated():
    '''    public boolean isAuthenticated()
    '''
def isAnonymous():
    '''    public boolean isAnonymous()
    '''
def disconnect():
    '''    public synchronized void disconnect(final Presence unavailablePresence)
    '''
def sendPacket():
    '''    public void sendPacket(final Packet packet)
    '''
def addPacketWriterInterceptor():
    '''    public void addPacketWriterInterceptor(final PacketInterceptor packetInterceptor, final PacketFilter packetFilter)
    '''
def removePacketWriterInterceptor():
    '''    public void removePacketWriterInterceptor(final PacketInterceptor packetInterceptor)
    '''
def addPacketWriterListener():
    '''    public void addPacketWriterListener(final PacketListener packetListener, final PacketFilter packetFilter)
    '''
def removePacketWriterListener():
    '''    public void removePacketWriterListener(final PacketListener packetListener)
    '''
def isUsingTLS():
    '''    public boolean isUsingTLS()
    '''
def isUsingCompression():
    '''    public boolean isUsingCompression()
    '''
def connect():
    '''    public void connect()
    '''
