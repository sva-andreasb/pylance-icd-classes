def ():
    '''returns StatementDescriptorImpl\n\n
    (final String methodNameAndParameterTypesString_, final String s, final SqlStatementType sqlStatementType_, final int[] statementAttributes_, final String[] columnNames_, final ParameterHandler parameterHandler_, final int[][] parameterMetaData_, final ResultHandler resultHandler_, final RowHandler rowHandler_, final int[][] resultSetMetaData_, final CallHandler callHandler_, final CallHandlerWithParameters callHandlerWithParameters_, final String packageName_, final long n, final String collection_, final boolean forceSingleBindIsolation_, final String cursorName_, final int section_, final String id_)\n
    (final String methodNameAndParameterTypesString_, final String s, final SqlStatementType sqlStatementType_, final int[] statementAttributes_, final String[] columnNames_, final ParameterHandler parameterHandler_, final int[][] parameterMetaData_, final RowHandler rowHandler_, final int[][] resultSetMetaData_, final CallHandler callHandler_, final CallHandlerWithParameters callHandlerWithParameters_, final String packageName_, final String collection_, final long n, final int section_, final String id_)\n
    (final String methodNameAndParameterTypesString_, final int[] statementAttributes_, final String originalSql_, final SqlStatementType sqlStatementType_, final String[] columnNames_, final ParameterHandler parameterHandler_, final ResultHandler resultHandler_, final CallHandlerWithParameters callHandlerWithParameters_)\n
    '''
def getColumnNames():
    '''returns String[]\n\n
    getColumnNames()\n
    '''
def getProcessedSql():
    '''returns String\n\n
    getProcessedSql()\n
    '''
def getOriginalSql():
    '''returns String\n\n
    getOriginalSql()\n
    '''
def setColumnNames():
    '''returns None\n\n
    setColumnNames(final String[] columnNames_)\n
    '''
def setDynamicSQL():
    '''returns None\n\n
    setDynamicSQL(final String processedSql_)\n
    '''
def setOriginalSql():
    '''returns None\n\n
    setOriginalSql(final String originalSql_)\n
    '''
def getMethodNameAndParameterTypesString():
    '''returns String\n\n
    getMethodNameAndParameterTypesString()\n
    '''
def getParameterHandlerForInline():
    '''returns ParameterHandler\n\n
    getParameterHandlerForInline()\n
    '''
def getParameterHandler():
    '''returns ParameterHandler\n\n
    getParameterHandler(final HandlerContainer<?, ?, ?> handlerContainer)\n
    '''
def getMethodInfoArray():
    '''returns ParameterInfoArray\n\n
    getMethodInfoArray()\n
    '''
def setMethodInfoArray():
    '''returns None\n\n
    setMethodInfoArray(final ParameterInfoArray parameterInfoArray_)\n
    '''
def getCallHandler():
    '''returns CallHandler\n\n
    getCallHandler()\n
    '''
def setCallHandler():
    '''returns None\n\n
    setCallHandler(final CallHandler callHandler_)\n
    '''
def setCallHandlerWithParameters():
    '''returns None\n\n
    setCallHandlerWithParameters(final CallHandlerWithParameters callHandlerWithParameters_)\n
    '''
def getSqlStatementType():
    '''returns SqlStatementType\n\n
    getSqlStatementType()\n
    '''
def setSqlStatementType():
    '''returns None\n\n
    setSqlStatementType(final SqlStatementType sqlStatementType_)\n
    '''
def getSection():
    '''returns int\n\n
    getSection()\n
    '''
def setSection():
    '''returns None\n\n
    setSection(final int section_)\n
    '''
def getParameterMetaData():
    '''returns int[][]\n\n
    getParameterMetaData()\n
    '''
def setParameterMetaDataAndParameterTypeInMethod():
    '''returns None\n\n
    setParameterMetaDataAndParameterTypeInMethod(final PreparedStatement preparedStatement, final Object... array)\n
    '''
def isParameterMetaDataPresent():
    '''returns boolean\n\n
    isParameterMetaDataPresent()\n
    '''
