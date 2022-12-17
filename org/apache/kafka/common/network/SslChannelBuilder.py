def ():
    '''returns SslChannelBuilder\n\n
    (final Mode mode, final ListenerName listenerName, final boolean isInterBrokerListener)\n
    '''
def configure():
    '''returns None\n\n
    configure(final Map<String, ?> configs)\n
    '''
def reconfigurableConfigs():
    '''returns Set<String>\n\n
    reconfigurableConfigs()\n
    '''
def validateReconfiguration():
    '''returns None\n\n
    validateReconfiguration(final Map<String, ?> configs)\n
    '''
def reconfigure():
    '''returns None\n\n
    reconfigure(final Map<String, ?> configs)\n
    '''
def listenerName():
    '''returns ListenerName\n\n
    listenerName()\n
    '''
def buildChannel():
    '''returns KafkaChannel\n\n
    buildChannel(final String id, final SelectionKey key, final int maxReceiveSize, final MemoryPool memoryPool)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    close()\n
    '''
def authenticate():
    '''returns None\n\n
    authenticate()\n
    '''
def principal():
    '''returns KafkaPrincipal\n\n
    principal()\n
    '''
def complete():
    '''returns boolean\n\n
    complete()\n
    '''
