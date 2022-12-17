COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloDomRecordTransactionListenerImpl\n\n
    (final IloScenario scenario, final boolean storeEvents)\n
    '''
def beginModifications():
    '''returns None\n\n
    beginModifications(final String label, final IloDomModelChangeEvent event)\n
    beginModifications(final IloDomModelChangeEvent event)\n
    '''
def recordAdded():
    '''returns IloDomRecord\n\n
    recordAdded(final IloDomRecord record, final int index)\n
    '''
def tableDeleted():
    '''returns None\n\n
    tableDeleted(final String tableName)\n
    '''
def recordDeleted():
    '''returns None\n\n
    recordDeleted(final IloDomRecord record, final int index)\n
    '''
def recordChanged():
    '''returns None\n\n
    recordChanged(final IloDomRecord record, final int column)\n
    '''
def endModifications():
    '''returns None\n\n
    endModifications()\n
    '''
def getStoreScenarioEvents():
    '''returns boolean\n\n
    getStoreScenarioEvents()\n
    '''
