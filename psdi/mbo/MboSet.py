def setNoNeedtoFetchFromDB():
    '''public void setNoNeedtoFetchFromDB(final boolean flag)
    '''
def MboSet():
    '''public MboSet(final MboServerInterface ms)
    '''
def init():
    '''public final void init(final UserInfo user)
    public void init()
    '''
def setProxy():
    '''public void setProxy(final Remote proxy)
    '''
def getProxy():
    '''public Remote getProxy()
    '''
def initDataDictionary():
    '''public void initDataDictionary()
    '''
def setApp():
    '''public void setApp(final String appName)
    '''
def getApp():
    '''public String getApp()
    '''
def getParentApp():
    '''public String getParentApp()
    '''
def getMboSetValueData():
    '''public MboValueData getMboSetValueData(final String attribute)
    public MboValueData[] getMboSetValueData(final String[] attribute)
    '''
def getZombie():
    '''public synchronized MboRemote getZombie()
    '''
def getOwner():
    '''public MboRemote getOwner()
    '''
def setOwner():
    '''public void setOwner(final MboRemote mbo)
    '''
def getMboSetData():
    '''public MboSetData getMboSetData(final String[] attributes)
    public MboSetData getMboSetData(final int row, final int count, final String[] attributes)
    '''
def getMboValueData():
    '''public MboValueData getMboValueData(final String attribute)
    public MboValueData[] getMboValueData(final String[] attribute)
    public MboValueData[][] getMboValueData(final int rowStart, final int rowCount, final String[] attribute)
    '''
def getMboValueInfoStatic():
    '''public MboValueInfoStatic getMboValueInfoStatic(final String attribute)
    public MboValueInfoStatic[] getMboValueInfoStatic(final String[] attribute)
    '''
def getClientLocale():
    '''public Locale getClientLocale()
    '''
def getClientTimeZone():
    '''public TimeZone getClientTimeZone()
    '''
def setWhere():
    '''public void setWhere(final String whereClause)
    '''
def getWhere():
    '''public String getWhere()
    '''
def setUserWhere():
    '''public void setUserWhere(final String userWhere)
    '''
def setUserWhereAfterParse():
    '''public void setUserWhereAfterParse(String where)
    '''
def getUserWhere():
    '''public String getUserWhere()
    public String getUserWhere(final String alias)
    '''
def getUserAndQbeWhere():
    '''public String getUserAndQbeWhere()
    '''
def useStoredQuery():
    '''public void useStoredQuery(final String queryName)
    '''
def splitOrderBy():
    '''public static String[] splitOrderBy(final String query)
    '''
def setSQLOptions():
    '''public void setSQLOptions(final String sqlOptions)
    '''
def getSQLOptions():
    '''public String getSQLOptions()
    '''
def findKey():
    '''public MboRemote findKey(final Object keyObject)
    '''
def setRelationship():
    '''public void setRelationship(final String relationClause)
    '''
def getRelationship():
    '''public String getRelationship()
    '''
def setOrderBy():
    '''public void setOrderBy(final String orderByClause)
    '''
def setOrderByNVL():
    '''public void setOrderByNVL(final Map<String, String[]> options)
    '''
def getOrderBy():
    '''public String getOrderBy()
    '''
def setDefaultOrderBy():
    '''public void setDefaultOrderBy()
    '''
def setPreserveOrderByCase():
    '''public void setPreserveOrderByCase(final boolean value)
    '''
def moveToKey():
    '''public MboRemote moveToKey(final KeyValue keyVal)
    '''
def moveNext():
    '''public MboRemote moveNext()
    '''
def movePrev():
    '''public MboRemote movePrev()
    '''
def moveFirst():
    '''public MboRemote moveFirst()
    '''
def moveLast():
    '''public MboRemote moveLast()
    '''
def moveTo():
    '''public MboRemote moveTo(final int pos)
    '''
def getCurrentPosition():
    '''public int getCurrentPosition()
    '''
def getMbo():
    '''public MboRemote getMbo()
    public MboRemote getMbo(final int index)
    '''
