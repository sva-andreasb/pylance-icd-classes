MULTILANGCOPY = "String  \"MultiLangCopy\""
def ():
    '''returns Mbo\n\n
    (final MboSet ms)\n
    '''
def setProxy():
    '''returns None\n\n
    setProxy(final Remote proxy)\n
    '''
def getProxy():
    '''returns Remote\n\n
    getProxy()\n
    '''
def getMboRecordData():
    '''returns MboRecordData\n\n
    getMboRecordData()\n
    '''
def setNewMbo():
    '''returns None\n\n
    setNewMbo(final boolean flag)\n
    '''
def getStringInBaseLanguage():
    '''returns String\n\n
    getStringInBaseLanguage(final String attributeName)\n
    '''
def getString():
    '''returns String\n\n
    getString(String attributeName, final String langCode)\n
    getString(final String attributeName)\n
    '''
def getStringTransparent():
    '''returns String\n\n
    getStringTransparent(final String attributeName, final String langCode)\n
    '''
def setMLValue():
    '''returns None\n\n
    setMLValue(final String attributeName, final String langCode, final String value, final long accessModifier)\n
    '''
def getRelationshipNameToLangTable():
    '''returns String\n\n
    getRelationshipNameToLangTable(final String attributeName)\n
    '''
def getDatabaseValue():
    '''returns Object\n\n
    getDatabaseValue(final String attributeName)\n
    '''
def setFetchIndex():
    '''returns None\n\n
    setFetchIndex(final int index)\n
    '''
def getFetchIndex():
    '''returns int\n\n
    getFetchIndex()\n
    '''
def setModified():
    '''returns None\n\n
    setModified(final boolean modified)\n
    '''
def setModifiedForIntegrationOnly():
    '''returns None\n\n
    setModifiedForIntegrationOnly(final boolean modified)\n
    '''
def setDeleted():
    '''returns None\n\n
    setDeleted(final boolean deleted)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getRecordMboName():
    '''returns String\n\n
    getRecordMboName()\n
    '''
def getOwner():
    '''returns MboRemote\n\n
    getOwner()\n
    '''
def getThisMboSet():
    '''returns MboSetRemote\n\n
    getThisMboSet()\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def hasUniqueID():
    '''returns boolean\n\n
    hasUniqueID()\n
    '''
def getUniqueIdentifer():
    '''returns String\n\n
    getUniqueIdentifer()\n
    '''
def getLockedByDisplayName():
    '''returns String\n\n
    getLockedByDisplayName()\n
    '''
