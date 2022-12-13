def FauxMboSet():
    '''    public FauxMboSet(final MboRemote owner)
    '''
def findKey():
    '''    public MboRemote findKey(final Object keyObject)
    '''
def setApp():
    '''    public void setApp(final String appName)
    '''
def getApp():
    '''    public String getApp()
    '''
def getParentApp():
    '''    public String getParentApp()
    '''
def setWhere():
    '''    public void setWhere(final String whereClause)
    '''
def getWhere():
    '''    public String getWhere()
    '''
def setUserWhere():
    '''    public void setUserWhere(final String userWhere)
    '''
def getUserWhere():
    '''    public final String getUserWhere()
    public String getUserWhere(final String alias)
    '''
def getUserAndQbeWhere():
    '''    public String getUserAndQbeWhere()
    '''
def getQbeWhere():
    '''    public String getQbeWhere()
    '''
def useStoredQuery():
    '''    public void useStoredQuery(final String queryName)
    '''
def setOrderBy():
    '''    public void setOrderBy(final String orderByClause)
    '''
def setDefaultOrderBy():
    '''    public void setDefaultOrderBy()
    '''
def getOrderBy():
    '''    public String getOrderBy()
    '''
def setSQLOptions():
    '''    public void setSQLOptions(final String sqlOptions)
    '''
def getSQLOptions():
    '''    public String getSQLOptions()
    '''
def setFetchAttributes():
    '''    public void setFetchAttributes(final String[] attributes)
    '''
def getFetchAttributes():
    '''    public String[] getFetchAttributes()
    public String[] getFetchAttributes(final String rel)
    '''
def hasFetchAttributes():
    '''    public boolean hasFetchAttributes()
    '''
def moveNext():
    '''    public MboRemote moveNext()
    '''
def movePrev():
    '''    public MboRemote movePrev()
    '''
def moveFirst():
    '''    public MboRemote moveFirst()
    '''
def moveLast():
    '''    public MboRemote moveLast()
    '''
def moveTo():
    '''    public MboRemote moveTo(final int pos)
    '''
def add():
    '''    public final MboRemote add()
    public final MboRemote add(final long accessModifier)
    '''
def addAtEnd():
    '''    public final MboRemote addAtEnd()
    public final MboRemote addAtEnd(final long accessModifier)
    '''
def addFakeAtEnd():
    '''    public MboRemote addFakeAtEnd()
    '''
def addAtIndex():
    '''    public final MboRemote addAtIndex(final int index)
    public MboRemote addAtIndex(final long accessModifier, final int index)
    '''
def count():
    '''    public int count(final int countConstant)
    public int count()
    '''
def sum():
    '''    public double sum(final String attribute)
    '''
def min():
    '''    public double min(final String attribute)
    '''
def max():
    '''    public double max(final String attribute)
    '''
def latestDate():
    '''    public Date latestDate(final String attributeName)
    '''
def earliestDate():
    '''    public Date earliestDate(final String attributeName)
    '''
def isEmpty():
    '''    public boolean isEmpty()
    '''
def notExist():
    '''    public final boolean notExist()
    '''
def save():
    '''    public void save()
    public void save(final long flag)
    '''
def close():
    '''    public void close()
    '''
def reset():
    '''    public void reset()
    '''
def getCurrentPosition():
    '''    public int getCurrentPosition()
    '''
def toBeSaved():
    '''    public boolean toBeSaved()
    '''
def getMbo():
    '''    public MboRemote getMbo()
    public MboRemote getMbo(final int pos)
    '''
def getMboValueData():
    '''    public MboValueData getMboValueData(final String attribute)
    public MboValueData[] getMboValueData(final String[] attribute)
    public MboValueData[][] getMboValueData(final int rowStart, final int rowCount, final String[] attribute)
    '''
def getMboSetData():
    '''    public MboSetData getMboSetData(final String[] attributes)
    public MboSetData getMboSetData(final int row, final int count, final String[] attributes)
    '''
def resetQbe():
    '''    public void resetQbe()
    '''
def setQbe():
    '''    public void setQbe(final String attribute, final String expression)
    public void setQbe(final String attribute, final String[] expression)
    public void setQbe(final String[] attribute, final String expression)
    public void setQbe(final String[] attribute, final String[] expression)
    public void setQbe(final String attribute, final MboSetRemote lookup)
    '''
def setQbeOperatorOr():
    '''    public void setQbeOperatorOr()
    '''
