def ():
    '''returns SqlStatementInfo\n\n
    (final ConnectionExecutionHandler connectionExecutionHandler)\n
    ()\n
    '''
def resetCaptureHelperStatesX():
    '''returns None\n\n
    resetCaptureHelperStatesX(final ConnectionExecutionHandler connectionExecutionHandler)\n
    '''
def resetCaptureHelperStates():
    '''returns None\n\n
    resetCaptureHelperStates(final ConnectionExecutionHandler connectionExecutionHandler)\n
    '''
def getLiteralSubstitutionSpecifiedInFile():
    '''returns String\n\n
    getLiteralSubstitutionSpecifiedInFile()\n
    '''
def initRuntimeMapForStaticExecution():
    '''returns None\n\n
    initRuntimeMapForStaticExecution(final ConnectionExecutionHandler connectionExecutionHandler)\n
    '''
def determineIfStmtAlreadyCaptured():
    '''returns boolean\n\n
    determineIfStmtAlreadyCaptured(final SqlStatementKey sqlStatementKey)\n
    '''
def incrementExecutionCountMRIAndSRSet():
    '''returns None\n\n
    incrementExecutionCountMRIAndSRSet(final ConnectionExecutionHandler connectionExecutionHandler, final SqlStatementInfo sqlStatementInfo, final boolean b, final SqlStatementType sqlStatementType, final long n, final long n2, final int n3, final int maxRowsIncrementalValue)\n
    '''
def recordQueryStmt():
    '''returns SqlStatementInfo\n\n
    recordQueryStmt(final ConnectionExecutionHandler connectionExecutionHandler, final String s, final Object o, final Object o2, final SqlStatementKey sqlStatementKey, final String s2, final String s3, final String[] array, final SqlStatementType sqlStatementType, final String[][] array2, final String[][] array3, final HashMap<String, int[]> hashMap, final long n, final long n2, final int n3, final int n4)\n
    '''
def recordNonQueryStmt():
    '''returns SqlStatementInfo\n\n
    recordNonQueryStmt(final ConnectionExecutionHandler connectionExecutionHandler, final String s, final Object o, final Object o2, final SqlStatementKey sqlStatementKey, final String s2, final String[] array, final SqlStatementType sqlStatementType, final Boolean b, final String[][] array2, final String[][] array3, final HashMap<String, int[]> hashMap, final String s3, final long n, final long n2, final int n3)\n
    '''
def captureDefinitionTrace():
    '''returns None\n\n
    captureDefinitionTrace(final String[][] array, final SqlStatementInfo sqlStatementInfo)\n
    '''
def captureExecutionTrace():
    '''returns None\n\n
    captureExecutionTrace(final String[][] array, final SqlStatementInfo sqlStatementInfo)\n
    '''
def captureTrace():
    '''returns None\n\n
    captureTrace(final String[][] array, final String[][] array2, final int n, final SqlStatementInfo sqlStatementInfo)\n
    '''
def captureBatchingExecutionTrace():
    '''returns None\n\n
    captureBatchingExecutionTrace(final ArrayList<SqlStatementKey> list, final Integer n, final int n2, final String[] array)\n
    '''
def createMultiLevelTraceInfo():
    '''returns String[][]\n\n
    createMultiLevelTraceInfo(final Integer n, final String[] array)\n
    '''
def UpdateNonParameterizedSqlCountNotCaptured():
    '''returns None\n\n
    UpdateNonParameterizedSqlCountNotCaptured(final int i)\n
    '''
def sqlStatementCaptureOrUpdate():
    '''returns None\n\n
    sqlStatementCaptureOrUpdate(final boolean b)\n
    '''
def incrementMinorChangesCount():
    '''returns None\n\n
    incrementMinorChangesCount()\n
    '''
def setCaptureRecord():
    '''returns None\n\n
    setCaptureRecord(final Element captureElement_)\n
    '''
def getCaptureRecord():
    '''returns Element\n\n
    getCaptureRecord()\n
    '''
def getProcessedSQL():
    '''returns String\n\n
    getProcessedSQL(final SqlStatementKey sqlStatementKey)\n
    getProcessedSQL()\n
    '''
def serializeDOMIfAny():
    '''returns None\n\n
    serializeDOMIfAny()\n
    '''
def run():
    '''returns ProfilerShutDownHook\n\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    run()\n
    '''
def computeSqlIndexInOutputFile():
    '''returns int\n\n
    computeSqlIndexInOutputFile(final SqlStatementKey sqlStatementKey)\n
    '''
