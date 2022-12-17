def getHeartbeatNoChangeCount():
    '''returns int\n\n
    getHeartbeatNoChangeCount()\n
    '''
def _getPC():
    '''returns Connection\n\n
    _getPC()\n
    '''
def getLogicalConnection():
    '''returns Connection\n\n
    getLogicalConnection(final OraclePooledConnection oraclePooledConnection, final boolean b)\n
    '''
def getPropertyForPooledConnection():
    '''returns None\n\n
    getPropertyForPooledConnection(final OraclePooledConnection oraclePooledConnection)\n
    '''
def closeInternal():
    '''returns None\n\n
    closeInternal(final boolean b)\n
    '''
def cleanupAndClose():
    '''returns None\n\n
    cleanupAndClose(final boolean b)\n
    cleanupAndClose()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    abort(final Executor executor)\n
    '''
def getConnectionCacheCallbackObj():
    '''returns OracleConnectionCacheCallback\n\n
    getConnectionCacheCallbackObj()\n
    '''
def getConnectionCacheCallbackPrivObj():
    '''returns Object\n\n
    getConnectionCacheCallbackPrivObj()\n
    '''
def getConnectionCacheCallbackFlag():
    '''returns int\n\n
    getConnectionCacheCallbackFlag()\n
    '''
def getConnectionReleasePriority():
    '''returns int\n\n
    getConnectionReleasePriority()\n
    '''
def setStartTime():
    '''returns None\n\n
    setStartTime(final long startTime)\n
    '''
def getStartTime():
    '''returns long\n\n
    getStartTime()\n
    '''
def getDatabaseTimeZone():
    '''returns String\n\n
    getDatabaseTimeZone()\n
    '''
def getServerSessionInfo():
    '''returns Properties\n\n
    getServerSessionInfo()\n
    '''
def getClientData():
    '''returns Object\n\n
    getClientData(final Object o)\n
    '''
def setClientData():
    '''returns Object\n\n
    setClientData(final Object o, final Object o2)\n
    '''
def removeClientData():
    '''returns Object\n\n
    removeClientData(final Object o)\n
    '''
def setClientIdentifier():
    '''returns None\n\n
    setClientIdentifier(final String clientIdentifier)\n
    '''
def clearClientIdentifier():
    '''returns None\n\n
    clearClientIdentifier(final String s)\n
    '''
def getStructAttrNCsId():
    '''returns short\n\n
    getStructAttrNCsId()\n
    '''
def getTypeMap():
    '''returns Map\n\n
    getTypeMap()\n
    '''
def getDBAccessProperties():
    '''returns Properties\n\n
    getDBAccessProperties()\n
    '''
def getOCIHandles():
    '''returns Properties\n\n
    getOCIHandles()\n
    '''
def getDatabaseProductVersion():
    '''returns String\n\n
    getDatabaseProductVersion()\n
    '''
def cancel():
    '''returns None\n\n
    cancel()\n
    '''
def getURL():
    '''returns String\n\n
    getURL()\n
    '''
def getIncludeSynonyms():
    '''returns boolean\n\n
    getIncludeSynonyms()\n
    '''
def getRemarksReporting():
    '''returns boolean\n\n
    getRemarksReporting()\n
    '''
def getRestrictGetTables():
    '''returns boolean\n\n
    getRestrictGetTables()\n
    '''
def getVersionNumber():
    '''returns short\n\n
    getVersionNumber()\n
    '''
def getJavaObjectTypeMap():
    '''returns Map\n\n
    getJavaObjectTypeMap()\n
    '''
def setJavaObjectTypeMap():
    '''returns None\n\n
    setJavaObjectTypeMap(final Map javaObjectTypeMap)\n
    '''
def createBfileDBAccess():
    '''returns BfileDBAccess\n\n
    createBfileDBAccess()\n
    '''
def createBlobDBAccess():
    '''returns BlobDBAccess\n\n
    createBlobDBAccess()\n
    '''
def createClobDBAccess():
    '''returns ClobDBAccess\n\n
    createClobDBAccess()\n
    '''
def setDefaultFixedString():
    '''returns None\n\n
    setDefaultFixedString(final boolean defaultFixedString)\n
    '''
def getTimestamptzInGmt():
    '''returns boolean\n\n
    getTimestamptzInGmt()\n
    '''
