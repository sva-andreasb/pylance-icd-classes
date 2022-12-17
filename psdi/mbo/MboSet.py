def setNoNeedtoFetchFromDB():
    '''returns None\n\n
    setNoNeedtoFetchFromDB(final boolean flag)\n
    '''
def ():
    '''returns MboSet\n\n
    (final MboServerInterface ms)\n
    '''
def setProxy():
    '''returns None\n\n
    setProxy(final Remote proxy)\n
    '''
def getProxy():
    '''returns Remote\n\n
    getProxy()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initDataDictionary():
    '''returns None\n\n
    initDataDictionary()\n
    '''
def setApp():
    '''returns None\n\n
    setApp(final String appName)\n
    '''
def getApp():
    '''returns String\n\n
    getApp()\n
    '''
def getParentApp():
    '''returns String\n\n
    getParentApp()\n
    '''
def getMboSetValueData():
    '''returns MboValueData[]\n\n
    getMboSetValueData(final String attribute)\n
    getMboSetValueData(final String[] attribute)\n
    '''
def getOwner():
    '''returns MboRemote\n\n
    getOwner()\n
    '''
def setOwner():
    '''returns None\n\n
    setOwner(final MboRemote mbo)\n
    '''
def getMboSetData():
    '''returns MboSetData\n\n
    getMboSetData(final String[] attributes)\n
    getMboSetData(final int row, final int count, final String[] attributes)\n
    '''
def getMboValueData():
    '''returns MboValueData[][]\n\n
    getMboValueData(final String attribute)\n
    getMboValueData(final String[] attribute)\n
    getMboValueData(final int rowStart, final int rowCount, final String[] attribute)\n
    '''
def getMboValueInfoStatic():
    '''returns MboValueInfoStatic[]\n\n
    getMboValueInfoStatic(final String attribute)\n
    getMboValueInfoStatic(final String[] attribute)\n
    '''
def getClientLocale():
    '''returns Locale\n\n
    getClientLocale()\n
    '''
def getClientTimeZone():
    '''returns TimeZone\n\n
    getClientTimeZone()\n
    '''
def setWhere():
    '''returns None\n\n
    setWhere(final String whereClause)\n
    '''
def getWhere():
    '''returns String\n\n
    getWhere()\n
    '''
def setUserWhere():
    '''returns None\n\n
    setUserWhere(final String userWhere)\n
    '''
def setUserWhereAfterParse():
    '''returns None\n\n
    setUserWhereAfterParse(String where)\n
    '''
def getUserWhere():
    '''returns String\n\n
    getUserWhere()\n
    getUserWhere(final String alias)\n
    '''
def getUserAndQbeWhere():
    '''returns String\n\n
    getUserAndQbeWhere()\n
    '''
def useStoredQuery():
    '''returns None\n\n
    useStoredQuery(final String queryName)\n
    '''
def setSQLOptions():
    '''returns None\n\n
    setSQLOptions(final String sqlOptions)\n
    '''
def getSQLOptions():
    '''returns String\n\n
    getSQLOptions()\n
    '''
def findKey():
    '''returns MboRemote\n\n
    findKey(final Object keyObject)\n
    '''
def setRelationship():
    '''returns None\n\n
    setRelationship(final String relationClause)\n
    '''
def getRelationship():
    '''returns String\n\n
    getRelationship()\n
    '''
def setOrderBy():
    '''returns None\n\n
    setOrderBy(final String orderByClause)\n
    '''
def setOrderByNVL():
    '''returns None\n\n
    setOrderByNVL(final Map<String, String[]> options)\n
    '''
def getOrderBy():
    '''returns String\n\n
    getOrderBy()\n
    '''
def setDefaultOrderBy():
    '''returns None\n\n
    setDefaultOrderBy()\n
    '''
def setPreserveOrderByCase():
    '''returns None\n\n
    setPreserveOrderByCase(final boolean value)\n
    '''
def moveToKey():
    '''returns MboRemote\n\n
    moveToKey(final KeyValue keyVal)\n
    '''
def moveNext():
    '''returns MboRemote\n\n
    moveNext()\n
    '''
def movePrev():
    '''returns MboRemote\n\n
    movePrev()\n
    '''
def moveFirst():
    '''returns MboRemote\n\n
    moveFirst()\n
    '''
def moveLast():
    '''returns MboRemote\n\n
    moveLast()\n
    '''
def moveTo():
    '''returns MboRemote\n\n
    moveTo(final int pos)\n
    '''
def getCurrentPosition():
    '''returns int\n\n
    getCurrentPosition()\n
    '''
def getMbo():
    '''returns MboRemote\n\n
    getMbo()\n
    getMbo(final int index)\n
    '''
def newMboIndex():
    '''returns int\n\n
    newMboIndex()\n
    '''
def processML():
    '''returns boolean\n\n
    processML()\n
    '''
def getMLFromClause():
    '''returns StringBuffer\n\n
    getMLFromClause(final boolean useSchemaOwner)\n
    '''
def fetchNext():
    '''returns MboRemote\n\n
    fetchNext()\n
    '''
def forceDBSort():
    '''returns boolean\n\n
    forceDBSort(final String attrName)\n
    '''
def appendToWhere():
    '''returns String\n\n
    appendToWhere()\n
    '''
def getUserPrefWhere():
    '''returns String\n\n
    getUserPrefWhere()\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def count():
    '''returns int\n\n
    count()\n
    count(final int countConstant)\n
    '''
