COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDomScenarioModelManagerImpl\n\n
    (final String modelid)\n
    (final String modelid, final IloDomFactory factory)\n
    '''
def getScenario():
    '''returns IloScenario\n\n
    getScenario()\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
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
def connect():
    '''returns None\n\n
    connect(final IloScenario scenario)\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect(final boolean abort)\n
    '''
def load():
    '''returns None\n\n
    load(final Class<? extends IloDomObject> entity)\n
    load(final Collection<Class<? extends IloDomObject>> entities)\n
    '''
def save():
    '''returns None\n\n
    save(final Class<? extends IloDomObject> entity)\n
    save(final Collection<Class<? extends IloDomObject>> entities)\n
    '''
def saveDisconnect():
    '''returns None\n\n
    saveDisconnect(final Collection<Class<? extends IloDomObject>> entities)\n
    '''
def saveDisconnectPerTable():
    '''returns None\n\n
    saveDisconnectPerTable(final Collection<Class<? extends IloDomObject>> entities)\n
    '''
def getDataLocation():
    '''returns IloDataLocation\n\n
    getDataLocation(final IloDomObject obj)\n
    '''
def getObject():
    '''returns IloDomObject\n\n
    getObject(final IloDataLocation location)\n
    '''