def getUse1900AsYearForTime():
    '''returns boolean\n\n
    getUse1900AsYearForTime()\n
    '''
def getDefaultFixedString():
    '''returns boolean\n\n
    getDefaultFixedString()\n
    '''
def classForNameAndSchema():
    '''returns Class\n\n
    classForNameAndSchema(final String s, final String s2)\n
    '''
def setFDO():
    '''returns None\n\n
    setFDO(final byte[] fdo)\n
    '''
def getFDO():
    '''returns byte[]\n\n
    getFDO(final boolean b)\n
    '''
def getBigEndian():
    '''returns boolean\n\n
    getBigEndian()\n
    '''
def getDescriptor():
    '''returns Object\n\n
    getDescriptor(final byte[] array)\n
    '''
def putDescriptor():
    '''returns None\n\n
    putDescriptor(final byte[] array, final Object o)\n
    '''
def removeDescriptor():
    '''returns None\n\n
    removeDescriptor(final String s)\n
    '''
def removeAllDescriptor():
    '''returns None\n\n
    removeAllDescriptor()\n
    '''
def numberOfDescriptorCacheEntries():
    '''returns int\n\n
    numberOfDescriptorCacheEntries()\n
    '''
def descriptorCacheKeys():
    '''returns Enumeration\n\n
    descriptorCacheKeys()\n
    '''
def getDbCsId():
    '''returns short\n\n
    getDbCsId()\n
    '''
def getJdbcCsId():
    '''returns short\n\n
    getJdbcCsId()\n
    '''
def getNCharSet():
    '''returns short\n\n
    getNCharSet()\n
    '''
def newArrayDataResultSet():
    '''returns ResultSet\n\n
    newArrayDataResultSet(final Datum[] array, final long n, final int n2, final Map map)\n
    newArrayDataResultSet(final OracleArray oracleArray, final long n, final int n2, final Map map)\n
    '''
def newArrayLocatorResultSet():
    '''returns ResultSet\n\n
    newArrayLocatorResultSet(final ArrayDescriptor arrayDescriptor, final byte[] array, final long n, final int n2, final Map map)\n
    '''
def newStructMetaData():
    '''returns ResultSetMetaData\n\n
    newStructMetaData(final StructDescriptor structDescriptor)\n
    '''
def getForm():
    '''returns None\n\n
    getForm(final OracleTypeADT oracleTypeADT, final OracleTypeCLOB oracleTypeCLOB, final int n)\n
    '''
def CHARBytesToJavaChars():
    '''returns int\n\n
    CHARBytesToJavaChars(final byte[] array, final int n, final char[] array2)\n
    '''
def NCHARBytesToJavaChars():
    '''returns int\n\n
    NCHARBytesToJavaChars(final byte[] array, final int n, final char[] array2)\n
    '''
def IsNCharFixedWith():
    '''returns boolean\n\n
    IsNCharFixedWith()\n
    '''
def getDriverCharSet():
    '''returns short\n\n
    getDriverCharSet()\n
    '''
def getC2SNlsRatio():
    '''returns int\n\n
    getC2SNlsRatio()\n
    '''
def getMaxCharSize():
    '''returns int\n\n
    getMaxCharSize()\n
    '''
def getMaxCharbyteSize():
    '''returns int\n\n
    getMaxCharbyteSize()\n
    '''
def getMaxNCharbyteSize():
    '''returns int\n\n
    getMaxNCharbyteSize()\n
    '''
def isCharSetMultibyte():
    '''returns boolean\n\n
    isCharSetMultibyte(final short n)\n
    '''
def javaCharsToCHARBytes():
    '''returns int\n\n
    javaCharsToCHARBytes(final char[] array, final int n, final byte[] array2)\n
    '''
def javaCharsToNCHARBytes():
    '''returns int\n\n
    javaCharsToNCHARBytes(final char[] array, final int n, final byte[] array2)\n
    '''
def getStmtCacheSize():
    '''returns int\n\n
    getStmtCacheSize()\n
    '''
def getStatementCacheSize():
    '''returns int\n\n
    getStatementCacheSize()\n
    '''
def getImplicitCachingEnabled():
    '''returns boolean\n\n
    getImplicitCachingEnabled()\n
    '''
def getExplicitCachingEnabled():
    '''returns boolean\n\n
    getExplicitCachingEnabled()\n
    '''
