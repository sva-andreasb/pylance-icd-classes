MULTILANGCOPY = "String  \"MultiLangCopy\""
def Mbo():
    '''public Mbo(final MboSet ms)
    '''
def setProxy():
    '''public void setProxy(final Remote proxy)
    '''
def getProxy():
    '''public Remote getProxy()
    '''
def getMboRecordData():
    '''public MboRecordData getMboRecordData()
    '''
def setNewMbo():
    '''public void setNewMbo(final boolean flag)
    '''
def getStringInBaseLanguage():
    '''public String getStringInBaseLanguage(final String attributeName)
    '''
def getString():
    '''public String getString(String attributeName, final String langCode)
    public String getString(final String attributeName)
    '''
def getStringTransparent():
    '''public String getStringTransparent(final String attributeName, final String langCode)
    '''
def setMLValue():
    '''public void setMLValue(final String attributeName, final String langCode, final String value, final long accessModifier)
    '''
def getRelationshipNameToLangTable():
    '''public String getRelationshipNameToLangTable(final String attributeName)
    '''
def getDatabaseValue():
    '''public Object getDatabaseValue(final String attributeName)
    '''
def setFetchIndex():
    '''public void setFetchIndex(final int index)
    '''
def getFetchIndex():
    '''public int getFetchIndex()
    '''
def setModified():
    '''public void setModified(final boolean modified)
    '''
def setModifiedForIntegrationOnly():
    '''public void setModifiedForIntegrationOnly(final boolean modified)
    '''
def setDeleted():
    '''public void setDeleted(final boolean deleted)
    '''
def getName():
    '''public String getName()
    '''
def getRecordMboName():
    '''public String getRecordMboName()
    '''
def getOwner():
    '''public MboRemote getOwner()
    '''
def getThisMboSet():
    '''public MboSetRemote getThisMboSet()
    '''
def getUserInfo():
    '''public UserInfo getUserInfo()
    '''
def init():
    '''public void init()
    '''
def hasUniqueID():
    '''public boolean hasUniqueID()
    '''
def getUniqueIdentifer():
    '''public String getUniqueIdentifer()
    '''
def getLockedByDisplayName():
    '''public String getLockedByDisplayName()
    '''
def getLockedByUserID():
    '''public String getLockedByUserID()
    '''