def getLockedByUserID():
    '''returns String\n\n
    getLockedByUserID()\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def setReadonlyWhenParentIsReadonly():
    '''returns None\n\n
    setReadonlyWhenParentIsReadonly(final String relationshipName, final MboSetRemote mboSet, final boolean flag)\n
    '''
def getClientLocale():
    '''returns Locale\n\n
    getClientLocale()\n
    '''
def getClientTimeZone():
    '''returns TimeZone\n\n
    getClientTimeZone()\n
    '''
def getMboValue():
    '''returns MboValue\n\n
    getMboValue(final String nameInput)\n
    '''
def moveFieldFlagsToMboValue():
    '''returns None\n\n
    moveFieldFlagsToMboValue(final MboValue mv)\n
    '''
def getInstanciatedMboValue():
    '''returns MboValue\n\n
    getInstanciatedMboValue(String name)\n
    '''
def getMboInitialValue():
    '''returns MaxType\n\n
    getMboInitialValue(final String name)\n
    '''
def getInstanciatedMboSet():
    '''returns MboSetRemote\n\n
    getInstanciatedMboSet(final String relationshipName)\n
    '''
def getMboValueData():
    '''returns MboValueData[]\n\n
    getMboValueData(final String attribute)\n
    getMboValueData(final String attribute, final boolean ignoreFieldFlags)\n
    getMboValueData(final String[] attribute)\n
    '''
def getMboValueDataForDownload():
    '''returns MboValueData[]\n\n
    getMboValueDataForDownload(final String[] attribute)\n
    '''
def getMboData():
    '''returns MboData\n\n
    getMboData(final String[] attributes)\n
    '''
def getMboValueInfoStatic():
    '''returns MboValueInfoStatic[]\n\n
    getMboValueInfoStatic(final String attribute)\n
    getMboValueInfoStatic(final String[] attribute)\n
    '''
def getMboForAttribute():
    '''returns MboRemote\n\n
    getMboForAttribute(final String attributeName)\n
    '''
def getMboForAttributeStatic():
    '''returns MboRemote\n\n
    getMboForAttributeStatic(final String attributeName)\n
    '''
def getList():
    '''returns MboSetRemote\n\n
    getList(final String attribute)\n
    '''
def smartFill():
    '''returns MboSetRemote\n\n
    smartFill(final String attribute, final String value, final boolean exact)\n
    '''
def smartFind():
    '''returns MboSetRemote\n\n
    smartFind(final String attribute, final String value, final boolean exact, final boolean isRecordHover)\n
    smartFind(final String attribute, final String value, final boolean exact)\n
    smartFind(final String appName, final String attribute, final String value, final boolean exact)\n
    '''
def smartFindByObjectName():
    '''returns MboSetRemote\n\n
    smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact, final String[][] cachedKeyMap)\n
    smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact)\n
    '''
def smartFindByObjectNameDirect():
    '''returns MboSetRemote\n\n
    smartFindByObjectNameDirect(final String sourceObj, final String targetAttrName, final String value, final boolean exact)\n
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
def setValue():
    '''returns None\n\n
    setValue(final String attributeName, final String val, final long accessModifier)\n
    setValue(final String attributeName, final MaxType mboValue, final long accessModifier)\n
    setValue(final String attributeName, final String val)\n
    setValue(final String attributeName, final boolean val)\n
    setValue(final String attributeName, final boolean val, final long accessModifier)\n
    setValue(final String attributeName, final byte val)\n
    setValue(final String attributeName, final byte val, final long accessModifier)\n
    setValue(final String attributeName, final int val)\n
    setValue(final String attributeName, final int val, final long accessModifier)\n
    setValue(final String attributeName, final float val)\n
    setValue(final String attributeName, final float val, final long accessModifier)\n
    setValue(final String attributeName, final byte[] val)\n
    setValue(final String attributeName, final byte[] val, final long accessModifier)\n
    setValue(final String attributeName, final Date val)\n
    setValue(final String attributeName, final Date val, final long accessModifier)\n
    setValue(final String attributeName, final short val)\n
    setValue(final String attributeName, final short val, final long accessModifier)\n
    setValue(final String attributeName, final long val)\n
    setValue(final String attributeName, final long val, final long accessModifier)\n
    setValue(final String attributeName, final double val)\n
    setValue(final String attributeName, final double val, final long accessModifier)\n
    setValue(final String targetAttrName, final MboRemote sourceMbo)\n
    setValue(final String targetAttrName, final MboSetRemote sourceMboSet)\n
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
def getKeyValue():
    '''returns KeyValue\n\n
    getKeyValue()\n
    '''
def getRecordIdentifer():
    '''returns String\n\n
    getRecordIdentifer()\n
    '''
def isAutoKeyed():
    '''returns boolean\n\n
    isAutoKeyed(final String attributeName)\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(String name, final String objectName)\n
    getMboSet(final String name, final String objectName, final String relationship)\n
    getMboSet(String name)\n
    '''
def getMboDataSet():
    '''returns Vector<MboRemote>\n\n
    getMboDataSet(final String relationship)\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid()\n
    '''
def isZombie():
    '''returns boolean\n\n
    isZombie()\n
    '''
def setForDM():
    '''returns None\n\n
    setForDM(final boolean forDM)\n
    '''
def isForDM():
    '''returns boolean\n\n
    isForDM()\n
    '''
def setTenantIdForNoMboRecordData():
    '''returns None\n\n
    setTenantIdForNoMboRecordData(final int tenantId)\n
    '''
def getTenantIdForNoMboRecordData():
    '''returns int\n\n
    getTenantIdForNoMboRecordData()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    delete()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def toBeDeleted():
    '''returns boolean\n\n
    toBeDeleted()\n
    '''
