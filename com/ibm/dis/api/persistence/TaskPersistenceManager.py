def TaskPersistenceManager():
'''public TaskPersistenceManager(final Connection conn)
'''
pass
def registerTask():
'''public void registerTask(final Guid mssGuid, final Guid classGuid, final Guid taskGuid, final Task task)
'''
pass
def unregisterTask():
'''public void unregisterTask(final Guid mssGuid, final String className, final String taskName)
'''
pass
def getMSSName():
'''public String getMSSName(final Guid mssGuid)
'''
pass
def getTaskGuid():
'''public Guid getTaskGuid(final String className, final String taskName, final String mssName)
'''
pass
def getTask():
'''public Task getTask(final Guid taskGuid)
'''
pass
