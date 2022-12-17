def ():
    '''returns PersistentObjectJdo\n\n
    ()\n
    (final Guid guid, final String className)\n
    '''
def getGuid():
    '''returns Guid\n\n
    getGuid()\n
    '''
def getClassName():
    '''returns String\n\n
    getClassName()\n
    '''
def setClassName():
    '''returns None\n\n
    setClassName(final String className)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final String type)\n
    '''
def getHwType():
    '''returns String\n\n
    getHwType()\n
    '''
def setHwType():
    '''returns None\n\n
    setHwType(final String type)\n
    '''
def getVersioned():
    '''returns boolean\n\n
    getVersioned()\n
    '''
def setVersioned():
    '''returns None\n\n
    setVersioned(final boolean versioned)\n
    '''
def getArchived():
    '''returns boolean\n\n
    getArchived()\n
    '''
def setArchived():
    '''returns None\n\n
    setArchived(final boolean archived)\n
    '''
def getDeleted():
    '''returns boolean\n\n
    getDeleted()\n
    '''
def setDeleted():
    '''returns None\n\n
    setDeleted(final boolean deleted)\n
    '''
def getCmdbSource():
    '''returns Guid\n\n
    getCmdbSource()\n
    '''
def setCmdbSource():
    '''returns None\n\n
    setCmdbSource(final Guid cmdbSource)\n
    '''
def getRunId():
    '''returns long\n\n
    getRunId()\n
    '''
def setRunId():
    '''returns None\n\n
    setRunId(final long runId)\n
    '''
def getLastModifiedTime():
    '''returns long\n\n
    getLastModifiedTime()\n
    '''
def setLastModifiedTime():
    '''returns None\n\n
    setLastModifiedTime(final long lastModifiedTime)\n
    '''
def jdoNewInstance():
    '''returns PersistenceCapable\n\n
    jdoNewInstance(final StateManager jdoStateManager, final Object o)\n
    jdoNewInstance(final StateManager jdoStateManager)\n
    '''
def jdoReplaceField():
    '''returns None\n\n
    jdoReplaceField(final int n)\n
    '''
def jdoReplaceFields():
    '''returns None\n\n
    jdoReplaceFields(final int[] array)\n
    '''
def jdoProvideField():
    '''returns None\n\n
    jdoProvideField(final int n)\n
    '''
def jdoProvideFields():
    '''returns None\n\n
    jdoProvideFields(final int[] array)\n
    '''
def jdoCopyFields():
    '''returns None\n\n
    jdoCopyFields(final Object o, final int[] array)\n
    '''
def jdoGetPersistenceManager():
    '''returns PersistenceManager\n\n
    jdoGetPersistenceManager()\n
    '''
def jdoGetObjectId():
    '''returns Object\n\n
    jdoGetObjectId()\n
    '''
def jdoGetTransactionalObjectId():
    '''returns Object\n\n
    jdoGetTransactionalObjectId()\n
    '''
def jdoIsDeleted():
    '''returns boolean\n\n
    jdoIsDeleted()\n
    '''
def jdoIsDirty():
    '''returns boolean\n\n
    jdoIsDirty()\n
    '''
def jdoIsNew():
    '''returns boolean\n\n
    jdoIsNew()\n
    '''
def jdoIsPersistent():
    '''returns boolean\n\n
    jdoIsPersistent()\n
    '''
def jdoIsTransactional():
    '''returns boolean\n\n
    jdoIsTransactional()\n
    '''
def jdoPreSerialize():
    '''returns None\n\n
    jdoPreSerialize()\n
    '''
def jdoMakeDirty():
    '''returns None\n\n
    jdoMakeDirty(final String s)\n
    '''
def jdoReplaceFlags():
    '''returns None\n\n
    jdoReplaceFlags()\n
    '''
def jdoCopyKeyFieldsToObjectId():
    '''returns None\n\n
    jdoCopyKeyFieldsToObjectId(final PersistenceCapable$ObjectIdFieldSupplier persistenceCapable$ObjectIdFieldSupplier, final Object o)\n
    jdoCopyKeyFieldsToObjectId(final Object o)\n
    '''
def jdoCopyKeyFieldsFromObjectId():
    '''returns None\n\n
    jdoCopyKeyFieldsFromObjectId(final PersistenceCapable$ObjectIdFieldConsumer persistenceCapable$ObjectIdFieldConsumer, final Object o)\n
    jdoCopyKeyFieldsFromObjectId(final Object o)\n
    '''
def jdoNewObjectIdInstance():
    '''returns Object\n\n
    jdoNewObjectIdInstance(final String guid)\n
    jdoNewObjectIdInstance()\n
    '''