def getName():
    '''public final String getName()
    '''
def newMboIndex():
    '''public int newMboIndex()
    '''
def processML():
    '''public boolean processML()
    '''
def getMLFromClause():
    '''public StringBuffer getMLFromClause(final boolean useSchemaOwner)
    '''
def fetchNext():
    '''public MboRemote fetchNext()
    '''
def forceDBSort():
    '''public boolean forceDBSort(final String attrName)
    '''
def appendToWhere():
    '''public String appendToWhere()
    '''
def getUserPrefWhere():
    '''public String getUserPrefWhere()
    '''
def getSize():
    '''public int getSize()
    '''
def count():
    '''public int count()
    public int count(final int countConstant)
    '''
def incrementDeletedCount():
    '''public void incrementDeletedCount(final boolean inc)
    '''
def avg():
    '''public double avg(final String attributeName)
    '''
def sum():
    '''public double sum(final String attributeName)
    '''
def max():
    '''public double max(final String attributeName)
    '''
def min():
    '''public double min(final String attributeName)
    '''
def latestDate():
    '''public Date latestDate(final String attributeName)
    '''
def earliestDate():
    '''public Date earliestDate(final String attributeName)
    '''
def isEmpty():
    '''public final boolean isEmpty()
    '''
def notExist():
    '''public final boolean notExist()
    '''
def add():
    '''public final MboRemote add()
    public final MboRemote add(final long accessModifier)
    '''
def addAtEnd():
    '''public final MboRemote addAtEnd()
    public final MboRemote addAtEnd(final long accessModifier)
    '''
def addAtIndex():
    '''public final MboRemote addAtIndex(final int ind)
    public MboRemote addAtIndex(final long accessModifier, final int ind)
    '''
def canAdd():
    '''public void canAdd()
    '''
def deleteAll():
    '''public void deleteAll()
    public void deleteAll(final long accessModifier)
    '''
def undeleteAll():
    '''public void undeleteAll()
    '''
def addFakeAtEnd():
    '''public final MboRemote addFakeAtEnd()
    '''
def clear():
    '''public void clear()
    '''
def remove():
    '''public void remove()
    public void remove(final int pos)
    public void remove(final MboRemote mbo)
    '''
def deleteAndRemove():
    '''public void deleteAndRemove()
    public void deleteAndRemove(final int pos)
    public void deleteAndRemove(final int pos, final long accessModifier)
    public void deleteAndRemove(final MboRemote mbo)
    public void deleteAndRemove(final MboRemote mbo, final long accessModifier)
    '''
def deleteAndRemoveAll():
    '''public void deleteAndRemoveAll()
    public void deleteAndRemoveAll(final long accessModifier)
    '''
def toBeSaved():
    '''public boolean toBeSaved()
    '''
def close():
    '''public void close()
    '''
def cancelAndClose():
    '''public void cancelAndClose()
    '''
def isClosed():
    '''public boolean isClosed()
    '''
def reset():
    '''public void reset()
    '''
def clearToBeSaved():
    '''public void clearToBeSaved()
    '''
def resetForRefreshOnSave():
    '''public void resetForRefreshOnSave()
    '''
def commit():
    '''public void commit()
    '''
def rollback():
    '''public void rollback()
    '''
def validate():
    '''public void validate()
    '''
def getList():
    '''public MboSetRemote getList(final String attributeName)
    public MboSetRemote getList(final int row, final String attributeName)
    '''
def smartFill():
    '''public MboSetRemote smartFill(final String attributeName, final String value, final boolean exact)
    public MboSetRemote smartFill(final int row, final String attributeName, final String value, final boolean exact)
    '''
def smartFind():
    '''public MboSetRemote smartFind(final String attributeName, final String value, final boolean exact)
    public MboSetRemote smartFind(final String objectName, final String attributeName, final String value, final boolean exact)
    public MboSetRemote smartFind(final int row, final String objectName, final String attributeName, final String value, final boolean exact)
    public MboSetRemote smartFind(final int row, final String attributeName, final String value, final boolean exact)
    '''