def toBeAdded():
    '''returns boolean\n\n
    toBeAdded()\n
    '''
def isNew():
    '''returns boolean\n\n
    isNew()\n
    '''
def toBeUpdated():
    '''returns boolean\n\n
    toBeUpdated()\n
    '''
def thisToBeUpdated():
    '''returns boolean\n\n
    thisToBeUpdated()\n
    '''
def isModified():
    '''returns boolean\n\n
    isModified()\n
    isModified(final String attribute)\n
    '''
def setESigFieldModified():
    '''returns None\n\n
    setESigFieldModified(final boolean eSigFieldModified)\n
    '''
def isESigFieldModified():
    '''returns boolean\n\n
    isESigFieldModified()\n
    '''
def setEAuditFieldModified():
    '''returns None\n\n
    setEAuditFieldModified(final boolean eAuditFieldModified)\n
    '''
def isEAuditFieldModified():
    '''returns boolean\n\n
    isEAuditFieldModified()\n
    '''
def toBeValidated():
    '''returns boolean\n\n
    toBeValidated()\n
    '''
def toBeSaved():
    '''returns boolean\n\n
    toBeSaved()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def isApiBatchError():
    '''returns boolean\n\n
    isApiBatchError()\n
    '''
def checkQualifiedRestriction():
    '''returns None\n\n
    checkQualifiedRestriction()\n
    '''
def orEvaluateConditions():
    '''returns boolean\n\n
    orEvaluateConditions(final DataRestrictionCache.RestrictionBundle restrictions)\n
    '''
def useDataSecurity():
    '''returns boolean\n\n
    useDataSecurity(final String group)\n
    '''
def andEvaluateConditions():
    '''returns boolean\n\n
    andEvaluateConditions(final DataRestrictionCache.RestrictionBundle restrictions)\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
def getInsertItemSetId():
    '''returns String\n\n
    getInsertItemSetId()\n
    '''
def getInsertCompanySetId():
    '''returns String\n\n
    getInsertCompanySetId()\n
    '''
def getInsertSite():
    '''returns String\n\n
    getInsertSite()\n
    '''
def getInsertOrgForSite():
    '''returns String\n\n
    getInsertOrgForSite(final String site)\n
    '''
def getInsertOrganization():
    '''returns String\n\n
    getInsertOrganization()\n
    '''
def getOrgSiteForMaxvar():
    '''returns String\n\n
    getOrgSiteForMaxvar(final String maxvarName)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def valueChanged():
    '''returns None\n\n
    valueChanged()\n
    '''
def getMboServer():
    '''returns MboServerInterface\n\n
    getMboServer()\n
    '''
def getMboSetInfo():
    '''returns MboSetInfo\n\n
    getMboSetInfo(final String mboName)\n
    '''
def getTranslator():
    '''returns Translate\n\n
    getTranslator()\n
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
def evaluateRestriction():
    '''returns boolean\n\n
    evaluateRestriction(final DataRestriction restriction)\n
    '''
def getAttrRestrictionFlag():
    '''returns BitFlag\n\n
    getAttrRestrictionFlag(final String attr)\n
    '''
def getRowRestrictionFlag():
    '''returns BitFlag\n\n
    getRowRestrictionFlag()\n
    '''
def setFieldFlags():
    '''returns None\n\n
    setFieldFlags(final String name, final long flags)\n
    '''
