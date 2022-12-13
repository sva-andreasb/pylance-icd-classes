ATTR_READONLY = "int  2"
ATTR_REQUIRED = "int  4"
ATTR_DEFAULT = "int  8"
ATTR_QBE = "int  16"
ATTR_COLUMN = "int  32"
ATTR_RESET = "int  64"
ATTR_REFRESH_TABLE = "int  128"
TABLE_EXPANDED = "int  1"
TABLE_AT_FIRST_PAGE = "int  2"
TABLE_AT_LAST_PAGE = "int  4"
TABLE_AT_FIRST_ROW = "int  8"
TABLE_AT_LAST_ROW = "int  16"
TABLE_FILTER_EXPANDED = "int  32"
TABLE_DETAILS_EXPANDED = "int  64"
TABLE_ROW_CHANGED = "int  128"
TABLE_FILTERED = "int  256"
TABLE_REFRESH_FILTER = "int  512"
TABLE_REFRESH_ROW = "int  1024"
TABLE_REFRESH_ALL_ROWS = "int  2048"
TABLE_ALL_SELECTED = "int  4096"
TABLE_START_EMPTY = "int  8192"
TABLE_USE_SUBSELECT = "int  16384"
TABLE_SUBSELECT_ON = "int  32768"
TABLE_REFRESH_TITLE = "int  65536"
MAX_TABLEROWS = "int  500"
ALL_BOOKMARKS = "String  \"ALL_BOOKMARKS\""
ALL_RECORDS = "String  \"ALL_RECORDS\""
def DataBean():
    '''public DataBean()
    '''
def setupBean():
    '''public void setupBean(final WebClientSession wcs)
    public void setupBean(final SessionContext sc)
    '''
def bindComponent():
    '''public void bindComponent(final BoundComponentInstance boundComponent)
    '''
def unbindComponent():
    '''public void unbindComponent(final BoundComponentInstance boundComponent)
    '''
def setNewRowUnedited():
    '''public void setNewRowUnedited(final boolean unedited)
    '''
def isNewRowUnedited():
    '''public boolean isNewRowUnedited()
    '''
def getTableAttributes():
    '''public String[] getTableAttributes()
    '''
def setAppDefault():
    '''public synchronized void setAppDefault(final String attribute, final String value)
    '''
def setQbeDefaults():
    '''public synchronized void setQbeDefaults()
    '''
def setAppDefaults():
    '''public synchronized void setAppDefaults()
    '''
def setParent():
    '''public void setParent(final DataBean parent, final String parentRelationship)
    '''
def getParent():
    '''public DataBean getParent()
    '''
def addListener():
    '''public void addListener(final DataBeanListener listener)
    '''
def removeListener():
    '''public void removeListener(final DataBeanListener listener)
    '''
def fireDataChangedEvent():
    '''public void fireDataChangedEvent(final DataBean speaker)
    public void fireDataChangedEvent()
    '''
def fireStructureChangedEvent():
    '''public void fireStructureChangedEvent(final DataBean speaker)
    public void fireStructureChangedEvent()
    '''
def sendRefreshTable():
    '''public void sendRefreshTable()
    '''
def listenerChangedEvent():
    '''public void listenerChangedEvent(final DataBean speaker)
    '''
def dataChangedEvent():
    '''public void dataChangedEvent(final DataBean speaker)
    '''
def structureChangedEvent():
    '''public void structureChangedEvent(final DataBean speaker)
    '''
def fireChildChangedEvent():
    '''public void fireChildChangedEvent()
    '''
def setMboName():
    '''public void setMboName(final String sMboName)
    '''
def getMboName():
    '''public String getMboName()
    '''
def getMXSession():
    '''public MXSession getMXSession()
    '''
def setDefaultOrderBy():
    '''public void setDefaultOrderBy(final String sOrderByClause)
    '''
def getDefaultOrderBy():
    '''public String getDefaultOrderBy()
    '''
def setOrderBy():
    '''public synchronized void setOrderBy(String sOrderByClause)
    '''
def getOrderBy():
    '''public String getOrderBy()
    '''
def setAppWhere():
    '''public synchronized void setAppWhere(final String sWhereClause)
    '''
