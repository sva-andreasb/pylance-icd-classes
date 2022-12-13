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
ALL_BOOKMARKS = "String  ALL_BOOKMARKS""
ALL_RECORDS = "String  ALL_RECORDS""
def DataBean():
'''public DataBean()
'''
pass
def setupBean():
'''public void setupBean(final WebClientSession wcs)
public void setupBean(final SessionContext sc)
'''
pass
def bindComponent():
'''public void bindComponent(final BoundComponentInstance boundComponent)
'''
pass
def unbindComponent():
'''public void unbindComponent(final BoundComponentInstance boundComponent)
'''
pass
def setNewRowUnedited():
'''public void setNewRowUnedited(final boolean unedited)
'''
pass
def isNewRowUnedited():
'''public boolean isNewRowUnedited()
'''
pass
def getTableAttributes():
'''public String[] getTableAttributes()
'''
pass
def setAppDefault():
'''public synchronized void setAppDefault(final String attribute, final String value)
'''
pass
def setQbeDefaults():
'''public synchronized void setQbeDefaults()
'''
pass
def setAppDefaults():
'''public synchronized void setAppDefaults()
'''
pass
def setParent():
'''public void setParent(final DataBean parent, final String parentRelationship)
'''
pass
def getParent():
'''public DataBean getParent()
'''
pass
def addListener():
'''public void addListener(final DataBeanListener listener)
'''
pass
def removeListener():
'''public void removeListener(final DataBeanListener listener)
'''
pass
def fireDataChangedEvent():
'''public void fireDataChangedEvent(final DataBean speaker)
public void fireDataChangedEvent()
'''
pass
def fireStructureChangedEvent():
'''public void fireStructureChangedEvent(final DataBean speaker)
public void fireStructureChangedEvent()
'''
pass
def sendRefreshTable():
'''public void sendRefreshTable()
'''
pass
def listenerChangedEvent():
'''public void listenerChangedEvent(final DataBean speaker)
'''
pass
def dataChangedEvent():
'''public void dataChangedEvent(final DataBean speaker)
'''
pass
def structureChangedEvent():
'''public void structureChangedEvent(final DataBean speaker)
'''
pass
def fireChildChangedEvent():
'''public void fireChildChangedEvent()
'''
pass
def setMboName():
'''public void setMboName(final String sMboName)
'''
pass
def getMboName():
'''public String getMboName()
'''
pass
def getMXSession():
'''public MXSession getMXSession()
'''
pass
def setDefaultOrderBy():
'''public void setDefaultOrderBy(final String sOrderByClause)
'''
pass
def getDefaultOrderBy():
'''public String getDefaultOrderBy()
'''
pass
def setOrderBy():
'''public synchronized void setOrderBy(String sOrderByClause)
'''
pass
def getOrderBy():
'''public String getOrderBy()
'''
pass
def setAppWhere():
'''public synchronized void setAppWhere(final String sWhereClause)
'''
pass
def getAppWhere():
'''public synchronized String getAppWhere()
'''
pass
def hasMboSetRemote():
'''public boolean hasMboSetRemote()
'''
pass
def getMboSet():
'''public MboSetRemote getMboSet()
'''
pass
def setApp():
'''public void setApp(final String appName)
'''
pass
def getKeyAttribute():
'''public String getKeyAttribute()
'''
pass
def getKeyAttributes():
'''public String[] getKeyAttributes()
'''
pass
def getAttributes():
'''public String[] getAttributes()
'''
pass
def isAttribute():
'''public boolean isAttribute(final String attribute)
'''
pass
def isTableAttribute():
'''public boolean isTableAttribute(final String attribute)
'''
pass
def addAttribute():
'''public void addAttribute(final String attribute, BitFlag flags)
'''
pass
def addQbeAttribute():
'''public void addQbeAttribute(final String attribute)
'''
pass
def setAttributes():
'''public void setAttributes(final String[] attributelist, final BitFlag[] flags)
'''
pass
def count():
'''public synchronized int count()
'''
pass
def setUserWhere():
'''public synchronized void setUserWhere(final String whereClause)
'''
pass
def getUserWhere():
'''public synchronized String getUserWhere()
'''
pass
def getUserAndQbeWhere():
'''public synchronized String getUserAndQbeWhere()
'''
pass
def useStoredQuery():
'''public synchronized void useStoredQuery(final String queryName)
'''
pass
def getQbe():
'''public synchronized String getQbe(final String attribute)
public synchronized String getQbe()
'''
pass
def saveCurrentQbeSettings():
'''public synchronized void saveCurrentQbeSettings(final boolean forceOverride)
'''
pass
def clearSavedQbeSettings():
'''public synchronized void clearSavedQbeSettings()
'''
pass
def restoreSavedQbeSettings():
'''public synchronized void restoreSavedQbeSettings()
'''
pass
def clearSavedFilterSettings():
'''public void clearSavedFilterSettings()
'''
pass
def setQbe():
'''public synchronized void setQbe(final String attribute, final String expression)
public synchronized void setQbe(final String attribute, final MboSetRemote expression)
public synchronized void setQbe(final String[] attributes, final String expression)
public synchronized void setQbe(final Hashtable<String, String> qbeAttrs)
public synchronized void setQbe(final String expression)
'''
pass
def setDefaultQbe():
'''public void setDefaultQbe(final String attribute, final String expression)
'''
pass
def getQbeAttributes():
'''public synchronized Hashtable<String, String> getQbeAttributes()
'''
pass
def setQbeAttributes():
'''public synchronized void setQbeAttributes(final Hashtable<String, String> newQbeAttributes)
'''
pass
def setQbeExactMatch():
'''public synchronized void setQbeExactMatch(final boolean exact)
'''
pass
def setQbeCaseSensitive():
'''public synchronized void setQbeCaseSensitive(final boolean caseSensitive)
'''
pass
def resetQbe():
'''public synchronized void resetQbe()
'''
pass
def getBoolean():
'''public synchronized boolean getBoolean(final String col)
public synchronized boolean getBoolean(final int row, final String col)
'''
pass
def getString():
'''public synchronized String getString(final String attribute)
public synchronized String getString(final int row, final String attribute)
'''
pass
def getColumnString():
'''public synchronized String getColumnString(final int row, final String col)
'''
pass
def getColumnDate():
'''public synchronized Date getColumnDate(final int row, final String col)
'''
pass
def getDate():
'''public synchronized Date getDate(final String attribute)
'''
pass
def getTitle():
'''public synchronized String getTitle(final String attribute)
'''
pass
def getZombie():
'''public MboRemote getZombie()
'''
pass
def getMboOrZombie():
'''public MboRemote getMboOrZombie()
'''
pass
def getMboValueInfo():
'''public synchronized MboValueInfoStatic getMboValueInfo(final String attribute)
'''
pass
def getZombieMboValueData():
'''public synchronized MboValueData getZombieMboValueData(final String attribute)
'''
pass
def getMboValueData():
'''public synchronized MboValueData getMboValueData(final int nRow, final String attribute)
public synchronized MboValueData getMboValueData(final String attribute)
'''
pass
def isAttributeHidden():
'''public boolean isAttributeHidden(final String attribute)
public boolean isAttributeHidden(final int row, final String attribute)
'''
pass
def isMboHidden():
'''public boolean isMboHidden()
public boolean isMboHidden(final int row)
'''
pass
def getRemoteForLookup():
'''public MboSetRemote getRemoteForLookup()
'''
pass
def getList():
'''public synchronized MboSetRemote getList(final String attribute)
public synchronized MboSetRemote getList(final Integer row, final String attribute)
public synchronized MboSetRemote getList(final int nRow, final String attribute)
'''
pass
def getDataList():
'''public synchronized String[][] getDataList(final String dataAttribute)
public synchronized String[][] getDataList(final int row, final String dataAttribute)
public synchronized String[][] getDataList(final int row, final String dataAttribute, final String keyAttributeName, final String displayAttribute)
public synchronized String[][] getDataList(final int row, final String dataAttribute, final String displayAttribute)
'''
pass
def getDataListFromMboSetRemote():
'''public synchronized String[][] getDataListFromMboSetRemote(final MboSetRemote setRemote, String dataAttribute, String displayAttribute)
'''
pass
def validate():
'''public void validate()
'''
pass
def validateMbo():
'''public void validateMbo()
'''
pass
def validateChildren():
'''public void validateChildren()
'''
pass
def checkAndDistributeRequiredError():
'''public MXException checkAndDistributeRequiredError(final MXException mxe)
'''
pass
def handleRequiredFieldException():
'''public void handleRequiredFieldException(MXRequiredFieldException requiredFieldException, final WebClientEvent event)
'''
pass
def save():
'''public synchronized void save()
public synchronized void save(final MboRemote mbo)
'''
pass
def checkForAppError():
'''public void checkForAppError()
'''
pass
def reset():
'''public synchronized void reset()
'''
pass
def canCloseBean():
'''public boolean canCloseBean()
'''
pass
def hasSameMboSet():
'''public boolean hasSameMboSet(final DataBean bean)
'''
pass
def addDialogReference():
'''public void addDialogReference()
'''
pass
def removeDialogReference():
'''public void removeDialogReference()
'''
pass
def close():
'''public void close()
'''
pass
def setCurrentRow():
'''public synchronized boolean setCurrentRow(final int nRow)
'''
pass
def getCurrentRow():
'''public int getCurrentRow()
'''
pass
def next():
'''public synchronized boolean next()
'''
pass
def previous():
'''public synchronized boolean previous()
'''
pass
def insert():
'''public synchronized void insert(final int nRow)
public synchronized void insert()
'''
pass
def insertAtEnd():
'''public synchronized void insertAtEnd()
'''
pass
def delete():
'''public synchronized void delete()
public synchronized void delete(final int nRow)
'''
pass
def deleteAndRemove():
'''public synchronized void deleteAndRemove()
public synchronized void deleteAndRemove(final int nRow)
'''
pass
def undelete():
'''public synchronized void undelete()
public synchronized void undelete(final int nRow)
'''
pass
def setDefaultValue():
'''public synchronized void setDefaultValue(final String attribute, final MboRemote value)
public synchronized void setDefaultValue(final String attribute, final String value)
'''
pass
def setUserDefaults():
'''public synchronized void setUserDefaults()
'''
pass
def getDefaultValue():
'''public synchronized String getDefaultValue(final String attribute)
'''
pass
def setValue():
'''public synchronized void setValue(final String attribute, final String value)
public synchronized void setValue(final int nRow, final String attribute, final String value)
public synchronized void setValue(final String attribute, final String value, final long accessModifier)
public synchronized void setValue(final int nRow, final String attribute, final String value, final long accessModifier)
public synchronized void setValue(final String attribute, final MboRemote mboRemote)
public synchronized void setValue(final int row, final String attribute, final MboRemote mboRemote)
public synchronized void setValue(final String attribute, final MboSetRemote mboSetRemote)
'''
pass
def setDate():
'''public synchronized void setDate(final String controlId, final String attribute, final Date value)
public synchronized void setDate(final String componentId, final Date value)
public synchronized void setDate(final BoundComponentInstance boundComponent, final Date value)
'''
pass
def returnLookupValue():
'''public synchronized int returnLookupValue(final String lookupValue)
public synchronized int returnLookupValue(final String componentId, final MboRemote lookupMbo)
public synchronized int returnLookupValue(final MboRemote lookupMbo)
public synchronized int returnLookupValue(final MboSetRemote lookupMboSet)
'''
pass
def getMbo():
'''public synchronized MboRemote getMbo()
public synchronized MboRemote getMbo(final int row)
'''
pass
def duplicateMbo():
'''public synchronized boolean duplicateMbo()
'''
pass
def getDataAsArray():
'''public String[][] getDataAsArray()
public String[][] getDataAsArray(final String[] attributeNames)
'''
pass
def getSelectedDataAsArray():
'''public String[][] getSelectedDataAsArray()
public String[][] getSelectedDataAsArray(final String[] attributeNames)
'''
pass
def propagateRequired():
'''public void propagateRequired()
'''
pass
def retainPosition():
'''public void retainPosition()
'''
pass
def fetchTableData():
'''public int fetchTableData()
public synchronized int fetchTableData(final int startingRow)
'''
pass
def fetchRecordData():
'''public synchronized boolean fetchRecordData()
'''
pass
def getMboSetData():
'''public synchronized MboSetData getMboSetData(final int row, final int count, final String[] attributeNames)
'''
pass
def hasLongDescriptionText():
'''public boolean hasLongDescriptionText(final int row, final String attribute)
public boolean hasLongDescriptionText(final String attribute)
'''
pass
def toBeSaved():
'''public boolean toBeSaved()
'''
pass
def isRowDeleted():
'''public boolean isRowDeleted(int row)
'''
pass
def isModifiedRow():
'''public boolean isModifiedRow()
public boolean isModifiedRow(int row)
'''
pass
def hasRow():
'''public boolean hasRow(final int row)
'''
pass
def isNewRow():
'''public boolean isNewRow()
public boolean isNewRow(int row)
'''
pass
def valueBound():
'''public void valueBound(final HttpSessionBindingEvent event)
'''
pass
def valueUnbound():
'''public void valueUnbound(final HttpSessionBindingEvent event)
'''
pass
def select():
'''public synchronized void select(final int row)
public synchronized void select(final int startIndex, final int count)
'''
pass
def unselect():
'''public synchronized void unselect(final int row)
public synchronized void unselect(final int startIndex, final int count)
'''
pass
def isSelected():
'''public synchronized boolean isSelected(int row)
'''
pass
def getSelection():
'''public synchronized Vector<MboRemote> getSelection()
'''
pass
def selectAll():
'''public synchronized void selectAll()
'''
pass
def unselectAll():
'''public synchronized void unselectAll()
'''
pass
def selectRows():
'''public synchronized void selectRows(final Vector<MboRemote> selectMboRows, final Vector<MboRemote> unselectMboRows)
'''
pass
def resetWithSelection():
'''public synchronized void resetWithSelection()
'''
pass
def sort():
'''public synchronized void sort()
public synchronized void sort(final String sOrderByClause)
'''
pass
def isColumnSorted():
'''public int isColumnSorted(final String componentId)
'''
pass
def isEmpty():
'''public synchronized boolean isEmpty()
'''
pass
def notExist():
'''public synchronized boolean notExist()
'''
pass
def getCompleteWhere():
'''public synchronized String getCompleteWhere()
'''
pass
def checkMethodAccess():
'''public synchronized boolean checkMethodAccess(final String methodName)
'''
pass
def needToAuthenticate():
'''public synchronized boolean needToAuthenticate(final SessionContext sc, String option)
'''
pass
def setShowDetails():
'''public void setShowDetails(final boolean b)
'''
pass
def setRemoveOnCancel():
'''public void setRemoveOnCancel(final int row)
'''
pass
def getLastFetchIndex():
'''public int getLastFetchIndex()
'''
pass
def getEndRow():
'''public int getEndRow()
'''
pass
def getCacheRowIndex():
'''public int getCacheRowIndex(final int rowDataBeanIndex)
'''
pass
def getMboRowIndex():
'''public int getMboRowIndex(final int tableRow)
'''
pass
def getPageStartIndex():
'''public int getPageStartIndex()
'''
pass
def getRowIndexFromEvent():
'''public int getRowIndexFromEvent(final WebClientEvent event)
'''
pass
def hasPageRows():
'''public boolean hasPageRows()
'''
pass
def removeRowOnCancel():
'''public boolean removeRowOnCancel(final int row)
'''
pass
def isTableRowSelected():
'''public boolean isTableRowSelected(final int row)
'''
pass
def getShowDetails():
'''public boolean getShowDetails()
'''
pass
def getPageEndRow():
'''public int getPageEndRow()
'''
pass
def getPageRowCount():
'''public int getPageRowCount()
'''
pass
def setfiltervalue():
'''public int setfiltervalue()
'''
pass
def applyValuesToSharedAttributes():
'''public boolean applyValuesToSharedAttributes(final ComponentInstance component, final String value)
public void applyValuesToSharedAttributes(final ComponentInstance component)
'''
pass
def setValueFromComponent():
'''public void setValueFromComponent(final BoundComponentInstance changedComponent, final WebClientEvent event, String newValue)
'''
pass
def setvalue():
'''public int setvalue()
'''
pass
def refreshFieldErrors():
'''public void refreshFieldErrors()
'''
pass
def getNullRequiedFields():
'''public List<ERMAttributeError> getNullRequiedFields()
'''
pass
def displaycount():
'''public String displaycount()
'''
pass
def copytonewrow():
'''public int copytonewrow()
'''
pass
def addrow():
'''public int addrow()
'''
pass
def scrollnext():
'''public int scrollnext()
'''
pass
def scrollprev():
'''public int scrollprev()
'''
pass
def nextrow():
'''public int nextrow()
'''
pass
def prevrow():
'''public int prevrow()
'''
pass
def toggledetailstate():
'''public int toggledetailstate(final boolean open)
'''
pass
def toggledeleterow():
'''public int toggledeleterow()
'''
pass
def highlightrow():
'''public int highlightrow()
public int highlightrow(final int row)
'''
pass
def toggleselectrow():
'''public int toggleselectrow()
'''
pass
def toggleselectallrows():
'''public int toggleselectallrows()
'''
pass
def sortcolumn():
'''public int sortcolumn()
public int sortcolumn(final String sortString)
'''
pass
def instantdelete():
'''public int instantdelete()
'''
pass
def filterrows():
'''public int filterrows()
'''
pass
def clearfilter():
'''public int clearfilter()
'''
pass
def isTableStateFlagSet():
'''public boolean isTableStateFlagSet(final long flag)
'''
pass
def getTableStateFlags():
'''public BitFlag getTableStateFlags()
'''
pass
def selectrecord():
'''public int selectrecord()
'''
pass
def resetJSPFlags():
'''public void resetJSPFlags()
'''
pass
def getEventRowIndex():
'''public int getEventRowIndex()
'''
pass
def setEventRowIndex():
'''public void setEventRowIndex(final int i)
'''
pass
def getLastEventHandled():
'''public WebClientEvent getLastEventHandled()
'''
pass
def setLastEventHandled():
'''public void setLastEventHandled(final WebClientEvent event)
'''
pass
def setTableFlag():
'''public void setTableFlag(final long flag, final boolean value)
'''
pass
def execute():
'''public synchronized int execute()
'''
pass
def callMethod():
'''public int callMethod(final WebClientEvent event)
public int callMethod(final String methodName, final WebClientEvent event)
public int callMethod(final WebClientEvent event, final Class<?>[] paramTypes, final Object[] params)
public int callMethod(final String methodName, final WebClientEvent event, final Class<?>[] paramTypes, final Object[] params)
'''
pass
def findAndCallMethod():
'''public int findAndCallMethod(final WebClientEvent event, final DataBean datasrc, final String method, final Class<?>[] paramTypes, final Object[] params)
'''
pass
def callRemoteMethod():
'''public int callRemoteMethod(final String method)
public int callRemoteMethod(final String method, final Class<?>[] paramTypes, final Object[] params)
'''
pass
def callBeanMethod():
'''public int callBeanMethod(final WebClientEvent event)
public int callBeanMethod(final String method, final WebClientEvent event)
public int callBeanMethod(final WebClientEvent event, final Class<?>[] paramTypes, final Object[] params)
public int callBeanMethod(final String method, final WebClientEvent event, final Class<?>[] paramTypes, final Object[] params)
'''
pass
def getReturnAttribute():
'''public String getReturnAttribute()
'''
pass
def setReturnAttribute():
'''public void setReturnAttribute(final String string)
'''
pass
def getReturnControlId():
'''public String getReturnControlId()
'''
pass
def getReturnComponentId():
'''public String getReturnComponentId()
'''
pass
def setReturnControlId():
'''public void setReturnControlId(final String string)
'''
pass
def setReturnComponentId():
'''public void setReturnComponentId(final String id)
'''
pass
def setReturnComponent():
'''public void setReturnComponent(final ComponentInstance comp)
'''
pass
def getReturnComponent():
'''public ComponentInstance getReturnComponent()
'''
pass
def handleRemoteException():
'''public void handleRemoteException(final RemoteException e)
'''
pass
def turnEmptyStateOn():
'''public void turnEmptyStateOn()
'''
pass
def getMboForUniqueId():
'''public MboRemote getMboForUniqueId(final long uid)
'''
pass
def getUniqueIdValue():
'''public long getUniqueIdValue()
'''
pass
def getUniqueIdName():
'''public String getUniqueIdName()
'''
pass
def smartFill():
'''public MboSetRemote smartFill(final int row, final String attribute, final String value, final boolean exactMatch)
public MboSetRemote smartFill(final String attribute, final String value, final boolean exactMatch)
'''
pass
def getUniqueIdFromSmartFill():
'''public long getUniqueIdFromSmartFill(final String attribute, final String value)
public long getUniqueIdFromSmartFill(final String applicName, final String attribute, final String value)
'''
pass
def refreshTable():
'''public void refreshTable()
'''
pass
def reloadTable():
'''public void reloadTable()
'''
pass
def getSmartFillValue():
'''public String getSmartFillValue()
'''
pass
def setSmartFillValue():
'''public void setSmartFillValue(final String smartFillValue)
'''
pass
def cancelDialog():
'''public int cancelDialog()
'''
pass
def checkESigAuthenticated():
'''public synchronized void checkESigAuthenticated(String option)
'''
pass
def setEsigValidated():
'''public synchronized void setEsigValidated(final boolean validated)
'''
pass
def getDescAttributeId():
'''public String getDescAttributeId()
'''
pass
def setDescAttributeId():
'''public void setDescAttributeId(final String string)
'''
pass
def setPageRowCount():
'''public void setPageRowCount(final int rowCount)
'''
pass
def _useAllRecsQuery():
'''public int _useAllRecsQuery()
'''
pass
def useAllRecsQuery():
'''public int useAllRecsQuery()
'''
pass
def _useAllBookmarksQuery():
'''public int _useAllBookmarksQuery()
'''
pass
def useAllBookmarksQuery():
'''public int useAllBookmarksQuery()
'''
pass
def _usequery():
'''public int _usequery()
'''
pass
def usequery():
'''public int usequery()
'''
pass
def useQuery():
'''public void useQuery(final String queryName)
'''
pass
def sqlwhere():
'''public int sqlwhere()
'''
pass
def useqbe():
'''public int useqbe()
'''
pass
def queryAllRecs():
'''public void queryAllRecs()
'''
pass
def queryAllBookmarks():
'''public void queryAllBookmarks()
'''
pass
def getCurrentQueryName():
'''public String getCurrentQueryName()
'''
pass
def clearBean():
'''public void clearBean()
'''
pass
def setQueryBySiteQbe():
'''public void setQueryBySiteQbe()
'''
pass
def getWarnings():
'''public MXException[] getWarnings()
'''
pass
def moveToMboFromDataBean():
'''public boolean moveToMboFromDataBean(final DataBean dataBean, final String dataAttribute)
'''
pass
def hierarchicalmove():
'''public int hierarchicalmove()
'''
pass
def getTableOffset():
'''public int getTableOffset()
'''
pass
def getSortOrder():
'''public String getSortOrder(final String sortAttribute)
'''
pass
def addSigOption():
'''public void addSigOption(final String sigoption)
'''
pass
def addConditionalProperties():
'''public void addConditionalProperties(final String sigOption, final int row, final HashMap<String, String> properties)
'''
pass
def getConditionalProperties():
'''public HashMap<String, String> getConditionalProperties(final int row, String sigOption)
'''
pass
def hasSigOptionAccess():
'''public boolean hasSigOptionAccess(final String sigOption)
public boolean hasSigOptionAccess(final int row, final String sigOption)
'''
pass
def getMboSetFromSmartFind():
'''public MboSetRemote getMboSetFromSmartFind(final int row, final String attribute)
public MboSetRemote getMboSetFromSmartFind(final String attribute)
public MboSetRemote getMboSetFromSmartFind(final String app, final String attribute)
'''
pass
def canFetchData():
'''public boolean canFetchData()
'''
pass
def getRemoteForDownload():
'''public MboSetRemote getRemoteForDownload()
'''
pass
def isSubSelect():
'''public boolean isSubSelect()
'''
pass
def setDynamicAppDefaults():
'''public void setDynamicAppDefaults(final MboRemote mbo)
'''
pass
def setDynamicDefault():
'''public void setDynamicDefault(final String attribute, final DataBean frmDataBean, final String frmAttribute, final String defaultType)
'''
pass
def setDynamicQbeDefaults():
'''public synchronized void setDynamicQbeDefaults()
'''
pass
def changeRequiredField():
'''public boolean changeRequiredField(int row, String attribute, final boolean required)
'''
pass
def getQueryNameBeforeReviseAction():
'''public String getQueryNameBeforeReviseAction()
'''
pass
def setQueryNameBeforeReviseAction():
'''public void setQueryNameBeforeReviseAction(final String queryName)
'''
pass
def getQueryDescBeforeReviseAction():
'''public String getQueryDescBeforeReviseAction()
'''
pass
def setQueryDescBeforeReviseAction():
'''public void setQueryDescBeforeReviseAction(final String queryDesc)
'''
pass
def setEmptyOnClear():
'''public void setEmptyOnClear(final boolean emptyOnClear)
'''
pass
def asyncLocked():
'''public boolean asyncLocked()
'''
pass
def setAsyncLock():
'''public void setAsyncLock(final boolean asyncLock)
'''
pass
def madeRequiredConditionally():
'''public boolean madeRequiredConditionally(String attribute)
'''
pass
def isListTableModified():
'''public boolean isListTableModified()
'''
pass
def setListTableModified():
'''public void setListTableModified(final boolean inChange)
'''
pass
def isListTableRetain():
'''public boolean isListTableRetain()
'''
pass
def setListTableRetain():
'''public void setListTableRetain(final boolean inRetain)
'''
pass
def getCurrentQueryDescription():
'''public String getCurrentQueryDescription()
'''
pass
def setCurrentQueryDescription():
'''public void setCurrentQueryDescription(final String queryDescription)
'''
pass
def boundToTable():
'''public boolean boundToTable()
'''
pass
def setApplicationError():
'''public void setApplicationError(final String dataAttribute, int row, final ApplicationError error)
'''
pass
def buildPortalMsg():
'''public String buildPortalMsg(final String attribute, final String newValue)
'''
pass
def rePosition():
'''public boolean rePosition()
'''
pass
def isAppTableRetain():
'''public boolean isAppTableRetain()
'''
pass
def positionState():
'''public void positionState()
'''
pass
def markTablePosition():
'''public void markTablePosition(final boolean inFlg)
'''
pass
def isTablePostionMarked():
'''public boolean isTablePostionMarked()
'''
pass
def getUIERMEntity():
'''public UIERMEntity getUIERMEntity()
'''
pass
def toString():
'''public String toString()
'''
pass
def registerDynamicControlsWithERM():
'''public void registerDynamicControlsWithERM(final List<ControlInstance> controls)
'''
pass
def getLockedByDisplayName():
'''public String getLockedByDisplayName(final int row)
'''
pass
def isRowLocked():
'''public boolean isRowLocked(final int row)
'''
pass
def isLookupMultiSelect():
'''public boolean isLookupMultiSelect(final BoundComponentInstance boundComponentInstance, final boolean isQueryInput)
'''
pass
def getSavedFilterSettings():
'''public Hashtable<String, String> getSavedFilterSettings()
'''
pass
def getParentRelationship():
'''public String getParentRelationship()
'''
pass
