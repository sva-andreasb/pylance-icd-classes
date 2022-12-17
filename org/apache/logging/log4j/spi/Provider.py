FACTORY_PRIORITY = "String  \"FactoryPriority\""
THREAD_CONTEXT_MAP = "String  \"ThreadContextMap\""
LOGGER_CONTEXT_FACTORY = "String  \"LoggerContextFactory\""
def ():
    '''returns Provider\n\n
    (final Properties props, final URL url, final ClassLoader classLoader)\n
    (final Integer priority, final String versions, final Class<? extends LoggerContextFactory> loggerContextFactoryClass)\n
    (final Integer priority, final String versions, final Class<? extends LoggerContextFactory> loggerContextFactoryClass, final Class<? extends ThreadContextMap> threadContextMapClass)\n
    '''
def getVersions():
    '''returns String\n\n
    getVersions()\n
    '''
def getPriority():
    '''returns Integer\n\n
    getPriority()\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def getThreadContextMap():
    '''returns String\n\n
    getThreadContextMap()\n
    '''
def getUrl():
    '''returns URL\n\n
    getUrl()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