def purgeImplicitCache():
    '''returns None\n\n
    purgeImplicitCache()\n
    '''
def purgeExplicitCache():
    '''returns None\n\n
    purgeExplicitCache()\n
    '''
def getStatementWithKey():
    '''returns PreparedStatement\n\n
    getStatementWithKey(final String s)\n
    '''
def getCallWithKey():
    '''returns CallableStatement\n\n
    getCallWithKey(final String s)\n
    '''
def isStatementCacheInitialized():
    '''returns boolean\n\n
    isStatementCacheInitialized()\n
    '''
def setTypeMap():
    '''returns None\n\n
    setTypeMap(final Map typeMap)\n
    '''
def getProtocolType():
    '''returns String\n\n
    getProtocolType()\n
    '''
def setTxnMode():
    '''returns None\n\n
    setTxnMode(final int txnMode)\n
    '''
def getTxnMode():
    '''returns int\n\n
    getTxnMode()\n
    '''
def getHeapAllocSize():
    '''returns int\n\n
    getHeapAllocSize()\n
    '''
def getOCIEnvHeapAllocSize():
    '''returns int\n\n
    getOCIEnvHeapAllocSize()\n
    '''
def createClob():
    '''returns CLOB\n\n
    createClob(final byte[] array)\n
    createClob(final byte[] array, final short n)\n
    '''
def createClobWithUnpickledBytes():
    '''returns CLOB\n\n
    createClobWithUnpickledBytes(final byte[] array)\n
    '''
def createBlob():
    '''returns BLOB\n\n
    createBlob(final byte[] array)\n
    '''
def createBlobWithUnpickledBytes():
    '''returns BLOB\n\n
    createBlobWithUnpickledBytes(final byte[] array)\n
    '''
def createBfile():
    '''returns BFILE\n\n
    createBfile(final byte[] array)\n
    '''
def isDescriptorSharable():
    '''returns boolean\n\n
    isDescriptorSharable(final oracle.jdbc.internal.OracleConnection oracleConnection)\n
    '''
def refCursorCursorToStatement():
    '''returns OracleStatement\n\n
    refCursorCursorToStatement(final int n)\n
    '''
def getTdoCState():
    '''returns long\n\n
    getTdoCState(final String s, final String s2)\n
    getTdoCState(final String s)\n
    '''
def toDatum():
    '''returns Datum\n\n
    toDatum(final CustomDatum customDatum)\n
    '''
def getXAResource():
    '''returns XAResource\n\n
    getXAResource()\n
    '''
def setApplicationContext():
    '''returns None\n\n
    setApplicationContext(final String s, final String s2, final String s3)\n
    '''
def clearAllApplicationContext():
    '''returns None\n\n
    clearAllApplicationContext(final String s)\n
    '''
def isV8Compatible():
    '''returns boolean\n\n
    isV8Compatible()\n
    '''
def getMapDateToTimestamp():
    '''returns boolean\n\n
    getMapDateToTimestamp()\n
    '''
def getJDBCStandardBehavior():
    '''returns boolean\n\n
    getJDBCStandardBehavior()\n
    '''
def getNetworkTimeout():
    '''returns int\n\n
    getNetworkTimeout()\n
    '''
def getSchema():
    '''returns String\n\n
    getSchema()\n
    '''
def setNetworkTimeout():
    '''returns None\n\n
    setNetworkTimeout(final Executor executor, final int n)\n
    '''
def setSchema():
    '''returns None\n\n
    setSchema(final String schema)\n
    '''
def createLightweightSession():
    '''returns byte[]\n\n
    createLightweightSession(final String s, final KeywordValueLong[] array, final int n, final KeywordValueLong[][] array2, final int[] array3)\n
    '''
def executeLightweightSessionPiggyback():
    '''returns None\n\n
    executeLightweightSessionPiggyback(final int n, final byte[] array, final KeywordValueLong[] array2, final int n2)\n
    '''
def doXSNamespaceOp():
    '''returns None\n\n
    doXSNamespaceOp(final XSOperationCode xsOperationCode, final byte[] array, final XSNamespace[] array2, final XSNamespace[][] array3, final XSSecureId xsSecureId)\n
    doXSNamespaceOp(final XSOperationCode xsOperationCode, final byte[] array, final XSNamespace[] array2, final XSSecureId xsSecureId)\n
    '''