def getAppWhere():
    '''public synchronized String getAppWhere()
    '''
def hasMboSetRemote():
    '''public boolean hasMboSetRemote()
    '''
def getMboSet():
    '''public MboSetRemote getMboSet()
    '''
def setApp():
    '''public void setApp(final String appName)
    '''
def getKeyAttribute():
    '''public String getKeyAttribute()
    '''
def getKeyAttributes():
    '''public String[] getKeyAttributes()
    '''
def getAttributes():
    '''public String[] getAttributes()
    '''
def isAttribute():
    '''public boolean isAttribute(final String attribute)
    '''
def isTableAttribute():
    '''public boolean isTableAttribute(final String attribute)
    '''
def addAttribute():
    '''public void addAttribute(final String attribute, BitFlag flags)
    '''
def addQbeAttribute():
    '''public void addQbeAttribute(final String attribute)
    '''
def setAttributes():
    '''public void setAttributes(final String[] attributelist, final BitFlag[] flags)
    '''
def count():
    '''public synchronized int count()
    '''
def setUserWhere():
    '''public synchronized void setUserWhere(final String whereClause)
    '''
def getUserWhere():
    '''public synchronized String getUserWhere()
    '''
def getUserAndQbeWhere():
    '''public synchronized String getUserAndQbeWhere()
    '''
def useStoredQuery():
    '''public synchronized void useStoredQuery(final String queryName)
    '''
def getQbe():
    '''public synchronized String getQbe(final String attribute)
    public synchronized String getQbe()
    '''
def saveCurrentQbeSettings():
    '''public synchronized void saveCurrentQbeSettings(final boolean forceOverride)
    '''
def clearSavedQbeSettings():
    '''public synchronized void clearSavedQbeSettings()
    '''
def restoreSavedQbeSettings():
    '''public synchronized void restoreSavedQbeSettings()
    '''
def clearSavedFilterSettings():
    '''public void clearSavedFilterSettings()
    '''
def setQbe():
    '''public synchronized void setQbe(final String attribute, final String expression)
    public synchronized void setQbe(final String attribute, final MboSetRemote expression)
    public synchronized void setQbe(final String[] attributes, final String expression)
    public synchronized void setQbe(final Hashtable<String, String> qbeAttrs)
    public synchronized void setQbe(final String expression)
    '''
def setDefaultQbe():
    '''public void setDefaultQbe(final String attribute, final String expression)
    '''
def getQbeAttributes():
    '''public synchronized Hashtable<String, String> getQbeAttributes()
    '''
def setQbeAttributes():
    '''public synchronized void setQbeAttributes(final Hashtable<String, String> newQbeAttributes)
    '''
def setQbeExactMatch():
    '''public synchronized void setQbeExactMatch(final boolean exact)
    '''
def setQbeCaseSensitive():
    '''public synchronized void setQbeCaseSensitive(final boolean caseSensitive)
    '''
def resetQbe():
    '''public synchronized void resetQbe()
    '''
def getBoolean():
    '''public synchronized boolean getBoolean(final String col)
    public synchronized boolean getBoolean(final int row, final String col)
    '''
def getString():
    '''public synchronized String getString(final String attribute)
    public synchronized String getString(final int row, final String attribute)
    '''
def getColumnString():
    '''public synchronized String getColumnString(final int row, final String col)
    '''
def getColumnDate():
    '''public synchronized Date getColumnDate(final int row, final String col)
    '''
def getDate():
    '''public synchronized Date getDate(final String attribute)
    '''
def getTitle():
    '''public synchronized String getTitle(final String attribute)
    '''
def getZombie():
    '''public MboRemote getZombie()
    '''
def getMboOrZombie():
    '''public MboRemote getMboOrZombie()
    '''
def getMboValueInfo():
    '''public synchronized MboValueInfoStatic getMboValueInfo(final String attribute)
    '''
def getZombieMboValueData():
    '''public synchronized MboValueData getZombieMboValueData(final String attribute)
    '''
def getMboValueData():
    '''public synchronized MboValueData getMboValueData(final int nRow, final String attribute)
    public synchronized MboValueData getMboValueData(final String attribute)
    '''
