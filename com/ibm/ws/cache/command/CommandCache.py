def ():
    '''returns CommandCache\n\n
    ()\n
    '''
def setCache():
    '''returns None\n\n
    setCache(final DCache cache)\n
    '''
def setBatchUpdateDaemon():
    '''returns None\n\n
    setBatchUpdateDaemon(final BatchUpdateDaemon batchUpdateDaemon)\n
    '''
def setRemoteServices():
    '''returns None\n\n
    setRemoteServices(final RemoteServices remoteServices)\n
    '''
def getCommandStoragePolicy():
    '''returns CommandStoragePolicy\n\n
    getCommandStoragePolicy()\n
    '''
def setCommandStoragePolicy():
    '''returns None\n\n
    setCommandStoragePolicy(final Object commandStoragePolicy)\n
    '''
def setDefaultPriority():
    '''returns None\n\n
    setDefaultPriority(final int defaultPriority)\n
    '''
def start():
    '''returns None\n\n
    start()\n
    '''
def getCommandLocally():
    '''returns CacheableCommand\n\n
    getCommandLocally(final CacheableCommand inputCommand, final boolean execute)\n
    '''
def getCommand():
    '''returns CacheableCommand\n\n
    getCommand(final CacheableCommand inputCommand, final boolean execute)\n
    '''
def setCommand():
    '''returns None\n\n
    setCommand(final CacheableCommand command)\n
    '''
def executeCommand():
    '''returns CacheableCommand\n\n
    executeCommand(final CacheableCommand command, final CommandTarget commandTarget)\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid(final String id)\n
    '''
def invalidateById():
    '''returns None\n\n
    invalidateById(final String id, final boolean waitOnInvalidation)\n
    invalidateById(final String id, final int causeOfInvalidation, final boolean waitOnInvalidation)\n
    '''
def invalidateByTemplate():
    '''returns None\n\n
    invalidateByTemplate(final String template, final boolean waitOnInvalidation)\n
    '''
def getCache():
    '''returns DCache\n\n
    getCache()\n
    '''
