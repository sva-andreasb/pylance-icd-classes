def setNoNeedtoFetchFromDB():
'''public void setNoNeedtoFetchFromDB(final boolean flag)
'''
pass
def MboSet():
'''public MboSet(final MboServerInterface ms)
'''
pass
def init():
'''public final void init(final UserInfo user)
public void init()
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
def initDataDictionary():
'''public void initDataDictionary()
'''
pass
def setApp():
'''public void setApp(final String appName)
'''
pass
def getApp():
'''public String getApp()
'''
pass
def getParentApp():
'''public String getParentApp()
'''
pass
def getMboSetValueData():
'''public MboValueData getMboSetValueData(final String attribute)
public MboValueData[] getMboSetValueData(final String[] attribute)
'''
pass
def getZombie():
'''public synchronized MboRemote getZombie()
'''
pass
def getOwner():
'''public MboRemote getOwner()
'''
pass
def setOwner():
'''public void setOwner(final MboRemote mbo)
'''
pass
def getMboSetData():
'''public MboSetData getMboSetData(final String[] attributes)
public MboSetData getMboSetData(final int row, final int count, final String[] attributes)
'''
pass
def getMboValueData():
'''public MboValueData getMboValueData(final String attribute)
public MboValueData[] getMboValueData(final String[] attribute)
public MboValueData[][] getMboValueData(final int rowStart, final int rowCount, final String[] attribute)
'''
pass
def getMboValueInfoStatic():
'''public MboValueInfoStatic getMboValueInfoStatic(final String attribute)
public MboValueInfoStatic[] getMboValueInfoStatic(final String[] attribute)
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
def setWhere():
'''public void setWhere(final String whereClause)
'''
pass
def getWhere():
'''public String getWhere()
'''
pass
def setUserWhere():
'''public void setUserWhere(final String userWhere)
'''
pass
def setUserWhereAfterParse():
'''public void setUserWhereAfterParse(String where)
'''
pass
def getUserWhere():
'''public String getUserWhere()
public String getUserWhere(final String alias)
'''
pass
def getUserAndQbeWhere():
'''public String getUserAndQbeWhere()
'''
pass
def useStoredQuery():
'''public void useStoredQuery(final String queryName)
'''
pass
def splitOrderBy():
'''public static String[] splitOrderBy(final String query)
'''
pass
def setSQLOptions():
'''public void setSQLOptions(final String sqlOptions)
'''
pass
def getSQLOptions():
'''public String getSQLOptions()
'''
pass
def findKey():
'''public MboRemote findKey(final Object keyObject)
'''
pass
def setRelationship():
'''public void setRelationship(final String relationClause)
'''
pass
def getRelationship():
'''public String getRelationship()
'''
pass
def setOrderBy():
'''public void setOrderBy(final String orderByClause)
'''
pass
def setOrderByNVL():
'''public void setOrderByNVL(final Map<String, String[]> options)
'''
pass
def getOrderBy():
'''public String getOrderBy()
'''
pass
def setDefaultOrderBy():
'''public void setDefaultOrderBy()
'''
pass
def setPreserveOrderByCase():
'''public void setPreserveOrderByCase(final boolean value)
'''
pass
def moveToKey():
'''public MboRemote moveToKey(final KeyValue keyVal)
'''
pass
def moveNext():
'''public MboRemote moveNext()
'''
pass
def movePrev():
'''public MboRemote movePrev()
'''
pass
def moveFirst():
'''public MboRemote moveFirst()
'''
pass
def moveLast():
'''public MboRemote moveLast()
'''
pass
def moveTo():
'''public MboRemote moveTo(final int pos)
'''
pass
def getCurrentPosition():
'''public int getCurrentPosition()
'''
pass
def getMbo():
'''public MboRemote getMbo()
public MboRemote getMbo(final int index)
'''
pass
def getName():
'''public final String getName()
'''
pass
def newMboIndex():
'''public int newMboIndex()
'''
pass
def processML():
'''public boolean processML()
'''
pass
def getMLFromClause():
'''public StringBuffer getMLFromClause(final boolean useSchemaOwner)
'''
pass
def fetchNext():
'''public MboRemote fetchNext()
'''
pass
def forceDBSort():
'''public boolean forceDBSort(final String attrName)
'''
pass
def appendToWhere():
'''public String appendToWhere()
'''
pass
def getUserPrefWhere():
'''public String getUserPrefWhere()
'''
pass
def getSize():
'''public int getSize()
'''
pass
def count():
'''public int count()
public int count(final int countConstant)
'''
pass
def incrementDeletedCount():
'''public void incrementDeletedCount(final boolean inc)
'''
pass
def avg():
'''public double avg(final String attributeName)
'''
pass
def sum():
'''public double sum(final String attributeName)
'''
pass
def max():
'''public double max(final String attributeName)
'''
pass
def min():
'''public double min(final String attributeName)
'''
pass
def latestDate():
'''public Date latestDate(final String attributeName)
'''
pass
def earliestDate():
'''public Date earliestDate(final String attributeName)
'''
pass
def isEmpty():
'''public final boolean isEmpty()
'''
pass
def notExist():
'''public final boolean notExist()
'''
pass
def add():
'''public final MboRemote add()
public final MboRemote add(final long accessModifier)
'''
pass
def addAtEnd():
'''public final MboRemote addAtEnd()
public final MboRemote addAtEnd(final long accessModifier)
'''
pass
def addAtIndex():
'''public final MboRemote addAtIndex(final int ind)
public MboRemote addAtIndex(final long accessModifier, final int ind)
'''
pass
def canAdd():
'''public void canAdd()
'''
pass
def deleteAll():
'''public void deleteAll()
public void deleteAll(final long accessModifier)
'''
pass
def undeleteAll():
'''public void undeleteAll()
'''
pass
def addFakeAtEnd():
'''public final MboRemote addFakeAtEnd()
'''
pass
def clear():
'''public void clear()
'''
pass
def remove():
'''public void remove()
public void remove(final int pos)
public void remove(final MboRemote mbo)
'''
pass
def deleteAndRemove():
'''public void deleteAndRemove()
public void deleteAndRemove(final int pos)
public void deleteAndRemove(final int pos, final long accessModifier)
public void deleteAndRemove(final MboRemote mbo)
public void deleteAndRemove(final MboRemote mbo, final long accessModifier)
'''
pass
def deleteAndRemoveAll():
'''public void deleteAndRemoveAll()
public void deleteAndRemoveAll(final long accessModifier)
'''
pass
def toBeSaved():
'''public boolean toBeSaved()
'''
pass
def close():
'''public void close()
'''
pass
def cancelAndClose():
'''public void cancelAndClose()
'''
pass
def isClosed():
'''public boolean isClosed()
'''
pass
def reset():
'''public void reset()
'''
pass
def clearToBeSaved():
'''public void clearToBeSaved()
'''
pass
def resetForRefreshOnSave():
'''public void resetForRefreshOnSave()
'''
pass
def commit():
'''public void commit()
'''
pass
def rollback():
'''public void rollback()
'''
pass
def validate():
'''public void validate()
'''
pass
def getList():
'''public MboSetRemote getList(final String attributeName)
public MboSetRemote getList(final int row, final String attributeName)
'''
pass
def smartFill():
'''public MboSetRemote smartFill(final String attributeName, final String value, final boolean exact)
public MboSetRemote smartFill(final int row, final String attributeName, final String value, final boolean exact)
'''
pass
def smartFind():
'''public MboSetRemote smartFind(final String attributeName, final String value, final boolean exact)
public MboSetRemote smartFind(final String objectName, final String attributeName, final String value, final boolean exact)
public MboSetRemote smartFind(final int row, final String objectName, final String attributeName, final String value, final boolean exact)
public MboSetRemote smartFind(final int row, final String attributeName, final String value, final boolean exact)
'''
pass
def getString():
'''public String getString(final String attributeName)
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
def isNull():
'''public boolean isNull(final String attributeName)
'''
pass
def setValueNull():
'''public void setValueNull(final String attributeName)
public void setValueNull(final String attributeName, final long accessModifier)
'''
pass
def setValue():
'''public void setValue(final String attributeName, final String val)
public void setValue(final String attributeName, final String val, final long accessModifier)
public void setValue(final String attributeName, final boolean val)
public void setValue(final String attributeName, final boolean val, final long accessModifier)
public void setValue(final String attributeName, final byte val)
public void setValue(final String attributeName, final byte val, final long accessModifier)
public void setValue(final String attributeName, final short val)
public void setValue(final String attributeName, final short val, final long accessModifier)
public void setValue(final String attributeName, final int val)
public void setValue(final String attributeName, final int val, final long accessModifier)
public void setValue(final String attributeName, final long val)
public void setValue(final String attributeName, final long val, final long accessModifier)
public void setValue(final String attributeName, final float val)
public void setValue(final String attributeName, final float val, final long accessModifier)
public void setValue(final String attributeName, final double val)
public void setValue(final String attributeName, final double val, final long accessModifier)
public void setValue(final String attributeName, final byte[] val)
public void setValue(final String attributeName, final byte[] val, final long accessModifier)
public void setValue(final String attributeName, final Date val)
public void setValue(final String attributeName, final Date val, final long accessModifier)
public void setValue(final String attributeName, final MboSetRemote source)
public void setValue(final String attributeName, final MboRemote source)
'''
pass
def setMboSetInfo():
'''public void setMboSetInfo(final MboSetInfo ms)
'''
pass
def getMboSetInfo():
'''public MboSetInfo getMboSetInfo()
'''
pass
def getMboServer():
'''public MboServerInterface getMboServer()
'''
pass
def getUserInfo():
'''public UserInfo getUserInfo()
'''
pass
def resetQbe():
'''public void resetQbe()
'''
pass
def setQbeOperatorOr():
'''public void setQbeOperatorOr()
'''
pass
def setQbe():
'''public void setQbe(final String[] attribute, final String expression)
public void setQbe(final String attribute, final String[] expression)
public void setQbe(final String[] attribute, final String[] expression)
public void setQbe(final String attribute, String expression)
public void setQbe(final String attribute, final MboSetRemote lookup)
'''
pass
def setQbeExactMatch():
'''public void setQbeExactMatch(final String state)
public void setQbeExactMatch(final boolean state)
'''
pass
def isQbeExactMatch():
'''public boolean isQbeExactMatch()
'''
pass
def ignoreQbeExactMatchSet():
'''public void ignoreQbeExactMatchSet(final boolean flag)
'''
pass
def isIgnoreQbeExactMatchSet():
'''public boolean isIgnoreQbeExactMatchSet()
'''
pass
def isQbeCaseSensitive():
'''public boolean isQbeCaseSensitive()
'''
pass
def setQbeCaseSensitive():
'''public void setQbeCaseSensitive(final boolean state)
public void setQbeCaseSensitive(final String state)
'''
pass
def getQbe():
'''public String[] getQbe(final String[] attributes)
public String[][] getQbe()
public String getQbe(final String attribute)
'''
pass
def hasQbe():
'''public boolean hasQbe()
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
def applyRowSecurity():
'''public void applyRowSecurity()
'''
pass
def getAlwaysFlags():
'''public BitFlag getAlwaysFlags()
public BitFlag getAlwaysFlags(final String attr)
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
def getProfile():
'''public ProfileRemote getProfile()
'''
pass
def copy():
'''public final void copy(final MboSetRemote mboset)
public final void copy(final MboSetRemote mboset, final long mboAddFlags)
public final void copy(final MboSetRemote sourceSet, final String[] srcAttributes, final String[] destAttributes)
'''
pass
def copyForDM():
'''public void copyForDM(final MboSetRemote mboset, final int begin, final int size)
'''
pass
def getSharedMboSet():
'''public MboSetRemote getSharedMboSet(String objectName, final String relationship)
'''
pass
def getWarnings():
'''public MXException[] getWarnings()
'''
pass
def clearWarnings():
'''public void clearWarnings()
'''
pass
def hasWarnings():
'''public boolean hasWarnings()
'''
pass
def addWarning():
'''public void addWarning(final MXException e)
'''
pass
def addWarnings():
'''public void addWarnings(final MXException[] es)
'''
pass
def setMXTransaction():
'''public void setMXTransaction(final MXTransaction txn)
'''
pass
def getMXTransaction():
'''public MXTransaction getMXTransaction()
'''
pass
def save():
'''public void save()
public void save(final long flags)
public void save(final MXTransaction txn)
public void save(final MXTransaction txn, final long flags)
'''
pass
def saveTransaction():
'''public void saveTransaction(final MXTransaction txn)
'''
pass
def validateTransaction():
'''public boolean validateTransaction(final MXTransaction txn)
'''
pass
def saveMbos():
'''public void saveMbos()
'''
pass
def fireEventsBeforeDB():
'''public void fireEventsBeforeDB(final MXTransaction txn)
'''
pass
def fireEventsAfterDB():
'''public void fireEventsAfterDB(final MXTransaction txn)
'''
pass
def fireEventsAfterDBCommit():
'''public void fireEventsAfterDBCommit(final MXTransaction txn)
'''
pass
def commitTransaction():
'''public void commitTransaction(final MXTransaction txn)
'''
pass
def rollbackTransaction():
'''public void rollbackTransaction(final MXTransaction txn)
'''
pass
def undoTransaction():
'''public void undoTransaction(final MXTransaction txn)
'''
pass
def logRowUpdatedException():
'''public void logRowUpdatedException(final MXRowUpdateException mxr)
'''
pass
def getQbeWhere():
'''public String getQbeWhere()
'''
pass
def isLookup():
'''public boolean isLookup()
'''
pass
def getQualifiedWhere():
'''public String getQualifiedWhere()
'''
pass
def getMaxAppsWhere():
'''public String getMaxAppsWhere()
'''
pass
def setTableDomainLookup():
'''public void setTableDomainLookup(final boolean flag)
'''
pass
def isTableDomainLookup():
'''public boolean isTableDomainLookup()
'''
pass
def setDMDeploySet():
'''public void setDMDeploySet(final boolean flag)
'''
pass
def isDMDeploySet():
'''public boolean isDMDeploySet()
'''
pass
def isDMSkipFieldValidation():
'''public boolean isDMSkipFieldValidation()
'''
pass
def setDMSkipFieldValidation():
'''public void setDMSkipFieldValidation(final boolean flag)
'''
pass
def getCompleteWhere():
'''public String getCompleteWhere()
'''
pass
def setWhereQbe():
'''public void setWhereQbe(final String attribute, final String value, final String where)
'''
pass
def cleanup():
'''public void cleanup()
'''
pass
def startCheckpoint():
'''public void startCheckpoint()
public void startCheckpoint(final int i)
'''
pass
def rollbackToCheckpoint():
'''public void rollbackToCheckpoint()
public void rollbackToCheckpoint(final int i)
'''
pass
def select():
'''public void select(final int index)
public void select(final int startIndex, final int count)
public void select(final Vector mboIndices)
'''
pass
def getSelection():
'''public Vector<MboRemote> getSelection()
'''
pass
def unselect():
'''public void unselect(final int index)
public void unselect(final int startIndex, final int count)
public void unselect(final Vector mboIndices)
'''
pass
def selectAll():
'''public void selectAll()
'''
pass
def unselectAll():
'''public void unselectAll()
'''
pass
def resetWithSelection():
'''public void resetWithSelection()
'''
pass
def getSelectionWhere():
'''public String getSelectionWhere()
'''
pass
def getMultiSiteWhere():
'''public String getMultiSiteWhere()
'''
pass
def setAppWhere():
'''public void setAppWhere(final String appWhere)
'''
pass
def getAppWhere():
'''public String getAppWhere()
'''
pass
def setDefaultValue():
'''public void setDefaultValue(final String attribute, String value)
public void setDefaultValue(final String attribute, final MboRemote mbo)
'''
pass
def getDefaultValue():
'''public String getDefaultValue(final String attribute)
'''
pass
def getDefaultValueHash():
'''public HashMap<String, String> getDefaultValueHash()
'''
pass
def setDefaultValues():
'''public void setDefaultValues(final String[] attributes, final String[] values)
public void setDefaultValues(final String attribute, String value)
'''
pass
def getJspDefaultValueHash():
'''public HashMap<String, String> getJspDefaultValueHash()
'''
pass
def isESigNeeded():
'''public boolean isESigNeeded(final String optionName)
'''
pass
def isESigFieldModified():
'''public boolean isESigFieldModified()
'''
pass
def setESigFieldModified():
'''public void setESigFieldModified(final boolean eSigFieldModified)
'''
pass
def isEAuditFieldModified():
'''public boolean isEAuditFieldModified()
'''
pass
def setEAuditFieldModified():
'''public void setEAuditFieldModified(final boolean eAuditFieldModified)
'''
pass
def handleMLMbo():
'''public void handleMLMbo(final Mbo mbo, final MXTransaction txn, final String action)
public void handleMLMbo(final Mbo mbo, final String action)
'''
pass
def getESigTransactionId():
'''public String getESigTransactionId()
'''
pass
def clearESigTransIDForAdmin():
'''public void clearESigTransIDForAdmin()
'''
pass
def clearESigTransactionIdThread():
'''public static void clearESigTransactionIdThread()
'''
pass
def setLastESigTransId():
'''public void setLastESigTransId(final String id)
'''
pass
def verifyESig():
'''public boolean verifyESig(final String loginid, final String password, final String reason)
'''
pass
def logESigVerification():
'''public void logESigVerification(final String username, final String reason, final boolean authenticatedSuccessfully)
'''
pass
def isBasedOn():
'''public boolean isBasedOn(final String objectName)
'''
pass
def getKeyAttributes():
'''public String[] getKeyAttributes()
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
def setAutoKeyFlag():
'''public boolean setAutoKeyFlag(final boolean flag)
'''
pass
def ignoreAutokeyAttr():
'''public void ignoreAutokeyAttr(final String attrName, final boolean flag)
public void ignoreAutokeyAttr(final String[] attrNames, final boolean flag)
'''
pass
def getIgnoredAutokeyAttrs():
'''public HashSet getIgnoredAutokeyAttrs()
'''
pass
def clearIgnoredAutokeyAttrs():
'''public void clearIgnoredAutokeyAttrs()
'''
pass
def findByIntegrationKey():
'''public MboRemote findByIntegrationKey(final String[] integrationKeys, final String[] integrationKeyValues)
'''
pass
def setRelationName():
'''public void setRelationName(final String relationName)
'''
pass
def getRelationName():
'''public String getRelationName()
'''
pass
def hasMLQbe():
'''public boolean hasMLQbe()
'''
pass
def getMboForUniqueId():
'''public MboRemote getMboForUniqueId(final long id)
'''
pass
def getMessage():
'''public String getMessage(final String errGrp, final String errKey)
public String getMessage(final String errGrp, final String errKey, final Object[] params)
public String getMessage(final String errGrp, final String errKey, Object param)
public String getMessage(final MXException ex)
'''
pass
def getMaxMessage():
'''public MaxMessage getMaxMessage(final String errGrp, final String errKey)
'''
pass
def setQueryBySiteQbe():
'''public void setQueryBySiteQbe()
'''
pass
def setLogLargFetchResultDisabled():
'''public boolean setLogLargFetchResultDisabled(final boolean disable)
'''
pass
def addSubQbe():
'''public void addSubQbe(final String name, final String[] attrs, final String operator)
public void addSubQbe(final String name, final String[] attrs, final String operator, final boolean exactMatch)
public void addSubQbe(final String parentQbe, final String name, final String[] attrs, final String operator, final boolean exactMatch)
public void addSubQbe(final String parentQbe, final String name, final String[] attrs, final String operator)
'''
pass
def setInsertSite():
'''public void setInsertSite(final String site)
'''
pass
def setInsertOrg():
'''public void setInsertOrg(final String org)
'''
pass
def setInsertCompanySet():
'''public void setInsertCompanySet(final String compSet)
'''
pass
def setInsertItemSet():
'''public void setInsertItemSet(final String itemSet)
'''
pass
def setExcludeMeFromPropagation():
'''public void setExcludeMeFromPropagation(final boolean flag)
'''
pass
def getExcludeMeFromPropagation():
'''public boolean getExcludeMeFromPropagation()
'''
pass
def getInsertSite():
'''public String getInsertSite()
'''
pass
def getInsertOrg():
'''public String getInsertOrg()
'''
pass
def setAllowQualifiedRestriction():
'''public void setAllowQualifiedRestriction(final boolean value)
'''
pass
def getAllowQualifiedRestriction():
'''public boolean getAllowQualifiedRestriction()
'''
pass
def getInsertCompanySet():
'''public String getInsertCompanySet()
'''
pass
def getInsertItemSet():
'''public String getInsertItemSet()
'''
pass
def sort():
'''public void sort()
'''
pass
def clearTransactionReference():
'''public void clearTransactionReference()
'''
pass
def locateMbo():
'''public MboRemote locateMbo(final String[] keys, final String[] values, final int option)
'''
pass
def setupLongOpPipe():
'''public InputStream setupLongOpPipe()
'''
pass
def clearLongOpPipe():
'''public void clearLongOpPipe()
'''
pass
def abortSql():
'''public void abortSql()
'''
pass
def getQueryTimeout():
'''public int getQueryTimeout()
'''
pass
def setQueryTimeout():
'''public void setQueryTimeout(final int queryTimeout)
'''
pass
def addToEndOfSelectStatement():
'''public String addToEndOfSelectStatement(final boolean fetchLimitEanbled)
'''
pass
def setAppAlwaysFieldFlag():
'''public void setAppAlwaysFieldFlag(final String attr, final long flag, final boolean state)
'''
pass
def getAppAlwaysFieldFlags():
'''public BitFlag getAppAlwaysFieldFlags(final String attr)
'''
pass
def setTxnPropertyMap():
'''public void setTxnPropertyMap(final Map<Object, Object> map)
'''
pass
def getTxnPropertyMap():
'''public Map<Object, Object> getTxnPropertyMap()
'''
pass
def getQbeSiteAuthorization():
'''public String getQbeSiteAuthorization()
'''
pass
def findAllNullRequiredFields():
'''public List<ERMAttributeError> findAllNullRequiredFields()
'''
pass
def determineRequiredFieldsFromERM():
'''public List<ERMAttributeError> determineRequiredFieldsFromERM()
'''
pass
def setRequiedFlagsFromERM():
'''public void setRequiedFlagsFromERM()
'''
pass
def setERMEntity():
'''public void setERMEntity(final ERMEntity ermEntity)
'''
pass
def getERMEntity():
'''public ERMEntity getERMEntity()
'''
pass
def isRetainMboPosition():
'''public boolean isRetainMboPosition()
'''
pass
def setRetainMboPosition():
'''public void setRetainMboPosition(final boolean retainMboPosition)
'''
pass
def getMboSetRetainMboPositionInfo():
'''public MboSetRetainMboPositionInfo getMboSetRetainMboPositionInfo()
'''
pass
def getMboSetRetainMboPositionData():
'''public MboSetRetainMboPositionData getMboSetRetainMboPositionData()
'''
pass
def positionState():
'''public void positionState()
'''
pass
def setDBFetchMaxRows():
'''public void setDBFetchMaxRows(final int fetchLimit)
'''
pass
def getDBFetchMaxRows():
'''public int getDBFetchMaxRows()
'''
pass
def setSkipFirstNRows():
'''public void setSkipFirstNRows(final int skipRows)
'''
pass
def getSkipFirstNRows():
'''public int getSkipFirstNRows()
'''
pass
def getSetOrderByForUI():
'''public String getSetOrderByForUI()
'''
pass
def setSetOrderByForUI():
'''public void setSetOrderByForUI(final String orderBy)
'''
pass
def isDeltaStorage():
'''public boolean isDeltaStorage(final Mbo mbo, final String tableName)
'''
pass
def dump():
'''public static String dump(final Object object)
'''
pass
def setFederatedResources():
'''public void setFederatedResources(final String federatedResourcesStr)
'''
pass
def addFederatedMboToSorter():
'''public void addFederatedMboToSorter(final MboRemote mbo)
'''
pass
def executeBatch():
'''public void executeBatch()
'''
pass
def getPreparedStmt():
'''public PreparedStatement getPreparedStmt(final Connection con, final String sql)
'''
pass
def clearBatchedPreparedStmt():
'''public void clearBatchedPreparedStmt(final String sql)
'''
pass
def clearBatchedPreparedStmts():
'''public void clearBatchedPreparedStmts()
'''
pass
def isDownloadSet():
'''public boolean isDownloadSet()
'''
pass
def setDownloadSet():
'''public void setDownloadSet(final boolean isDownloadSet)
'''
pass