def isAttributeHidden():
    '''public boolean isAttributeHidden(final String attribute)
    public boolean isAttributeHidden(final int row, final String attribute)
    '''
def isMboHidden():
    '''public boolean isMboHidden()
    public boolean isMboHidden(final int row)
    '''
def getRemoteForLookup():
    '''public MboSetRemote getRemoteForLookup()
    '''
def getList():
    '''public synchronized MboSetRemote getList(final String attribute)
    public synchronized MboSetRemote getList(final Integer row, final String attribute)
    public synchronized MboSetRemote getList(final int nRow, final String attribute)
    '''
def getDataList():
    '''public synchronized String[][] getDataList(final String dataAttribute)
    public synchronized String[][] getDataList(final int row, final String dataAttribute)
    public synchronized String[][] getDataList(final int row, final String dataAttribute, final String keyAttributeName, final String displayAttribute)
    public synchronized String[][] getDataList(final int row, final String dataAttribute, final String displayAttribute)
    '''
def getDataListFromMboSetRemote():
    '''public synchronized String[][] getDataListFromMboSetRemote(final MboSetRemote setRemote, String dataAttribute, String displayAttribute)
    '''
def validate():
    '''public void validate()
    '''
def validateMbo():
    '''public void validateMbo()
    '''
def validateChildren():
    '''public void validateChildren()
    '''
def checkAndDistributeRequiredError():
    '''public MXException checkAndDistributeRequiredError(final MXException mxe)
    '''
def handleRequiredFieldException():
    '''public void handleRequiredFieldException(MXRequiredFieldException requiredFieldException, final WebClientEvent event)
    '''
def save():
    '''public synchronized void save()
    public synchronized void save(final MboRemote mbo)
    '''
def checkForAppError():
    '''public void checkForAppError()
    '''
def reset():
    '''public synchronized void reset()
    '''
def canCloseBean():
    '''public boolean canCloseBean()
    '''
def hasSameMboSet():
    '''public boolean hasSameMboSet(final DataBean bean)
    '''
def addDialogReference():
    '''public void addDialogReference()
    '''
def removeDialogReference():
    '''public void removeDialogReference()
    '''
def close():
    '''public void close()
    '''
def setCurrentRow():
    '''public synchronized boolean setCurrentRow(final int nRow)
    '''
def getCurrentRow():
    '''public int getCurrentRow()
    '''
def next():
    '''public synchronized boolean next()
    '''
def previous():
    '''public synchronized boolean previous()
    '''
def insert():
    '''public synchronized void insert(final int nRow)
    public synchronized void insert()
    '''
def insertAtEnd():
    '''public synchronized void insertAtEnd()
    '''
def delete():
    '''public synchronized void delete()
    public synchronized void delete(final int nRow)
    '''
def deleteAndRemove():
    '''public synchronized void deleteAndRemove()
    public synchronized void deleteAndRemove(final int nRow)
    '''
def undelete():
    '''public synchronized void undelete()
    public synchronized void undelete(final int nRow)
    '''
def setDefaultValue():
    '''public synchronized void setDefaultValue(final String attribute, final MboRemote value)
    public synchronized void setDefaultValue(final String attribute, final String value)
    '''
def setUserDefaults():
    '''public synchronized void setUserDefaults()
    '''
def getDefaultValue():
    '''public synchronized String getDefaultValue(final String attribute)
    '''
def setValue():
    '''public synchronized void setValue(final String attribute, final String value)
    public synchronized void setValue(final int nRow, final String attribute, final String value)
    public synchronized void setValue(final String attribute, final String value, final long accessModifier)
    public synchronized void setValue(final int nRow, final String attribute, final String value, final long accessModifier)
    public synchronized void setValue(final String attribute, final MboRemote mboRemote)
    public synchronized void setValue(final int row, final String attribute, final MboRemote mboRemote)
    public synchronized void setValue(final String attribute, final MboSetRemote mboSetRemote)
    '''
def setDate():
    '''public synchronized void setDate(final String controlId, final String attribute, final Date value)
    public synchronized void setDate(final String componentId, final Date value)
    public synchronized void setDate(final BoundComponentInstance boundComponent, final Date value)
    '''
