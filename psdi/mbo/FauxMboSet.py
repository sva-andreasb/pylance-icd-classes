def ():
    '''returns FauxMboSet\n\n
    (final MboRemote owner)\n
    '''
def findKey():
    '''returns MboRemote\n\n
    findKey(final Object keyObject)\n
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
def getUserWhere():
    '''returns String\n\n
    getUserWhere(final String alias)\n
    '''
def getUserAndQbeWhere():
    '''returns String\n\n
    getUserAndQbeWhere()\n
    '''
def getQbeWhere():
    '''returns String\n\n
    getQbeWhere()\n
    '''
def useStoredQuery():
    '''returns None\n\n
    useStoredQuery(final String queryName)\n
    '''
def setOrderBy():
    '''returns None\n\n
    setOrderBy(final String orderByClause)\n
    '''
def setDefaultOrderBy():
    '''returns None\n\n
    setDefaultOrderBy()\n
    '''
def getOrderBy():
    '''returns String\n\n
    getOrderBy()\n
    '''
def setSQLOptions():
    '''returns None\n\n
    setSQLOptions(final String sqlOptions)\n
    '''
def getSQLOptions():
    '''returns String\n\n
    getSQLOptions()\n
    '''
def setFetchAttributes():
    '''returns None\n\n
    setFetchAttributes(final String[] attributes)\n
    '''
def getFetchAttributes():
    '''returns String[]\n\n
    getFetchAttributes()\n
    getFetchAttributes(final String rel)\n
    '''
def hasFetchAttributes():
    '''returns boolean\n\n
    hasFetchAttributes()\n
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
def addFakeAtEnd():
    '''returns MboRemote\n\n
    addFakeAtEnd()\n
    '''
def addAtIndex():
    '''returns MboRemote\n\n
    addAtIndex(final long accessModifier, final int index)\n
    '''
def count():
    '''returns int\n\n
    count(final int countConstant)\n
    count()\n
    '''
def sum():
    '''returns double\n\n
    sum(final String attribute)\n
    '''
def min():
    '''returns double\n\n
    min(final String attribute)\n
    '''
def max():
    '''returns double\n\n
    max(final String attribute)\n
    '''
def latestDate():
    '''returns Date\n\n
    latestDate(final String attributeName)\n
    '''
def earliestDate():
    '''returns Date\n\n
    earliestDate(final String attributeName)\n
    '''
def isEmpty():
    '''returns boolean\n\n
    isEmpty()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    save(final long flag)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def getCurrentPosition():
    '''returns int\n\n
    getCurrentPosition()\n
    '''
def toBeSaved():
    '''returns boolean\n\n
    toBeSaved()\n
    '''
def getMbo():
    '''returns MboRemote\n\n
    getMbo()\n
    getMbo(final int pos)\n
    '''
def getMboValueData():
    '''returns MboValueData[][]\n\n
    getMboValueData(final String attribute)\n
    getMboValueData(final String[] attribute)\n
    getMboValueData(final int rowStart, final int rowCount, final String[] attribute)\n
    '''
def getMboSetData():
    '''returns MboSetData\n\n
    getMboSetData(final String[] attributes)\n
    getMboSetData(final int row, final int count, final String[] attributes)\n
    '''
def resetQbe():
    '''returns None\n\n
    resetQbe()\n
    '''
def setQbe():
    '''returns None\n\n
    setQbe(final String attribute, final String expression)\n
    setQbe(final String attribute, final String[] expression)\n
    setQbe(final String[] attribute, final String expression)\n
    setQbe(final String[] attribute, final String[] expression)\n
    setQbe(final String attribute, final MboSetRemote lookup)\n
    '''
def setQbeOperatorOr():
    '''returns None\n\n
    setQbeOperatorOr()\n
    '''
def getQbe():
    '''returns String[]\n\n
    getQbe()\n
    getQbe(final String attribute)\n
    getQbe(final String[] attribute)\n
    '''
def hasQbe():
    '''returns boolean\n\n
    hasQbe()\n
    '''
def setQbeExactMatch():
    '''returns None\n\n
    setQbeExactMatch(final boolean state)\n
    setQbeExactMatch(final String state)\n
    '''
def isQbeExactMatch():
    '''returns boolean\n\n
    isQbeExactMatch()\n
    '''
def ignoreQbeExactMatchSet():
    '''returns None\n\n
    ignoreQbeExactMatchSet(final boolean flag)\n
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
def getList():
    '''returns MboSetRemote\n\n
    getList(final String attributeName)\n
    getList(final int row, final String attributeName)\n
    '''