def getMetadataCorrelator():
    '''returns String\n\n
    getMetadataCorrelator(final SqlStatementKey sqlStatementKey)\n
    getMetadataCorrelator()\n
    '''
def isDbNameSet():
    '''returns boolean\n\n
    isDbNameSet()\n
    '''
def isSchemaNameSet():
    '''returns boolean\n\n
    isSchemaNameSet()\n
    '''
def isUserNameSet():
    '''returns boolean\n\n
    isUserNameSet()\n
    '''
def setDbNameSet():
    '''returns None\n\n
    setDbNameSet()\n
    '''
def setSchemaNameSet():
    '''returns None\n\n
    setSchemaNameSet()\n
    '''
def setUserNameSet():
    '''returns None\n\n
    setUserNameSet()\n
    '''
def setDbAndSchemaNameAndUserName():
    '''returns None\n\n
    setDbAndSchemaNameAndUserName(final String s, final String s2, final String s3)\n
    '''
def createAndStoreStmtInfo():
    '''returns SqlStatementInfo\n\n
    createAndStoreStmtInfo(final ConnectionExecutionHandler connectionExecutionHandler, final SqlStatementKey sqlStatementKey, final String sqlString, final String[] sqlStrings, final Object parameterMetaData, final Object resultSetMetaData, final String cursorName, final String cursorAttributes, final SqlStatementType sqlType, final boolean isMRI, final HashMap<String, int[]> markerMap, final String posUpdateCursor, final String referencedQueryKey, final String[][] array, final String[][] array2, final int n, final int n2, final long stmtExecutionTime, final long batchExecutionTime, final int batchCount, final int maxRowsIncrementalValue)\n
    '''
def getXmlOutputFileHelper():
    '''returns XmlFileHelper\n\n
    getXmlOutputFileHelper()\n
    '''
def updateOrdinalPosition():
    '''returns None\n\n
    updateOrdinalPosition(final SqlStatementInfo sqlStatementInfo, final int n)\n
    '''
def generateAndCaptureSpecialRegSet():
    '''returns None\n\n
    generateAndCaptureSpecialRegSet(final ConnectionExecutionHandler connectionExecutionHandler)\n
    '''
def captureSetSpecialRegisterMethods():
    '''returns None\n\n
    captureSetSpecialRegisterMethods(final ConnectionExecutionHandler connectionExecutionHandler, final String s)\n
    '''
def checkForStaticPreparedStatementNotFound():
    '''returns None\n\n
    checkForStaticPreparedStatementNotFound(final SqlStatementKey sqlStatementKey, final SqlStatementKey sqlStatementKey2, final PreparedStatementExecutionHandler preparedStatementExecutionHandler)\n
    '''
def getXmlInputCaptureKey():
    '''returns CentralStoreKey\n\n
    getXmlInputCaptureKey()\n
    '''
def resetcaptureSessionStatementSetInitialized():
    '''returns None\n\n
    resetcaptureSessionStatementSetInitialized()\n
    '''
def getIsInitialized():
    '''returns boolean\n\n
    getIsInitialized()\n
    '''
def setIsInitialized():
    '''returns None\n\n
    setIsInitialized()\n
    '''
def setSQLStmtLiteralReplacement():
    '''returns None\n\n
    setSQLStmtLiteralReplacement(final short sqlLiteralSubstitionCRS)\n
    '''
def isStatementInfoCaptured():
    '''returns boolean\n\n
    isStatementInfoCaptured()\n
    '''
def setStatementInfoCaptured():
    '''returns None\n\n
    setStatementInfoCaptured(final boolean isStatementInfoCaptured_)\n
    '''
def getOutputStatementOrIncrementElement():
    '''returns Element\n\n
    getOutputStatementOrIncrementElement()\n
    '''
def setOutputStatementOrIncrementElement():
    '''returns None\n\n
    setOutputStatementOrIncrementElement(final Element outputStatementOrIncrementElement_)\n
    '''
def getSqlString():
    '''returns String\n\n
    getSqlString()\n
    '''
def setSqlString():
    '''returns None\n\n
    setSqlString(final String sqlString_)\n
    '''
def getParameterMetaData():
    '''returns Object\n\n
    getParameterMetaData()\n
    '''
def setParameterMetaData():
    '''returns None\n\n
    setParameterMetaData(final Object parameterMetaData_)\n
    '''
