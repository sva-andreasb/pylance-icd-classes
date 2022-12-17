LeftMargin = "short  0"
RightMargin = "short  1"
TopMargin = "short  2"
BottomMargin = "short  3"
PANE_LOWER_RIGHT = "byte  0"
PANE_UPPER_RIGHT = "byte  1"
PANE_LOWER_LEFT = "byte  2"
PANE_UPPER_LEFT = "byte  3"
def visitRecord():
    '''returns None\n\n
    visitRecord(final Record r)\n
    visitRecord(final Record r)\n
    '''
def cloneSheet():
    '''returns InternalSheet\n\n
    cloneSheet()\n
    '''
def getRowsAggregate():
    '''returns RowRecordsAggregate\n\n
    getRowsAggregate()\n
    '''
def updateFormulasAfterCellShift():
    '''returns None\n\n
    updateFormulasAfterCellShift(final FormulaShifter shifter, final int externSheetIndex)\n
    '''
def addMergedRegion():
    '''returns int\n\n
    addMergedRegion(final int rowFrom, final int colFrom, final int rowTo, final int colTo)\n
    '''
def removeMergedRegion():
    '''returns None\n\n
    removeMergedRegion(final int index)\n
    '''
def getMergedRegionAt():
    '''returns CellRangeAddress\n\n
    getMergedRegionAt(final int index)\n
    '''
def getNumMergedRegions():
    '''returns int\n\n
    getNumMergedRegions()\n
    '''
def getConditionalFormattingTable():
    '''returns ConditionalFormattingTable\n\n
    getConditionalFormattingTable()\n
    '''
def setDimensions():
    '''returns None\n\n
    setDimensions(final int firstrow, final short firstcol, final int lastrow, final short lastcol)\n
    '''
def visitContainedRecords():
    '''returns None\n\n
    visitContainedRecords(final RecordAggregate.RecordVisitor rv, final int offset)\n
    '''
def addValueRecord():
    '''returns None\n\n
    addValueRecord(final int row, final CellValueRecordInterface col)\n
    '''
def removeValueRecord():
    '''returns None\n\n
    removeValueRecord(final int row, final CellValueRecordInterface col)\n
    '''
def replaceValueRecord():
    '''returns None\n\n
    replaceValueRecord(final CellValueRecordInterface newval)\n
    '''
def addRow():
    '''returns None\n\n
    addRow(final RowRecord row)\n
    '''
def removeRow():
    '''returns None\n\n
    removeRow(final RowRecord row)\n
    '''
def getCellValueIterator():
    '''returns Iterator<CellValueRecordInterface>\n\n
    getCellValueIterator()\n
    '''
def getNextRow():
    '''returns RowRecord\n\n
    getNextRow()\n
    '''
def getRow():
    '''returns RowRecord\n\n
    getRow(final int rownum)\n
    '''
def getDefaultColumnWidth():
    '''returns int\n\n
    getDefaultColumnWidth()\n
    '''
def isGridsPrinted():
    '''returns boolean\n\n
    isGridsPrinted()\n
    '''
def setGridsPrinted():
    '''returns None\n\n
    setGridsPrinted(final boolean value)\n
    '''
def setDefaultColumnWidth():
    '''returns None\n\n
    setDefaultColumnWidth(final int dcw)\n
    '''
def setDefaultRowHeight():
    '''returns None\n\n
    setDefaultRowHeight(final short dch)\n
    '''
def getDefaultRowHeight():
    '''returns short\n\n
    getDefaultRowHeight()\n
    '''
def getColumnWidth():
    '''returns int\n\n
    getColumnWidth(final int columnIndex)\n
    '''
def getXFIndexForColAt():
    '''returns short\n\n
    getXFIndexForColAt(final short columnIndex)\n
    '''
def setColumnWidth():
    '''returns None\n\n
    setColumnWidth(final int column, final int width)\n
    '''
def isColumnHidden():
    '''returns boolean\n\n
    isColumnHidden(final int columnIndex)\n
    '''
def setColumnHidden():
    '''returns None\n\n
    setColumnHidden(final int column, final boolean hidden)\n
    '''
def setDefaultColumnStyle():
    '''returns None\n\n
    setDefaultColumnStyle(final int column, final int styleIndex)\n
    '''
def groupColumnRange():
    '''returns None\n\n
    groupColumnRange(final int fromColumn, final int toColumn, final boolean indent)\n
    '''
def getTopRow():
    '''returns short\n\n
    getTopRow()\n
    '''
def setTopRow():
    '''returns None\n\n
    setTopRow(final short topRow)\n
    '''
def setLeftCol():
    '''returns None\n\n
    setLeftCol(final short leftCol)\n
    '''
def getLeftCol():
    '''returns short\n\n
    getLeftCol()\n
    '''