def init():
    '''returns None\n\n
    init(final UserInfo ui)\n
    '''
def getOwner():
    '''returns MboRemote\n\n
    getOwner()\n
    '''
def checkMethodAccess():
    '''returns None\n\n
    checkMethodAccess(final String methodName)\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
def commit():
    '''returns None\n\n
    commit()\n
    '''
def rollback():
    '''returns None\n\n
    rollback()\n
    '''
def getClientLocale():
    '''returns Locale\n\n
    getClientLocale()\n
    '''
def getClientTimeZone():
    '''returns TimeZone\n\n
    getClientTimeZone()\n
    '''
def setOwner():
    '''returns None\n\n
    setOwner(final MboRemote mbo)\n
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
def setRelationship():
    '''returns None\n\n
    setRelationship(final String relationClause)\n
    '''
def getRelationship():
    '''returns String\n\n
    getRelationship()\n
    '''
def setMboSetInfo():
    '''returns None\n\n
    setMboSetInfo(final MboSetInfo ms)\n
    '''
def fetchNext():
    '''returns MboRemote\n\n
    fetchNext()\n
    '''
def isFlagSet():
    '''returns boolean\n\n
    isFlagSet(final long flag)\n
    '''
def getFlags():
    '''returns long\n\n
    getFlags()\n
    '''
def setFlags():
    '''returns None\n\n
    setFlags(final long flags)\n
    '''
def setFlag():
    '''returns None\n\n
    setFlag(final long flag, final boolean state)\n
    setFlag(final long flag, final boolean state, final MXException mxe)\n
    '''
def getUserName():
    '''returns String\n\n
    getUserName()\n
    '''
def getMboSetInfo():
    '''returns MboSetInfo\n\n
    getMboSetInfo()\n
    '''
def setMXTransaction():
    '''returns None\n\n
    setMXTransaction(final MXTransaction txn)\n
    '''
def getMXTransaction():
    '''returns MXTransaction\n\n
    getMXTransaction()\n
    '''
def getCompleteWhere():
    '''returns String\n\n
    getCompleteWhere()\n
    '''
def getMboSetValueData():
    '''returns MboValueData\n\n
    getMboSetValueData(final String[] attribute)\n
    getMboSetValueData(final String attribute)\n
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
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def incrementDeletedCount():
    '''returns None\n\n
    incrementDeletedCount(final boolean inc)\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo()\n
    '''
def getZombie():
    '''returns MboRemote\n\n
    getZombie()\n
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
def setOverrideOptimisticLock():
    '''returns None\n\n
    setOverrideOptimisticLock(final boolean val)\n
    '''
def select():
    '''returns None\n\n
    select(final int index)\n
    select(final Vector mboIndices)\n
    select(final int startIndex, final int count)\n
    '''
def unselect():
    '''returns None\n\n
    unselect(final int index)\n
    unselect(final Vector mboIndices)\n
    unselect(final int startIndex, final int count)\n
    '''
def getSelection():
    '''returns Vector\n\n
    getSelection()\n
    '''
def selectAll():
    '''returns None\n\n
    selectAll()\n
    '''
def unselectAll():
    '''returns None\n\n
    unselectAll()\n
    '''
def setWhereQbe():
    '''returns None\n\n
    setWhereQbe(final String attribute, final String value, final String where)\n
    '''
