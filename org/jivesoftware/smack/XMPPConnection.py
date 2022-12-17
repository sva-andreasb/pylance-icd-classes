def ():
    '''returns XMPPConnection\n\n
    (final String serviceName, final CallbackHandler callbackHandler)\n
    (final String serviceName)\n
    (final ConnectionConfiguration config)\n
    (final ConnectionConfiguration config, final CallbackHandler callbackHandler)\n
    '''
def getConnectionID():
    '''returns String\n\n
    getConnectionID()\n
    '''
def getUser():
    '''returns String\n\n
    getUser()\n
    '''
def getRoster():
    '''returns Roster\n\n
    getRoster()\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def isSecureConnection():
    '''returns boolean\n\n
    isSecureConnection()\n
    '''
def isAuthenticated():
    '''returns boolean\n\n
    isAuthenticated()\n
    '''
def isAnonymous():
    '''returns boolean\n\n
    isAnonymous()\n
    '''
def sendPacket():
    '''returns None\n\n
    sendPacket(final Packet packet)\n
    '''
def addPacketWriterInterceptor():
    '''returns None\n\n
    addPacketWriterInterceptor(final PacketInterceptor packetInterceptor, final PacketFilter packetFilter)\n
    '''
def removePacketWriterInterceptor():
    '''returns None\n\n
    removePacketWriterInterceptor(final PacketInterceptor packetInterceptor)\n
    '''
def addPacketWriterListener():
    '''returns None\n\n
    addPacketWriterListener(final PacketListener packetListener, final PacketFilter packetFilter)\n
    '''
def removePacketWriterListener():
    '''returns None\n\n
    removePacketWriterListener(final PacketListener packetListener)\n
    '''
def isUsingTLS():
    '''returns boolean\n\n
    isUsingTLS()\n
    '''
def isUsingCompression():
    '''returns boolean\n\n
    isUsingCompression()\n
    '''
def connect():
    '''returns None\n\n
    connect()\n
    '''