def getParameterMetaDataType():
    '''returns int[]\n\n
    getParameterMetaDataType(final boolean b)\n
    '''
def getParameterMetaDataPrecision():
    '''returns int[]\n\n
    getParameterMetaDataPrecision()\n
    '''
def getParameterMetaDataScale():
    '''returns int[]\n\n
    getParameterMetaDataScale()\n
    '''
def getParameterMetaDataMode():
    '''returns int[]\n\n
    getParameterMetaDataMode()\n
    '''
def getResultSetMetaData():
    '''returns int[][]\n\n
    getResultSetMetaData()\n
    '''
def setResultSetMetaData():
    '''returns None\n\n
    setResultSetMetaData(final int[][] resultSetMetaData_)\n
    '''
def isResultSetMetaDataPresent():
    '''returns boolean\n\n
    isResultSetMetaDataPresent()\n
    '''
def getResultSetMetaDataType():
    '''returns int[]\n\n
    getResultSetMetaDataType(final boolean b)\n
    '''
def getResultSetMetaDataPrecision():
    '''returns int[]\n\n
    getResultSetMetaDataPrecision()\n
    '''
def getResultSetMetaDataScale():
    '''returns int[]\n\n
    getResultSetMetaDataScale()\n
    '''
def getResultSetMetaDataCCSID():
    '''returns int[]\n\n
    getResultSetMetaDataCCSID()\n
    '''
def getResultSetMetaDataColumnCount():
    '''returns int\n\n
    getResultSetMetaDataColumnCount()\n
    '''
def getCollection():
    '''returns String\n\n
    getCollection()\n
    '''
def setCollection():
    '''returns None\n\n
    setCollection(final String collection_)\n
    '''
def getConsistencyToken():
    '''returns byte[]\n\n
    getConsistencyToken()\n
    '''
def setConsistencyToken():
    '''returns None\n\n
    setConsistencyToken(final byte[] consistencyToken_)\n
    '''
def getPackageName():
    '''returns String\n\n
    getPackageName()\n
    '''
def setPackageName():
    '''returns None\n\n
    setPackageName(final String packageName_)\n
    '''
def getStatementAttributes():
    '''returns int[]\n\n
    getStatementAttributes()\n
    '''
def setStatementAttributes():
    '''returns None\n\n
    setStatementAttributes(final int[] statementAttributes_)\n
    '''
def hasMutiRowParameters():
    '''returns boolean\n\n
    hasMutiRowParameters()\n
    '''
def hasSingleRowResult():
    '''returns boolean\n\n
    hasSingleRowResult()\n
    '''
def getConcurrency():
    '''returns int\n\n
    getConcurrency()\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def getHoldability():
    '''returns int\n\n
    getHoldability()\n
    '''
def isAllowStaticRowsetCursors():
    '''returns boolean\n\n
    isAllowStaticRowsetCursors()\n
    '''
def getResultSetMetaDataColNames():
    '''returns String[]\n\n
    getResultSetMetaDataColNames()\n
    '''
def setResultSetMetaDataColNames():
    '''returns None\n\n
    setResultSetMetaDataColNames(final String[] resultSetMetaDataColNames_)\n
    '''
def setParameterTypeinMethod():
    '''returns None\n\n
    setParameterTypeinMethod(final JdbcData.InputParameterType[] parameterTypeinMethod_)\n
    '''
def isSELECTorVALUESorXQUERYorSINGLEROWQUERY():
    '''returns boolean\n\n
    isSELECTorVALUESorXQUERYorSINGLEROWQUERY()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def setId():
    '''returns None\n\n
    setId(final String id_)\n
    '''
def getCursorName():
    '''returns String\n\n
    getCursorName()\n
    '''
def setCursorName():
    '''returns None\n\n
    setCursorName(final String cursorName_)\n
    '''
def isForceSingleBindIsolation():
    '''returns boolean\n\n
    isForceSingleBindIsolation()\n
    '''
def setForceSingleBindIsolation():
    '''returns None\n\n
    setForceSingleBindIsolation(final Boolean b)\n
    '''