def resetWithSelection():
    '''returns None\n\n
    resetWithSelection()\n
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
def getDefaultValueHash():
    '''returns HashMap\n\n
    getDefaultValueHash()\n
    '''
def setDefaultValues():
    '''returns None\n\n
    setDefaultValues(final String[] attributes, final String[] values)\n
    setDefaultValues(final String attribute, String value)\n
    '''
def getJspDefaultValueHash():
    '''returns HashMap\n\n
    getJspDefaultValueHash()\n
    '''
def isESigNeeded():
    '''returns boolean\n\n
    isESigNeeded(final String optionName)\n
    '''
def verifyESig():
    '''returns boolean\n\n
    verifyESig(final String username, final String password, final String reason)\n
    '''
def logESigVerification():
    '''returns None\n\n
    logESigVerification(final String username, final String reason, final boolean authenticatedSuccessfully)\n
    '''
def getESigTransactionId():
    '''returns String\n\n
    getESigTransactionId()\n
    '''
def setLastESigTransId():
    '''returns None\n\n
    setLastESigTransId(final String id)\n
    '''
def setESigFieldModified():
    '''returns None\n\n
    setESigFieldModified(final boolean esigFieldModified)\n
    '''
def saveTransaction():
    '''returns None\n\n
    saveTransaction(final MXTransaction txn)\n
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
def validateTransaction():
    '''returns boolean\n\n
    validateTransaction(final MXTransaction txn)\n
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
    setValue(final String attributeName, final boolean val)\n
    setValue(final String attributeName, final byte val)\n
    setValue(final String attributeName, final short val)\n
    setValue(final String attributeName, final int val)\n
    setValue(final String attributeName, final long val)\n
    setValue(final String attributeName, final float val)\n
    setValue(final String attributeName, final double val)\n
    setValue(final String attributeName, final byte[] val)\n
    setValue(final String attributeName, final Date val)\n
    setValue(final String attributeName, final String val, final long accessModifier)\n
    setValue(final String attributeName, final boolean val, final long accessModifier)\n
    setValue(final String attributeName, final byte val, final long accessModifier)\n
    setValue(final String attributeName, final short val, final long accessModifier)\n
    setValue(final String attributeName, final int val, final long accessModifier)\n
    setValue(final String attributeName, final long val, final long accessModifier)\n
    setValue(final String attributeName, final float val, final long accessModifier)\n
    setValue(final String attributeName, final double val, final long accessModifier)\n
    setValue(final String attributeName, final byte[] val, final long accessModifier)\n
    setValue(final String attributeName, final Date val, final long accessModifier)\n
    '''
def isClosed():
    '''returns boolean\n\n
    isClosed()\n
    '''
def getSelectionWhere():
    '''returns String\n\n
    getSelectionWhere()\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final MboSetListener l)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final MboSetListener l)\n
    '''
def reportModifiedMbo():
    '''returns None\n\n
    reportModifiedMbo(final MboRemote modifiedMbo)\n
    '''
def setTableDomainLookup():
    '''returns None\n\n
    setTableDomainLookup(final boolean flag)\n
    '''
def isBasedOn():
    '''returns boolean\n\n
    isBasedOn(final String objectName)\n
    '''
def getKeyAttributes():
    '''returns String[]\n\n
    getKeyAttributes()\n
    '''
def getProfile():
    '''returns ProfileRemote\n\n
    getProfile()\n
    '''
