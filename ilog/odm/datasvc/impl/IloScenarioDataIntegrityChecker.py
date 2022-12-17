COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
CHECKDATA_DYNAMIC_INDEX_PROPERTY = "String  \"CHECKDATA_DYNAMIC_INDEX\""
DEFAULT_CHECKDATA_DYNAMIC_INDEX = "boolean  true"
def ():
    '''returns IloScenarioDataIntegrityChecker\n\n
    (final IloTransactionalSession session, final Collection<String> tableIds)\n
    '''
def check():
    '''returns None\n\n
    check(final IloScenario scenario)\n
    '''
def getSkippedCount():
    '''returns int\n\n
    getSkippedCount()\n
    '''
def getIndexedCount():
    '''returns int\n\n
    getIndexedCount()\n
    '''