def getResultSetMetaData():
    '''returns Object\n\n
    getResultSetMetaData()\n
    '''
def setResultSetMetaData():
    '''returns None\n\n
    setResultSetMetaData(final Object resultSetMetaData_)\n
    '''
def getCursorName():
    '''returns String\n\n
    getCursorName()\n
    '''
def setCursorName():
    '''returns None\n\n
    setCursorName(final String cursorName_)\n
    '''
def getPosUpdateCursor():
    '''returns String\n\n
    getPosUpdateCursor()\n
    '''
def setPosUpdateCursor():
    '''returns None\n\n
    setPosUpdateCursor(final String posUpdateCursor_)\n
    '''
def getCursorAttributes():
    '''returns String\n\n
    getCursorAttributes()\n
    '''
def setCursorAttributes():
    '''returns None\n\n
    setCursorAttributes(final String cursorAttributes_)\n
    '''
def getSqlStrings():
    '''returns String[]\n\n
    getSqlStrings()\n
    '''
def setSqlStrings():
    '''returns None\n\n
    setSqlStrings(final String[] sqlStrings_)\n
    '''
def getSqlType():
    '''returns SqlStatementType\n\n
    getSqlType()\n
    '''
def setSqlType():
    '''returns None\n\n
    setSqlType(final SqlStatementType sqlType_)\n
    '''
def isMRI():
    '''returns boolean\n\n
    isMRI()\n
    '''
def setIsMRI():
    '''returns None\n\n
    setIsMRI(final boolean isMRI_)\n
    '''
def setMarkerMap():
    '''returns None\n\n
    setMarkerMap(final HashMap<String, int[]> markerMap_)\n
    '''
def getReferencedQueryKey():
    '''returns String\n\n
    getReferencedQueryKey()\n
    '''
def setReferencedQueryKey():
    '''returns None\n\n
    setReferencedQueryKey(final String referencedQueryKey_)\n
    '''
def getIncrSpecialRegValuesUsed():
    '''returns int\n\n
    getIncrSpecialRegValuesUsed()\n
    '''
def setIncrSpecialRegValuesUsed():
    '''returns None\n\n
    setIncrSpecialRegValuesUsed(final int incrSpecialRegValuesUsed_)\n
    '''
def setProcessedSQL():
    '''returns None\n\n
    setProcessedSQL(final String processedSQL_, final boolean b)\n
    '''
def isProcessedSQLSetInXML():
    '''returns boolean\n\n
    isProcessedSQLSetInXML()\n
    '''
def setNamedParamInfoMap():
    '''returns None\n\n
    setNamedParamInfoMap(final HashMap<String, ArrayList<Integer>> namedParameterInfo_)\n
    '''
def setMetadataCorrelator():
    '''returns None\n\n
    setMetadataCorrelator(final String s, final String s2, final String s3)\n
    '''
def setDefTraceHashcodeList():
    '''returns None\n\n
    setDefTraceHashcodeList(final ArrayList<Integer> defTraceHashCodeList_)\n
    '''
def getDefTraceHashcodeList():
    '''returns ArrayList<Integer>\n\n
    getDefTraceHashcodeList()\n
    '''
def setExeTraceHashcodeList():
    '''returns None\n\n
    setExeTraceHashcodeList(final ArrayList<Integer> exeTraceHashCodeList_)\n
    '''
def getExeTraceHashcodeList():
    '''returns ArrayList<Integer>\n\n
    getExeTraceHashcodeList()\n
    '''
def getRelativeOrdinalPosition():
    '''returns int\n\n
    getRelativeOrdinalPosition()\n
    '''
def addDefTrace():
    '''returns None\n\n
    addDefTrace(final String[][] e)\n
    '''
def cleanDefTraces():
    '''returns None\n\n
    cleanDefTraces()\n
    '''
def addExeTrace():
    '''returns None\n\n
    addExeTrace(final String[][] e)\n
    '''
def cleanExeTraces():
    '''returns None\n\n
    cleanExeTraces()\n
    '''
def getDefTraces():
    '''returns ArrayList<String[][]>\n\n
    getDefTraces()\n
    '''
def getExeTraces():
    '''returns ArrayList<String[][]>\n\n
    getExeTraces()\n
    '''
def incrementDeltaExecutionCount():
    '''returns None\n\n
    incrementDeltaExecutionCount()\n
    '''
def getDeltaExecutionCount():
    '''returns int\n\n
    getDeltaExecutionCount()\n
    '''