def setAutoKeyFlag():
    '''returns boolean\n\n
    setAutoKeyFlag(final boolean flag)\n
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
def smartFill():
    '''returns MboSetRemote\n\n
    smartFill(final String attributeName, final String value, final boolean exact)\n
    smartFill(final int row, final String attributeName, final String value, final boolean exact)\n
    '''
def smartFind():
    '''returns MboSetRemote\n\n
    smartFind(final String objectName, final String attributeName, final String value, final boolean exact)\n
    smartFind(final int row, final String objectName, final String attributeName, final String value, final boolean exact)\n
    smartFind(final String attributeName, final String value, final boolean exact)\n
    smartFind(final int row, final String attributeName, final String value, final boolean exact)\n
    '''
def getMLFromClause():
    '''returns StringBuffer\n\n
    getMLFromClause(final boolean useSchemaOwner)\n
    '''
def hasMLQbe():
    '''returns boolean\n\n
    hasMLQbe()\n
    '''
def getMboValueInfoStatic():
    '''returns MboValueInfoStatic[]\n\n
    getMboValueInfoStatic(final String attribute)\n
    getMboValueInfoStatic(final String[] attribute)\n
    '''
def isFromGetList():
    '''returns boolean\n\n
    isFromGetList()\n
    '''
def setFromGetList():
    '''returns None\n\n
    setFromGetList(final boolean value)\n
    '''
def getMboForUniqueId():
    '''returns MboRemote\n\n
    getMboForUniqueId(final long id)\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage(final String errGrp, final String errKey)\n
    getMessage(final String errGrp, final String errKey, final Object[] params)\n
    getMessage(final String errGrp, final String errKey, final Object param)\n
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
    addSubQbe(final String name, final String[] attrs, final String operator, final boolean exactMatch)\n
    addSubQbe(final String name, final String[] attrs, final String operator)\n
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
def processML():
    '''returns boolean\n\n
    processML()\n
    '''
def isIgnoreQbeExactMatchSet():
    '''returns boolean\n\n
    isIgnoreQbeExactMatchSet()\n
    '''
def setNoNeedtoFetchFromDB():
    '''returns None\n\n
    setNoNeedtoFetchFromDB(final boolean flag)\n
    '''
def setUserWhereAfterParse():
    '''returns None\n\n
    setUserWhereAfterParse(final String where)\n
    '''
def copyForDM():
    '''returns None\n\n
    copyForDM(final MboSetRemote mboset, final int begin, final int size)\n
    '''
def locateMbo():
    '''returns MboRemote\n\n
    locateMbo(final String[] keys, final String[] values, final int option)\n
    '''
def setDMDeploySet():
    '''returns None\n\n
    setDMDeploySet(final boolean flag)\n
    '''
def isDMDeploySet():
    '''returns boolean\n\n
    isDMDeploySet()\n
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
def setAllowQualifiedRestriction():
    '''returns None\n\n
    setAllowQualifiedRestriction(final boolean value)\n
    '''
def setTxnPropertyMap():
    '''returns None\n\n
    setTxnPropertyMap(final Map<Object, Object> map)\n
    '''
def isDMSkipFieldValidation():
    '''returns boolean\n\n
    isDMSkipFieldValidation()\n
    '''
def setDMSkipFieldValidation():
    '''returns None\n\n
    setDMSkipFieldValidation(final boolean flag)\n
    '''
def setAppAlwaysFieldFlag():
    '''returns None\n\n
    setAppAlwaysFieldFlag(final String attr, final long flag, final boolean state)\n
    '''
def getAppAlwaysFieldFlags():
    '''returns BitFlag\n\n
    getAppAlwaysFieldFlags(final String attr)\n
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
def getMboSetRetainMboPositionData():
    '''returns MboSetRetainMboPositionData\n\n
    getMboSetRetainMboPositionData()\n
    '''
def getMboSetRetainMboPositionInfo():
    '''returns MboSetRetainMboPositionInfo\n\n
    getMboSetRetainMboPositionInfo()\n
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
def getSetOrderByForUI():
    '''returns String\n\n
    getSetOrderByForUI()\n
    '''
def setSetOrderByForUI():
    '''returns None\n\n
    setSetOrderByForUI(final String orderBy)\n
    '''
def newMboIndex():
    '''returns int\n\n
    newMboIndex()\n
    '''
def isDownloadSet():
    '''returns boolean\n\n
    isDownloadSet()\n
    '''
def setDownloadSet():
    '''returns None\n\n
    setDownloadSet(final boolean isDownloadSet)\n
    '''