def setFieldFlag():
    '''returns None\n\n
    setFieldFlag(final String name, final long flag, final boolean state)\n
    setFieldFlag(String name, final long flag, final boolean state, final MXException mxe)\n
    setFieldFlag(final String[] names, final long flag, final boolean state)\n
    setFieldFlag(final String[] names, final long flag, final boolean state, final MXException mxe)\n
    setFieldFlag(final String[] names, final boolean inclusive, final long flag, final boolean state)\n
    setFieldFlag(final String[] names, final boolean inclusive, final long flag, final boolean state, final MXException mxe)\n
    '''
def checkFieldAccess():
    '''returns None\n\n
    checkFieldAccess(final long accessModifier)\n
    '''
def hasFieldAccess():
    '''returns boolean\n\n
    hasFieldAccess(final long accessModifier)\n
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
def fireEvent():
    '''returns None\n\n
    fireEvent(final String type)\n
    '''
def getProfile():
    '''returns ProfileRemote\n\n
    getProfile()\n
    '''
def copy():
    '''returns MboRemote\n\n
    copy()\n
    copy(final MboSetRemote mboset)\n
    copy(final MboSetRemote mboset, final long mboAddFlags)\n
    '''
def copyFake():
    '''returns MboRemote\n\n
    copyFake(final MboSetRemote mboset)\n
    '''
def setAutokeyFields():
    '''returns None\n\n
    setAutokeyFields()\n
    '''
def blindCopy():
    '''returns MboRemote\n\n
    blindCopy(final MboSetRemote mboset)\n
    '''
def isSkipCopyField():
    '''returns boolean\n\n
    isSkipCopyField(final MboValueInfo mvi)\n
    '''
def setCopyDefaults():
    '''returns None\n\n
    setCopyDefaults()\n
    '''
def getMXTransaction():
    '''returns MXTransaction\n\n
    getMXTransaction()\n
    '''
def getRelatedWhere():
    '''returns String\n\n
    getRelatedWhere()\n
    getRelatedWhere(final String alias)\n
    '''
def hasRelatedQbe():
    '''returns boolean\n\n
    hasRelatedQbe()\n
    '''
def getIntegrationService():
    '''returns ServiceRemote\n\n
    getIntegrationService()\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def getCheckpoint():
    '''returns boolean\n\n
    getCheckpoint()\n
    '''
def startCheckpoint():
    '''returns None\n\n
    startCheckpoint()\n
    '''
def rollbackToCheckpoint():
    '''returns None\n\n
    rollbackToCheckpoint()\n
    '''
def select():
    '''returns None\n\n
    select()\n
    '''
def unselect():
    '''returns None\n\n
    unselect()\n
    '''
def isSelected():
    '''returns boolean\n\n
    isSelected()\n
    '''
def copyValue():
    '''returns None\n\n
    copyValue(final MboRemote sourceMbo, final String attrSource, final String attrTarget, final long flags)\n
    copyValue(final MboRemote sourceMbo, final String[] attrSource, final String[] attrTarget, final long flags)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def setPropagateKeyFlag():
    '''returns None\n\n
    setPropagateKeyFlag(final boolean flag)\n
    setPropagateKeyFlag(final String[] objectName, final boolean flag)\n
    '''
def excludeObjectForPropagate():
    '''returns boolean\n\n
    excludeObjectForPropagate(final String name)\n
    '''
def getPropagateKeyFlag():
    '''returns boolean\n\n
    getPropagateKeyFlag()\n
    '''
def propagateKeyValue():
    '''returns None\n\n
    propagateKeyValue(final String keyName, final String keyValue)\n
    '''
def setHierarchyLink():
    '''returns None\n\n
    setHierarchyLink(final boolean flag)\n
    '''
def hasHierarchyLink():
    '''returns boolean\n\n
    hasHierarchyLink()\n
    '''
def setDefaultValue():
    '''returns None\n\n
    setDefaultValue()\n
    '''
def setDefaultValues():
    '''returns None\n\n
    setDefaultValues()\n
    '''
def setAppDefaultValue():
    '''returns None\n\n
    setAppDefaultValue()\n
    '''
def isBasedOn():
    '''returns boolean\n\n
    isBasedOn(final String objectName)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
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
def getOrgForGL():
    '''returns String\n\n
    getOrgForGL(final String lookupAttr)\n
    '''