def getString():
    '''public String getString(final String attributeName)
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
def isNull():
    '''public boolean isNull(final String attributeName)
    '''
def setValueNull():
    '''public void setValueNull(final String attributeName)
    public void setValueNull(final String attributeName, final long accessModifier)
    '''
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
def setMboSetInfo():
    '''public void setMboSetInfo(final MboSetInfo ms)
    '''
def getMboSetInfo():
    '''public MboSetInfo getMboSetInfo()
    '''
def getMboServer():
    '''public MboServerInterface getMboServer()
    '''
def getUserInfo():
    '''public UserInfo getUserInfo()
    '''
def resetQbe():
    '''public void resetQbe()
    '''
def setQbeOperatorOr():
    '''public void setQbeOperatorOr()
    '''
def setQbe():
    '''public void setQbe(final String[] attribute, final String expression)
    public void setQbe(final String attribute, final String[] expression)
    public void setQbe(final String[] attribute, final String[] expression)
    public void setQbe(final String attribute, String expression)
    public void setQbe(final String attribute, final MboSetRemote lookup)
    '''
def setQbeExactMatch():
    '''public void setQbeExactMatch(final String state)
    public void setQbeExactMatch(final boolean state)
    '''
def isQbeExactMatch():
    '''public boolean isQbeExactMatch()
    '''
def ignoreQbeExactMatchSet():
    '''public void ignoreQbeExactMatchSet(final boolean flag)
    '''
def isIgnoreQbeExactMatchSet():
    '''public boolean isIgnoreQbeExactMatchSet()
    '''
def isQbeCaseSensitive():
    '''public boolean isQbeCaseSensitive()
    '''
def setQbeCaseSensitive():
    '''public void setQbeCaseSensitive(final boolean state)
    public void setQbeCaseSensitive(final String state)
    '''
def getQbe():
    '''public String[] getQbe(final String[] attributes)
    public String[][] getQbe()
    public String getQbe(final String attribute)
    '''
def hasQbe():
    '''public boolean hasQbe()
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
def applyRowSecurity():
    '''public void applyRowSecurity()
    '''
