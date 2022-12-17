def ():
    '''returns KafkaChannel\n\n
    (final String id, final TransportLayer transportLayer, final Authenticator authenticator, final int maxReceiveSize, final MemoryPool memoryPool)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def principal():
    '''returns KafkaPrincipal\n\n
    principal()\n
    '''
def prepare():
    '''returns None\n\n
    prepare()\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    '''
def state():
    '''returns ChannelState\n\n
    state(final ChannelState state)\n
    state()\n
    '''
def finishConnect():
    '''returns boolean\n\n
    finishConnect()\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def id():
    '''returns String\n\n
    id()\n
    '''
def selectionKey():
    '''returns SelectionKey\n\n
    selectionKey()\n
    '''
def isMute():
    '''returns boolean\n\n
    isMute()\n
    '''
def isInMutableState():
    '''returns boolean\n\n
    isInMutableState()\n
    '''
def ready():
    '''returns boolean\n\n
    ready()\n
    '''
def hasSend():
    '''returns boolean\n\n
    hasSend()\n
    '''
def socketAddress():
    '''returns InetAddress\n\n
    socketAddress()\n
    '''
def socketDescription():
    '''returns String\n\n
    socketDescription()\n
    '''
def setSend():
    '''returns None\n\n
    setSend(final Send send)\n
    '''
def read():
    '''returns NetworkReceive\n\n
    read()\n
    '''
def write():
    '''returns Send\n\n
    write()\n
    '''
def addNetworkThreadTimeNanos():
    '''returns None\n\n
    addNetworkThreadTimeNanos(final long nanos)\n
    '''
def getAndResetNetworkThreadTimeNanos():
    '''returns long\n\n
    getAndResetNetworkThreadTimeNanos()\n
    '''
def hasBytesBuffered():
    '''returns boolean\n\n
    hasBytesBuffered()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