def resetDeltaExecutionCount():
    '''returns None\n\n
    resetDeltaExecutionCount()\n
    '''
def setDeltaExecutionCount():
    '''returns None\n\n
    setDeltaExecutionCount(final int deltaExecutionCount_)\n
    '''
def setMRIIndicator():
    '''returns None\n\n
    setMRIIndicator()\n
    '''
def getMRIIndicator():
    '''returns boolean\n\n
    getMRIIndicator()\n
    '''
def setStmtId():
    '''returns None\n\n
    setStmtId(final int stmtId_)\n
    '''
def getStmtId():
    '''returns int\n\n
    getStmtId()\n
    '''
def getIncrementalSRIds():
    '''returns String\n\n
    getIncrementalSRIds()\n
    '''
def addToIncrementalSRId():
    '''returns None\n\n
    addToIncrementalSRId(final String s)\n
    '''
def setIncrementalSRIds():
    '''returns None\n\n
    setIncrementalSRIds(final String incrementalSRIds_)\n
    '''
def setSRIds():
    '''returns None\n\n
    setSRIds(final String srIds_)\n
    '''
def getSRIds():
    '''returns String\n\n
    getSRIds()\n
    '''
def setBaseIncrementsOrdinalPos_():
    '''returns None\n\n
    setBaseIncrementsOrdinalPos_(final int baseIncrementsOrdinalPos_)\n
    '''
def getBaseIncrementsOrdinalPos_():
    '''returns int\n\n
    getBaseIncrementsOrdinalPos_()\n
    '''
def setIsSETUsedAfterConnectionInit():
    '''returns None\n\n
    setIsSETUsedAfterConnectionInit()\n
    '''
def getIsSETUsedAfterConnectionInit():
    '''returns boolean\n\n
    getIsSETUsedAfterConnectionInit()\n
    '''
def countDefinitionTraces():
    '''returns int\n\n
    countDefinitionTraces()\n
    '''
def countExecutionTraces():
    '''returns int\n\n
    countExecutionTraces()\n
    '''
def setReasonCannotExecuteStatically():
    '''returns None\n\n
    setReasonCannotExecuteStatically(final String reasonCannotExecuteStatically_)\n
    '''
def getReasonCannotExecuteStatically():
    '''returns String\n\n
    getReasonCannotExecuteStatically()\n
    '''
def getStmtExecutionTime():
    '''returns long\n\n
    getStmtExecutionTime()\n
    '''
def setStmtExecutionTime():
    '''returns None\n\n
    setStmtExecutionTime(final long stmtExecutionTime_)\n
    '''
def getBatchExecutionTime():
    '''returns long\n\n
    getBatchExecutionTime()\n
    '''
def setBatchExecutionTime():
    '''returns None\n\n
    setBatchExecutionTime(final long batchExecutionTime_)\n
    '''
def getBatchCount():
    '''returns int\n\n
    getBatchCount()\n
    '''
def setBatchCount():
    '''returns None\n\n
    setBatchCount(final int batchCount_)\n
    '''
def setCaptureStats():
    '''returns None\n\n
    setCaptureStats(final long stmtExecutionTime_, final long n, final int batchCount_)\n
    '''
def isStatsUpdated():
    '''returns boolean\n\n
    isStatsUpdated()\n
    '''
def setStatsUpdated():
    '''returns None\n\n
    setStatsUpdated(final boolean isStatsUpdated_)\n
    '''
def isNewSPRegisterUsed():
    '''returns boolean\n\n
    isNewSPRegisterUsed()\n
    '''
def setNewSPRegisterUsed():
    '''returns None\n\n
    setNewSPRegisterUsed(final boolean isNewSPRegisterUsed_)\n
    '''
def setMaxRowsInvoked():
    '''returns None\n\n
    setMaxRowsInvoked(final boolean maxRowsInvoked_)\n
    '''
def getMaxRowsInvoked():
    '''returns boolean\n\n
    getMaxRowsInvoked()\n
    '''
def setMaxRowsValue():
    '''returns None\n\n
    setMaxRowsValue(final int maxRowsValue_)\n
    '''
def getMaxRowsValue():
    '''returns int\n\n
    getMaxRowsValue()\n
    '''
def setMaxRowsIncrementalValue():
    '''returns None\n\n
    setMaxRowsIncrementalValue(final int maxRowsIncrementalValue_)\n
    '''
def getMaxRowsIncrementalValue():
    '''returns int\n\n
    getMaxRowsIncrementalValue()\n
    '''