def getActiveCellRow():
    '''returns int\n\n
    getActiveCellRow()\n
    '''
def setActiveCellRow():
    '''returns None\n\n
    setActiveCellRow(final int row)\n
    '''
def getActiveCellCol():
    '''returns short\n\n
    getActiveCellCol()\n
    '''
def setActiveCellCol():
    '''returns None\n\n
    setActiveCellCol(final short col)\n
    '''
def getRecords():
    '''returns List<RecordBase>\n\n
    getRecords()\n
    '''
def getGridsetRecord():
    '''returns GridsetRecord\n\n
    getGridsetRecord()\n
    '''
def findFirstRecordBySid():
    '''returns Record\n\n
    findFirstRecordBySid(final short sid)\n
    '''
def setSCLRecord():
    '''returns None\n\n
    setSCLRecord(final SCLRecord sclRecord)\n
    '''
def findFirstRecordLocBySid():
    '''returns int\n\n
    findFirstRecordLocBySid(final short sid)\n
    '''
def getWindowTwo():
    '''returns WindowTwoRecord\n\n
    getWindowTwo()\n
    '''
def getPrintGridlines():
    '''returns PrintGridlinesRecord\n\n
    getPrintGridlines()\n
    '''
def setPrintGridlines():
    '''returns None\n\n
    setPrintGridlines(final PrintGridlinesRecord newPrintGridlines)\n
    '''
def getPrintHeaders():
    '''returns PrintHeadersRecord\n\n
    getPrintHeaders()\n
    '''
def setPrintHeaders():
    '''returns None\n\n
    setPrintHeaders(final PrintHeadersRecord newPrintHeaders)\n
    '''
def setSelected():
    '''returns None\n\n
    setSelected(final boolean sel)\n
    '''
def createFreezePane():
    '''returns None\n\n
    createFreezePane(final int colSplit, final int rowSplit, final int topRow, final int leftmostColumn)\n
    '''
def createSplitPane():
    '''returns None\n\n
    createSplitPane(final int xSplitPos, final int ySplitPos, final int topRow, final int leftmostColumn, final int activePane)\n
    '''
def getPaneInformation():
    '''returns PaneInformation\n\n
    getPaneInformation()\n
    '''
def getSelection():
    '''returns SelectionRecord\n\n
    getSelection()\n
    '''
def setSelection():
    '''returns None\n\n
    setSelection(final SelectionRecord selection)\n
    '''
def getProtectionBlock():
    '''returns WorksheetProtectionBlock\n\n
    getProtectionBlock()\n
    '''
def setDisplayGridlines():
    '''returns None\n\n
    setDisplayGridlines(final boolean show)\n
    '''
def isDisplayGridlines():
    '''returns boolean\n\n
    isDisplayGridlines()\n
    '''
def setDisplayFormulas():
    '''returns None\n\n
    setDisplayFormulas(final boolean show)\n
    '''
def isDisplayFormulas():
    '''returns boolean\n\n
    isDisplayFormulas()\n
    '''
def setDisplayRowColHeadings():
    '''returns None\n\n
    setDisplayRowColHeadings(final boolean show)\n
    '''
def isDisplayRowColHeadings():
    '''returns boolean\n\n
    isDisplayRowColHeadings()\n
    '''
def setPrintRowColHeadings():
    '''returns None\n\n
    setPrintRowColHeadings(final boolean show)\n
    '''
def isPrintRowColHeadings():
    '''returns boolean\n\n
    isPrintRowColHeadings()\n
    '''
def getUncalced():
    '''returns boolean\n\n
    getUncalced()\n
    '''
def setUncalced():
    '''returns None\n\n
    setUncalced(final boolean uncalced)\n
    '''
def aggregateDrawingRecords():
    '''returns int\n\n
    aggregateDrawingRecords(final DrawingManager2 drawingManager, final boolean createIfMissing)\n
    '''
def preSerialize():
    '''returns None\n\n
    preSerialize()\n
    '''
def getPageSettings():
    '''returns PageSettingsBlock\n\n
    getPageSettings()\n
    '''
def setColumnGroupCollapsed():
    '''returns None\n\n
    setColumnGroupCollapsed(final int columnNumber, final boolean collapsed)\n
    '''
def groupRowRange():
    '''returns None\n\n
    groupRowRange(final int fromRow, final int toRow, final boolean indent)\n
    '''
def getOrCreateDataValidityTable():
    '''returns DataValidityTable\n\n
    getOrCreateDataValidityTable()\n
    '''
def getNoteRecords():
    '''returns NoteRecord[]\n\n
    getNoteRecords()\n
    '''
def getColumnOutlineLevel():
    '''returns int\n\n
    getColumnOutlineLevel(final int columnIndex)\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def ():
    '''returns RecordCloner\n\n
    (final List<Record> destList)\n
    '''