def initRelationship():
    '''public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
def setReadonlyWhenParentIsReadonly():
    '''public void setReadonlyWhenParentIsReadonly(final String relationshipName, final MboSetRemote mboSet, final boolean flag)
    '''
def getClientLocale():
    '''public Locale getClientLocale()
    '''
def getClientTimeZone():
    '''public TimeZone getClientTimeZone()
    '''
def getMboValue():
    '''public MboValue getMboValue(final String nameInput)
    '''
def moveFieldFlagsToMboValue():
    '''public void moveFieldFlagsToMboValue(final MboValue mv)
    '''
def getInstanciatedMboValue():
    '''public MboValue getInstanciatedMboValue(String name)
    '''
def getMboInitialValue():
    '''public MaxType getMboInitialValue(final String name)
    '''
def getInstanciatedMboSet():
    '''public MboSetRemote getInstanciatedMboSet(final String relationshipName)
    '''
def getMboValueData():
    '''public MboValueData getMboValueData(final String attribute)
    public MboValueData getMboValueData(final String attribute, final boolean ignoreFieldFlags)
    public MboValueData[] getMboValueData(final String[] attribute)
    '''
def getMboValueDataForDownload():
    '''public MboValueData[] getMboValueDataForDownload(final String[] attribute)
    '''
def getMboData():
    '''public MboData getMboData(final String[] attributes)
    '''
def getMboValueInfoStatic():
    '''public MboValueInfoStatic getMboValueInfoStatic(final String attribute)
    public MboValueInfoStatic[] getMboValueInfoStatic(final String[] attribute)
    '''
def getMboForAttribute():
    '''public MboRemote getMboForAttribute(final String attributeName)
    '''
def getMboForAttributeStatic():
    '''public MboRemote getMboForAttributeStatic(final String attributeName)
    '''
def getList():
    '''public MboSetRemote getList(final String attribute)
    '''
def smartFill():
    '''public MboSetRemote smartFill(final String attribute, final String value, final boolean exact)
    '''
def smartFind():
    '''public MboSetRemote smartFind(final String attribute, final String value, final boolean exact, final boolean isRecordHover)
    public MboSetRemote smartFind(final String attribute, final String value, final boolean exact)
    public MboSetRemote smartFind(final String appName, final String attribute, final String value, final boolean exact)
    '''
def smartFindByObjectName():
    '''public MboSetRemote smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact, final String[][] cachedKeyMap)
    public MboSetRemote smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact)
    '''
def smartFindByObjectNameDirect():
    '''public MboSetRemote smartFindByObjectNameDirect(final String sourceObj, final String targetAttrName, final String value, final boolean exact)
    '''
def getBoolean():
    '''public boolean getBoolean(final String attributeName)
    '''
def getByte():
    '''public byte getByte(final String attributeName)
    '''
def getInt():
    '''public int getInt(final String attributeName)
    '''
def getLong():
    '''public long getLong(final String attributeName)
    '''
def getFloat():
    '''public float getFloat(final String attributeName)
    '''
def getDouble():
    '''public double getDouble(final String attributeName)
    '''
def getDate():
    '''public Date getDate(final String attributeName)
    '''
def getBytes():
    '''public byte[] getBytes(final String attributeName)
    '''
def setValue():
    '''public void setValue(final String attributeName, final String val, final long accessModifier)
    public void setValue(final String attributeName, final MaxType mboValue, final long accessModifier)
    public void setValue(final String attributeName, final String val)
    public void setValue(final String attributeName, final boolean val)
    public void setValue(final String attributeName, final boolean val, final long accessModifier)
    public void setValue(final String attributeName, final byte val)
    public void setValue(final String attributeName, final byte val, final long accessModifier)
    public void setValue(final String attributeName, final int val)
    public void setValue(final String attributeName, final int val, final long accessModifier)
    public void setValue(final String attributeName, final float val)
    public void setValue(final String attributeName, final float val, final long accessModifier)
    public void setValue(final String attributeName, final byte[] val)
    public void setValue(final String attributeName, final byte[] val, final long accessModifier)
    public void setValue(final String attributeName, final Date val)
    public void setValue(final String attributeName, final Date val, final long accessModifier)
    public void setValue(final String attributeName, final short val)
    public void setValue(final String attributeName, final short val, final long accessModifier)
    public void setValue(final String attributeName, final long val)
    public void setValue(final String attributeName, final long val, final long accessModifier)
    public void setValue(final String attributeName, final double val)
    public void setValue(final String attributeName, final double val, final long accessModifier)
    public void setValue(final String targetAttrName, final MboRemote sourceMbo)
    public void setValue(final String targetAttrName, final MboSetRemote sourceMboSet)
    '''
def isNull():
    '''public boolean isNull(final String attributeName)
    '''
def setValueNull():
    '''public void setValueNull(final String attributeName)
    public void setValueNull(final String attributeName, final long accessModifier)
    '''
def getKeyValue():
    '''public KeyValue getKeyValue()
    '''
def getRecordIdentifer():
    '''public String getRecordIdentifer()
    '''
def isAutoKeyed():
    '''public boolean isAutoKeyed(final String attributeName)
    '''
def getMboSet():
    '''public MboSetRemote getMboSet(String name, final String objectName)
    public MboSetRemote getMboSet(final String name, final String objectName, final String relationship)
    public MboSetRemote getMboSet(String name)
    '''
def getMboDataSet():
    '''public Vector<MboRemote> getMboDataSet(final String relationship)
    '''
def isValid():
    '''public boolean isValid()
    '''
def isZombie():
    '''public boolean isZombie()
    '''
def setForDM():
    '''public void setForDM(final boolean forDM)
    '''
def isForDM():
    '''public boolean isForDM()
    '''
def setTenantIdForNoMboRecordData():
    '''public void setTenantIdForNoMboRecordData(final int tenantId)
    '''
def getTenantIdForNoMboRecordData():
    '''public int getTenantIdForNoMboRecordData()
    '''
def delete():
    '''public void delete(final long accessModifier)
    public void delete()
    '''
def canDelete():
    '''public void canDelete()
    '''
def undelete():
    '''public void undelete()
    '''
def toBeDeleted():
    '''public boolean toBeDeleted()
    '''
def toBeAdded():
    '''public boolean toBeAdded()
    '''
def isNew():
    '''public boolean isNew()
    '''
def toBeUpdated():
    '''public boolean toBeUpdated()
    '''
def thisToBeUpdated():
    '''public boolean thisToBeUpdated()
    '''
def isModified():
    '''public boolean isModified()
    public boolean isModified(final String attribute)
    '''
def setESigFieldModified():
    '''public void setESigFieldModified(final boolean eSigFieldModified)
    '''
def isESigFieldModified():
    '''public boolean isESigFieldModified()
    '''
def setEAuditFieldModified():
    '''public void setEAuditFieldModified(final boolean eAuditFieldModified)
    '''
def isEAuditFieldModified():
    '''public boolean isEAuditFieldModified()
    '''
def toBeValidated():
    '''public boolean toBeValidated()
    '''
def toBeSaved():
    '''public boolean toBeSaved()
    '''
def appValidate():
    '''public void appValidate()
    '''
def isApiBatchError():
    '''public boolean isApiBatchError()
    '''
def validate():
    '''public final void validate()
    '''
def checkQualifiedRestriction():
    '''public void checkQualifiedRestriction()
    '''
def orEvaluateConditions():
    '''public boolean orEvaluateConditions(final DataRestrictionCache.RestrictionBundle restrictions)
    '''
def useDataSecurity():
    '''public boolean useDataSecurity(final String group)
    '''
def andEvaluateConditions():
    '''public boolean andEvaluateConditions(final DataRestrictionCache.RestrictionBundle restrictions)
    '''
def validateAttributes():
    '''public Hashtable<String, Exception> validateAttributes()
    '''
def getValidateOrder():
    '''public String[] getValidateOrder()
    '''
def getInsertItemSetId():
    '''public String getInsertItemSetId()
    '''
def getInsertCompanySetId():
    '''public String getInsertCompanySetId()
    '''
def getInsertSite():
    '''public String getInsertSite()
    '''
def getInsertOrgForSite():
    '''public String getInsertOrgForSite(final String site)
    '''
def getInsertOrganization():
    '''public String getInsertOrganization()
    '''
def getOrgSiteForMaxvar():
    '''public String getOrgSiteForMaxvar(final String maxvarName)
    '''
def add():
    '''public void add()
    '''
def modify():
    '''public void modify()
    '''
def valueChanged():
    '''public void valueChanged()
    '''
def getMboServer():
    '''public MboServerInterface getMboServer()
    '''
def getMboSetInfo():
    '''public MboSetInfo getMboSetInfo(final String mboName)
    '''
def getTranslator():
    '''public Translate getTranslator()
    '''
def setFlags():
    '''public void setFlags(final long flags)
    '''
def getFlags():
    '''public long getFlags()
    '''
def setFlag():
    '''public void setFlag(final long flag, final boolean state)
    public void setFlag(final long flag, final boolean state, final MXException mxe)
    '''
def isFlagSet():
    '''public boolean isFlagSet(final long flag)
    '''
def evaluateRestriction():
    '''public boolean evaluateRestriction(final DataRestriction restriction)
    '''
def getAttrRestrictionFlag():
    '''public BitFlag getAttrRestrictionFlag(final String attr)
    '''
def getRowRestrictionFlag():
    '''public BitFlag getRowRestrictionFlag()
    '''
def getFieldExceptions():
    '''public Hashtable<String, MXException> getFieldExceptions()
    '''
def setFieldFlags():
    '''public void setFieldFlags(final String name, final long flags)
    '''
def setFieldFlag():
    '''public void setFieldFlag(final String name, final long flag, final boolean state)
    public void setFieldFlag(String name, final long flag, final boolean state, final MXException mxe)
    public void setFieldFlag(final String[] names, final long flag, final boolean state)
    public void setFieldFlag(final String[] names, final long flag, final boolean state, final MXException mxe)
    public void setFieldFlag(final String[] names, final boolean inclusive, final long flag, final boolean state)
    public void setFieldFlag(final String[] names, final boolean inclusive, final long flag, final boolean state, final MXException mxe)
    '''
def checkFieldAccess():
    '''public void checkFieldAccess(final long accessModifier)
    '''
def hasFieldAccess():
    '''public boolean hasFieldAccess(final long accessModifier)
    '''
def enableMethod():
    '''public void enableMethod(final String methodName, final boolean state)
    '''
def checkMethodAccess():
    '''public void checkMethodAccess(final String methodName, final long accessModifier)
    public final void checkMethodAccess(final String methodName)
    '''
def getUserName():
    '''public String getUserName()
    '''
def fireEvent():
    '''public void fireEvent(final String type)
    '''
def getProfile():
    '''public ProfileRemote getProfile()
    '''
def copy():
    '''public MboRemote copy()
    public MboRemote copy(final MboSetRemote mboset)
    public MboRemote copy(final MboSetRemote mboset, final long mboAddFlags)
    '''
def copyFake():
    '''public MboRemote copyFake(final MboSetRemote mboset)
    '''
def setAutokeyFields():
    '''public void setAutokeyFields()
    '''
def blindCopy():
    '''public MboRemote blindCopy(final MboSetRemote mboset)
    '''
def isSkipCopyField():
    '''public boolean isSkipCopyField(final MboValueInfo mvi)
    '''
def setCopyDefaults():
    '''public void setCopyDefaults()
    '''
def getMXTransaction():
    '''public MXTransaction getMXTransaction()
    '''
def getRelatedWhere():
    '''public String getRelatedWhere()
    public String getRelatedWhere(final String alias)
    '''
def hasRelatedQbe():
    '''public boolean hasRelatedQbe()
    '''
def getIntegrationService():
    '''public ServiceRemote getIntegrationService()
    '''
def generateAutoKey():
    '''public void generateAutoKey()
    '''
def getCheckpoint():
    '''public boolean getCheckpoint()
    '''
def startCheckpoint():
    '''public void startCheckpoint()
    '''
def rollbackToCheckpoint():
    '''public void rollbackToCheckpoint()
    '''
def select():
    '''public void select()
    '''
def unselect():
    '''public void unselect()
    '''
def isSelected():
    '''public boolean isSelected()
    '''
def copyValue():
    '''public void copyValue(final MboRemote sourceMbo, final String attrSource, final String attrTarget, final long flags)
    public void copyValue(final MboRemote sourceMbo, final String[] attrSource, final String[] attrTarget, final long flags)
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def setPropagateKeyFlag():
    '''public void setPropagateKeyFlag(final boolean flag)
    public void setPropagateKeyFlag(final String[] objectName, final boolean flag)
    '''