def returnLookupValue():
    '''public synchronized int returnLookupValue(final String lookupValue)
    public synchronized int returnLookupValue(final String componentId, final MboRemote lookupMbo)
    public synchronized int returnLookupValue(final MboRemote lookupMbo)
    public synchronized int returnLookupValue(final MboSetRemote lookupMboSet)
    '''
def getMbo():
    '''public synchronized MboRemote getMbo()
    public synchronized MboRemote getMbo(final int row)
    '''
def duplicateMbo():
    '''public synchronized boolean duplicateMbo()
    '''
def getDataAsArray():
    '''public String[][] getDataAsArray()
    public String[][] getDataAsArray(final String[] attributeNames)
    '''
def getSelectedDataAsArray():
    '''public String[][] getSelectedDataAsArray()
    public String[][] getSelectedDataAsArray(final String[] attributeNames)
    '''
def propagateRequired():
    '''public void propagateRequired()
    '''
def retainPosition():
    '''public void retainPosition()
    '''
def fetchTableData():
    '''public int fetchTableData()
    public synchronized int fetchTableData(final int startingRow)
    '''
def fetchRecordData():
    '''public synchronized boolean fetchRecordData()
    '''
def getMboSetData():
    '''public synchronized MboSetData getMboSetData(final int row, final int count, final String[] attributeNames)
    '''
def hasLongDescriptionText():
    '''public boolean hasLongDescriptionText(final int row, final String attribute)
    public boolean hasLongDescriptionText(final String attribute)
    '''
def toBeSaved():
    '''public boolean toBeSaved()
    '''
def isRowDeleted():
    '''public boolean isRowDeleted(int row)
    '''
def isModifiedRow():
    '''public boolean isModifiedRow()
    public boolean isModifiedRow(int row)
    '''
def hasRow():
    '''public boolean hasRow(final int row)
    '''
def isNewRow():
    '''public boolean isNewRow()
    public boolean isNewRow(int row)
    '''
def valueBound():
    '''public void valueBound(final HttpSessionBindingEvent event)
    '''
def valueUnbound():
    '''public void valueUnbound(final HttpSessionBindingEvent event)
    '''
def select():
    '''public synchronized void select(final int row)
    public synchronized void select(final int startIndex, final int count)
    '''
def unselect():
    '''public synchronized void unselect(final int row)
    public synchronized void unselect(final int startIndex, final int count)
    '''
def isSelected():
    '''public synchronized boolean isSelected(int row)
    '''
def getSelection():
    '''public synchronized Vector<MboRemote> getSelection()
    '''
def selectAll():
    '''public synchronized void selectAll()
    '''
def unselectAll():
    '''public synchronized void unselectAll()
    '''
def selectRows():
    '''public synchronized void selectRows(final Vector<MboRemote> selectMboRows, final Vector<MboRemote> unselectMboRows)
    '''
def resetWithSelection():
    '''public synchronized void resetWithSelection()
    '''
def sort():
    '''public synchronized void sort()
    public synchronized void sort(final String sOrderByClause)
    '''
def isColumnSorted():
    '''public int isColumnSorted(final String componentId)
    '''
def isEmpty():
    '''public synchronized boolean isEmpty()
    '''
def notExist():
    '''public synchronized boolean notExist()
    '''
def getCompleteWhere():
    '''public synchronized String getCompleteWhere()
    '''
def checkMethodAccess():
    '''public synchronized boolean checkMethodAccess(final String methodName)
    '''
def needToAuthenticate():
    '''public synchronized boolean needToAuthenticate(final SessionContext sc, String option)
    '''
def setShowDetails():
    '''public void setShowDetails(final boolean b)
    '''
def setRemoveOnCancel():
    '''public void setRemoveOnCancel(final int row)
    '''
def getLastFetchIndex():
    '''public int getLastFetchIndex()
    '''
def getEndRow():
    '''public int getEndRow()
    '''
def getCacheRowIndex():
    '''public int getCacheRowIndex(final int rowDataBeanIndex)
    '''
def getMboRowIndex():
    '''public int getMboRowIndex(final int tableRow)
    '''
def getPageStartIndex():
    '''public int getPageStartIndex()
    '''
