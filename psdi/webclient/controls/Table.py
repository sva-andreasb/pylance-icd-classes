def ():
    '''returns Table\n\n
    ()\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def getHideSelectRows():
    '''returns boolean\n\n
    getHideSelectRows()\n
    '''
def setHideSelectRows():
    '''returns None\n\n
    setHideSelectRows(final boolean hide)\n
    '''
def getMultiple():
    '''returns boolean\n\n
    getMultiple()\n
    '''
def addSelectAllRowControl():
    '''returns None\n\n
    addSelectAllRowControl(final ControlInstance selectRow)\n
    '''
def addSelectRowControl():
    '''returns None\n\n
    addSelectRowControl(final ControlInstance selectRow)\n
    '''
def setBody():
    '''returns None\n\n
    setBody(final TableBody body)\n
    '''
def getBody():
    '''returns TableBody\n\n
    getBody()\n
    '''
def getFlagValue():
    '''returns boolean\n\n
    getFlagValue(final int flag)\n
    '''
def needsRefresh():
    '''returns Object\n\n
    needsRefresh()\n
    '''
def isExpanded():
    '''returns Object\n\n
    isExpanded()\n
    '''
def isFilterOpen():
    '''returns Object\n\n
    isFilterOpen()\n
    '''
def isFilterable():
    '''returns Object\n\n
    isFilterable()\n
    '''
def canDownload():
    '''returns Object\n\n
    canDownload()\n
    '''
def moreRowsBefore():
    '''returns String\n\n
    moreRowsBefore()\n
    '''
def moreRowsAfter():
    '''returns String\n\n
    moreRowsAfter()\n
    '''
def morePagesBefore():
    '''returns String\n\n
    morePagesBefore()\n
    '''
def morePagesAfter():
    '''returns String\n\n
    morePagesAfter()\n
    '''
def isFiltered():
    '''returns String\n\n
    isFiltered()\n
    '''
def isDetailsExpanded():
    '''returns String\n\n
    isDetailsExpanded()\n
    '''
def isTableStartEmpty():
    '''returns String\n\n
    isTableStartEmpty()\n
    '''
def isTableAllSelected():
    '''returns String\n\n
    isTableAllSelected()\n
    '''
def isTableSelectRowsOpen():
    '''returns String\n\n
    isTableSelectRowsOpen()\n
    '''
def getCurrentRow():
    '''returns int\n\n
    getCurrentRow()\n
    '''
def setOldCurrentRow():
    '''returns None\n\n
    setOldCurrentRow(final int row)\n
    '''
def getOldCurrentRow():
    '''returns int\n\n
    getOldCurrentRow()\n
    '''
def setCurrentRow():
    '''returns int\n\n
    setCurrentRow(final int row)\n
    '''
def togglefilter():
    '''returns int\n\n
    togglefilter()\n
    '''
def defaultRowFocus():
    '''returns None\n\n
    defaultRowFocus(final int row)\n
    '''
def setDefaultFocus():
    '''returns None\n\n
    setDefaultFocus()\n
    setDefaultFocus(final int row)\n
    '''
def defaultDetailFocus():
    '''returns None\n\n
    defaultDetailFocus()\n
    '''
def toggledetails():
    '''returns int\n\n
    toggledetails(final boolean expanded)\n
    toggledetails(final boolean expanded, final boolean setFocus)\n
    '''
def getDetails():
    '''returns ControlInstance\n\n
    getDetails()\n
    '''
def getExpandedRow():
    '''returns int\n\n
    getExpandedRow()\n
    '''
def setExpandedRow():
    '''returns int\n\n
    setExpandedRow(final int row)\n
    '''
def filtertable():
    '''returns int\n\n
    filtertable()\n
    '''
def clearfilter():
    '''returns int\n\n
    clearfilter()\n
    '''
def columnFocus():
    '''returns None\n\n
    columnFocus()\n
    '''
def noRowFocus():
    '''returns None\n\n
    noRowFocus()\n
    '''
def setFocusedCellId():
    '''returns None\n\n
    setFocusedCellId(final String id)\n
    '''
def previousrow():
    '''returns int\n\n
    previousrow()\n
    '''
def nextrow():
    '''returns int\n\n
    nextrow()\n
    '''
def previouspage():
    '''returns int\n\n
    previouspage()\n
    '''
def nextpage():
    '''returns int\n\n
    nextpage()\n
    '''
def tablehelp():
    '''returns int\n\n
    tablehelp()\n
    '''
def togglecollapse():
    '''returns int\n\n
    togglecollapse()\n
    '''
def toggleselectallrows():
    '''returns int\n\n
    toggleselectallrows()\n
    '''
def toggleselectrecords():
    '''returns int\n\n
    toggleselectrecords()\n
    '''
def getRowSelectVis():
    '''returns boolean\n\n
    getRowSelectVis()\n
    '''
def wasTableFilterStateChanged():
    '''returns boolean\n\n
    wasTableFilterStateChanged()\n
    '''
def wasTableDetailStateChanged():
    '''returns boolean\n\n
    wasTableDetailStateChanged()\n
    '''
def wasTableCollapseStateChanged():
    '''returns boolean\n\n
    wasTableCollapseStateChanged()\n
    '''
def wasTableFilterCleared():
    '''returns boolean\n\n
    wasTableFilterCleared()\n
    '''
def wasTableRowChanged():
    '''returns boolean\n\n
    wasTableRowChanged()\n
    '''
def rowChanged():
    '''returns boolean\n\n
    rowChanged()\n
    '''
def wasTablePageChanged():
    '''returns boolean\n\n
    wasTablePageChanged()\n
    '''
def shouldTableShowHelp():
    '''returns boolean\n\n
    shouldTableShowHelp()\n
    '''
def wasTableSelectRowStateChanged():
    '''returns boolean\n\n
    wasTableSelectRowStateChanged()\n
    '''
def setHasDetails():
    '''returns None\n\n
    setHasDetails(final boolean hasDetails)\n
    '''
def dataChangedEvent():
    '''returns None\n\n
    dataChangedEvent(final DataBean bean)\n
    '''
def structureChangedEvent():
    '''returns None\n\n
    structureChangedEvent(final DataBean bean)\n
    '''
def render():
    '''returns int\n\n
    render()\n
    '''
def preRender():
    '''returns boolean\n\n
    preRender()\n
    '''
def resetPreRender():
    '''returns None\n\n
    resetPreRender()\n
    '''
def isLastColumn():
    '''returns boolean\n\n
    isLastColumn(final String colId)\n
    '''
def getColumnId():
    '''returns String\n\n
    getColumnId(final int colNum)\n
    '''
def getColumnCount():
    '''returns int\n\n
    getColumnCount()\n
    '''
def sortColumn():
    '''returns None\n\n
    sortColumn()\n
    '''
def getSortLevel():
    '''returns String\n\n
    getSortLevel(final String sortAttribute)\n
    '''
def getSortOrder():
    '''returns String\n\n
    getSortOrder(String sortAttribute)\n
    '''
def getRowControl():
    '''returns TableDataRow\n\n
    getRowControl()\n
    '''
def increaseFilters():
    '''returns None\n\n
    increaseFilters()\n
    '''
def getFilterCount():
    '''returns int\n\n
    getFilterCount()\n
    '''
def getTableDownloadSheetName():
    '''returns String\n\n
    getTableDownloadSheetName()\n
    '''
def addrow():
    '''returns int\n\n
    addrow()\n
    '''
def showMXException():
    '''returns None\n\n
    showMXException(final MXException mxe)\n
    '''
def showRemoteException():
    '''returns None\n\n
    showRemoteException(final RemoteException rme)\n
    '''
def forceFocusRow():
    '''returns None\n\n
    forceFocusRow(final String row)\n
    forceFocusRow(final int row)\n
    '''
def setFilterRow():
    '''returns None\n\n
    setFilterRow(final TableFilterRow tableFilterRow)\n
    '''
def getFilterRow():
    '''returns TableFilterRow\n\n
    getFilterRow()\n
    '''
def useNPMbo():
    '''returns boolean\n\n
    useNPMbo()\n
    '''
def isListTabRetain():
    '''returns boolean\n\n
    isListTabRetain()\n
    '''
def errorLevelChanged():
    '''returns boolean\n\n
    errorLevelChanged()\n
    '''
def childHasError():
    '''returns None\n\n
    childHasError(final BoundComponentInstance childWithError, final SetValueError newError)\n
    '''
def getErrorLevelForRow():
    '''returns int\n\n
    getErrorLevelForRow(final int row)\n
    '''
def getErrorLevel():
    '''returns int\n\n
    getErrorLevel()\n
    '''
def clearErrors():
    '''returns None\n\n
    clearErrors()\n
    '''
def resetNewRowNum():
    '''returns None\n\n
    resetNewRowNum()\n
    '''
def getNewRowNum():
    '''returns int\n\n
    getNewRowNum()\n
    '''
def reset():
    '''returns int\n\n
    reset()\n
    '''
def selectmockedrecord():
    '''returns None\n\n
    selectmockedrecord()\n
    '''
def maintainControlId():
    '''returns boolean\n\n
    maintainControlId()\n
    '''
def createRenderId():
    '''returns String\n\n
    createRenderId(final String id, final PageInstance page)\n
    '''
def isOnTable():
    '''returns boolean\n\n
    isOnTable()\n
    '''
