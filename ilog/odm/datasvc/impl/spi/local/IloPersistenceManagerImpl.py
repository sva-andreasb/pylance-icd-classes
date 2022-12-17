COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
DEFAULT_ROW_COUNT = "int  100000"
def ():
    '''returns IloConnectionPerformanceCommand\n\n
    (final IloApplicationContext context, final IloAbstractDataManager data_manager)\n
    (final Class<?> repository_manager_class)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def getRepositoryManager():
    '''returns IloRepositoryManager\n\n
    getRepositoryManager()\n
    '''
def getPerformanceMetrics():
    '''returns IloPerformanceMetrics\n\n
    getPerformanceMetrics()\n
    getPerformanceMetrics()\n
    '''
def process():
    '''returns None\n\n
    process(final IloTransactionalSession session)\n
    '''
def postCommit():
    '''returns None\n\n
    postCommit(final IloTransactionalSession session, final boolean error)\n
    '''
def rollback():
    '''returns None\n\n
    rollback(final IloTransactionalSession session, final boolean error)\n
    '''
