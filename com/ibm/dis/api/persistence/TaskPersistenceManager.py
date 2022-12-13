def TaskPersistenceManager():
    '''public TaskPersistenceManager(final Connection conn)
    '''
def registerTask():
    '''public void registerTask(final Guid mssGuid, final Guid classGuid, final Guid taskGuid, final Task task)
    '''
def unregisterTask():
    '''public void unregisterTask(final Guid mssGuid, final String className, final String taskName)
    '''
def getMSSName():
    '''public String getMSSName(final Guid mssGuid)
    '''
def getTaskGuid():
    '''public Guid getTaskGuid(final String className, final String taskName, final String mssName)
    '''
def getTask():
    '''public Task getTask(final Guid taskGuid)
    '''