def incrementDeletedCount():
    '''returns None\n\n
    incrementDeletedCount(final boolean inc)\n
    '''
def avg():
    '''returns double\n\n
    avg(final String attributeName)\n
    '''
def sum():
    '''returns double\n\n
    sum(final String attributeName)\n
    '''
def max():
    '''returns double\n\n
    max(final String attributeName)\n
    '''
def min():
    '''returns double\n\n
    min(final String attributeName)\n
    '''
def latestDate():
    '''returns Date\n\n
    latestDate(final String attributeName)\n
    '''
def earliestDate():
    '''returns Date\n\n
    earliestDate(final String attributeName)\n
    '''
def canAdd():
    '''returns None\n\n
    canAdd()\n
    '''
def deleteAll():
    '''returns None\n\n
    deleteAll()\n
    deleteAll(final long accessModifier)\n
    '''
def undeleteAll():
    '''returns None\n\n
    undeleteAll()\n
    '''
def addAtIndex():
    '''returns MboRemote\n\n
    addAtIndex(final long accessModifier, final int ind)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    remove(final int pos)\n
    remove(final MboRemote mbo)\n
    '''
def deleteAndRemove():
    '''returns None\n\n
    deleteAndRemove()\n
    deleteAndRemove(final int pos)\n
    deleteAndRemove(final int pos, final long accessModifier)\n
    deleteAndRemove(final MboRemote mbo)\n
    deleteAndRemove(final MboRemote mbo, final long accessModifier)\n
    '''
def deleteAndRemoveAll():
    '''returns None\n\n
    deleteAndRemoveAll()\n
    deleteAndRemoveAll(final long accessModifier)\n
    '''
def toBeSaved():
    '''returns boolean\n\n
    toBeSaved()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def cancelAndClose():
    '''returns None\n\n
    cancelAndClose()\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def clearToBeSaved():
    '''returns None\n\n
    clearToBeSaved()\n
    '''
def resetForRefreshOnSave():
    '''returns None\n\n
    resetForRefreshOnSave()\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def rollback():
    '''returns None\n\n
    rollback()\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
def getList():
    '''returns MboSetRemote\n\n
    getList(final String attributeName)\n
    getList(final int row, final String attributeName)\n
    '''
def smartFill():
    '''returns MboSetRemote\n\n
    smartFill(final String attributeName, final String value, final boolean exact)\n
    smartFill(final int row, final String attributeName, final String value, final boolean exact)\n
    '''
def smartFind():
    '''returns MboSetRemote\n\n
    smartFind(final String attributeName, final String value, final boolean exact)\n
    smartFind(final String objectName, final String attributeName, final String value, final boolean exact)\n
    smartFind(final int row, final String objectName, final String attributeName, final String value, final boolean exact)\n
    smartFind(final int row, final String attributeName, final String value, final boolean exact)\n
    '''
def getString():
    '''returns String\n\n
    getString(final String attributeName)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final String attributeName)\n
    '''