def excludeObjectForPropagate():
    '''public boolean excludeObjectForPropagate(final String name)
    '''
def getPropagateKeyFlag():
    '''public boolean getPropagateKeyFlag()
    '''
def propagateKeyValue():
    '''public void propagateKeyValue(final String keyName, final String keyValue)
    '''
def setHierarchyLink():
    '''public void setHierarchyLink(final boolean flag)
    '''
def hasHierarchyLink():
    '''public boolean hasHierarchyLink()
    '''
def setDefaultValue():
    '''public void setDefaultValue()
    '''
def setDefaultValues():
    '''public void setDefaultValues()
    '''
def setAppDefaultValue():
    '''public void setAppDefaultValue()
    '''
def isBasedOn():
    '''public boolean isBasedOn(final String objectName)
    '''
def clear():
    '''public void clear()
    '''
def getMboLogger():
    '''public MXLogger getMboLogger()
    '''
def getSecurityLogger():
    '''public MXLogger getSecurityLogger()
    '''
def getSqlLogger():
    '''public MXLogger getSqlLogger()
    '''
def getOrgForGL():
    '''public String getOrgForGL(final String lookupAttr)
    '''
def getSiteOrg():
    '''public String[] getSiteOrg()
    '''
def setLangCodeDefault():
    '''public final void setLangCodeDefault()
    '''
