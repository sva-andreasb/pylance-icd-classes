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
def ():
    '''returns DataBean\n\n
    ()\n
    '''
def setupBean():
    '''returns None\n\n
    setupBean(final WebClientSession wcs)\n
    setupBean(final SessionContext sc)\n
    '''
def bindComponent():
    '''returns None\n\n
    bindComponent(final BoundComponentInstance boundComponent)\n
    '''
def unbindComponent():
    '''returns None\n\n
    unbindComponent(final BoundComponentInstance boundComponent)\n
    '''
def setNewRowUnedited():
    '''returns None\n\n
    setNewRowUnedited(final boolean unedited)\n
    '''
def isNewRowUnedited():
    '''returns boolean\n\n
    isNewRowUnedited()\n
    '''
def getTableAttributes():
    '''returns String[]\n\n
    getTableAttributes()\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final DataBean parent, final String parentRelationship)\n
    '''
def getParent():
    '''returns DataBean\n\n
    getParent()\n
    '''
def addListener():
    '''returns None\n\n
    addListener(final DataBeanListener listener)\n
    '''
def removeListener():
    '''returns None\n\n
    removeListener(final DataBeanListener listener)\n
    '''
def fireDataChangedEvent():
    '''returns None\n\n
    fireDataChangedEvent(final DataBean speaker)\n
    fireDataChangedEvent()\n
    '''
def fireStructureChangedEvent():
    '''returns None\n\n
    fireStructureChangedEvent(final DataBean speaker)\n
    fireStructureChangedEvent()\n
    '''
def sendRefreshTable():
    '''returns None\n\n
    sendRefreshTable()\n
    '''
def listenerChangedEvent():
    '''returns None\n\n
    listenerChangedEvent(final DataBean speaker)\n
    '''
def dataChangedEvent():
    '''returns None\n\n
    dataChangedEvent(final DataBean speaker)\n
    '''
def structureChangedEvent():
    '''returns None\n\n
    structureChangedEvent(final DataBean speaker)\n
    '''
def fireChildChangedEvent():
    '''returns None\n\n
    fireChildChangedEvent()\n
    '''
def setMboName():
    '''returns None\n\n
    setMboName(final String sMboName)\n
    '''
def getMboName():
    '''returns String\n\n
    getMboName()\n
    '''
def getMXSession():
    '''returns MXSession\n\n
    getMXSession()\n
    '''
def setDefaultOrderBy():
    '''returns None\n\n
    setDefaultOrderBy(final String sOrderByClause)\n
    '''
def getDefaultOrderBy():
    '''returns String\n\n
    getDefaultOrderBy()\n
    '''
def getOrderBy():
    '''returns String\n\n
    getOrderBy()\n
    '''
def hasMboSetRemote():
    '''returns boolean\n\n
    hasMboSetRemote()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet()\n
    '''
def setApp():
    '''returns None\n\n
    setApp(final String appName)\n
    '''
def getKeyAttribute():
    '''returns String\n\n
    getKeyAttribute()\n
    '''
def getKeyAttributes():
    '''returns String[]\n\n
    getKeyAttributes()\n
    '''
def getAttributes():
    '''returns String[]\n\n
    getAttributes()\n
    '''
def isAttribute():
    '''returns boolean\n\n
    isAttribute(final String attribute)\n
    '''
def isTableAttribute():
    '''returns boolean\n\n
    isTableAttribute(final String attribute)\n
    '''
def addAttribute():
    '''returns None\n\n
    addAttribute(final String attribute, BitFlag flags)\n
    '''
def addQbeAttribute():
    '''returns None\n\n
    addQbeAttribute(final String attribute)\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final String[] attributelist, final BitFlag[] flags)\n
    '''
def clearSavedFilterSettings():
    '''returns None\n\n
    clearSavedFilterSettings()\n
    '''
def setDefaultQbe():
    '''returns None\n\n
    setDefaultQbe(final String attribute, final String expression)\n
    '''
def getZombie():
    '''returns MboRemote\n\n
    getZombie()\n
    '''
def getMboOrZombie():
    '''returns MboRemote\n\n
    getMboOrZombie()\n
    '''
def isAttributeHidden():
    '''returns boolean\n\n
    isAttributeHidden(final String attribute)\n
    isAttributeHidden(final int row, final String attribute)\n
    '''
def isMboHidden():
    '''returns boolean\n\n
    isMboHidden()\n
    isMboHidden(final int row)\n
    '''
def getRemoteForLookup():
    '''returns MboSetRemote\n\n
    getRemoteForLookup()\n
    '''