def getByte():
    '''returns byte\n\n
    getByte(final String attributeName)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final String attributeName)\n
    '''
def getLong():
    '''returns long\n\n
    getLong(final String attributeName)\n
    '''
def getFloat():
    '''returns float\n\n
    getFloat(final String attributeName)\n
    '''
def getDouble():
    '''returns double\n\n
    getDouble(final String attributeName)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate(final String attributeName)\n
    '''
def getBytes():
    '''returns byte[]\n\n
    getBytes(final String attributeName)\n
    '''
def isNull():
    '''returns boolean\n\n
    isNull(final String attributeName)\n
    '''
def setValueNull():
    '''returns None\n\n
    setValueNull(final String attributeName)\n
    setValueNull(final String attributeName, final long accessModifier)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String attributeName, final String val)\n
    setValue(final String attributeName, final String val, final long accessModifier)\n
    setValue(final String attributeName, final boolean val)\n
    setValue(final String attributeName, final boolean val, final long accessModifier)\n
    setValue(final String attributeName, final byte val)\n
    setValue(final String attributeName, final byte val, final long accessModifier)\n
    setValue(final String attributeName, final short val)\n
    setValue(final String attributeName, final short val, final long accessModifier)\n
    setValue(final String attributeName, final int val)\n
    setValue(final String attributeName, final int val, final long accessModifier)\n
    setValue(final String attributeName, final long val)\n
    setValue(final String attributeName, final long val, final long accessModifier)\n
    setValue(final String attributeName, final float val)\n
    setValue(final String attributeName, final float val, final long accessModifier)\n
    setValue(final String attributeName, final double val)\n
    setValue(final String attributeName, final double val, final long accessModifier)\n
    setValue(final String attributeName, final byte[] val)\n
    setValue(final String attributeName, final byte[] val, final long accessModifier)\n
    setValue(final String attributeName, final Date val)\n
    setValue(final String attributeName, final Date val, final long accessModifier)\n
    setValue(final String attributeName, final MboSetRemote source)\n
    setValue(final String attributeName, final MboRemote source)\n
    '''
def setMboSetInfo():
    '''returns None\n\n
    setMboSetInfo(final MboSetInfo ms)\n
    '''
def getMboSetInfo():
    '''returns MboSetInfo\n\n
    getMboSetInfo()\n
    '''
def getMboServer():
    '''returns MboServerInterface\n\n
    getMboServer()\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo()\n
    '''
def resetQbe():
    '''returns None\n\n
    resetQbe()\n
    '''
def setQbeOperatorOr():
    '''returns None\n\n
    setQbeOperatorOr()\n
    '''
def setQbe():
    '''returns None\n\n
    setQbe(final String[] attribute, final String expression)\n
    setQbe(final String attribute, final String[] expression)\n
    setQbe(final String[] attribute, final String[] expression)\n
    setQbe(final String attribute, String expression)\n
    setQbe(final String attribute, final MboSetRemote lookup)\n
    '''
def setQbeExactMatch():
    '''returns None\n\n
    setQbeExactMatch(final String state)\n
    setQbeExactMatch(final boolean state)\n
    '''
def isQbeExactMatch():
    '''returns boolean\n\n
    isQbeExactMatch()\n
    '''
def ignoreQbeExactMatchSet():
    '''returns None\n\n
    ignoreQbeExactMatchSet(final boolean flag)\n
    '''
def isIgnoreQbeExactMatchSet():
    '''returns boolean\n\n
    isIgnoreQbeExactMatchSet()\n
    '''
def isQbeCaseSensitive():
    '''returns boolean\n\n
    isQbeCaseSensitive()\n
    '''
def setQbeCaseSensitive():
    '''returns None\n\n
    setQbeCaseSensitive(final boolean state)\n
    setQbeCaseSensitive(final String state)\n
    '''
def getQbe():
    '''returns String\n\n
    getQbe(final String[] attributes)\n
    getQbe()\n
    getQbe(final String attribute)\n
    '''
def hasQbe():
    '''returns boolean\n\n
    hasQbe()\n
    '''
def setFlags():
    '''returns None\n\n
    setFlags(final long flags)\n
    '''
