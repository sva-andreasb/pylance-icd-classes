def getServiceName():
    '''returns String\n\n
    getServiceName()\n
    '''
def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
def login():
    '''returns None\n\n
    login(final String username, final String password)\n
    '''
def getAccountManager():
    '''returns AccountManager\n\n
    getAccountManager()\n
    '''
def getSASLAuthentication():
    '''returns SASLAuthentication\n\n
    getSASLAuthentication()\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def addConnectionListener():
    '''returns None\n\n
    addConnectionListener(final ConnectionListener connectionListener)\n
    '''
def removeConnectionListener():
    '''returns None\n\n
    removeConnectionListener(final ConnectionListener connectionListener)\n
    '''
def createPacketCollector():
    '''returns PacketCollector\n\n
    createPacketCollector(final PacketFilter packetFilter)\n
    '''
def addPacketListener():
    '''returns None\n\n
    addPacketListener(final PacketListener packetListener, final PacketFilter packetFilter)\n
    '''
def removePacketListener():
    '''returns None\n\n
    removePacketListener(final PacketListener packetListener)\n
    '''
def addPacketSendingListener():
    '''returns None\n\n
    addPacketSendingListener(final PacketListener packetListener, final PacketFilter packetFilter)\n
    '''
def removePacketSendingListener():
    '''returns None\n\n
    removePacketSendingListener(final PacketListener packetListener)\n
    '''
def addPacketInterceptor():
    '''returns None\n\n
    addPacketInterceptor(final PacketInterceptor packetInterceptor, final PacketFilter packetFilter)\n
    '''
def removePacketInterceptor():
    '''returns None\n\n
    removePacketInterceptor(final PacketInterceptor packetInterceptor)\n
    '''
def ():
    '''returns InterceptorWrapper\n\n
    (final PacketListener packetListener, final PacketFilter packetFilter)\n
    (final PacketInterceptor packetInterceptor, final PacketFilter packetFilter)\n
    '''
def notifyListener():
    '''returns None\n\n
    notifyListener(final Packet packet)\n
    notifyListener(final Packet packet)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object object)\n
    '''
