def ():
    '''returns DB2JdbcData\n\n
    (final Connection connection, final Hook hook, final Map<Object, Object> map, final Integer n, final Integer n2, final DatabaseMetaData databaseMetaData)\n
    '''
def setConnection():
    '''returns None\n\n
    setConnection(final Connection connection)\n
    '''
def getListOfHeteroBatchStmts():
    '''returns ArrayList<DB2PreparedStatement>\n\n
    getListOfHeteroBatchStmts()\n
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
    '''returns Method\n\n
    run()\n
    '''