def getFlags():
    '''returns long\n\n
    getFlags()\n
    '''
def setFlag():
    '''returns None\n\n
    setFlag(final long flag, final boolean state)\n
    setFlag(final long flag, final boolean state, final MXException mxe)\n
    '''
def isFlagSet():
    '''returns boolean\n\n
    isFlagSet(final long flag)\n
    '''
def applyRowSecurity():
    '''returns None\n\n
    applyRowSecurity()\n
    '''
def getAlwaysFlags():
    '''returns BitFlag\n\n
    getAlwaysFlags()\n
    getAlwaysFlags(final String attr)\n
    '''
def enableMethod():
    '''returns None\n\n
    enableMethod(final String methodName, final boolean state)\n
    '''
def checkMethodAccess():
    '''returns None\n\n
    checkMethodAccess(final String methodName, final long accessModifier)\n
    '''
def getUserName():
    '''returns String\n\n
    getUserName()\n
    '''
def getProfile():
    '''returns ProfileRemote\n\n
    getProfile()\n
    '''
def copyForDM():
    '''returns None\n\n
    copyForDM(final MboSetRemote mboset, final int begin, final int size)\n
    '''
def getSharedMboSet():
    '''returns MboSetRemote\n\n
    getSharedMboSet(String objectName, final String relationship)\n
    '''
def getWarnings():
    '''returns MXException[]\n\n
    getWarnings()\n
    '''
def clearWarnings():
    '''returns None\n\n
    clearWarnings()\n
    '''
def hasWarnings():
    '''returns boolean\n\n
    hasWarnings()\n
    '''
def addWarning():
    '''returns None\n\n
    addWarning(final MXException e)\n
    '''
def addWarnings():
    '''returns None\n\n
    addWarnings(final MXException[] es)\n
    '''
def setMXTransaction():
    '''returns None\n\n
    setMXTransaction(final MXTransaction txn)\n
    '''
def getMXTransaction():
    '''returns MXTransaction\n\n
    getMXTransaction()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    save(final long flags)\n
    save(final MXTransaction txn)\n
    save(final MXTransaction txn, final long flags)\n
    '''
def saveTransaction():
    '''returns None\n\n
    saveTransaction(final MXTransaction txn)\n
    '''
def validateTransaction():
    '''returns boolean\n\n
    validateTransaction(final MXTransaction txn)\n
    '''
def saveMbos():
    '''returns None\n\n
    saveMbos()\n
    '''
def fireEventsBeforeDB():
    '''returns None\n\n
    fireEventsBeforeDB(final MXTransaction txn)\n
    '''
def fireEventsAfterDB():
    '''returns None\n\n
    fireEventsAfterDB(final MXTransaction txn)\n
    '''
def fireEventsAfterDBCommit():
    '''returns None\n\n
    fireEventsAfterDBCommit(final MXTransaction txn)\n
    '''
def commitTransaction():
    '''returns None\n\n
    commitTransaction(final MXTransaction txn)\n
    '''
def rollbackTransaction():
    '''returns None\n\n
    rollbackTransaction(final MXTransaction txn)\n
    '''
def undoTransaction():
    '''returns None\n\n
    undoTransaction(final MXTransaction txn)\n
    '''
def logRowUpdatedException():
    '''returns None\n\n
    logRowUpdatedException(final MXRowUpdateException mxr)\n
    '''
def getQbeWhere():
    '''returns String\n\n
    getQbeWhere()\n
    '''
def isLookup():
    '''returns boolean\n\n
    isLookup()\n
    '''
def getQualifiedWhere():
    '''returns String\n\n
    getQualifiedWhere()\n
    '''
def getMaxAppsWhere():
    '''returns String\n\n
    getMaxAppsWhere()\n
    '''
def setTableDomainLookup():
    '''returns None\n\n
    setTableDomainLookup(final boolean flag)\n
    '''
def isTableDomainLookup():
    '''returns boolean\n\n
    isTableDomainLookup()\n
    '''
def setDMDeploySet():
    '''returns None\n\n
    setDMDeploySet(final boolean flag)\n
    '''
def isDMDeploySet():
    '''returns boolean\n\n
    isDMDeploySet()\n
    '''