def doXSSessionAttachOp():
    '''returns None\n\n
    doXSSessionAttachOp(final int n, final byte[] array, final XSSecureId xsSecureId, final byte[] array2, final XSPrincipal xsPrincipal, final String[] array3, final String[] array4, final String[] array5, final XSNamespace[] array6, final XSNamespace[] array7, final XSNamespace[] array8, final TIMESTAMPTZ timestamptz, final TIMESTAMPTZ timestamptz2, final int n2, final long n3, final XSKeyval xsKeyval, final int[] array9)\n
    '''
def doXSSessionChangeOp():
    '''returns None\n\n
    doXSSessionChangeOp(final XSSessionSetOperationCode xsSessionSetOperationCode, final byte[] array, final XSSecureId xsSecureId, final XSSessionParameters xsSessionParameters)\n
    '''
def doXSSessionCreateOp():
    '''returns byte[]\n\n
    doXSSessionCreateOp(final XSSessionOperationCode xsSessionOperationCode, final XSSecureId xsSecureId, final byte[] array, final XSPrincipal xsPrincipal, final String s, final XSNamespace[] array2, final XSSessionModeFlag xsSessionModeFlag, final XSKeyval xsKeyval)\n
    '''
def doXSSessionDestroyOp():
    '''returns None\n\n
    doXSSessionDestroyOp(final byte[] array, final XSSecureId xsSecureId, final byte[] array2)\n
    '''
def doXSSessionDetachOp():
    '''returns None\n\n
    doXSSessionDetachOp(final int n, final byte[] array, final XSSecureId xsSecureId, final boolean b)\n
    '''
def createTemporaryBlob():
    '''returns BLOB\n\n
    createTemporaryBlob(final Connection connection, final boolean b, final int n)\n
    '''
def createTemporaryClob():
    '''returns CLOB\n\n
    createTemporaryClob(final Connection connection, final boolean b, final int n, final short n2)\n
    '''
def getDefaultSchemaNameForNamedTypes():
    '''returns String\n\n
    getDefaultSchemaNameForNamedTypes()\n
    '''
def isUsable():
    '''returns boolean\n\n
    isUsable()\n
    isUsable(final boolean b)\n
    '''
def getInstanceProperty():
    '''returns byte\n\n
    getInstanceProperty(final InstanceProperty instanceProperty)\n
    '''
def setUsable():
    '''returns None\n\n
    setUsable(final boolean usable)\n
    '''
def getTimezoneVersionNumber():
    '''returns int\n\n
    getTimezoneVersionNumber()\n
    '''
def getTIMEZONETAB():
    '''returns TIMEZONETAB\n\n
    getTIMEZONETAB()\n
    '''
def setPDBChangeEventListener():
    '''returns None\n\n
    setPDBChangeEventListener(final PDBChangeEventListener pdbChangeEventListener)\n
    setPDBChangeEventListener(final PDBChangeEventListener pdbChangeEventListener, final Executor executor)\n
    '''
def addXSEventListener():
    '''returns None\n\n
    addXSEventListener(final XSEventListener xsEventListener)\n
    addXSEventListener(final XSEventListener xsEventListener, final Executor executor)\n
    '''
def removeXSEventListener():
    '''returns None\n\n
    removeXSEventListener(final XSEventListener xsEventListener)\n
    '''
def removeAllXSEventListener():
    '''returns None\n\n
    removeAllXSEventListener()\n
    '''
def getByteBufferCacheStatistics():
    '''returns BufferCacheStatistics\n\n
    getByteBufferCacheStatistics()\n
    '''
def getCharBufferCacheStatistics():
    '''returns BufferCacheStatistics\n\n
    getCharBufferCacheStatistics()\n
    '''
def isDataInLocatorEnabled():
    '''returns boolean\n\n
    isDataInLocatorEnabled()\n
    '''
def isLobStreamPosStandardCompliant():
    '''returns boolean\n\n
    isLobStreamPosStandardCompliant()\n
    '''
def getCurrentSCN():
    '''returns long\n\n
    getCurrentSCN()\n
    '''
def getTransactionState():
    '''returns EnumSet<TransactionState>\n\n
    getTransactionState()\n
    '''
def isConnectionSocketKeepAlive():
    '''returns boolean\n\n
    isConnectionSocketKeepAlive()\n
    '''
