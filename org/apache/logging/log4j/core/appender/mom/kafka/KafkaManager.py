DEFAULT_TIMEOUT_MILLIS = "String  \"30000\""
def ():
    '''returns FactoryData\n\n
    (final LoggerContext loggerContext, final String name, final String topic, final boolean syncSend, final Property[] properties, final String key)\n
    (final LoggerContext loggerContext, final String topic, final boolean syncSend, final Property[] properties, final String key)\n
    '''
def releaseSub():
    '''returns boolean\n\n
    releaseSub(final long timeout, final TimeUnit timeUnit)\n
    '''
def send():
    '''returns None\n\n
    send(final byte[] msg)\n
    '''
def startup():
    '''returns None\n\n
    startup()\n
    '''
def getTopic():
    '''returns String\n\n
    getTopic()\n
    '''
def createManager():
    '''returns KafkaManager\n\n
    createManager(final String name, final FactoryData data)\n
    '''