def isDMSkipFieldValidation():
    '''returns boolean\n\n
    isDMSkipFieldValidation()\n
    '''
def setDMSkipFieldValidation():
    '''returns None\n\n
    setDMSkipFieldValidation(final boolean flag)\n
    '''
def getCompleteWhere():
    '''returns String\n\n
    getCompleteWhere()\n
    '''
def setWhereQbe():
    '''returns None\n\n
    setWhereQbe(final String attribute, final String value, final String where)\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup()\n
    '''
def startCheckpoint():
    '''returns None\n\n
    startCheckpoint()\n
    startCheckpoint(final int i)\n
    '''
def rollbackToCheckpoint():
    '''returns None\n\n
    rollbackToCheckpoint()\n
    rollbackToCheckpoint(final int i)\n
    '''
def select():
    '''returns None\n\n
    select(final int index)\n
    select(final int startIndex, final int count)\n
    select(final Vector mboIndices)\n
    '''
def getSelection():
    '''returns Vector<MboRemote>\n\n
    getSelection()\n
    '''
def unselect():
    '''returns None\n\n
    unselect(final int index)\n
    unselect(final int startIndex, final int count)\n
    unselect(final Vector mboIndices)\n
    '''
def selectAll():
    '''returns None\n\n
    selectAll()\n
    '''
def unselectAll():
    '''returns None\n\n
    unselectAll()\n
    '''
def resetWithSelection():
    '''returns None\n\n
    resetWithSelection()\n
    '''
def getSelectionWhere():
    '''returns String\n\n
    getSelectionWhere()\n
    '''
def getMultiSiteWhere():
    '''returns String\n\n
    getMultiSiteWhere()\n
    '''
def setAppWhere():
    '''returns None\n\n
    setAppWhere(final String appWhere)\n
    '''
def getAppWhere():
    '''returns String\n\n
    getAppWhere()\n
    '''
def setDefaultValue():
    '''returns None\n\n
    setDefaultValue(final String attribute, String value)\n
    setDefaultValue(final String attribute, final MboRemote mbo)\n
    '''
def getDefaultValue():
    '''returns String\n\n
    getDefaultValue(final String attribute)\n
    '''
def setDefaultValues():
    '''returns None\n\n
    setDefaultValues(final String[] attributes, final String[] values)\n
    setDefaultValues(final String attribute, String value)\n
    '''
def isESigNeeded():
    '''returns boolean\n\n
    isESigNeeded(final String optionName)\n
    '''
def isESigFieldModified():
    '''returns boolean\n\n
    isESigFieldModified()\n
    '''
def setESigFieldModified():
    '''returns None\n\n
    setESigFieldModified(final boolean eSigFieldModified)\n
    '''
def isEAuditFieldModified():
    '''returns boolean\n\n
    isEAuditFieldModified()\n
    '''
def setEAuditFieldModified():
    '''returns None\n\n
    setEAuditFieldModified(final boolean eAuditFieldModified)\n
    '''
def handleMLMbo():
    '''returns None\n\n
    handleMLMbo(final Mbo mbo, final MXTransaction txn, final String action)\n
    handleMLMbo(final Mbo mbo, final String action)\n
    '''
def getESigTransactionId():
    '''returns String\n\n
    getESigTransactionId()\n
    '''
def clearESigTransIDForAdmin():
    '''returns None\n\n
    clearESigTransIDForAdmin()\n
    '''
def setLastESigTransId():
    '''returns None\n\n
    setLastESigTransId(final String id)\n
    '''
def verifyESig():
    '''returns boolean\n\n
    verifyESig(final String loginid, final String password, final String reason)\n
    '''
def logESigVerification():
    '''returns None\n\n
    logESigVerification(final String username, final String reason, final boolean authenticatedSuccessfully)\n
    '''
def isBasedOn():
    '''returns boolean\n\n
    isBasedOn(final String objectName)\n
    '''
def getKeyAttributes():
    '''returns String[]\n\n
    getKeyAttributes()\n
    '''
def getMboLogger():
    '''returns MXLogger\n\n
    getMboLogger()\n
    '''
def getSecurityLogger():
    '''returns MXLogger\n\n
    getSecurityLogger()\n
    '''