def validate():
    '''returns None\n\n
    validate()\n
    '''
def validateMbo():
    '''returns None\n\n
    validateMbo()\n
    '''
def validateChildren():
    '''returns None\n\n
    validateChildren()\n
    '''
def checkAndDistributeRequiredError():
    '''returns MXException\n\n
    checkAndDistributeRequiredError(final MXException mxe)\n
    '''
def handleRequiredFieldException():
    '''returns None\n\n
    handleRequiredFieldException(MXRequiredFieldException requiredFieldException, final WebClientEvent event)\n
    '''
def checkForAppError():
    '''returns None\n\n
    checkForAppError()\n
    '''
def canCloseBean():
    '''returns boolean\n\n
    canCloseBean()\n
    '''
def hasSameMboSet():
    '''returns boolean\n\n
    hasSameMboSet(final DataBean bean)\n
    '''
def addDialogReference():
    '''returns None\n\n
    addDialogReference()\n
    '''
def removeDialogReference():
    '''returns None\n\n
    removeDialogReference()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getCurrentRow():
    '''returns int\n\n
    getCurrentRow()\n
    '''
def getDataAsArray():
    '''returns String[][]\n\n
    getDataAsArray()\n
    getDataAsArray(final String[] attributeNames)\n
    '''
def getSelectedDataAsArray():
    '''returns String[][]\n\n
    getSelectedDataAsArray()\n
    getSelectedDataAsArray(final String[] attributeNames)\n
    '''
def propagateRequired():
    '''returns None\n\n
    propagateRequired()\n
    '''
def retainPosition():
    '''returns None\n\n
    retainPosition()\n
    '''
def fetchTableData():
    '''returns int\n\n
    fetchTableData()\n
    '''
def hasLongDescriptionText():
    '''returns boolean\n\n
    hasLongDescriptionText(final int row, final String attribute)\n
    hasLongDescriptionText(final String attribute)\n
    '''
def toBeSaved():
    '''returns boolean\n\n
    toBeSaved()\n
    '''
def isRowDeleted():
    '''returns boolean\n\n
    isRowDeleted(int row)\n
    '''
def isModifiedRow():
    '''returns boolean\n\n
    isModifiedRow()\n
    isModifiedRow(int row)\n
    '''
def hasRow():
    '''returns boolean\n\n
    hasRow(final int row)\n
    '''
def isNewRow():
    '''returns boolean\n\n
    isNewRow()\n
    isNewRow(int row)\n
    '''
def valueBound():
    '''returns None\n\n
    valueBound(final HttpSessionBindingEvent event)\n
    '''
def valueUnbound():
    '''returns None\n\n
    valueUnbound(final HttpSessionBindingEvent event)\n
    '''
def isColumnSorted():
    '''returns int\n\n
    isColumnSorted(final String componentId)\n
    '''
def setShowDetails():
    '''returns None\n\n
    setShowDetails(final boolean b)\n
    '''
def setRemoveOnCancel():
    '''returns None\n\n
    setRemoveOnCancel(final int row)\n
    '''
def getLastFetchIndex():
    '''returns int\n\n
    getLastFetchIndex()\n
    '''
def getEndRow():
    '''returns int\n\n
    getEndRow()\n
    '''
def getCacheRowIndex():
    '''returns int\n\n
    getCacheRowIndex(final int rowDataBeanIndex)\n
    '''
def getMboRowIndex():
    '''returns int\n\n
    getMboRowIndex(final int tableRow)\n
    '''
def getPageStartIndex():
    '''returns int\n\n
    getPageStartIndex()\n
    '''
def getRowIndexFromEvent():
    '''returns int\n\n
    getRowIndexFromEvent(final WebClientEvent event)\n
    '''
def hasPageRows():
    '''returns boolean\n\n
    hasPageRows()\n
    '''
def removeRowOnCancel():
    '''returns boolean\n\n
    removeRowOnCancel(final int row)\n
    '''
def isTableRowSelected():
    '''returns boolean\n\n
    isTableRowSelected(final int row)\n
    '''
def getShowDetails():
    '''returns boolean\n\n
    getShowDetails()\n
    '''
def getPageEndRow():
    '''returns int\n\n
    getPageEndRow()\n
    '''
def getPageRowCount():
    '''returns int\n\n
    getPageRowCount()\n
    '''
def setfiltervalue():
    '''returns int\n\n
    setfiltervalue()\n
    '''
def applyValuesToSharedAttributes():
    '''returns None\n\n
    applyValuesToSharedAttributes(final ComponentInstance component, final String value)\n
    applyValuesToSharedAttributes(final ComponentInstance component)\n
    '''
def setValueFromComponent():
    '''returns None\n\n
    setValueFromComponent(final BoundComponentInstance changedComponent, final WebClientEvent event, String newValue)\n
    '''
def setvalue():
    '''returns int\n\n
    setvalue()\n
    '''
def refreshFieldErrors():
    '''returns None\n\n
    refreshFieldErrors()\n
    '''
def getNullRequiedFields():
    '''returns List<ERMAttributeError>\n\n
    getNullRequiedFields()\n
    '''
def displaycount():
    '''returns String\n\n
    displaycount()\n
    '''
def copytonewrow():
    '''returns int\n\n
    copytonewrow()\n
    '''
def addrow():
    '''returns int\n\n
    addrow()\n
    '''
def scrollnext():
    '''returns int\n\n
    scrollnext()\n
    '''
def scrollprev():
    '''returns int\n\n
    scrollprev()\n
    '''
def nextrow():
    '''returns int\n\n
    nextrow()\n
    '''
def prevrow():
    '''returns int\n\n
    prevrow()\n
    '''
def toggledetailstate():
    '''returns int\n\n
    toggledetailstate(final boolean open)\n
    '''
def toggledeleterow():
    '''returns int\n\n
    toggledeleterow()\n
    '''
def highlightrow():
    '''returns int\n\n
    highlightrow()\n
    highlightrow(final int row)\n
    '''
def toggleselectrow():
    '''returns int\n\n
    toggleselectrow()\n
    '''
def toggleselectallrows():
    '''returns int\n\n
    toggleselectallrows()\n
    '''
def sortcolumn():
    '''returns int\n\n
    sortcolumn()\n
    sortcolumn(final String sortString)\n
    '''
def instantdelete():
    '''returns int\n\n
    instantdelete()\n
    '''
def filterrows():
    '''returns int\n\n
    filterrows()\n
    '''
def clearfilter():
    '''returns int\n\n
    clearfilter()\n
    '''
def isTableStateFlagSet():
    '''returns boolean\n\n
    isTableStateFlagSet(final long flag)\n
    '''
def getTableStateFlags():
    '''returns BitFlag\n\n
    getTableStateFlags()\n
    '''
def selectrecord():
    '''returns int\n\n
    selectrecord()\n
    '''
def resetJSPFlags():
    '''returns None\n\n
    resetJSPFlags()\n
    '''
def getEventRowIndex():
    '''returns int\n\n
    getEventRowIndex()\n
    '''
def setEventRowIndex():
    '''returns None\n\n
    setEventRowIndex(final int i)\n
    '''
def getLastEventHandled():
    '''returns WebClientEvent\n\n
    getLastEventHandled()\n
    '''
def setLastEventHandled():
    '''returns None\n\n
    setLastEventHandled(final WebClientEvent event)\n
    '''
def setTableFlag():
    '''returns None\n\n
    setTableFlag(final long flag, final boolean value)\n
    '''
def callMethod():
    '''returns int\n\n
    callMethod(final WebClientEvent event)\n
    callMethod(final String methodName, final WebClientEvent event)\n
    callMethod(final WebClientEvent event, final Class<?>[] paramTypes, final Object[] params)\n
    callMethod(final String methodName, final WebClientEvent event, final Class<?>[] paramTypes, final Object[] params)\n
    '''
def findAndCallMethod():
    '''returns int\n\n
    findAndCallMethod(final WebClientEvent event, final DataBean datasrc, final String method, final Class<?>[] paramTypes, final Object[] params)\n
    '''
def callRemoteMethod():
    '''returns int\n\n
    callRemoteMethod(final String method)\n
    callRemoteMethod(final String method, final Class<?>[] paramTypes, final Object[] params)\n
    '''
def callBeanMethod():
    '''returns int\n\n
    callBeanMethod(final WebClientEvent event)\n
    callBeanMethod(final String method, final WebClientEvent event)\n
    callBeanMethod(final WebClientEvent event, final Class<?>[] paramTypes, final Object[] params)\n
    callBeanMethod(final String method, final WebClientEvent event, final Class<?>[] paramTypes, final Object[] params)\n
    '''
def getReturnAttribute():
    '''returns String\n\n
    getReturnAttribute()\n
    '''
def setReturnAttribute():
    '''returns None\n\n
    setReturnAttribute(final String string)\n
    '''
def getReturnControlId():
    '''returns String\n\n
    getReturnControlId()\n
    '''
def getReturnComponentId():
    '''returns String\n\n
    getReturnComponentId()\n
    '''
def setReturnControlId():
    '''returns None\n\n
    setReturnControlId(final String string)\n
    '''
def setReturnComponentId():
    '''returns None\n\n
    setReturnComponentId(final String id)\n
    '''
def setReturnComponent():
    '''returns None\n\n
    setReturnComponent(final ComponentInstance comp)\n
    '''
def getReturnComponent():
    '''returns ComponentInstance\n\n
    getReturnComponent()\n
    '''
def handleRemoteException():
    '''returns None\n\n
    handleRemoteException(final RemoteException e)\n
    '''
def turnEmptyStateOn():
    '''returns None\n\n
    turnEmptyStateOn()\n
    '''
def getMboForUniqueId():
    '''returns MboRemote\n\n
    getMboForUniqueId(final long uid)\n
    '''
def getUniqueIdValue():
    '''returns long\n\n
    getUniqueIdValue()\n
    '''
def getUniqueIdName():
    '''returns String\n\n
    getUniqueIdName()\n
    '''
def smartFill():
    '''returns MboSetRemote\n\n
    smartFill(final int row, final String attribute, final String value, final boolean exactMatch)\n
    smartFill(final String attribute, final String value, final boolean exactMatch)\n
    '''
def getUniqueIdFromSmartFill():
    '''returns long\n\n
    getUniqueIdFromSmartFill(final String attribute, final String value)\n
    getUniqueIdFromSmartFill(final String applicName, final String attribute, final String value)\n
    '''
def refreshTable():
    '''returns None\n\n
    refreshTable()\n
    '''
def reloadTable():
    '''returns None\n\n
    reloadTable()\n
    '''
def getSmartFillValue():
    '''returns String\n\n
    getSmartFillValue()\n
    '''
def setSmartFillValue():
    '''returns None\n\n
    setSmartFillValue(final String smartFillValue)\n
    '''
def cancelDialog():
    '''returns int\n\n
    cancelDialog()\n
    '''
def getDescAttributeId():
    '''returns String\n\n
    getDescAttributeId()\n
    '''
def setDescAttributeId():
    '''returns None\n\n
    setDescAttributeId(final String string)\n
    '''
def setPageRowCount():
    '''returns None\n\n
    setPageRowCount(final int rowCount)\n
    '''
def _useAllRecsQuery():
    '''returns int\n\n
    _useAllRecsQuery()\n
    '''
def useAllRecsQuery():
    '''returns int\n\n
    useAllRecsQuery()\n
    '''
def _useAllBookmarksQuery():
    '''returns int\n\n
    _useAllBookmarksQuery()\n
    '''
def useAllBookmarksQuery():
    '''returns int\n\n
    useAllBookmarksQuery()\n
    '''
def _usequery():
    '''returns int\n\n
    _usequery()\n
    '''
def usequery():
    '''returns int\n\n
    usequery()\n
    '''
def useQuery():
    '''returns None\n\n
    useQuery(final String queryName)\n
    '''
def sqlwhere():
    '''returns int\n\n
    sqlwhere()\n
    '''
def useqbe():
    '''returns int\n\n
    useqbe()\n
    '''
def queryAllRecs():
    '''returns None\n\n
    queryAllRecs()\n
    '''
def queryAllBookmarks():
    '''returns None\n\n
    queryAllBookmarks()\n
    '''
def getCurrentQueryName():
    '''returns String\n\n
    getCurrentQueryName()\n
    '''
def clearBean():
    '''returns None\n\n
    clearBean()\n
    '''
def setQueryBySiteQbe():
    '''returns None\n\n
    setQueryBySiteQbe()\n
    '''
def getWarnings():
    '''returns MXException[]\n\n
    getWarnings()\n
    '''
def moveToMboFromDataBean():
    '''returns boolean\n\n
    moveToMboFromDataBean(final DataBean dataBean, final String dataAttribute)\n
    '''
def hierarchicalmove():
    '''returns int\n\n
    hierarchicalmove()\n
    '''
def getTableOffset():
    '''returns int\n\n
    getTableOffset()\n
    '''
def getSortOrder():
    '''returns String\n\n
    getSortOrder(final String sortAttribute)\n
    '''
def addSigOption():
    '''returns None\n\n
    addSigOption(final String sigoption)\n
    '''
def addConditionalProperties():
    '''returns None\n\n
    addConditionalProperties(final String sigOption, final int row, final HashMap<String, String> properties)\n
    '''
def hasSigOptionAccess():
    '''returns boolean\n\n
    hasSigOptionAccess(final String sigOption)\n
    hasSigOptionAccess(final int row, final String sigOption)\n
    '''
def getMboSetFromSmartFind():
    '''returns MboSetRemote\n\n
    getMboSetFromSmartFind(final int row, final String attribute)\n
    getMboSetFromSmartFind(final String attribute)\n
    getMboSetFromSmartFind(final String app, final String attribute)\n
    '''
def canFetchData():
    '''returns boolean\n\n
    canFetchData()\n
    '''
def getRemoteForDownload():
    '''returns MboSetRemote\n\n
    getRemoteForDownload()\n
    '''
def isSubSelect():
    '''returns boolean\n\n
    isSubSelect()\n
    '''
def setDynamicAppDefaults():
    '''returns None\n\n
    setDynamicAppDefaults(final MboRemote mbo)\n
    '''
def setDynamicDefault():
    '''returns None\n\n
    setDynamicDefault(final String attribute, final DataBean frmDataBean, final String frmAttribute, final String defaultType)\n
    '''
def changeRequiredField():
    '''returns boolean\n\n
    changeRequiredField(int row, String attribute, final boolean required)\n
    '''
def getQueryNameBeforeReviseAction():
    '''returns String\n\n
    getQueryNameBeforeReviseAction()\n
    '''
def setQueryNameBeforeReviseAction():
    '''returns None\n\n
    setQueryNameBeforeReviseAction(final String queryName)\n
    '''
def getQueryDescBeforeReviseAction():
    '''returns String\n\n
    getQueryDescBeforeReviseAction()\n
    '''
def setQueryDescBeforeReviseAction():
    '''returns None\n\n
    setQueryDescBeforeReviseAction(final String queryDesc)\n
    '''
def setEmptyOnClear():
    '''returns None\n\n
    setEmptyOnClear(final boolean emptyOnClear)\n
    '''
def asyncLocked():
    '''returns boolean\n\n
    asyncLocked()\n
    '''
def setAsyncLock():
    '''returns None\n\n
    setAsyncLock(final boolean asyncLock)\n
    '''
def madeRequiredConditionally():
    '''returns boolean\n\n
    madeRequiredConditionally(String attribute)\n
    '''
def isListTableModified():
    '''returns boolean\n\n
    isListTableModified()\n
    '''
def setListTableModified():
    '''returns None\n\n
    setListTableModified(final boolean inChange)\n
    '''
def isListTableRetain():
    '''returns boolean\n\n
    isListTableRetain()\n
    '''
def setListTableRetain():
    '''returns None\n\n
    setListTableRetain(final boolean inRetain)\n
    '''
def getCurrentQueryDescription():
    '''returns String\n\n
    getCurrentQueryDescription()\n
    '''
def setCurrentQueryDescription():
    '''returns None\n\n
    setCurrentQueryDescription(final String queryDescription)\n
    '''
def boundToTable():
    '''returns boolean\n\n
    boundToTable()\n
    '''
def setApplicationError():
    '''returns None\n\n
    setApplicationError(final String dataAttribute, int row, final ApplicationError error)\n
    '''
def buildPortalMsg():
    '''returns String\n\n
    buildPortalMsg(final String attribute, final String newValue)\n
    '''
def rePosition():
    '''returns boolean\n\n
    rePosition()\n
    '''
def isAppTableRetain():
    '''returns boolean\n\n
    isAppTableRetain()\n
    '''
def positionState():
    '''returns None\n\n
    positionState()\n
    '''
def markTablePosition():
    '''returns None\n\n
    markTablePosition(final boolean inFlg)\n
    '''
def isTablePostionMarked():
    '''returns boolean\n\n
    isTablePostionMarked()\n
    '''
def getUIERMEntity():
    '''returns UIERMEntity\n\n
    getUIERMEntity()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def registerDynamicControlsWithERM():
    '''returns None\n\n
    registerDynamicControlsWithERM(final List<ControlInstance> controls)\n
    '''
def getLockedByDisplayName():
    '''returns String\n\n
    getLockedByDisplayName(final int row)\n
    '''
def isRowLocked():
    '''returns boolean\n\n
    isRowLocked(final int row)\n
    '''
def isLookupMultiSelect():
    '''returns boolean\n\n
    isLookupMultiSelect(final BoundComponentInstance boundComponentInstance, final boolean isQueryInput)\n
    '''
def getParentRelationship():
    '''returns String\n\n
    getParentRelationship()\n
    '''