def getAlwaysFlags():
    '''public BitFlag getAlwaysFlags()
    public BitFlag getAlwaysFlags(final String attr)
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
def getProfile():
    '''public ProfileRemote getProfile()
    '''
def copy():
    '''public final void copy(final MboSetRemote mboset)
    public final void copy(final MboSetRemote mboset, final long mboAddFlags)
    public final void copy(final MboSetRemote sourceSet, final String[] srcAttributes, final String[] destAttributes)
    '''
def copyForDM():
    '''public void copyForDM(final MboSetRemote mboset, final int begin, final int size)
    '''
def getSharedMboSet():
    '''public MboSetRemote getSharedMboSet(String objectName, final String relationship)
    '''
def getWarnings():
    '''public MXException[] getWarnings()
    '''
def clearWarnings():
    '''public void clearWarnings()
    '''
def hasWarnings():
    '''public boolean hasWarnings()
    '''
def addWarning():
    '''public void addWarning(final MXException e)
    '''
def addWarnings():
    '''public void addWarnings(final MXException[] es)
    '''
def setMXTransaction():
    '''public void setMXTransaction(final MXTransaction txn)
    '''
def getMXTransaction():
    '''public MXTransaction getMXTransaction()
    '''
def save():
    '''public void save()
    public void save(final long flags)
    public void save(final MXTransaction txn)
    public void save(final MXTransaction txn, final long flags)
    '''
def saveTransaction():
    '''public void saveTransaction(final MXTransaction txn)
    '''
def validateTransaction():
    '''public boolean validateTransaction(final MXTransaction txn)
    '''
def saveMbos():
    '''public void saveMbos()
    '''
def fireEventsBeforeDB():
    '''public void fireEventsBeforeDB(final MXTransaction txn)
    '''
def fireEventsAfterDB():
    '''public void fireEventsAfterDB(final MXTransaction txn)
    '''
def fireEventsAfterDBCommit():
    '''public void fireEventsAfterDBCommit(final MXTransaction txn)
    '''
def commitTransaction():
    '''public void commitTransaction(final MXTransaction txn)
    '''
def rollbackTransaction():
    '''public void rollbackTransaction(final MXTransaction txn)
    '''
def undoTransaction():
    '''public void undoTransaction(final MXTransaction txn)
    '''
def logRowUpdatedException():
    '''public void logRowUpdatedException(final MXRowUpdateException mxr)
    '''
def getQbeWhere():
    '''public String getQbeWhere()
    '''
def isLookup():
    '''public boolean isLookup()
    '''
def getQualifiedWhere():
    '''public String getQualifiedWhere()
    '''
def getMaxAppsWhere():
    '''public String getMaxAppsWhere()
    '''
def setTableDomainLookup():
    '''public void setTableDomainLookup(final boolean flag)
    '''
def isTableDomainLookup():
    '''public boolean isTableDomainLookup()
    '''
def setDMDeploySet():
    '''public void setDMDeploySet(final boolean flag)
    '''
def isDMDeploySet():
    '''public boolean isDMDeploySet()
    '''
def isDMSkipFieldValidation():
    '''public boolean isDMSkipFieldValidation()
    '''
def setDMSkipFieldValidation():
    '''public void setDMSkipFieldValidation(final boolean flag)
    '''
def getCompleteWhere():
    '''public String getCompleteWhere()
    '''
def setWhereQbe():
    '''public void setWhereQbe(final String attribute, final String value, final String where)
    '''
def cleanup():
    '''public void cleanup()
    '''
def startCheckpoint():
    '''public void startCheckpoint()
    public void startCheckpoint(final int i)
    '''
def rollbackToCheckpoint():
    '''public void rollbackToCheckpoint()
    public void rollbackToCheckpoint(final int i)
    '''
def select():
    '''public void select(final int index)
    public void select(final int startIndex, final int count)
    public void select(final Vector mboIndices)
    '''
def getSelection():
    '''public Vector<MboRemote> getSelection()
    '''
def unselect():
    '''public void unselect(final int index)
    public void unselect(final int startIndex, final int count)
    public void unselect(final Vector mboIndices)
    '''
def selectAll():
    '''public void selectAll()
    '''
def unselectAll():
    '''public void unselectAll()
    '''
def resetWithSelection():
    '''public void resetWithSelection()
    '''
def getSelectionWhere():
    '''public String getSelectionWhere()
    '''
def getMultiSiteWhere():
    '''public String getMultiSiteWhere()
    '''
def setAppWhere():
    '''public void setAppWhere(final String appWhere)
    '''
def getAppWhere():
    '''public String getAppWhere()
    '''
def setDefaultValue():
    '''public void setDefaultValue(final String attribute, String value)
    public void setDefaultValue(final String attribute, final MboRemote mbo)
    '''
def getDefaultValue():
    '''public String getDefaultValue(final String attribute)
    '''
def getDefaultValueHash():
    '''public HashMap<String, String> getDefaultValueHash()
    '''
def setDefaultValues():
    '''public void setDefaultValues(final String[] attributes, final String[] values)
    public void setDefaultValues(final String attribute, String value)
    '''
def getJspDefaultValueHash():
    '''public HashMap<String, String> getJspDefaultValueHash()
    '''
def isESigNeeded():
    '''public boolean isESigNeeded(final String optionName)
    '''
def isESigFieldModified():
    '''public boolean isESigFieldModified()
    '''
def setESigFieldModified():
    '''public void setESigFieldModified(final boolean eSigFieldModified)
    '''
def isEAuditFieldModified():
    '''public boolean isEAuditFieldModified()
    '''
def setEAuditFieldModified():
    '''public void setEAuditFieldModified(final boolean eAuditFieldModified)
    '''
def handleMLMbo():
    '''public void handleMLMbo(final Mbo mbo, final MXTransaction txn, final String action)
    public void handleMLMbo(final Mbo mbo, final String action)
    '''
def getESigTransactionId():
    '''public String getESigTransactionId()
    '''
def clearESigTransIDForAdmin():
    '''public void clearESigTransIDForAdmin()
    '''
def clearESigTransactionIdThread():
    '''public static void clearESigTransactionIdThread()
    '''
def setLastESigTransId():
    '''public void setLastESigTransId(final String id)
    '''
def verifyESig():
    '''public boolean verifyESig(final String loginid, final String password, final String reason)
    '''
def logESigVerification():
    '''public void logESigVerification(final String username, final String reason, final boolean authenticatedSuccessfully)
    '''
def isBasedOn():
    '''public boolean isBasedOn(final String objectName)
    '''
def getKeyAttributes():
    '''public String[] getKeyAttributes()
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
def setAutoKeyFlag():
    '''public boolean setAutoKeyFlag(final boolean flag)
    '''