def getSqlLogger():
    '''returns MXLogger\n\n
    getSqlLogger()\n
    '''
def setAutoKeyFlag():
    '''returns boolean\n\n
    setAutoKeyFlag(final boolean flag)\n
    '''
def ignoreAutokeyAttr():
    '''returns None\n\n
    ignoreAutokeyAttr(final String attrName, final boolean flag)\n
    ignoreAutokeyAttr(final String[] attrNames, final boolean flag)\n
    '''
def getIgnoredAutokeyAttrs():
    '''returns HashSet\n\n
    getIgnoredAutokeyAttrs()\n
    '''
def clearIgnoredAutokeyAttrs():
    '''returns None\n\n
    clearIgnoredAutokeyAttrs()\n
    '''
def findByIntegrationKey():
    '''returns MboRemote\n\n
    findByIntegrationKey(final String[] integrationKeys, final String[] integrationKeyValues)\n
    '''
def setRelationName():
    '''returns None\n\n
    setRelationName(final String relationName)\n
    '''
def getRelationName():
    '''returns String\n\n
    getRelationName()\n
    '''
def hasMLQbe():
    '''returns boolean\n\n
    hasMLQbe()\n
    '''
def getMboForUniqueId():
    '''returns MboRemote\n\n
    getMboForUniqueId(final long id)\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage(final String errGrp, final String errKey)\n
    getMessage(final String errGrp, final String errKey, final Object[] params)\n
    getMessage(final String errGrp, final String errKey, Object param)\n
    getMessage(final MXException ex)\n
    '''
def getMaxMessage():
    '''returns MaxMessage\n\n
    getMaxMessage(final String errGrp, final String errKey)\n
    '''
def setQueryBySiteQbe():
    '''returns None\n\n
    setQueryBySiteQbe()\n
    '''
def setLogLargFetchResultDisabled():
    '''returns boolean\n\n
    setLogLargFetchResultDisabled(final boolean disable)\n
    '''
def addSubQbe():
    '''returns None\n\n
    addSubQbe(final String name, final String[] attrs, final String operator)\n
    addSubQbe(final String name, final String[] attrs, final String operator, final boolean exactMatch)\n
    addSubQbe(final String parentQbe, final String name, final String[] attrs, final String operator, final boolean exactMatch)\n
    addSubQbe(final String parentQbe, final String name, final String[] attrs, final String operator)\n
    '''
def setInsertSite():
    '''returns None\n\n
    setInsertSite(final String site)\n
    '''
def setInsertOrg():
    '''returns None\n\n
    setInsertOrg(final String org)\n
    '''
def setInsertCompanySet():
    '''returns None\n\n
    setInsertCompanySet(final String compSet)\n
    '''
def setInsertItemSet():
    '''returns None\n\n
    setInsertItemSet(final String itemSet)\n
    '''
def setExcludeMeFromPropagation():
    '''returns None\n\n
    setExcludeMeFromPropagation(final boolean flag)\n
    '''
def getExcludeMeFromPropagation():
    '''returns boolean\n\n
    getExcludeMeFromPropagation()\n
    '''
def getInsertSite():
    '''returns String\n\n
    getInsertSite()\n
    '''
def getInsertOrg():
    '''returns String\n\n
    getInsertOrg()\n
    '''
def setAllowQualifiedRestriction():
    '''returns None\n\n
    setAllowQualifiedRestriction(final boolean value)\n
    '''
def getAllowQualifiedRestriction():
    '''returns boolean\n\n
    getAllowQualifiedRestriction()\n
    '''
def getInsertCompanySet():
    '''returns String\n\n
    getInsertCompanySet()\n
    '''
def getInsertItemSet():
    '''returns String\n\n
    getInsertItemSet()\n
    '''
def sort():
    '''returns None\n\n
    sort()\n
    '''
def clearTransactionReference():
    '''returns None\n\n
    clearTransactionReference()\n
    '''
def locateMbo():
    '''returns MboRemote\n\n
    locateMbo(final String[] keys, final String[] values, final int option)\n
    '''
def setupLongOpPipe():
    '''returns InputStream\n\n
    setupLongOpPipe()\n
    '''