def getQbe():
    '''    public String[][] getQbe()
    public String getQbe(final String attribute)
    public String[] getQbe(final String[] attribute)
    '''
def hasQbe():
    '''    public boolean hasQbe()
    '''
def setQbeExactMatch():
    '''    public void setQbeExactMatch(final boolean state)
    public void setQbeExactMatch(final String state)
    '''
def isQbeExactMatch():
    '''    public boolean isQbeExactMatch()
    '''
def ignoreQbeExactMatchSet():
    '''    public void ignoreQbeExactMatchSet(final boolean flag)
    '''
def isQbeCaseSensitive():
    '''    public boolean isQbeCaseSensitive()
    '''
def setQbeCaseSensitive():
    '''    public void setQbeCaseSensitive(final boolean state)
    public void setQbeCaseSensitive(final String state)
    '''
def getList():
    '''    public MboSetRemote getList(final String attributeName)
    public MboSetRemote getList(final int row, final String attributeName)
    '''
def init():
    '''    public void init(final UserInfo ui)
    '''
def getOwner():
    '''    public MboRemote getOwner()
    '''
def checkMethodAccess():
    '''    public void checkMethodAccess(final String methodName)
    '''
def validate():
    '''    public void validate()
    '''
def commit():
    '''    public void commit()
    '''
def rollback():
    '''    public void rollback()
    '''
def getClientLocale():
    '''    public Locale getClientLocale()
    '''
def getClientTimeZone():
    '''    public TimeZone getClientTimeZone()
    '''
def setOwner():
    '''    public void setOwner(final MboRemote mbo)
    '''
def deleteAll():
    '''    public void deleteAll()
    public void deleteAll(final long accessModifier)
    '''
def undeleteAll():
    '''    public void undeleteAll()
    '''
def setRelationship():
    '''    public void setRelationship(final String relationClause)
    '''
def getRelationship():
    '''    public String getRelationship()
    '''
def setMboSetInfo():
    '''    public void setMboSetInfo(final MboSetInfo ms)
    '''
def fetchNext():
    '''    public MboRemote fetchNext()
    '''
def isFlagSet():
    '''    public boolean isFlagSet(final long flag)
    '''
def getFlags():
    '''    public long getFlags()
    '''
def setFlags():
    '''    public void setFlags(final long flags)
    '''
def setFlag():
    '''    public void setFlag(final long flag, final boolean state)
    public void setFlag(final long flag, final boolean state, final MXException mxe)
    '''
def getUserName():
    '''    public String getUserName()
    '''
def copy():
    '''    public final void copy(final MboSetRemote mboset)
    public final void copy(final MboSetRemote sourceSet, final String[] srcAttributes, final String[] destAttributes)
    '''
def getMboSetInfo():
    '''    public MboSetInfo getMboSetInfo()
    '''
def setMXTransaction():
    '''    public void setMXTransaction(final MXTransaction txn)
    '''
def getMXTransaction():
    '''    public MXTransaction getMXTransaction()
    '''
def getCompleteWhere():
    '''    public String getCompleteWhere()
    '''
def getMboSetValueData():
    '''    public MboValueData[] getMboSetValueData(final String[] attribute)
    public MboValueData getMboSetValueData(final String attribute)
    '''
def remove():
    '''    public void remove()
    public void remove(final int pos)
    public void remove(final MboRemote mbo)
    '''
def deleteAndRemove():
    '''    public void deleteAndRemove()
    public void deleteAndRemove(final int pos)
    public void deleteAndRemove(final int pos, final long accessModifier)
    public void deleteAndRemove(final MboRemote mbo)
    public void deleteAndRemove(final MboRemote mbo, final long accessModifier)
    '''
def deleteAndRemoveAll():
    '''    public void deleteAndRemoveAll()
    public void deleteAndRemoveAll(final long accessModifier)
    '''
def getSize():
    '''    public int getSize()
    '''
def clear():
    '''    public void clear()
    '''
def incrementDeletedCount():
    '''    public void incrementDeletedCount(final boolean inc)
    '''
def getUserInfo():
    '''    public UserInfo getUserInfo()
    '''
def getZombie():
    '''    public MboRemote getZombie()
    '''
def cleanup():
    '''    public void cleanup()
    '''
def startCheckpoint():
    '''    public void startCheckpoint()
    public void startCheckpoint(final int i)
    '''
def rollbackToCheckpoint():
    '''    public void rollbackToCheckpoint()
    public void rollbackToCheckpoint(final int i)
    '''
