COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def isScenarioInBulkModifications():
    '''returns boolean\n\n
    isScenarioInBulkModifications()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def getUserData():
    '''returns Object\n\n
    getUserData()\n
    '''
def ():
    '''returns IloDomSynchronizedModelManagerImpl\n\n
    (final String modelid)\n
    (final String modelid, final IloDomFactory factory)\n
    '''
def setInputMode():
    '''returns None\n\n
    setInputMode(final Class<? extends IloDomObject> entity, final IloDomInputMode mode)\n
    setInputMode(final Collection<Class<? extends IloDomObject>> entities, final IloDomInputMode mode)\n
    '''
def getInputMode():
    '''returns IloDomInputMode\n\n
    getInputMode(final Class<? extends IloDomObject> entity)\n
    '''
def setOutputMode():
    '''returns None\n\n
    setOutputMode(final Class<? extends IloDomObject> entity, final IloDomOutputMode mode)\n
    setOutputMode(final Collection<Class<? extends IloDomObject>> entities, final IloDomOutputMode mode)\n
    '''
def getOutputMode():
    '''returns IloDomOutputMode\n\n
    getOutputMode(final Class<? extends IloDomObject> entity)\n
    '''
def connect():
    '''returns None\n\n
    connect(final ilog.odm.datasvc.IloScenario scenario)\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect(final boolean abort)\n
    '''
def recordBeginModifications():
    '''returns None\n\n
    recordBeginModifications(final String label, final IloDomModelChangeEvent event)\n
    '''
def recordEndModifications():
    '''returns None\n\n
    recordEndModifications()\n
    '''
def recordChanged():
    '''returns None\n\n
    recordChanged(final IloDomRecord record, final int col)\n
    '''
def deleteObject():
    '''returns None\n\n
    deleteObject(final IloDomObject obj)\n
    '''
def deleteEntityObjects():
    '''returns None\n\n
    deleteEntityObjects(final Class<? extends IloDomObject> entity)\n
    '''
def deleteObjectAndRefences():
    '''returns None\n\n
    deleteObjectAndRefences(final IloDomObject obj)\n
    '''
def deleteEntityObjectsAndReferences():
    '''returns None\n\n
    deleteEntityObjectsAndReferences(final Class<? extends IloDomObject> entity)\n
    '''
def deleteAllObjects():
    '''returns None\n\n
    deleteAllObjects()\n
    '''
def loadSnapshot():
    '''returns None\n\n
    loadSnapshot(final URL data, final Collection<Class<? extends IloDomObject>> entities)\n
    '''
def saveSnapshot():
    '''returns None\n\n
    saveSnapshot(final URL data, final Collection<Class<? extends IloDomObject>> entities)\n
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
def setUpdateScenarioBlockSize():
    '''returns None\n\n
    setUpdateScenarioBlockSize(final int blockSize)\n
    '''
def getUpdateScenarioBlockSize():
    '''returns int\n\n
    getUpdateScenarioBlockSize()\n
    '''
def setStoreScenarioEvents():
    '''returns None\n\n
    setStoreScenarioEvents(final boolean storeEvents)\n
    '''
def getStoreScenarioEvents():
    '''returns boolean\n\n
    getStoreScenarioEvents()\n
    '''
def canExecute():
    '''returns boolean\n\n
    canExecute()\n
    '''
def isSynchronized():
    '''returns boolean\n\n
    isSynchronized(final Class<? extends IloDomObject> entity)\n
    '''
def synchronize():
    '''returns None\n\n
    synchronize(final Collection<Class<? extends IloDomObject>> entities)\n
    synchronize(final Class<? extends IloDomObject> entity)\n
    '''
def desynchronize():
    '''returns None\n\n
    desynchronize(final Collection<Class<? extends IloDomObject>> entities)\n
    desynchronize(final Class<? extends IloDomObject> entity)\n
    '''
def getDataLocation():
    '''returns IloDataLocation\n\n
    getDataLocation(final IloDomObject obj)\n
    '''
def getObject():
    '''returns IloDomObject\n\n
    getObject(final IloDataLocation location)\n
    '''
def setProcessingTransaction():
    '''returns None\n\n
    setProcessingTransaction(final boolean processingTransaction)\n
    '''
def isProcessingTransaction():
    '''returns boolean\n\n
    isProcessingTransaction()\n
    '''
def beginModifications():
    '''returns None\n\n
    beginModifications()\n
    '''
def endModifications():
    '''returns None\n\n
    endModifications()\n
    '''
def notifyChanged():
    '''returns None\n\n
    notifyChanged(final IloScenarioEvent evt)\n
    '''