def getRowIndexFromEvent():
    '''public int getRowIndexFromEvent(final WebClientEvent event)
    '''
def hasPageRows():
    '''public boolean hasPageRows()
    '''
def removeRowOnCancel():
    '''public boolean removeRowOnCancel(final int row)
    '''
def isTableRowSelected():
    '''public boolean isTableRowSelected(final int row)
    '''
def getShowDetails():
    '''public boolean getShowDetails()
    '''
def getPageEndRow():
    '''public int getPageEndRow()
    '''
def getPageRowCount():
    '''public int getPageRowCount()
    '''
def setfiltervalue():
    '''public int setfiltervalue()
    '''
def applyValuesToSharedAttributes():
    '''public boolean applyValuesToSharedAttributes(final ComponentInstance component, final String value)
    public void applyValuesToSharedAttributes(final ComponentInstance component)
    '''
def setValueFromComponent():
    '''public void setValueFromComponent(final BoundComponentInstance changedComponent, final WebClientEvent event, String newValue)
    '''
def setvalue():
    '''public int setvalue()
    '''
def refreshFieldErrors():
    '''public void refreshFieldErrors()
    '''
def getNullRequiedFields():
    '''public List<ERMAttributeError> getNullRequiedFields()
    '''
def displaycount():
    '''public String displaycount()
    '''
def copytonewrow():
    '''public int copytonewrow()
    '''
def addrow():
    '''public int addrow()
    '''
def scrollnext():
    '''public int scrollnext()
    '''
def scrollprev():
    '''public int scrollprev()
    '''
def nextrow():
    '''public int nextrow()
    '''
def prevrow():
    '''public int prevrow()
    '''
def toggledetailstate():
    '''public int toggledetailstate(final boolean open)
    '''
def toggledeleterow():
    '''public int toggledeleterow()
    '''
def highlightrow():
    '''public int highlightrow()
    public int highlightrow(final int row)
    '''
def toggleselectrow():
    '''public int toggleselectrow()
    '''
def toggleselectallrows():
    '''public int toggleselectallrows()
    '''
def sortcolumn():
    '''public int sortcolumn()
    public int sortcolumn(final String sortString)
    '''
def instantdelete():
    '''public int instantdelete()
    '''
def filterrows():
    '''public int filterrows()
    '''
def clearfilter():
    '''public int clearfilter()
    '''
def isTableStateFlagSet():
    '''public boolean isTableStateFlagSet(final long flag)
    '''
def getTableStateFlags():
    '''public BitFlag getTableStateFlags()
    '''
def selectrecord():
    '''public int selectrecord()
    '''
def resetJSPFlags():
    '''public void resetJSPFlags()
    '''
def getEventRowIndex():
    '''public int getEventRowIndex()
    '''
def setEventRowIndex():
    '''public void setEventRowIndex(final int i)
    '''
def getLastEventHandled():
    '''public WebClientEvent getLastEventHandled()
    '''
def setLastEventHandled():
    '''public void setLastEventHandled(final WebClientEvent event)
    '''
def setTableFlag():
    '''public void setTableFlag(final long flag, final boolean value)
    '''
def execute():
    '''public synchronized int execute()
    '''
def callMethod():
    '''public int callMethod(final WebClientEvent event)
    public int callMethod(final String methodName, final WebClientEvent event)
    public int callMethod(final WebClientEvent event, final Class<?>[] paramTypes, final Object[] params)
    public int callMethod(final String methodName, final WebClientEvent event, final Class<?>[] paramTypes, final Object[] params)
    '''
def findAndCallMethod():
    '''public int findAndCallMethod(final WebClientEvent event, final DataBean datasrc, final String method, final Class<?>[] paramTypes, final Object[] params)
    '''
def callRemoteMethod():
    '''public int callRemoteMethod(final String method)
    public int callRemoteMethod(final String method, final Class<?>[] paramTypes, final Object[] params)
    '''
def callBeanMethod():
    '''public int callBeanMethod(final WebClientEvent event)
    public int callBeanMethod(final String method, final WebClientEvent event)
    public int callBeanMethod(final WebClientEvent event, final Class<?>[] paramTypes, final Object[] params)
    public int callBeanMethod(final String method, final WebClientEvent event, final Class<?>[] paramTypes, final Object[] params)
    '''