def getSiteOrg():
    '''returns String[]\n\n
    getSiteOrg()\n
    '''
def getUniqueIDName():
    '''returns String\n\n
    getUniqueIDName()\n
    '''
def getUniqueIDValue():
    '''returns long\n\n
    getUniqueIDValue()\n
    '''
def setUniqueIDValue():
    '''returns None\n\n
    setUniqueIDValue()\n
    '''
def setValueFromSequence():
    '''returns None\n\n
    setValueFromSequence(final String attributeName)\n
    '''
def getDocLinksCount():
    '''returns int\n\n
    getDocLinksCount()\n
    '''
def getLinesRelationship():
    '''returns String\n\n
    getLinesRelationship()\n
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
def createComm():
    '''returns MboRemote\n\n
    createComm()\n
    '''
def getMatchingAttr():
    '''returns String\n\n
    getMatchingAttr(final String attribute)\n
    getMatchingAttr(final String sourceObjectName, final String attribute)\n
    '''
def getStringInSpecificLocale():
    '''returns String\n\n
    getStringInSpecificLocale(final String attribute, final Locale l, final TimeZone tz)\n
    '''
def getMatchingAttrs():
    '''returns Object[]\n\n
    getMatchingAttrs(final String sourceName, final String targetAttr)\n
    '''
def sigOptionAccessAuthorized():
    '''returns None\n\n
    sigOptionAccessAuthorized(final String optionname)\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
    '''
def needCallInitFieldFlag():
    '''returns boolean\n\n
    needCallInitFieldFlag(final String attrName)\n
    '''
def checkSiteOrgAccessForSave():
    '''returns None\n\n
    checkSiteOrgAccessForSave()\n
    '''
def sigopGranted():
    '''returns boolean\n\n
    sigopGranted(final String optionname)\n
    sigopGranted(final String app, final String optionname)\n
    '''
def getCondition():
    '''returns MaxCondition\n\n
    getCondition(final String conditionNum)\n
    '''
def evaluateCondition():
    '''returns boolean\n\n
    evaluateCondition(final String conditionNum, final boolean logErrorOnly)\n
    evaluateCondition(final String conditionNum)\n
    '''
def getAlwaysFlags():
    '''returns BitFlag\n\n
    getAlwaysFlags(final String attr)\n
    '''
def getDomainIDs():
    '''returns String[]\n\n
    getDomainIDs(final String attr)\n
    '''
def addToDeleteForInsertList():
    '''returns None\n\n
    addToDeleteForInsertList(final String mboName)\n
    '''
def getDeleteForInsertList():
    '''returns Vector<String>\n\n
    getDeleteForInsertList()\n
    '''
def getInitialValue():
    '''returns MaxType\n\n
    getInitialValue(final String attributeName)\n
    '''
def getCommLogOwnerNameAndUniqueId():
    '''returns Object[]\n\n
    getCommLogOwnerNameAndUniqueId()\n
    '''
def isChangeByUserWhenSetFromLookup():
    '''returns boolean\n\n
    isChangeByUserWhenSetFromLookup(final String lookupAttrName, final String attributeName)\n
    '''
def validateKeyUniqueness():
    '''returns None\n\n
    validateKeyUniqueness()\n
    '''
def generateContentUID():
    '''returns None\n\n
    generateContentUID()\n
    '''
def getDomainFilterWhere():
    '''returns String\n\n
    getDomainFilterWhere(final String filterKeyword)\n
    '''
def removeRelatedSet():
    '''returns boolean\n\n
    removeRelatedSet(final MboSetRemote relatedSet)\n
    '''
def determineRequiredFieldsFromERM():
    '''returns List<ERMAttributeError>\n\n
    determineRequiredFieldsFromERM(final Collection<ERMAttribute> attributes, final int mboVectorIndex)\n
    '''
def findAllNullRequiredFields():
    '''returns List<ERMAttributeError>\n\n
    findAllNullRequiredFields(final Collection<ERMAttribute> attributes, final int mboIndex)\n
    '''
def getExistingMboSet():
    '''returns MboSetRemote\n\n
    getExistingMboSet(String relationship)\n
    '''
def addMboSetForRequiredCheck():
    '''returns None\n\n
    addMboSetForRequiredCheck(final MboSetRemote mboSet)\n
    '''
def getMboList():
    '''returns List<MboRemote>\n\n
    getMboList(final String mrp)\n
    '''
def setApplicationError():
    '''returns None\n\n
    setApplicationError(final String attribute, final ApplicationError appError)\n
    '''
def setApplicationRequired():
    '''returns None\n\n
    setApplicationRequired(final String attribute, final boolean required)\n
    '''
def isMasterTenant():
    '''returns boolean\n\n
    isMasterTenant(final String tableName)\n
    '''
def setReferencedMbo():
    '''returns None\n\n
    setReferencedMbo(final String token, final MboRemote refMbo)\n
    setReferencedMbo(final String token, final Mbo refMbo)\n
    '''
def getLanguageRecordRowStamp():
    '''returns long[]\n\n
    getLanguageRecordRowStamp()\n
    '''
def getUniqueLanguageIDRecord():
    '''returns long[]\n\n
    getUniqueLanguageIDRecord()\n
    '''
def isLocked():
    '''returns boolean\n\n
    isLocked()\n
    isLocked(final boolean cache)\n
    '''
def isLockedByMe():
    '''returns boolean\n\n
    isLockedByMe()\n
    '''
def isMboLockedByMe():
    '''returns boolean\n\n
    isMboLockedByMe()\n
    '''
def lock():
    '''returns None\n\n
    lock(final boolean lockNow)\n
    '''
def unlock():
    '''returns None\n\n
    unlock(final boolean unlockNow)\n
    '''
def setIgnoreRecordLockCheck():
    '''returns None\n\n
    setIgnoreRecordLockCheck(final boolean ignoreRecordLock)\n
    '''
def getIgnoreLockCheck():
    '''returns boolean\n\n
    getIgnoreLockCheck()\n
    '''
def isOptionGranted():
    '''returns boolean\n\n
    isOptionGranted(final String app, final String option)\n
    '''
def hasLockSaveRights():
    '''returns boolean\n\n
    hasLockSaveRights(final String app)\n
    '''
def isNoSql():
    '''returns boolean\n\n
    isNoSql()\n
    '''
def setNoSql():
    '''returns None\n\n
    setNoSql(final boolean noSql)\n
    '''
def resolveNoSqlWhere():
    '''returns boolean\n\n
    resolveNoSqlWhere()\n
    '''
def setResolveNoSqlWhere():
    '''returns None\n\n
    setResolveNoSqlWhere(final boolean resolveNoSqlWhere)\n
    '''
def getResourceName():
    '''returns String\n\n
    getResourceName()\n
    '''
def setResourceName():
    '''returns None\n\n
    setResourceName(final String resourceName)\n
    '''
def getESId():
    '''returns String\n\n
    getESId()\n
    '''
def setESId():
    '''returns None\n\n
    setESId(final String esId)\n
    '''
def setMboCtx():
    '''returns None\n\n
    setMboCtx(final String propName, final Object o)\n
    '''
def getMboCtx():
    '''returns Object\n\n
    getMboCtx(String propName)\n
    '''
def removeCtx():
    '''returns Object\n\n
    removeCtx(String propName)\n
    '''
def format():
    '''returns String\n\n
    format(final String objName)\n
    '''
def getFieldValue():
    '''returns String\n\n
    getFieldValue(final String attribute, final MboRemote mbo)\n
    getFieldValue(final String attribute, final MboRemote mbo, final boolean useLocale)\n
    getFieldValue(final String attribute, final MboRemote mbo, final boolean useLocale, final int i)\n
    '''