def setOverrideOptimisticLock():
    '''    public void setOverrideOptimisticLock(final boolean val)
    '''
def select():
    '''    public void select(final int index)
    public void select(final Vector mboIndices)
    public void select(final int startIndex, final int count)
    '''
def unselect():
    '''    public void unselect(final int index)
    public void unselect(final Vector mboIndices)
    public void unselect(final int startIndex, final int count)
    '''
def getSelection():
    '''    public Vector getSelection()
    '''
def selectAll():
    '''    public void selectAll()
    '''
def unselectAll():
    '''    public void unselectAll()
    '''
def setWhereQbe():
    '''    public void setWhereQbe(final String attribute, final String value, final String where)
    '''
def resetWithSelection():
    '''    public void resetWithSelection()
    '''
def setAppWhere():
    '''    public void setAppWhere(final String appWhere)
    '''
def getAppWhere():
    '''    public String getAppWhere()
    '''
def setDefaultValue():
    '''    public void setDefaultValue(final String attribute, String value)
    public void setDefaultValue(final String attribute, final MboRemote mbo)
    '''
def getDefaultValue():
    '''    public String getDefaultValue(final String attribute)
    '''
def getDefaultValueHash():
    '''    public HashMap getDefaultValueHash()
    '''
def setDefaultValues():
    '''    public void setDefaultValues(final String[] attributes, final String[] values)
    public void setDefaultValues(final String attribute, String value)
    '''
def getJspDefaultValueHash():
    '''    public HashMap getJspDefaultValueHash()
    '''
def isESigNeeded():
    '''    public boolean isESigNeeded(final String optionName)
    '''
def verifyESig():
    '''    public boolean verifyESig(final String username, final String password, final String reason)
    '''
def logESigVerification():
    '''    public void logESigVerification(final String username, final String reason, final boolean authenticatedSuccessfully)
    '''
def getESigTransactionId():
    '''    public String getESigTransactionId()
    '''
def setLastESigTransId():
    '''    public void setLastESigTransId(final String id)
    '''
def setESigFieldModified():
    '''    public void setESigFieldModified(final boolean esigFieldModified)
    '''
def saveTransaction():
    '''    public void saveTransaction(final MXTransaction txn)
    '''
def commitTransaction():
    '''    public void commitTransaction(final MXTransaction txn)
    '''
def rollbackTransaction():
    '''    public void rollbackTransaction(final MXTransaction txn)
    '''
def undoTransaction():
    '''    public void undoTransaction(final MXTransaction txn)
    '''
def validateTransaction():
    '''    public boolean validateTransaction(final MXTransaction txn)
    '''
def fireEventsBeforeDB():
    '''    public void fireEventsBeforeDB(final MXTransaction txn)
    '''
def fireEventsAfterDB():
    '''    public void fireEventsAfterDB(final MXTransaction txn)
    '''
def fireEventsAfterDBCommit():
    '''    public void fireEventsAfterDBCommit(final MXTransaction txn)
    '''
def getString():
    '''    public String getString(final String attributeName)
    '''
def getBoolean():
    '''    public boolean getBoolean(final String attributeName)
    '''
def getByte():
    '''    public byte getByte(final String attributeName)
    '''
def getInt():
    '''    public int getInt(final String attributeName)
    '''
def getLong():
    '''    public long getLong(final String attributeName)
    '''
def getFloat():
    '''    public float getFloat(final String attributeName)
    '''
def getDouble():
    '''    public double getDouble(final String attributeName)
    '''
def getDate():
    '''    public Date getDate(final String attributeName)
    '''
def getBytes():
    '''    public byte[] getBytes(final String attributeName)
    '''
def isNull():
    '''    public boolean isNull(final String attributeName)
    '''
def setValueNull():
    '''    public void setValueNull(final String attributeName)
    public void setValueNull(final String attributeName, final long accessModifier)
    '''