def getUniqueIDName():
    '''public String getUniqueIDName()
    '''
def getUniqueIDValue():
    '''public long getUniqueIDValue()
    '''
def setUniqueIDValue():
    '''public void setUniqueIDValue()
    '''
def setValueFromSequence():
    '''public void setValueFromSequence(final String attributeName)
    '''
def getDocLinksCount():
    '''public int getDocLinksCount()
    '''
def getLinesRelationship():
    '''public String getLinesRelationship()
    '''
def getMessage():
    '''public String getMessage(final String errGrp, final String errKey)
    public String getMessage(final String errGrp, final String errKey, final Object[] params)
    public String getMessage(final String errGrp, final String errKey, final Object param)
    public String getMessage(final MXException ex)
    '''
def getMaxMessage():
    '''public MaxMessage getMaxMessage(final String errGrp, final String errKey)
    '''
def createComm():
    '''public MboRemote createComm()
    '''
def getMatchingAttr():
    '''public String getMatchingAttr(final String attribute)
    public String getMatchingAttr(final String sourceObjectName, final String attribute)
    '''
def getStringInSpecificLocale():
    '''public String getStringInSpecificLocale(final String attribute, final Locale l, final TimeZone tz)
    '''
def getMatchingAttrs():
    '''public Object[] getMatchingAttrs(final String sourceName, final String targetAttr)
    '''