def ignoreAutokeyAttr():
    '''public void ignoreAutokeyAttr(final String attrName, final boolean flag)
    public void ignoreAutokeyAttr(final String[] attrNames, final boolean flag)
    '''
def getIgnoredAutokeyAttrs():
    '''public HashSet getIgnoredAutokeyAttrs()
    '''
def clearIgnoredAutokeyAttrs():
    '''public void clearIgnoredAutokeyAttrs()
    '''
def findByIntegrationKey():
    '''public MboRemote findByIntegrationKey(final String[] integrationKeys, final String[] integrationKeyValues)
    '''
def setRelationName():
    '''public void setRelationName(final String relationName)
    '''
def getRelationName():
    '''public String getRelationName()
    '''
def hasMLQbe():
    '''public boolean hasMLQbe()
    '''
def getMboForUniqueId():
    '''public MboRemote getMboForUniqueId(final long id)
    '''
def getMessage():
    '''public String getMessage(final String errGrp, final String errKey)
    public String getMessage(final String errGrp, final String errKey, final Object[] params)
    public String getMessage(final String errGrp, final String errKey, Object param)
    public String getMessage(final MXException ex)
    '''
def getMaxMessage():
    '''public MaxMessage getMaxMessage(final String errGrp, final String errKey)
    '''
def setQueryBySiteQbe():
    '''public void setQueryBySiteQbe()
    '''
def setLogLargFetchResultDisabled():
    '''public boolean setLogLargFetchResultDisabled(final boolean disable)
    '''
def addSubQbe():
    '''public void addSubQbe(final String name, final String[] attrs, final String operator)
    public void addSubQbe(final String name, final String[] attrs, final String operator, final boolean exactMatch)
    public void addSubQbe(final String parentQbe, final String name, final String[] attrs, final String operator, final boolean exactMatch)
    public void addSubQbe(final String parentQbe, final String name, final String[] attrs, final String operator)
    '''
def setInsertSite():
    '''public void setInsertSite(final String site)
    '''
def setInsertOrg():
    '''public void setInsertOrg(final String org)
    '''
def setInsertCompanySet():
    '''public void setInsertCompanySet(final String compSet)
    '''
def setInsertItemSet():
    '''public void setInsertItemSet(final String itemSet)
    '''
def setExcludeMeFromPropagation():
    '''public void setExcludeMeFromPropagation(final boolean flag)
    '''
def getExcludeMeFromPropagation():
    '''public boolean getExcludeMeFromPropagation()
    '''
def getInsertSite():
    '''public String getInsertSite()
    '''
def getInsertOrg():
    '''public String getInsertOrg()
    '''
def setAllowQualifiedRestriction():
    '''public void setAllowQualifiedRestriction(final boolean value)
    '''
def getAllowQualifiedRestriction():
    '''public boolean getAllowQualifiedRestriction()
    '''
def getInsertCompanySet():
    '''public String getInsertCompanySet()
    '''
def getInsertItemSet():
    '''public String getInsertItemSet()
    '''
