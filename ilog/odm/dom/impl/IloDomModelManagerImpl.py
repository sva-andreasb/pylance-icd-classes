COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDomModelManagerImpl\n\n
    (final String modelid)\n
    (final String modelid, final IloDomFactory factory)\n
    '''
def getResource():
    '''returns IloDomResourceImpl\n\n
    getResource()\n
    '''
def getResourceSet():
    '''returns IloDomResourceSetImpl\n\n
    getResourceSet()\n
    '''
def assertConcreteEntity():
    '''returns None\n\n
    assertConcreteEntity(final Class<? extends IloDomObject> entity)\n
    '''
def getCollector():
    '''returns Collector\n\n
    getCollector()\n
    '''
def loadSnapshot():
    '''returns None\n\n
    loadSnapshot(final URL data)\n
    loadSnapshot(final URL data, final Collection<Class<? extends IloDomObject>> entities)\n
    loadSnapshot(final File data)\n
    '''
def saveSnapshot():
    '''returns None\n\n
    saveSnapshot(final URL data)\n
    saveSnapshot(final URL data, final Collection<Class<? extends IloDomObject>> entities)\n
    saveSnapshot(final File data)\n
    '''
def loadSnapshotConcrete():
    '''returns None\n\n
    loadSnapshotConcrete(final URL data, final Collection<Class<? extends IloDomObject>> entities)\n
    '''
def saveSnapshotConcrete():
    '''returns None\n\n
    saveSnapshotConcrete(final URL data, final Collection<Class<? extends IloDomObject>> entities)\n
    '''
def saveObjectsToSnapshot():
    '''returns None\n\n
    saveObjectsToSnapshot(final URL data, final Collection<IloDomObject> objects)\n
    '''
def getModelId():
    '''returns String\n\n
    getModelId()\n
    '''
def getEntityObjects():
    '''returns List<IloDomObject>\n\n
    getEntityObjects(final Class<? extends IloDomObject> entity)\n
    '''
def deleteObjectAndReferences():
    '''returns None\n\n
    deleteObjectAndReferences(final IloDomObject obj)\n
    '''
def deleteObject():
    '''returns None\n\n
    deleteObject(final IloDomObject obj)\n
    '''
def deleteEntityObjects():
    '''returns None\n\n
    deleteEntityObjects(final Class<? extends IloDomObject> entity)\n
    '''
def deleteEntityObjectsAndReferences():
    '''returns None\n\n
    deleteEntityObjectsAndReferences(final Class<? extends IloDomObject> entity)\n
    '''
def bulkDeleteEntityObjects():
    '''returns None\n\n
    bulkDeleteEntityObjects(final Class<? extends IloDomObject> entity)\n
    '''
def bulkDeleteEntityObjectsAndReferences():
    '''returns None\n\n
    bulkDeleteEntityObjectsAndReferences(final Class<? extends IloDomObject> entity)\n
    '''
def bulkDeleteAllObjects():
    '''returns None\n\n
    bulkDeleteAllObjects()\n
    '''
def deleteAllObjects():
    '''returns None\n\n
    deleteAllObjects()\n
    '''
def listUnresolvedReferences():
    '''returns List<IloDomUnresolvedReference>\n\n
    listUnresolvedReferences()\n
    listUnresolvedReferences(final Collection<Class<? extends IloDomObject>> scope)\n
    '''
def unloadEntity():
    '''returns None\n\n
    unloadEntity(final Class<? extends IloDomObject> entity)\n
    '''
def unloadEntityConcrete():
    '''returns None\n\n
    unloadEntityConcrete(final Class<? extends IloDomObject> entity)\n
    '''
def getFactory():
    '''returns IloDomFactory\n\n
    getFactory()\n
    '''
def createObjectKey():
    '''returns IloDomObjectKey\n\n
    createObjectKey(final Class<? extends IloDomObject> entity, final Object[] keyParts)\n
    '''
def getObjectByKey():
    '''returns IloDomObject\n\n
    getObjectByKey(final IloDomObjectKey key)\n
    '''
def isApplicable():
    '''returns boolean\n\n
    isApplicable(final Class<? extends IloDomObject> entity)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def scrambleSnapshot():
    '''returns None\n\n
    scrambleSnapshot(final URL input, final URL output)\n
    '''
def getDomEntityClass():
    '''returns IloDomEntityClass\n\n
    getDomEntityClass(final Class<? extends IloDomObject> entity)\n
    '''
def indexEntity():
    '''returns None\n\n
    indexEntity(final Class<? extends IloDomObject> entity)\n
    '''
def isEntityIndexed():
    '''returns boolean\n\n
    isEntityIndexed(final Class<? extends IloDomObject> entity)\n
    '''
def getModel():
    '''returns IloDomModel\n\n
    getModel()\n
    '''
def scrambleRecord():
    '''returns IloDomRecord\n\n
    scrambleRecord(final IloDomRecord r)\n
    '''
def setDuplicationCheck():
    '''returns None\n\n
    setDuplicationCheck(final boolean duplicationCheck)\n
    '''