def setValue():
    '''    public void setValue(final String attributeName, final String val)
    public void setValue(final String attributeName, final boolean val)
    public void setValue(final String attributeName, final byte val)
    public void setValue(final String attributeName, final short val)
    public void setValue(final String attributeName, final int val)
    public void setValue(final String attributeName, final long val)
    public void setValue(final String attributeName, final float val)
    public void setValue(final String attributeName, final double val)
    public void setValue(final String attributeName, final byte[] val)
    public void setValue(final String attributeName, final Date val)
    public void setValue(final String attributeName, final String val, final long accessModifier)
    public void setValue(final String attributeName, final boolean val, final long accessModifier)
    public void setValue(final String attributeName, final byte val, final long accessModifier)
    public void setValue(final String attributeName, final short val, final long accessModifier)
    public void setValue(final String attributeName, final int val, final long accessModifier)
    public void setValue(final String attributeName, final long val, final long accessModifier)
    public void setValue(final String attributeName, final float val, final long accessModifier)
    public void setValue(final String attributeName, final double val, final long accessModifier)
    public void setValue(final String attributeName, final byte[] val, final long accessModifier)
    public void setValue(final String attributeName, final Date val, final long accessModifier)
    '''
def isClosed():
    '''    public boolean isClosed()
    '''
def getSelectionWhere():
    '''    public String getSelectionWhere()
    '''
def addListener():
    '''    public void addListener(final MboSetListener l)
    '''
def removeListener():
    '''    public void removeListener(final MboSetListener l)
    '''
def reportModifiedMbo():
    '''    public void reportModifiedMbo(final MboRemote modifiedMbo)
    '''
def setTableDomainLookup():
    '''    public void setTableDomainLookup(final boolean flag)
    '''
def isBasedOn():
    '''    public boolean isBasedOn(final String objectName)
    '''
def getKeyAttributes():
    '''    public String[] getKeyAttributes()
    '''
def getProfile():
    '''    public ProfileRemote getProfile()
    '''
def setAutoKeyFlag():
    '''    public boolean setAutoKeyFlag(final boolean flag)
    '''
def getWarnings():
    '''    public MXException[] getWarnings()
    '''
def clearWarnings():
    '''    public void clearWarnings()
    '''
def hasWarnings():
    '''    public boolean hasWarnings()
    '''
def addWarning():
    '''    public void addWarning(final MXException e)
    '''
def addWarnings():
    '''    public void addWarnings(final MXException[] es)
    '''
def findByIntegrationKey():
    '''    public MboRemote findByIntegrationKey(final String[] integrationKeys, final String[] integrationKeyValues)
    '''
def setRelationName():
    '''    public void setRelationName(final String relationName)
    '''
def getRelationName():
    '''    public String getRelationName()
    '''
def smartFill():
    '''    public MboSetRemote smartFill(final String attributeName, final String value, final boolean exact)
    public MboSetRemote smartFill(final int row, final String attributeName, final String value, final boolean exact)
    '''
def smartFind():
    '''    public MboSetRemote smartFind(final String objectName, final String attributeName, final String value, final boolean exact)
    public MboSetRemote smartFind(final int row, final String objectName, final String attributeName, final String value, final boolean exact)
    public MboSetRemote smartFind(final String attributeName, final String value, final boolean exact)
    public MboSetRemote smartFind(final int row, final String attributeName, final String value, final boolean exact)
    '''
def getMLFromClause():
    '''    public StringBuffer getMLFromClause(final boolean useSchemaOwner)
    '''
def hasMLQbe():
    '''    public boolean hasMLQbe()
    '''
def getMboValueInfoStatic():
    '''    public MboValueInfoStatic getMboValueInfoStatic(final String attribute)
    public MboValueInfoStatic[] getMboValueInfoStatic(final String[] attribute)
    '''
def isFromGetList():
    '''    public boolean isFromGetList()
    '''
def setFromGetList():
    '''    public void setFromGetList(final boolean value)
    '''
def getMboForUniqueId():
    '''    public MboRemote getMboForUniqueId(final long id)
    '''
def getMessage():
    '''    public String getMessage(final String errGrp, final String errKey)
    public String getMessage(final String errGrp, final String errKey, final Object[] params)
    public String getMessage(final String errGrp, final String errKey, final Object param)
    public String getMessage(final MXException ex)
    '''
def getMaxMessage():
    '''    public MaxMessage getMaxMessage(final String errGrp, final String errKey)
    '''
def setQueryBySiteQbe():
    '''    public void setQueryBySiteQbe()
    '''
def setLogLargFetchResultDisabled():
    '''    public boolean setLogLargFetchResultDisabled(final boolean disable)
    '''
def addSubQbe():
    '''    public void addSubQbe(final String name, final String[] attrs, final String operator, final boolean exactMatch)
    public void addSubQbe(final String name, final String[] attrs, final String operator)
    public void addSubQbe(final String parentQbe, final String name, final String[] attrs, final String operator, final boolean exactMatch)
    public void addSubQbe(final String parentQbe, final String name, final String[] attrs, final String operator)
    '''