def sigOptionAccessAuthorized():
    '''public void sigOptionAccessAuthorized(final String optionname)
    '''
def initFieldFlagsOnMbo():
    '''public void initFieldFlagsOnMbo(final String attrName)
    '''
def needCallInitFieldFlag():
    '''public boolean needCallInitFieldFlag(final String attrName)
    '''
def checkSiteOrgAccessForSave():
    '''public void checkSiteOrgAccessForSave()
    '''
def sigopGranted():
    '''public boolean sigopGranted(final String optionname)
    public boolean sigopGranted(final String app, final String optionname)
    public HashMap<String, Boolean> sigopGranted(final Set optionnames)
    '''
def evaluateCtrlConditions():
    '''public HashMap<String, TreeMap<Integer, String[]>> evaluateCtrlConditions(final HashSet options)
    public HashMap<String, TreeMap<Integer, String[]>> evaluateCtrlConditions(final HashSet options, final String app)
    '''
def getCondition():
    '''public MaxCondition getCondition(final String conditionNum)
    '''
def evaluateCondition():
    '''public boolean evaluateCondition(final String conditionNum, final boolean logErrorOnly)
    public boolean evaluateCondition(final String conditionNum)
    '''
def getAlwaysFlags():
    '''public BitFlag getAlwaysFlags(final String attr)
    '''
def getDomainIDs():
    '''public String[] getDomainIDs(final String attr)
    '''
def addToDeleteForInsertList():
    '''public void addToDeleteForInsertList(final String mboName)
    '''
def getDeleteForInsertList():
    '''public Vector<String> getDeleteForInsertList()
    '''
def getInitialValue():
    '''public MaxType getInitialValue(final String attributeName)
    '''
def getCommLogOwnerNameAndUniqueId():
    '''public Object[] getCommLogOwnerNameAndUniqueId()
    '''
def isChangeByUserWhenSetFromLookup():
    '''public boolean isChangeByUserWhenSetFromLookup(final String lookupAttrName, final String attributeName)
    '''
def validateKeyUniqueness():
    '''public void validateKeyUniqueness()
    '''
def generateContentUID():
    '''public void generateContentUID()
    '''
