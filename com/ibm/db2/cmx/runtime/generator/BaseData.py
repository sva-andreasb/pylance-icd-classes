SINGLE_ROW_PARAMETERS = "int  1"
MULTI_ROW_PARAMETERS = "int  2"
NO_PARAMETERS = "int  3"
SINGLE_ROW_RESULT = "int  4"
MULTI_ROW_RESULT = "int  5"
ALLOW_STATIC_ROWSET_CURSORS = "int  6"
DISALLOW_STATIC_ROWSET_CURSORS = "int  7"
def getGeneratorVersion():
    '''returns String\n\n
    getGeneratorVersion()\n
    '''
def checkCompatibleRuntimeVersion():
    '''returns None\n\n
    checkCompatibleRuntimeVersion(final String s)\n
    '''
def ():
    '''returns BaseData\n\n
    ()\n
    '''
def queryResults():
    '''returns ResultSet\n\n
    queryResults(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ?, ?> handlerContainer, final Object... array)\n
    queryResults(final String s, final Object... array)\n
    queryResults(final int n, final int n2, final int n3, final String s, final Object... array)\n
    queryResults(final StatementDescriptor statementDescriptor, final Object... array)\n
    '''
def update():
    '''returns int\n\n
    update(final StatementDescriptor statementDescriptor, final HandlerContainer<?, ?, ?> handlerContainer, final Object... array)\n
    update(final String s, final Object... array)\n
    update(final StatementDescriptor statementDescriptor, final Object... array)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def getAutoCommit():
    '''returns boolean\n\n
    getAutoCommit()\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    '''
def rollback():
    '''returns None\n\n
    rollback()\n
    '''
def setAutoCommit():
    '''returns None\n\n
    setAutoCommit(final boolean autoCommit)\n
    '''
def getData():
    '''returns Data\n\n
    getData()\n
    '''
def getStatementDescriptor():
    '''returns StatementDescriptor\n\n
    getStatementDescriptor(final String key)\n
    getStatementDescriptor(final String s, final String s2, final SqlStatementType sqlStatementType, final int n, final Object[] array)\n
    '''
def setData():
    '''returns None\n\n
    setData(final Data data)\n
    '''
def call():
    '''returns StoredProcedureResult\n\n
    call(final String s, final Object... array)\n
    '''
def updateMany():
    '''returns int[]\n\n
    updateMany(final String... array)\n
    '''
def getLogger():
    '''returns Logger\n\n
    getLogger()\n
    '''
def setLogger():
    '''returns None\n\n
    setLogger(final Logger logger_)\n
    '''
def endBatch():
    '''returns int[][]\n\n
    endBatch()\n
    '''
def cancelBatch():
    '''returns None\n\n
    cancelBatch()\n
    '''
def getBatchKind():
    '''returns HeterogeneousBatchKind\n\n
    getBatchKind()\n
    '''
def startBatch():
    '''returns None\n\n
    startBatch(final HeterogeneousBatchKind heterogeneousBatchKind)\n
    '''
def run():
    '''returns Field[]\n\n
    run()\n
    '''