def setInsertSite():
    '''    public void setInsertSite(final String site)
    '''
def setInsertOrg():
    '''    public void setInsertOrg(final String org)
    '''
def setInsertCompanySet():
    '''    public void setInsertCompanySet(final String compSet)
    '''
def setInsertItemSet():
    '''    public void setInsertItemSet(final String itemSet)
    '''
def setExcludeMeFromPropagation():
    '''    public void setExcludeMeFromPropagation(final boolean flag)
    '''
def getExcludeMeFromPropagation():
    '''    public boolean getExcludeMeFromPropagation()
    '''
def processML():
    '''    public boolean processML()
    '''
def isIgnoreQbeExactMatchSet():
    '''    public boolean isIgnoreQbeExactMatchSet()
    '''
def setNoNeedtoFetchFromDB():
    '''    public void setNoNeedtoFetchFromDB(final boolean flag)
    '''
def setUserWhereAfterParse():
    '''    public void setUserWhereAfterParse(final String where)
    '''
def copyForDM():
    '''    public void copyForDM(final MboSetRemote mboset, final int begin, final int size)
    '''
def locateMbo():
    '''    public MboRemote locateMbo(final String[] keys, final String[] values, final int option)
    '''
def setDMDeploySet():
    '''    public void setDMDeploySet(final boolean flag)
    '''
def isDMDeploySet():
    '''    public boolean isDMDeploySet()
    '''
def setupLongOpPipe():
    '''    public InputStream setupLongOpPipe()
    '''
def clearLongOpPipe():
    '''    public void clearLongOpPipe()
    '''
def abortSql():
    '''    public void abortSql()
    '''
def getQueryTimeout():
    '''    public int getQueryTimeout()
    '''
def setQueryTimeout():
    '''    public void setQueryTimeout(final int queryTimeout)
    '''
def setAllowQualifiedRestriction():
    '''    public void setAllowQualifiedRestriction(final boolean value)
    '''
def setTxnPropertyMap():
    '''    public void setTxnPropertyMap(final Map<Object, Object> map)
    '''
def getTxnPropertyMap():
    '''    public Map<Object, Object> getTxnPropertyMap()
    '''
def isDMSkipFieldValidation():
    '''    public boolean isDMSkipFieldValidation()
    '''
def setDMSkipFieldValidation():
    '''    public void setDMSkipFieldValidation(final boolean flag)
    '''
def setAppAlwaysFieldFlag():
    '''    public void setAppAlwaysFieldFlag(final String attr, final long flag, final boolean state)
    '''
def getAppAlwaysFieldFlags():
    '''    public BitFlag getAppAlwaysFieldFlags(final String attr)
    '''
def findAllNullRequiredFields():
    '''    public List<ERMAttributeError> findAllNullRequiredFields()
    '''
def determineRequiredFieldsFromERM():
    '''    public List<ERMAttributeError> determineRequiredFieldsFromERM()
    '''
def setRequiedFlagsFromERM():
    '''    public void setRequiedFlagsFromERM()
    '''
def setERMEntity():
    '''    public void setERMEntity(final ERMEntity ermEntity)
    '''
def getERMEntity():
    '''    public ERMEntity getERMEntity()
    '''
def isRetainMboPosition():
    '''    public boolean isRetainMboPosition()
    '''
def setRetainMboPosition():
    '''    public void setRetainMboPosition(final boolean retainMboPosition)
    '''
def getMboSetRetainMboPositionData():
    '''    public MboSetRetainMboPositionData getMboSetRetainMboPositionData()
    '''
def getMboSetRetainMboPositionInfo():
    '''    public MboSetRetainMboPositionInfo getMboSetRetainMboPositionInfo()
    '''
def positionState():
    '''    public void positionState()
    '''
def setDBFetchMaxRows():
    '''    public void setDBFetchMaxRows(final int fetchLimit)
    '''
def getDBFetchMaxRows():
    '''    public int getDBFetchMaxRows()
    '''
def getSetOrderByForUI():
    '''    public String getSetOrderByForUI()
    '''
def setSetOrderByForUI():
    '''    public void setSetOrderByForUI(final String orderBy)
    '''
def newMboIndex():
    '''    public int newMboIndex()
    '''
def isDownloadSet():
    '''    public boolean isDownloadSet()
    '''
def setDownloadSet():
    '''    public void setDownloadSet(final boolean isDownloadSet)
    '''