def sort():
    '''public void sort()
    '''
def clearTransactionReference():
    '''public void clearTransactionReference()
    '''
def locateMbo():
    '''public MboRemote locateMbo(final String[] keys, final String[] values, final int option)
    '''
def setupLongOpPipe():
    '''public InputStream setupLongOpPipe()
    '''
def clearLongOpPipe():
    '''public void clearLongOpPipe()
    '''
def abortSql():
    '''public void abortSql()
    '''
def getQueryTimeout():
    '''public int getQueryTimeout()
    '''
def setQueryTimeout():
    '''public void setQueryTimeout(final int queryTimeout)
    '''
def addToEndOfSelectStatement():
    '''public String addToEndOfSelectStatement(final boolean fetchLimitEanbled)
    '''
def setAppAlwaysFieldFlag():
    '''public void setAppAlwaysFieldFlag(final String attr, final long flag, final boolean state)
    '''
def getAppAlwaysFieldFlags():
    '''public BitFlag getAppAlwaysFieldFlags(final String attr)
    '''
def setTxnPropertyMap():
    '''public void setTxnPropertyMap(final Map<Object, Object> map)
    '''
def getTxnPropertyMap():
    '''public Map<Object, Object> getTxnPropertyMap()
    '''
def getQbeSiteAuthorization():
    '''public String getQbeSiteAuthorization()
    '''
def findAllNullRequiredFields():
    '''public List<ERMAttributeError> findAllNullRequiredFields()
    '''
def determineRequiredFieldsFromERM():
    '''public List<ERMAttributeError> determineRequiredFieldsFromERM()
    '''
def setRequiedFlagsFromERM():
    '''public void setRequiedFlagsFromERM()
    '''
def setERMEntity():
    '''public void setERMEntity(final ERMEntity ermEntity)
    '''
def getERMEntity():
    '''public ERMEntity getERMEntity()
    '''
def isRetainMboPosition():
    '''public boolean isRetainMboPosition()
    '''
def setRetainMboPosition():
    '''public void setRetainMboPosition(final boolean retainMboPosition)
    '''
def getMboSetRetainMboPositionInfo():
    '''public MboSetRetainMboPositionInfo getMboSetRetainMboPositionInfo()
    '''
def getMboSetRetainMboPositionData():
    '''public MboSetRetainMboPositionData getMboSetRetainMboPositionData()
    '''
def positionState():
    '''public void positionState()
    '''
def setDBFetchMaxRows():
    '''public void setDBFetchMaxRows(final int fetchLimit)
    '''
def getDBFetchMaxRows():
    '''public int getDBFetchMaxRows()
    '''
def setSkipFirstNRows():
    '''public void setSkipFirstNRows(final int skipRows)
    '''
def getSkipFirstNRows():
    '''public int getSkipFirstNRows()
    '''
def getSetOrderByForUI():
    '''public String getSetOrderByForUI()
    '''
def setSetOrderByForUI():
    '''public void setSetOrderByForUI(final String orderBy)
    '''
def isDeltaStorage():
    '''public boolean isDeltaStorage(final Mbo mbo, final String tableName)
    '''
def dump():
    '''public static String dump(final Object object)
    '''
def setFederatedResources():
    '''public void setFederatedResources(final String federatedResourcesStr)
    '''
def addFederatedMboToSorter():
    '''public void addFederatedMboToSorter(final MboRemote mbo)
    '''
def executeBatch():
    '''public void executeBatch()
    '''
def getPreparedStmt():
    '''public PreparedStatement getPreparedStmt(final Connection con, final String sql)
    '''
def clearBatchedPreparedStmt():
    '''public void clearBatchedPreparedStmt(final String sql)
    '''
def clearBatchedPreparedStmts():
    '''public void clearBatchedPreparedStmts()
    '''
def isDownloadSet():
    '''public boolean isDownloadSet()
    '''
def setDownloadSet():
    '''public void setDownloadSet(final boolean isDownloadSet)
    '''
