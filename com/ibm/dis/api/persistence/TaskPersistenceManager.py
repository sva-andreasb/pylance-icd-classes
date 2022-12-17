def ():
    '''returns TaskPersistenceManager\n\n
    (final Connection conn)\n
    '''
def registerTask():
    '''returns None\n\n
    registerTask(final Guid mssGuid, final Guid classGuid, final Guid taskGuid, final Task task)\n
    '''
def unregisterTask():
    '''returns None\n\n
    unregisterTask(final Guid mssGuid, final String className, final String taskName)\n
    '''
def getMSSName():
    '''returns String\n\n
    getMSSName(final Guid mssGuid)\n
    '''
def getTaskGuid():
    '''returns Guid\n\n
    getTaskGuid(final String className, final String taskName, final String mssName)\n
    '''
def getTask():
    '''returns Task\n\n
    getTask(final Guid taskGuid)\n
    '''