def getReturnAttribute():
    '''public String getReturnAttribute()
    '''
def setReturnAttribute():
    '''public void setReturnAttribute(final String string)
    '''
def getReturnControlId():
    '''public String getReturnControlId()
    '''
def getReturnComponentId():
    '''public String getReturnComponentId()
    '''
def setReturnControlId():
    '''public void setReturnControlId(final String string)
    '''
def setReturnComponentId():
    '''public void setReturnComponentId(final String id)
    '''
def setReturnComponent():
    '''public void setReturnComponent(final ComponentInstance comp)
    '''
def getReturnComponent():
    '''public ComponentInstance getReturnComponent()
    '''
def handleRemoteException():
    '''public void handleRemoteException(final RemoteException e)
    '''
def turnEmptyStateOn():
    '''public void turnEmptyStateOn()
    '''
def getMboForUniqueId():
    '''public MboRemote getMboForUniqueId(final long uid)
    '''
def getUniqueIdValue():
    '''public long getUniqueIdValue()
    '''
def getUniqueIdName():
    '''public String getUniqueIdName()
    '''
def smartFill():
    '''public MboSetRemote smartFill(final int row, final String attribute, final String value, final boolean exactMatch)
    public MboSetRemote smartFill(final String attribute, final String value, final boolean exactMatch)
    '''
def getUniqueIdFromSmartFill():
    '''public long getUniqueIdFromSmartFill(final String attribute, final String value)
    public long getUniqueIdFromSmartFill(final String applicName, final String attribute, final String value)
    '''
def refreshTable():
    '''public void refreshTable()
    '''
def reloadTable():
    '''public void reloadTable()
    '''
def getSmartFillValue():
    '''public String getSmartFillValue()
    '''
def setSmartFillValue():
    '''public void setSmartFillValue(final String smartFillValue)
    '''
def cancelDialog():
    '''public int cancelDialog()
    '''
def checkESigAuthenticated():
    '''public synchronized void checkESigAuthenticated(String option)
    '''
def setEsigValidated():
    '''public synchronized void setEsigValidated(final boolean validated)
    '''
def getDescAttributeId():
    '''public String getDescAttributeId()
    '''
def setDescAttributeId():
    '''public void setDescAttributeId(final String string)
    '''
def setPageRowCount():
    '''public void setPageRowCount(final int rowCount)
    '''
def _useAllRecsQuery():
    '''public int _useAllRecsQuery()
    '''
def useAllRecsQuery():
    '''public int useAllRecsQuery()
    '''
def _useAllBookmarksQuery():
    '''public int _useAllBookmarksQuery()
    '''
def useAllBookmarksQuery():
    '''public int useAllBookmarksQuery()
    '''
def _usequery():
    '''public int _usequery()
    '''
def usequery():
    '''public int usequery()
    '''
def useQuery():
    '''public void useQuery(final String queryName)
    '''
def sqlwhere():
    '''public int sqlwhere()
    '''
def useqbe():
    '''public int useqbe()
    '''
def queryAllRecs():
    '''public void queryAllRecs()
    '''
def queryAllBookmarks():
    '''public void queryAllBookmarks()
    '''
def getCurrentQueryName():
    '''public String getCurrentQueryName()
    '''
def clearBean():
    '''public void clearBean()
    '''
def setQueryBySiteQbe():
    '''public void setQueryBySiteQbe()
    '''
def getWarnings():
    '''public MXException[] getWarnings()
    '''
def moveToMboFromDataBean():
    '''public boolean moveToMboFromDataBean(final DataBean dataBean, final String dataAttribute)
    '''
def hierarchicalmove():
    '''public int hierarchicalmove()
    '''
def getTableOffset():
    '''public int getTableOffset()
    '''
def getSortOrder():
    '''public String getSortOrder(final String sortAttribute)
    '''
def addSigOption():
    '''public void addSigOption(final String sigoption)
    '''
def addConditionalProperties():
    '''public void addConditionalProperties(final String sigOption, final int row, final HashMap<String, String> properties)
    '''
