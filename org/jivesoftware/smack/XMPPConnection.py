def XMPPConnection():
'''public XMPPConnection(final String serviceName, final CallbackHandler callbackHandler)
public XMPPConnection(final String serviceName)
public XMPPConnection(final ConnectionConfiguration config)
public XMPPConnection(final ConnectionConfiguration config, final CallbackHandler callbackHandler)
'''
pass
def getConnectionID():
'''public String getConnectionID()
'''
pass
def getUser():
'''public String getUser()
'''
pass
def login():
'''public synchronized void login(String username, final String password, final String resource)
'''
pass
def loginAnonymously():
'''public synchronized void loginAnonymously()
'''
pass
def getRoster():
'''public Roster getRoster()
'''
pass
def isConnected():
'''public boolean isConnected()
'''
pass
def isSecureConnection():
'''public boolean isSecureConnection()
'''
pass
def isAuthenticated():
'''public boolean isAuthenticated()
'''
pass
def isAnonymous():
'''public boolean isAnonymous()
'''
pass
def disconnect():
'''public synchronized void disconnect(final Presence unavailablePresence)
'''
pass
def sendPacket():
'''public void sendPacket(final Packet packet)
'''
pass
def addPacketWriterInterceptor():
'''public void addPacketWriterInterceptor(final PacketInterceptor packetInterceptor, final PacketFilter packetFilter)
'''
pass
def removePacketWriterInterceptor():
'''public void removePacketWriterInterceptor(final PacketInterceptor packetInterceptor)
'''
pass
def addPacketWriterListener():
'''public void addPacketWriterListener(final PacketListener packetListener, final PacketFilter packetFilter)
'''
pass
def removePacketWriterListener():
'''public void removePacketWriterListener(final PacketListener packetListener)
'''
pass
def isUsingTLS():
'''public boolean isUsingTLS()
'''
pass
def isUsingCompression():
'''public boolean isUsingCompression()
'''
pass
def connect():
'''public void connect()
'''
pass