def clearLongOpPipe():
    '''returns None\n\n
    clearLongOpPipe()\n
    '''
def abortSql():
    '''returns None\n\n
    abortSql()\n
    '''
def getQueryTimeout():
    '''returns int\n\n
    getQueryTimeout()\n
    '''
def setQueryTimeout():
    '''returns None\n\n
    setQueryTimeout(final int queryTimeout)\n
    '''
def addToEndOfSelectStatement():
    '''returns String\n\n
    addToEndOfSelectStatement(final boolean fetchLimitEanbled)\n
    '''
def setAppAlwaysFieldFlag():
    '''returns None\n\n
    setAppAlwaysFieldFlag(final String attr, final long flag, final boolean state)\n
    '''
def getAppAlwaysFieldFlags():
    '''returns BitFlag\n\n
    getAppAlwaysFieldFlags(final String attr)\n
    '''
def setTxnPropertyMap():
    '''returns None\n\n
    setTxnPropertyMap(final Map<Object, Object> map)\n
    '''
def getQbeSiteAuthorization():
    '''returns String\n\n
    getQbeSiteAuthorization()\n
    '''
def findAllNullRequiredFields():
    '''returns List<ERMAttributeError>\n\n
    findAllNullRequiredFields()\n
    '''
def determineRequiredFieldsFromERM():
    '''returns List<ERMAttributeError>\n\n
    determineRequiredFieldsFromERM()\n
    '''
def setRequiedFlagsFromERM():
    '''returns None\n\n
    setRequiedFlagsFromERM()\n
    '''
def setERMEntity():
    '''returns None\n\n
    setERMEntity(final ERMEntity ermEntity)\n
    '''
def getERMEntity():
    '''returns ERMEntity\n\n
    getERMEntity()\n
    '''
def isRetainMboPosition():
    '''returns boolean\n\n
    isRetainMboPosition()\n
    '''
def setRetainMboPosition():
    '''returns None\n\n
    setRetainMboPosition(final boolean retainMboPosition)\n
    '''
def getMboSetRetainMboPositionInfo():
    '''returns MboSetRetainMboPositionInfo\n\n
    getMboSetRetainMboPositionInfo()\n
    '''
def getMboSetRetainMboPositionData():
    '''returns MboSetRetainMboPositionData\n\n
    getMboSetRetainMboPositionData()\n
    '''
def positionState():
    '''returns None\n\n
    positionState()\n
    '''
def setDBFetchMaxRows():
    '''returns None\n\n
    setDBFetchMaxRows(final int fetchLimit)\n
    '''
def getDBFetchMaxRows():
    '''returns int\n\n
    getDBFetchMaxRows()\n
    '''
def setSkipFirstNRows():
    '''returns None\n\n
    setSkipFirstNRows(final int skipRows)\n
    '''
def getSkipFirstNRows():
    '''returns int\n\n
    getSkipFirstNRows()\n
    '''
def getSetOrderByForUI():
    '''returns String\n\n
    getSetOrderByForUI()\n
    '''
def setSetOrderByForUI():
    '''returns None\n\n
    setSetOrderByForUI(final String orderBy)\n
    '''
def isDeltaStorage():
    '''returns boolean\n\n
    isDeltaStorage(final Mbo mbo, final String tableName)\n
    '''
def setFederatedResources():
    '''returns None\n\n
    setFederatedResources(final String federatedResourcesStr)\n
    '''
def addFederatedMboToSorter():
    '''returns None\n\n
    addFederatedMboToSorter(final MboRemote mbo)\n
    '''
def executeBatch():
    '''returns None\n\n
    executeBatch()\n
    '''
def getPreparedStmt():
    '''returns PreparedStatement\n\n
    getPreparedStmt(final Connection con, final String sql)\n
    '''
def clearBatchedPreparedStmt():
    '''returns None\n\n
    clearBatchedPreparedStmt(final String sql)\n
    '''
def clearBatchedPreparedStmts():
    '''returns None\n\n
    clearBatchedPreparedStmts()\n
    '''
def isDownloadSet():
    '''returns boolean\n\n
    isDownloadSet()\n
    '''
def setDownloadSet():
    '''returns None\n\n
    setDownloadSet(final boolean isDownloadSet)\n
    '''
