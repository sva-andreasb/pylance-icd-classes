def CommandCache():
    '''    public CommandCache()
    '''
def setCache():
    '''    public void setCache(final DCache cache)
    '''
def setBatchUpdateDaemon():
    '''    public void setBatchUpdateDaemon(final BatchUpdateDaemon batchUpdateDaemon)
    '''
def setRemoteServices():
    '''    public void setRemoteServices(final RemoteServices remoteServices)
    '''
def getCommandStoragePolicy():
    '''    public CommandStoragePolicy getCommandStoragePolicy()
    '''
def setCommandStoragePolicy():
    '''    public void setCommandStoragePolicy(final Object commandStoragePolicy)
    '''
def setDefaultPriority():
    '''    public void setDefaultPriority(final int defaultPriority)
    '''
def start():
    '''    public void start()
    '''
def getCommandLocally():
    '''    public CacheableCommand getCommandLocally(final CacheableCommand inputCommand, final boolean execute)
    '''
def getCommand():
    '''    public CacheableCommand getCommand(final CacheableCommand inputCommand, final boolean execute)
    '''
def setCommand():
    '''    public void setCommand(final CacheableCommand command)
    '''
def executeCommand():
    '''    public CacheableCommand executeCommand(final CacheableCommand command, final CommandTarget commandTarget)
    '''
def isValid():
    '''    public boolean isValid(final String id)
    '''
def invalidateById():
    '''    public void invalidateById(final String id, final boolean waitOnInvalidation)
    public void invalidateById(final String id, final int causeOfInvalidation, final boolean waitOnInvalidation)
    '''
def invalidateByTemplate():
    '''    public void invalidateByTemplate(final String template, final boolean waitOnInvalidation)
    '''
def getCache():
    '''    public DCache getCache()
    '''