def removeLogicalTransactionIdEventListener():
    '''returns None\n\n
    removeLogicalTransactionIdEventListener(final LogicalTransactionIdEventListener logicalTransactionIdEventListener)\n
    '''
def setReplayOperations():
    '''returns None\n\n
    setReplayOperations(final EnumSet<ReplayOperation> replayOperations)\n
    '''
def beginNonRequestCalls():
    '''returns None\n\n
    beginNonRequestCalls()\n
    '''
def endNonRequestCalls():
    '''returns None\n\n
    endNonRequestCalls()\n
    '''
def setReplayContext():
    '''returns None\n\n
    setReplayContext(final ReplayContext[] replayContext)\n
    '''
def registerEndReplayCallback():
    '''returns None\n\n
    registerEndReplayCallback(final EndReplayCallback endReplayCallback)\n
    '''
def getEOC():
    '''returns int\n\n
    getEOC()\n
    '''
def getReplayContext():
    '''returns ReplayContext[]\n\n
    getReplayContext()\n
    '''
def getLastReplayContext():
    '''returns ReplayContext\n\n
    getLastReplayContext()\n
    '''
def setLastReplayContext():
    '''returns None\n\n
    setLastReplayContext(final ReplayContext lastReplayContext)\n
    '''
def getDerivedKeyInternal():
    '''returns byte[]\n\n
    getDerivedKeyInternal(final byte[] array, final int n)\n
    '''
def getExecutingRPCFunctionCode():
    '''returns short\n\n
    getExecutingRPCFunctionCode()\n
    '''
def getExecutingRPCSQL():
    '''returns String\n\n
    getExecutingRPCSQL()\n
    '''
def setReplayingMode():
    '''returns None\n\n
    setReplayingMode(final boolean replayingMode)\n
    '''
def jmsEnqueue():
    '''returns None\n\n
    jmsEnqueue(final String s, final JMSEnqueueOptions jmsEnqueueOptions, final JMSMessage jmsMessage, final AQMessageProperties aqMessageProperties)\n
    '''
def jmsDequeue():
    '''returns JMSMessage\n\n
    jmsDequeue(final String s, final JMSDequeueOptions jmsDequeueOptions)\n
    jmsDequeue(final String s, final JMSDequeueOptions jmsDequeueOptions, final OutputStream outputStream)\n
    jmsDequeue(final String s, final JMSDequeueOptions jmsDequeueOptions, final String s2)\n
    '''
def unregisterJMSNotification():
    '''returns None\n\n
    unregisterJMSNotification(final JMSNotificationRegistration jmsNotificationRegistration)\n
    '''
def startJMSNotification():
    '''returns None\n\n
    startJMSNotification(final JMSNotificationRegistration jmsNotificationRegistration)\n
    '''
def stopJMSNotification():
    '''returns None\n\n
    stopJMSNotification(final JMSNotificationRegistration jmsNotificationRegistration)\n
    '''
def ackJMSNotification():
    '''returns None\n\n
    ackJMSNotification(final JMSNotificationRegistration jmsNotificationRegistration, final byte[] array, final JMSNotificationRegistration.Directive directive)\n
    ackJMSNotification(final ArrayList<JMSNotificationRegistration> list, final byte[][] array, final JMSNotificationRegistration.Directive directive)\n
    '''
def isDRCPEnabled():
    '''returns boolean\n\n
    isDRCPEnabled()\n
    '''
def isDRCPMultitagEnabled():
    '''returns boolean\n\n
    isDRCPMultitagEnabled()\n
    '''
def getDRCPReturnTag():
    '''returns String\n\n
    getDRCPReturnTag()\n
    '''
def getDRCPPLSQLCallbackName():
    '''returns String\n\n
    getDRCPPLSQLCallbackName()\n
    '''
def attachServerConnection():
    '''returns boolean\n\n
    attachServerConnection()\n
    '''
def detachServerConnection():
    '''returns None\n\n
    detachServerConnection(final String s)\n
    '''
def prepareDirectPath():
    '''returns PreparedStatement\n\n
    prepareDirectPath(final String s, final String s2, final String[] array)\n
    prepareDirectPath(final String s, final String s2, final String[] array, final String s3)\n
    prepareDirectPath(final String s, final String s2, final String[] array, final Properties properties)\n
    prepareDirectPath(final String s, final String s2, final String[] array, final String s3, final Properties properties)\n
    '''
