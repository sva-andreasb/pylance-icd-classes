MULTILANGCOPY = "String  MultiLangCopy""
def Mbo():
'''public Mbo(final MboSet ms)
'''
pass
def setProxy():
'''public void setProxy(final Remote proxy)
'''
pass
def getProxy():
'''public Remote getProxy()
'''
pass
def getMboRecordData():
'''public MboRecordData getMboRecordData()
'''
pass
def setNewMbo():
'''public void setNewMbo(final boolean flag)
'''
pass
def getStringInBaseLanguage():
'''public String getStringInBaseLanguage(final String attributeName)
'''
pass
def getString():
'''public String getString(String attributeName, final String langCode)
public String getString(final String attributeName)
'''
pass
def getStringTransparent():
'''public String getStringTransparent(final String attributeName, final String langCode)
'''
pass
def setMLValue():
'''public void setMLValue(final String attributeName, final String langCode, final String value, final long accessModifier)
'''
pass
def getRelationshipNameToLangTable():
'''public String getRelationshipNameToLangTable(final String attributeName)
'''
pass
def getDatabaseValue():
'''public Object getDatabaseValue(final String attributeName)
'''
pass
def setFetchIndex():
'''public void setFetchIndex(final int index)
'''
pass
def getFetchIndex():
'''public int getFetchIndex()
'''
pass
def setModified():
'''public void setModified(final boolean modified)
'''
pass
def setModifiedForIntegrationOnly():
'''public void setModifiedForIntegrationOnly(final boolean modified)
'''
pass
def setDeleted():
'''public void setDeleted(final boolean deleted)
'''
pass
def getName():
'''public String getName()
'''
pass
def getRecordMboName():
'''public String getRecordMboName()
'''
pass
def getOwner():
'''public MboRemote getOwner()
'''
pass
def getThisMboSet():
'''public MboSetRemote getThisMboSet()
'''
pass
def getUserInfo():
'''public UserInfo getUserInfo()
'''
pass
def init():
'''public void init()
'''
pass
def hasUniqueID():
'''public boolean hasUniqueID()
'''
pass
def getUniqueIdentifer():
'''public String getUniqueIdentifer()
'''
pass
def getLockedByDisplayName():
'''public String getLockedByDisplayName()
'''
pass
def getLockedByUserID():
'''public String getLockedByUserID()
'''
pass
def initRelationship():
'''public void initRelationship(final String relationName, final MboSetRemote mboSet)
'''
pass
def setReadonlyWhenParentIsReadonly():
'''public void setReadonlyWhenParentIsReadonly(final String relationshipName, final MboSetRemote mboSet, final boolean flag)
'''
pass
def getClientLocale():
'''public Locale getClientLocale()
'''
pass
def getClientTimeZone():
'''public TimeZone getClientTimeZone()
'''
pass
def getMboValue():
'''public MboValue getMboValue(final String nameInput)
'''
pass
def moveFieldFlagsToMboValue():
'''public void moveFieldFlagsToMboValue(final MboValue mv)
'''
pass
def getInstanciatedMboValue():
'''public MboValue getInstanciatedMboValue(String name)
'''
pass
def getMboInitialValue():
'''public MaxType getMboInitialValue(final String name)
'''
pass
def getInstanciatedMboSet():
'''public MboSetRemote getInstanciatedMboSet(final String relationshipName)
'''
pass
def getMboValueData():
'''public MboValueData getMboValueData(final String attribute)
public MboValueData getMboValueData(final String attribute, final boolean ignoreFieldFlags)
public MboValueData[] getMboValueData(final String[] attribute)
'''
pass
def getMboValueDataForDownload():
'''public MboValueData[] getMboValueDataForDownload(final String[] attribute)
'''
pass
def getMboData():
'''public MboData getMboData(final String[] attributes)
'''
pass
def getMboValueInfoStatic():
'''public MboValueInfoStatic getMboValueInfoStatic(final String attribute)
public MboValueInfoStatic[] getMboValueInfoStatic(final String[] attribute)
'''
pass
def getMboForAttribute():
'''public MboRemote getMboForAttribute(final String attributeName)
'''
pass
def getMboForAttributeStatic():
'''public MboRemote getMboForAttributeStatic(final String attributeName)
'''
pass
def getList():
'''public MboSetRemote getList(final String attribute)
'''
pass
def smartFill():
'''public MboSetRemote smartFill(final String attribute, final String value, final boolean exact)
'''
pass
def smartFind():
'''public MboSetRemote smartFind(final String attribute, final String value, final boolean exact, final boolean isRecordHover)
public MboSetRemote smartFind(final String attribute, final String value, final boolean exact)
public MboSetRemote smartFind(final String appName, final String attribute, final String value, final boolean exact)
'''
pass
def smartFindByObjectName():
'''public MboSetRemote smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact, final String[][] cachedKeyMap)
public MboSetRemote smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact)
'''
pass
def smartFindByObjectNameDirect():
'''public MboSetRemote smartFindByObjectNameDirect(final String sourceObj, final String targetAttrName, final String value, final boolean exact)
'''
pass
def getBoolean():
'''public boolean getBoolean(final String attributeName)
'''
pass
def getByte():
'''public byte getByte(final String attributeName)
'''
pass
def getInt():
'''public int getInt(final String attributeName)
'''
pass
def getLong():
'''public long getLong(final String attributeName)
'''
pass
def getFloat():
'''public float getFloat(final String attributeName)
'''
pass
def getDouble():
'''public double getDouble(final String attributeName)
'''
pass
def getDate():
'''public Date getDate(final String attributeName)
'''
pass
def getBytes():
'''public byte[] getBytes(final String attributeName)
'''
pass
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
pass
def isNull():
'''public boolean isNull(final String attributeName)
'''
pass
def setValueNull():
'''public void setValueNull(final String attributeName)
public void setValueNull(final String attributeName, final long accessModifier)
'''
pass
def getKeyValue():
'''public KeyValue getKeyValue()
'''
pass
def getRecordIdentifer():
'''public String getRecordIdentifer()
'''
pass
def isAutoKeyed():
'''public boolean isAutoKeyed(final String attributeName)
'''
pass
def getMboSet():
'''public MboSetRemote getMboSet(String name, final String objectName)
public MboSetRemote getMboSet(final String name, final String objectName, final String relationship)
public MboSetRemote getMboSet(String name)
'''
pass
def getMboDataSet():
'''public Vector<MboRemote> getMboDataSet(final String relationship)
'''
pass
def isValid():
'''public boolean isValid()
'''
pass
def isZombie():
'''public boolean isZombie()
'''
pass
def setForDM():
'''public void setForDM(final boolean forDM)
'''
pass
def isForDM():
'''public boolean isForDM()
'''
pass
def setTenantIdForNoMboRecordData():
'''public void setTenantIdForNoMboRecordData(final int tenantId)
'''
pass
def getTenantIdForNoMboRecordData():
'''public int getTenantIdForNoMboRecordData()
'''
pass
def delete():
'''public void delete(final long accessModifier)
public void delete()
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def undelete():
'''public void undelete()
'''
pass
def toBeDeleted():
'''public boolean toBeDeleted()
'''
pass
def toBeAdded():
'''public boolean toBeAdded()
'''
pass
def isNew():
'''public boolean isNew()
'''
pass
def toBeUpdated():
'''public boolean toBeUpdated()
'''
pass
def thisToBeUpdated():
'''public boolean thisToBeUpdated()
'''
pass
def isModified():
'''public boolean isModified()
public boolean isModified(final String attribute)
'''
pass
def setESigFieldModified():
'''public void setESigFieldModified(final boolean eSigFieldModified)
'''
pass
def isESigFieldModified():
'''public boolean isESigFieldModified()
'''
pass
def setEAuditFieldModified():
'''public void setEAuditFieldModified(final boolean eAuditFieldModified)
'''
pass
def isEAuditFieldModified():
'''public boolean isEAuditFieldModified()
'''
pass
def toBeValidated():
'''public boolean toBeValidated()
'''
pass
def toBeSaved():
'''public boolean toBeSaved()
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def isApiBatchError():
'''public boolean isApiBatchError()
'''
pass
def validate():
'''public final void validate()
'''
pass
def checkQualifiedRestriction():
'''public void checkQualifiedRestriction()
'''
pass
def orEvaluateConditions():
'''public boolean orEvaluateConditions(final DataRestrictionCache.RestrictionBundle restrictions)
'''
pass
def useDataSecurity():
'''public boolean useDataSecurity(final String group)
'''
pass
def andEvaluateConditions():
'''public boolean andEvaluateConditions(final DataRestrictionCache.RestrictionBundle restrictions)
'''
pass
def validateAttributes():
'''public Hashtable<String, Exception> validateAttributes()
'''
pass
def getValidateOrder():
'''public String[] getValidateOrder()
'''
pass
def getInsertItemSetId():
'''public String getInsertItemSetId()
'''
pass
def getInsertCompanySetId():
'''public String getInsertCompanySetId()
'''
pass
def getInsertSite():
'''public String getInsertSite()
'''
pass
def getInsertOrgForSite():
'''public String getInsertOrgForSite(final String site)
'''
pass
def getInsertOrganization():
'''public String getInsertOrganization()
'''
pass
def getOrgSiteForMaxvar():
'''public String getOrgSiteForMaxvar(final String maxvarName)
'''
pass
def add():
'''public void add()
'''
pass
def modify():
'''public void modify()
'''
pass
def valueChanged():
'''public void valueChanged()
'''
pass
def getMboServer():
'''public MboServerInterface getMboServer()
'''
pass
def getMboSetInfo():
'''public MboSetInfo getMboSetInfo(final String mboName)
'''
pass
def getTranslator():
'''public Translate getTranslator()
'''
pass
def setFlags():
'''public void setFlags(final long flags)
'''
pass
def getFlags():
'''public long getFlags()
'''
pass
def setFlag():
'''public void setFlag(final long flag, final boolean state)
public void setFlag(final long flag, final boolean state, final MXException mxe)
'''
pass
def isFlagSet():
'''public boolean isFlagSet(final long flag)
'''
pass
def evaluateRestriction():
'''public boolean evaluateRestriction(final DataRestriction restriction)
'''
pass
def getAttrRestrictionFlag():
'''public BitFlag getAttrRestrictionFlag(final String attr)
'''
pass
def getRowRestrictionFlag():
'''public BitFlag getRowRestrictionFlag()
'''
pass
def getFieldExceptions():
'''public Hashtable<String, MXException> getFieldExceptions()
'''
pass
def setFieldFlags():
'''public void setFieldFlags(final String name, final long flags)
'''
pass
def setFieldFlag():
'''public void setFieldFlag(final String name, final long flag, final boolean state)
public void setFieldFlag(String name, final long flag, final boolean state, final MXException mxe)
public void setFieldFlag(final String[] names, final long flag, final boolean state)
public void setFieldFlag(final String[] names, final long flag, final boolean state, final MXException mxe)
public void setFieldFlag(final String[] names, final boolean inclusive, final long flag, final boolean state)
public void setFieldFlag(final String[] names, final boolean inclusive, final long flag, final boolean state, final MXException mxe)
'''
pass
def checkFieldAccess():
'''public void checkFieldAccess(final long accessModifier)
'''
pass
def hasFieldAccess():
'''public boolean hasFieldAccess(final long accessModifier)
'''
pass
def enableMethod():
'''public void enableMethod(final String methodName, final boolean state)
'''
pass
def checkMethodAccess():
'''public void checkMethodAccess(final String methodName, final long accessModifier)
public final void checkMethodAccess(final String methodName)
'''
pass
def getUserName():
'''public String getUserName()
'''
pass
def fireEvent():
'''public void fireEvent(final String type)
'''
pass
def getProfile():
'''public ProfileRemote getProfile()
'''
pass
def copy():
'''public MboRemote copy()
public MboRemote copy(final MboSetRemote mboset)
public MboRemote copy(final MboSetRemote mboset, final long mboAddFlags)
'''
pass
def copyFake():
'''public MboRemote copyFake(final MboSetRemote mboset)
'''
pass
def setAutokeyFields():
'''public void setAutokeyFields()
'''
pass
def blindCopy():
'''public MboRemote blindCopy(final MboSetRemote mboset)
'''
pass
def isSkipCopyField():
'''public boolean isSkipCopyField(final MboValueInfo mvi)
'''
pass
def setCopyDefaults():
'''public void setCopyDefaults()
'''
pass
def getMXTransaction():
'''public MXTransaction getMXTransaction()
'''
pass
def getRelatedWhere():
'''public String getRelatedWhere()
public String getRelatedWhere(final String alias)
'''
pass
def hasRelatedQbe():
'''public boolean hasRelatedQbe()
'''
pass
def getIntegrationService():
'''public ServiceRemote getIntegrationService()
'''
pass
def generateAutoKey():
'''public void generateAutoKey()
'''
pass
def getCheckpoint():
'''public boolean getCheckpoint()
'''
pass
def startCheckpoint():
'''public void startCheckpoint()
'''
pass
def rollbackToCheckpoint():
'''public void rollbackToCheckpoint()
'''
pass
def select():
'''public void select()
'''
pass
def unselect():
'''public void unselect()
'''
pass
def isSelected():
'''public boolean isSelected()
'''
pass
def copyValue():
'''public void copyValue(final MboRemote sourceMbo, final String attrSource, final String attrTarget, final long flags)
public void copyValue(final MboRemote sourceMbo, final String[] attrSource, final String[] attrTarget, final long flags)
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def setPropagateKeyFlag():
'''public void setPropagateKeyFlag(final boolean flag)
public void setPropagateKeyFlag(final String[] objectName, final boolean flag)
'''
pass
def excludeObjectForPropagate():
'''public boolean excludeObjectForPropagate(final String name)
'''
pass
def getPropagateKeyFlag():
'''public boolean getPropagateKeyFlag()
'''
pass
def propagateKeyValue():
'''public void propagateKeyValue(final String keyName, final String keyValue)
'''
pass
def setHierarchyLink():
'''public void setHierarchyLink(final boolean flag)
'''
pass
def hasHierarchyLink():
'''public boolean hasHierarchyLink()
'''
pass
def setDefaultValue():
'''public void setDefaultValue()
'''
pass
def setDefaultValues():
'''public void setDefaultValues()
'''
pass
def setAppDefaultValue():
'''public void setAppDefaultValue()
'''
pass
def isBasedOn():
'''public boolean isBasedOn(final String objectName)
'''
pass
def clear():
'''public void clear()
'''
pass
def getMboLogger():
'''public MXLogger getMboLogger()
'''
pass
def getSecurityLogger():
'''public MXLogger getSecurityLogger()
'''
pass
def getSqlLogger():
'''public MXLogger getSqlLogger()
'''
pass
def getOrgForGL():
'''public String getOrgForGL(final String lookupAttr)
'''
pass
def getSiteOrg():
'''public String[] getSiteOrg()
'''
pass
def setLangCodeDefault():
'''public final void setLangCodeDefault()
'''
pass
def getUniqueIDName():
'''public String getUniqueIDName()
'''
pass
def getUniqueIDValue():
'''public long getUniqueIDValue()
'''
pass
def setUniqueIDValue():
'''public void setUniqueIDValue()
'''
pass
def setValueFromSequence():
'''public void setValueFromSequence(final String attributeName)
'''
pass
def getDocLinksCount():
'''public int getDocLinksCount()
'''
pass
def getLinesRelationship():
'''public String getLinesRelationship()
'''
pass
def getMessage():
'''public String getMessage(final String errGrp, final String errKey)
public String getMessage(final String errGrp, final String errKey, final Object[] params)
public String getMessage(final String errGrp, final String errKey, final Object param)
public String getMessage(final MXException ex)
'''
pass
def getMaxMessage():
'''public MaxMessage getMaxMessage(final String errGrp, final String errKey)
'''
pass
def createComm():
'''public MboRemote createComm()
'''
pass
def getMatchingAttr():
'''public String getMatchingAttr(final String attribute)
public String getMatchingAttr(final String sourceObjectName, final String attribute)
'''
pass
def getStringInSpecificLocale():
'''public String getStringInSpecificLocale(final String attribute, final Locale l, final TimeZone tz)
'''
pass
def getMatchingAttrs():
'''public Object[] getMatchingAttrs(final String sourceName, final String targetAttr)
'''
pass
def sigOptionAccessAuthorized():
'''public void sigOptionAccessAuthorized(final String optionname)
'''
pass
def initFieldFlagsOnMbo():
'''public void initFieldFlagsOnMbo(final String attrName)
'''
pass
def needCallInitFieldFlag():
'''public boolean needCallInitFieldFlag(final String attrName)
'''
pass
def checkSiteOrgAccessForSave():
'''public void checkSiteOrgAccessForSave()
'''
pass
def sigopGranted():
'''public boolean sigopGranted(final String optionname)
public boolean sigopGranted(final String app, final String optionname)
public HashMap<String, Boolean> sigopGranted(final Set optionnames)
'''
pass
def evaluateCtrlConditions():
'''public HashMap<String, TreeMap<Integer, String[]>> evaluateCtrlConditions(final HashSet options)
public HashMap<String, TreeMap<Integer, String[]>> evaluateCtrlConditions(final HashSet options, final String app)
'''
pass
def getCondition():
'''public MaxCondition getCondition(final String conditionNum)
'''
pass
def evaluateCondition():
'''public boolean evaluateCondition(final String conditionNum, final boolean logErrorOnly)
public boolean evaluateCondition(final String conditionNum)
'''
pass
def getAlwaysFlags():
'''public BitFlag getAlwaysFlags(final String attr)
'''
pass
def getDomainIDs():
'''public String[] getDomainIDs(final String attr)
'''
pass
def addToDeleteForInsertList():
'''public void addToDeleteForInsertList(final String mboName)
'''
pass
def getDeleteForInsertList():
'''public Vector<String> getDeleteForInsertList()
'''
pass
def getInitialValue():
'''public MaxType getInitialValue(final String attributeName)
'''
pass
def getCommLogOwnerNameAndUniqueId():
'''public Object[] getCommLogOwnerNameAndUniqueId()
'''
pass
def isChangeByUserWhenSetFromLookup():
'''public boolean isChangeByUserWhenSetFromLookup(final String lookupAttrName, final String attributeName)
'''
pass
def validateKeyUniqueness():
'''public void validateKeyUniqueness()
'''
pass
def generateContentUID():
'''public void generateContentUID()
'''
pass
def getDomainFilterWhere():
'''public String getDomainFilterWhere(final String filterKeyword)
'''
pass
def removeRelatedSet():
'''public boolean removeRelatedSet(final MboSetRemote relatedSet)
'''
pass
def determineRequiredFieldsFromERM():
'''public List<ERMAttributeError> determineRequiredFieldsFromERM(final Collection<ERMAttribute> attributes, final int mboVectorIndex)
'''
pass
def findAllNullRequiredFields():
'''public List<ERMAttributeError> findAllNullRequiredFields(final Collection<ERMAttribute> attributes, final int mboIndex)
'''
pass
def getExistingMboSet():
'''public MboSetRemote getExistingMboSet(String relationship)
'''
pass
def addMboSetForRequiredCheck():
'''public void addMboSetForRequiredCheck(final MboSetRemote mboSet)
'''
pass
def getMboList():
'''public List<MboRemote> getMboList(final String mrp)
'''
pass
def setApplicationError():
'''public void setApplicationError(final String attribute, final ApplicationError appError)
'''
pass
def setApplicationRequired():
'''public void setApplicationRequired(final String attribute, final boolean required)
'''
pass
def getSynonymValueWhere():
'''public static String getSynonymValueWhere(final String filterKeyword)
'''
pass
def getRowStamp():
'''public final String getRowStamp()
'''
pass
def getRowStampObject():
'''public final Object getRowStampObject()
'''
pass
def getTenantId():
'''public final int getTenantId(final String tableName)
'''
pass
def isMasterTenant():
'''public boolean isMasterTenant(final String tableName)
'''
pass
def setReferencedMbo():
'''public void setReferencedMbo(final String token, final MboRemote refMbo)
public void setReferencedMbo(final String token, final Mbo refMbo)
'''
pass
def getLanguageRecordRowStamp():
'''public long[] getLanguageRecordRowStamp()
'''
pass
def getUniqueLanguageIDRecord():
'''public long[] getUniqueLanguageIDRecord()
'''
pass
def isLocked():
'''public boolean isLocked()
public boolean isLocked(final boolean cache)
'''
pass
def isLockedByMe():
'''public boolean isLockedByMe()
'''
pass
def isMboLockedByMe():
'''public boolean isMboLockedByMe()
'''
pass
def lock():
'''public void lock(final boolean lockNow)
'''
pass
def unlock():
'''public void unlock(final boolean unlockNow)
'''
pass
def setIgnoreRecordLockCheck():
'''public void setIgnoreRecordLockCheck(final boolean ignoreRecordLock)
'''
pass
def getIgnoreLockCheck():
'''public boolean getIgnoreLockCheck()
'''
pass
def isOptionGranted():
'''public boolean isOptionGranted(final String app, final String option)
'''
pass
def hasLockSaveRights():
'''public boolean hasLockSaveRights(final String app)
'''
pass
def isNoSql():
'''public boolean isNoSql()
'''
pass
def setNoSql():
'''public void setNoSql(final boolean noSql)
'''
pass
def resolveNoSqlWhere():
'''public boolean resolveNoSqlWhere()
'''
pass
def setResolveNoSqlWhere():
'''public void setResolveNoSqlWhere(final boolean resolveNoSqlWhere)
'''
pass
def getResourceName():
'''public String getResourceName()
'''
pass
def setResourceName():
'''public void setResourceName(final String resourceName)
'''
pass
def getESId():
'''public String getESId()
'''
pass
def setESId():
'''public void setESId(final String esId)
'''
pass
def setMboCtx():
'''public void setMboCtx(final String propName, final Object o)
'''
pass
def getMboCtx():
'''public Object getMboCtx(String propName)
'''
pass
def removeCtx():
'''public Object removeCtx(String propName)
'''
pass
def format():
'''public String format(final String objName)
'''
pass
def getFieldValue():
'''public String getFieldValue(final String attribute, final MboRemote mbo)
public String getFieldValue(final String attribute, final MboRemote mbo, final boolean useLocale)
public String getFieldValue(final String attribute, final MboRemote mbo, final boolean useLocale, final int i)
'''
pass
