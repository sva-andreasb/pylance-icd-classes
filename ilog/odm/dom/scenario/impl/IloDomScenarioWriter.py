COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDomScenarioWriter\n\n
    (final IloScenario scenario, final Collection<String> outputTables)\n
    (final IloScenario scenario, final Collection<String> outputTables, final int blockSize)\n
    '''
def begin():
    '''returns None\n\n
    begin()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def putRecord():
    '''returns None\n\n
    putRecord(final IloDomRecord domRecord)\n
    '''
def setStoreScenarioEvents():
    '''returns None\n\n
    setStoreScenarioEvents(final boolean storeEvents)\n
    '''
def getStoreScenarioEvents():
    '''returns boolean\n\n
    getStoreScenarioEvents()\n
    '''
def beginModifications():
    '''returns None\n\n
    beginModifications(final String tableName, final int size)\n
    '''
def endModifications():
    '''returns None\n\n
    endModifications(final String tableName)\n
    '''