def needToPurgeStatementCache():
    '''returns boolean\n\n
    needToPurgeStatementCache()\n
    '''
def getNegotiatedSDU():
    '''returns int\n\n
    getNegotiatedSDU()\n
    '''
def getNegotiatedTTCVersion():
    '''returns byte\n\n
    getNegotiatedTTCVersion()\n
    '''
def getVarTypeMaxLenCompat():
    '''returns int\n\n
    getVarTypeMaxLenCompat()\n
    '''
def setChecksumMode():
    '''returns None\n\n
    setChecksumMode(final ChecksumMode checksumMode)\n
    '''
def getResultSetCache():
    '''returns ResultSetCache\n\n
    getResultSetCache()\n
    '''
def closeLogicalConnection():
    '''returns None\n\n
    closeLogicalConnection()\n
    '''
def isLifecycleOpen():
    '''returns boolean\n\n
    isLifecycleOpen()\n
    '''
def clearDrcpTagName():
    '''returns None\n\n
    clearDrcpTagName()\n
    '''
def beginRequest():
    '''returns None\n\n
    beginRequest()\n
    '''
def endRequest():
    '''returns None\n\n
    endRequest()\n
    endRequest(final boolean b)\n
    '''
def sendRequestFlags():
    '''returns None\n\n
    sendRequestFlags()\n
    '''
def freeTemporaryBlobsAndClobs():
    '''returns int\n\n
    freeTemporaryBlobsAndClobs()\n
    '''
def getHAManager():
    '''returns HAManager\n\n
    getHAManager()\n
    '''
def setHAManager():
    '''returns None\n\n
    setHAManager(final HAManager haManager)\n
    '''
def getLogicalTransactionId():
    '''returns LogicalTransactionId\n\n
    getLogicalTransactionId()\n
    '''
def setChunkInfo():
    '''returns None\n\n
    setChunkInfo(final OracleShardingKey oracleShardingKey, final OracleShardingKey oracleShardingKey2, final String s)\n
    '''
def setShardingKey():
    '''returns None\n\n
    setShardingKey(final OracleShardingKey oracleShardingKey, final OracleShardingKey oracleShardingKey2)\n
    setShardingKey(final OracleShardingKey shardingKey)\n
    '''
def setShardingKeyIfValid():
    '''returns boolean\n\n
    setShardingKeyIfValid(final OracleShardingKey oracleShardingKey, final OracleShardingKey oracleShardingKey2, final int n)\n
    setShardingKeyIfValid(final OracleShardingKey oracleShardingKey, final int n)\n
    '''
def isNetworkCompressionEnabled():
    '''returns boolean\n\n
    isNetworkCompressionEnabled()\n
    '''
def getNetworkStat():
    '''returns NetStat\n\n
    getNetworkStat()\n
    '''
def run():
    '''returns Object\n\n
    run()\n
    '''
def hasNoOpenHandles():
    '''returns boolean\n\n
    hasNoOpenHandles()\n
    '''
def getStateSignatures():
    '''returns StateSignatures\n\n
    getStateSignatures()\n
    '''
def isSafelyClosed():
    '''returns boolean\n\n
    isSafelyClosed()\n
    '''
def setSafelyClosed():
    '''returns None\n\n
    setSafelyClosed(final boolean safelyClosed)\n
    '''
def prepareStatement():
    '''returns PreparedStatement\n\n
    prepareStatement(final String s, final Properties properties)\n
    '''
def prepareCall():
    '''returns CallableStatement\n\n
    prepareCall(final String s, final Properties properties)\n
    '''
def getClientInfoInternal():
    '''returns Properties\n\n
    getClientInfoInternal()\n
    '''
def getAutoCommitInternal():
    '''returns boolean\n\n
    getAutoCommitInternal()\n
    '''
def addLargeObject():
    '''returns None\n\n
    addLargeObject(final OracleLargeObject oracleLargeObject)\n
    '''
def removeLargeObject():
    '''returns None\n\n
    removeLargeObject(final OracleLargeObject oracleLargeObject)\n
    '''
def addBfile():
    '''returns None\n\n
    addBfile(final OracleBfile oracleBfile)\n
    '''
def removeBfile():
    '''returns None\n\n
    removeBfile(final OracleBfile oracleBfile)\n
    '''
