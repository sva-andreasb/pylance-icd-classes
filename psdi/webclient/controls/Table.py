def Table():
    '''public Table()
    '''
def initialize():
    '''public void initialize()
    '''
def getHideSelectRows():
    '''public boolean getHideSelectRows()
    '''
def setHideSelectRows():
    '''public void setHideSelectRows(final boolean hide)
    '''
def getMultiple():
    '''public boolean getMultiple()
    '''
def addSelectAllRowControl():
    '''public void addSelectAllRowControl(final ControlInstance selectRow)
    '''
def addSelectRowControl():
    '''public void addSelectRowControl(final ControlInstance selectRow)
    '''
def setBody():
    '''public void setBody(final TableBody body)
    '''
def getBody():
    '''public TableBody getBody()
    '''
def getFlagValue():
    '''public boolean getFlagValue(final int flag)
    '''
def needsRefresh():
    '''public Object needsRefresh()
    '''
def isExpanded():
    '''public Object isExpanded()
    '''
def isFilterOpen():
    '''public Object isFilterOpen()
    '''
def isFilterable():
    '''public Object isFilterable()
    '''
def canDownload():
    '''public Object canDownload()
    '''
def moreRowsBefore():
    '''public String moreRowsBefore()
    '''
def moreRowsAfter():
    '''public String moreRowsAfter()
    '''
def morePagesBefore():
    '''public String morePagesBefore()
    '''
def morePagesAfter():
    '''public String morePagesAfter()
    '''
def isFiltered():
    '''public String isFiltered()
    '''
def isDetailsExpanded():
    '''public String isDetailsExpanded()
    '''
def isTableStartEmpty():
    '''public String isTableStartEmpty()
    '''
def isTableAllSelected():
    '''public String isTableAllSelected()
    '''
def isTableSelectRowsOpen():
    '''public String isTableSelectRowsOpen()
    '''
def getCurrentRow():
    '''public int getCurrentRow()
    '''
def setOldCurrentRow():
    '''public void setOldCurrentRow(final int row)
    '''
def getOldCurrentRow():
    '''public int getOldCurrentRow()
    '''
def setCurrentRow():
    '''public int setCurrentRow(final int row)
    '''
def togglefilter():
    '''public int togglefilter()
    '''
def defaultRowFocus():
    '''public void defaultRowFocus(final int row)
    '''
def setDefaultFocus():
    '''public void setDefaultFocus()
    public void setDefaultFocus(final int row)
    '''
def defaultDetailFocus():
    '''public void defaultDetailFocus()
    '''
def toggledetails():
    '''public int toggledetails(final boolean expanded)
    public int toggledetails(final boolean expanded, final boolean setFocus)
    '''
def getDetails():
    '''public ControlInstance getDetails()
    '''
def getExpandedRow():
    '''public int getExpandedRow()
    '''
def setExpandedRow():
    '''public int setExpandedRow(final int row)
    '''
def filtertable():
    '''public int filtertable()
    '''
def clearfilter():
    '''public int clearfilter()
    '''
def columnFocus():
    '''public void columnFocus()
    '''
def noRowFocus():
    '''public void noRowFocus()
    '''
def setFocusedCellId():
    '''public void setFocusedCellId(final String id)
    '''
def previousrow():
    '''public int previousrow()
    '''
def nextrow():
    '''public int nextrow()
    '''
def previouspage():
    '''public int previouspage()
    '''
def nextpage():
    '''public int nextpage()
    '''
def tablehelp():
    '''public int tablehelp()
    '''
def togglecollapse():
    '''public int togglecollapse()
    '''
def toggleselectallrows():
    '''public int toggleselectallrows()
    '''
def toggleselectrecords():
    '''public int toggleselectrecords()
    '''
def getRowSelectVis():
    '''public boolean getRowSelectVis()
    '''
def wasTableFilterStateChanged():
    '''public boolean wasTableFilterStateChanged()
    '''
def wasTableDetailStateChanged():
    '''public boolean wasTableDetailStateChanged()
    '''
def wasTableCollapseStateChanged():
    '''public boolean wasTableCollapseStateChanged()
    '''
def wasTableFilterCleared():
    '''public boolean wasTableFilterCleared()
    '''
def wasTableRowChanged():
    '''public boolean wasTableRowChanged()
    '''
def rowChanged():
    '''public boolean rowChanged()
    '''
def wasTablePageChanged():
    '''public boolean wasTablePageChanged()
    '''
def shouldTableShowHelp():
    '''public boolean shouldTableShowHelp()
    '''
def wasTableSelectRowStateChanged():
    '''public boolean wasTableSelectRowStateChanged()
    '''
def setHasDetails():
    '''public void setHasDetails(final boolean hasDetails)
    '''
def dataChangedEvent():
    '''public void dataChangedEvent(final DataBean bean)
    '''
def structureChangedEvent():
    '''public void structureChangedEvent(final DataBean bean)
    '''
def render():
    '''public int render()
    '''
def preRender():
    '''public boolean preRender()
    '''
def resetPreRender():
    '''public void resetPreRender()
    '''
def isLastColumn():
    '''public boolean isLastColumn(final String colId)
    '''
def getColumnId():
    '''public String getColumnId(final int colNum)
    '''
def getColumnCount():
    '''public int getColumnCount()
    '''
def sortColumn():
    '''public void sortColumn()
    '''
def getSortLevel():
    '''public String getSortLevel(final String sortAttribute)
    '''
def getSortOrder():
    '''public String getSortOrder(String sortAttribute)
    '''
def getRowControl():
    '''public TableDataRow getRowControl()
    '''
def increaseFilters():
    '''public void increaseFilters()
    '''
def getFilterCount():
    '''public int getFilterCount()
    '''
def getTableDownloadSheetName():
    '''public String getTableDownloadSheetName()
    '''
def addrow():
    '''public int addrow()
    '''
def showMXException():
    '''public void showMXException(final MXException mxe)
    '''
def showRemoteException():
    '''public void showRemoteException(final RemoteException rme)
    '''
def forceFocusRow():
    '''public void forceFocusRow(final String row)
    public void forceFocusRow(final int row)
    '''
def setFilterRow():
    '''public void setFilterRow(final TableFilterRow tableFilterRow)
    '''
def getFilterRow():
    '''public TableFilterRow getFilterRow()
    '''
def useNPMbo():
    '''public boolean useNPMbo()
    '''
def isListTabRetain():
    '''public boolean isListTabRetain()
    '''
def errorLevelChanged():
    '''public boolean errorLevelChanged()
    '''
def childHasError():
    '''public void childHasError(final BoundComponentInstance childWithError, final SetValueError newError)
    '''
def getErrorLevelForRow():
    '''public int getErrorLevelForRow(final int row)
    '''
def getErrorLevel():
    '''public int getErrorLevel()
    '''
def clearErrors():
    '''public void clearErrors()
    '''
def resetNewRowNum():
    '''public void resetNewRowNum()
    '''
def getNewRowNum():
    '''public int getNewRowNum()
    '''
def reset():
    '''public int reset()
    '''
def selectmockedrecord():
    '''public void selectmockedrecord()
    '''
def maintainControlId():
    '''public boolean maintainControlId()
    '''
def createRenderId():
    '''public String createRenderId(final String id, final PageInstance page)
    '''
def isOnTable():
    '''public boolean isOnTable()
    '''
