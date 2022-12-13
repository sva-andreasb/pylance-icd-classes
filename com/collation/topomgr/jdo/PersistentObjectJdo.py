def PersistentObjectJdo():
    '''public PersistentObjectJdo()
    public PersistentObjectJdo(final Guid guid, final String className)
    '''
def getGuid():
    '''public Guid getGuid()
    '''
def getClassName():
    '''public String getClassName()
    '''
def setClassName():
    '''public void setClassName(final String className)
    '''
def getName():
    '''public String getName()
    '''
def setName():
    '''public void setName(final String name)
    '''
def getType():
    '''public String getType()
    '''
def setType():
    '''public void setType(final String type)
    '''
def getHwType():
    '''public String getHwType()
    '''
def setHwType():
    '''public void setHwType(final String type)
    '''
def getVersioned():
    '''public boolean getVersioned()
    '''
def setVersioned():
    '''public void setVersioned(final boolean versioned)
    '''
def getArchived():
    '''public boolean getArchived()
    '''
def setArchived():
    '''public void setArchived(final boolean archived)
    '''
def getDeleted():
    '''public boolean getDeleted()
    '''
def setDeleted():
    '''public void setDeleted(final boolean deleted)
    '''
def getCmdbSource():
    '''public Guid getCmdbSource()
    '''
def setCmdbSource():
    '''public void setCmdbSource(final Guid cmdbSource)
    '''
def getRunId():
    '''public long getRunId()
    '''
def setRunId():
    '''public void setRunId(final long runId)
    '''
def getLastModifiedTime():
    '''public long getLastModifiedTime()
    '''
def setLastModifiedTime():
    '''public void setLastModifiedTime(final long lastModifiedTime)
    '''
def jdoNewInstance():
    '''public PersistenceCapable jdoNewInstance(final StateManager jdoStateManager, final Object o)
    public PersistenceCapable jdoNewInstance(final StateManager jdoStateManager)
    '''
def jdoReplaceField():
    '''public void jdoReplaceField(final int n)
    '''
def jdoReplaceFields():
    '''public void jdoReplaceFields(final int[] array)
    '''
def jdoProvideField():
    '''public void jdoProvideField(final int n)
    '''
def jdoProvideFields():
    '''public void jdoProvideFields(final int[] array)
    '''
def jdoCopyFields():
    '''public void jdoCopyFields(final Object o, final int[] array)
    '''
def jdoGetPersistenceManager():
    '''public PersistenceManager jdoGetPersistenceManager()
    '''
def jdoGetObjectId():
    '''public Object jdoGetObjectId()
    '''
def jdoGetTransactionalObjectId():
    '''public Object jdoGetTransactionalObjectId()
    '''
def jdoIsDeleted():
    '''public boolean jdoIsDeleted()
    '''
def jdoIsDirty():
    '''public boolean jdoIsDirty()
    '''
def jdoIsNew():
    '''public boolean jdoIsNew()
    '''
def jdoIsPersistent():
    '''public boolean jdoIsPersistent()
    '''
def jdoIsTransactional():
    '''public boolean jdoIsTransactional()
    '''
def jdoPreSerialize():
    '''public void jdoPreSerialize()
    '''
def jdoMakeDirty():
    '''public void jdoMakeDirty(final String s)
    '''
def jdoReplaceFlags():
    '''public void jdoReplaceFlags()
    '''
def jdoReplaceStateManager():
    '''public synchronized void jdoReplaceStateManager(final StateManager jdoStateManager)
    '''
def jdoCopyKeyFieldsToObjectId():
    '''public void jdoCopyKeyFieldsToObjectId(final PersistenceCapable$ObjectIdFieldSupplier persistenceCapable$ObjectIdFieldSupplier, final Object o)
    public void jdoCopyKeyFieldsToObjectId(final Object o)
    '''
def jdoCopyKeyFieldsFromObjectId():
    '''public void jdoCopyKeyFieldsFromObjectId(final PersistenceCapable$ObjectIdFieldConsumer persistenceCapable$ObjectIdFieldConsumer, final Object o)
    public void jdoCopyKeyFieldsFromObjectId(final Object o)
    '''
def jdoNewObjectIdInstance():
    '''public Object jdoNewObjectIdInstance(final String guid)
    public Object jdoNewObjectIdInstance()
    '''