def getDomainFilterWhere():
    '''public String getDomainFilterWhere(final String filterKeyword)
    '''
def removeRelatedSet():
    '''public boolean removeRelatedSet(final MboSetRemote relatedSet)
    '''
def determineRequiredFieldsFromERM():
    '''public List<ERMAttributeError> determineRequiredFieldsFromERM(final Collection<ERMAttribute> attributes, final int mboVectorIndex)
    '''
def findAllNullRequiredFields():
    '''public List<ERMAttributeError> findAllNullRequiredFields(final Collection<ERMAttribute> attributes, final int mboIndex)
    '''
def getExistingMboSet():
    '''public MboSetRemote getExistingMboSet(String relationship)
    '''
def addMboSetForRequiredCheck():
    '''public void addMboSetForRequiredCheck(final MboSetRemote mboSet)
    '''
def getMboList():
    '''public List<MboRemote> getMboList(final String mrp)
    '''
def setApplicationError():
    '''public void setApplicationError(final String attribute, final ApplicationError appError)
    '''
def setApplicationRequired():
    '''public void setApplicationRequired(final String attribute, final boolean required)
    '''
def getSynonymValueWhere():
    '''public static String getSynonymValueWhere(final String filterKeyword)
    '''
def getRowStamp():
    '''public final String getRowStamp()
    '''
def getRowStampObject():
    '''public final Object getRowStampObject()
    '''
def getTenantId():
    '''public final int getTenantId(final String tableName)
    '''
def isMasterTenant():
    '''public boolean isMasterTenant(final String tableName)
    '''
def setReferencedMbo():
    '''public void setReferencedMbo(final String token, final MboRemote refMbo)
    public void setReferencedMbo(final String token, final Mbo refMbo)
    '''
def getLanguageRecordRowStamp():
    '''public long[] getLanguageRecordRowStamp()
    '''
def getUniqueLanguageIDRecord():
    '''public long[] getUniqueLanguageIDRecord()
    '''
def isLocked():
    '''public boolean isLocked()
    public boolean isLocked(final boolean cache)
    '''
def isLockedByMe():
    '''public boolean isLockedByMe()
    '''
def isMboLockedByMe():
    '''public boolean isMboLockedByMe()
    '''
def lock():
    '''public void lock(final boolean lockNow)
    '''
def unlock():
    '''public void unlock(final boolean unlockNow)
    '''
def setIgnoreRecordLockCheck():
    '''public void setIgnoreRecordLockCheck(final boolean ignoreRecordLock)
    '''
def getIgnoreLockCheck():
    '''public boolean getIgnoreLockCheck()
    '''
def isOptionGranted():
    '''public boolean isOptionGranted(final String app, final String option)
    '''
def hasLockSaveRights():
    '''public boolean hasLockSaveRights(final String app)
    '''
def isNoSql():
    '''public boolean isNoSql()
    '''
def setNoSql():
    '''public void setNoSql(final boolean noSql)
    '''
def resolveNoSqlWhere():
    '''public boolean resolveNoSqlWhere()
    '''
def setResolveNoSqlWhere():
    '''public void setResolveNoSqlWhere(final boolean resolveNoSqlWhere)
    '''
def getResourceName():
    '''public String getResourceName()
    '''
def setResourceName():
    '''public void setResourceName(final String resourceName)
    '''
def getESId():
    '''public String getESId()
    '''
def setESId():
    '''public void setESId(final String esId)
    '''
def setMboCtx():
    '''public void setMboCtx(final String propName, final Object o)
    '''
def getMboCtx():
    '''public Object getMboCtx(String propName)
    '''
def removeCtx():
    '''public Object removeCtx(String propName)
    '''
def format():
    '''public String format(final String objName)
    '''
def getFieldValue():
    '''public String getFieldValue(final String attribute, final MboRemote mbo)
    public String getFieldValue(final String attribute, final MboRemote mbo, final boolean useLocale)
    public String getFieldValue(final String attribute, final MboRemote mbo, final boolean useLocale, final int i)
    '''