def getConditionalProperties():
    '''public HashMap<String, String> getConditionalProperties(final int row, String sigOption)
    '''
def hasSigOptionAccess():
    '''public boolean hasSigOptionAccess(final String sigOption)
    public boolean hasSigOptionAccess(final int row, final String sigOption)
    '''
def getMboSetFromSmartFind():
    '''public MboSetRemote getMboSetFromSmartFind(final int row, final String attribute)
    public MboSetRemote getMboSetFromSmartFind(final String attribute)
    public MboSetRemote getMboSetFromSmartFind(final String app, final String attribute)
    '''
def canFetchData():
    '''public boolean canFetchData()
    '''
def getRemoteForDownload():
    '''public MboSetRemote getRemoteForDownload()
    '''
def isSubSelect():
    '''public boolean isSubSelect()
    '''
def setDynamicAppDefaults():
    '''public void setDynamicAppDefaults(final MboRemote mbo)
    '''
def setDynamicDefault():
    '''public void setDynamicDefault(final String attribute, final DataBean frmDataBean, final String frmAttribute, final String defaultType)
    '''
def setDynamicQbeDefaults():
    '''public synchronized void setDynamicQbeDefaults()
    '''
def changeRequiredField():
    '''public boolean changeRequiredField(int row, String attribute, final boolean required)
    '''
def getQueryNameBeforeReviseAction():
    '''public String getQueryNameBeforeReviseAction()
    '''
def setQueryNameBeforeReviseAction():
    '''public void setQueryNameBeforeReviseAction(final String queryName)
    '''
def getQueryDescBeforeReviseAction():
    '''public String getQueryDescBeforeReviseAction()
    '''
def setQueryDescBeforeReviseAction():
    '''public void setQueryDescBeforeReviseAction(final String queryDesc)
    '''
def setEmptyOnClear():
    '''public void setEmptyOnClear(final boolean emptyOnClear)
    '''
def asyncLocked():
    '''public boolean asyncLocked()
    '''
def setAsyncLock():
    '''public void setAsyncLock(final boolean asyncLock)
    '''
def madeRequiredConditionally():
    '''public boolean madeRequiredConditionally(String attribute)
    '''
def isListTableModified():
    '''public boolean isListTableModified()
    '''
def setListTableModified():
    '''public void setListTableModified(final boolean inChange)
    '''
def isListTableRetain():
    '''public boolean isListTableRetain()
    '''
def setListTableRetain():
    '''public void setListTableRetain(final boolean inRetain)
    '''
def getCurrentQueryDescription():
    '''public String getCurrentQueryDescription()
    '''
def setCurrentQueryDescription():
    '''public void setCurrentQueryDescription(final String queryDescription)
    '''
def boundToTable():
    '''public boolean boundToTable()
    '''
def setApplicationError():
    '''public void setApplicationError(final String dataAttribute, int row, final ApplicationError error)
    '''
def buildPortalMsg():
    '''public String buildPortalMsg(final String attribute, final String newValue)
    '''
def rePosition():
    '''public boolean rePosition()
    '''
def isAppTableRetain():
    '''public boolean isAppTableRetain()
    '''
def positionState():
    '''public void positionState()
    '''
def markTablePosition():
    '''public void markTablePosition(final boolean inFlg)
    '''
def isTablePostionMarked():
    '''public boolean isTablePostionMarked()
    '''
def getUIERMEntity():
    '''public UIERMEntity getUIERMEntity()
    '''
def toString():
    '''public String toString()
    '''
def registerDynamicControlsWithERM():
    '''public void registerDynamicControlsWithERM(final List<ControlInstance> controls)
    '''
def getLockedByDisplayName():
    '''public String getLockedByDisplayName(final int row)
    '''
def isRowLocked():
    '''public boolean isRowLocked(final int row)
    '''
def isLookupMultiSelect():
    '''public boolean isLookupMultiSelect(final BoundComponentInstance boundComponentInstance, final boolean isQueryInput)
    '''
def getSavedFilterSettings():
    '''public Hashtable<String, String> getSavedFilterSettings()
    '''
def getParentRelationship():
    '''public String getParentRelationship()
    '''
