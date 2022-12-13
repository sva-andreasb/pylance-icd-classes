LeftMargin = "short  0"
RightMargin = "short  1"
TopMargin = "short  2"
BottomMargin = "short  3"
PANE_LOWER_RIGHT = "byte  0"
PANE_UPPER_RIGHT = "byte  1"
PANE_LOWER_LEFT = "byte  2"
PANE_UPPER_LEFT = "byte  3"
def createSheet():
'''public static InternalSheet createSheet(final RecordStream rs)
public static InternalSheet createSheet()
'''
pass
def visitRecord():
'''public void visitRecord(final Record r)
public void visitRecord(final Record r)
'''
pass
def cloneSheet():
'''public InternalSheet cloneSheet()
'''
pass
def getRowsAggregate():
'''public RowRecordsAggregate getRowsAggregate()
'''
pass
def updateFormulasAfterCellShift():
'''public void updateFormulasAfterCellShift(final FormulaShifter shifter, final int externSheetIndex)
'''
pass
def addMergedRegion():
'''public int addMergedRegion(final int rowFrom, final int colFrom, final int rowTo, final int colTo)
'''
pass
def removeMergedRegion():
'''public void removeMergedRegion(final int index)
'''
pass
def getMergedRegionAt():
'''public CellRangeAddress getMergedRegionAt(final int index)
'''
pass
def getNumMergedRegions():
'''public int getNumMergedRegions()
'''
pass
def getConditionalFormattingTable():
'''public ConditionalFormattingTable getConditionalFormattingTable()
'''
pass
def setDimensions():
'''public void setDimensions(final int firstrow, final short firstcol, final int lastrow, final short lastcol)
'''
pass
def visitContainedRecords():
'''public void visitContainedRecords(final RecordAggregate.RecordVisitor rv, final int offset)
'''
pass
def addValueRecord():
'''public void addValueRecord(final int row, final CellValueRecordInterface col)
'''
pass
def removeValueRecord():
'''public void removeValueRecord(final int row, final CellValueRecordInterface col)
'''
pass
def replaceValueRecord():
'''public void replaceValueRecord(final CellValueRecordInterface newval)
'''
pass
def addRow():
'''public void addRow(final RowRecord row)
'''
pass
def removeRow():
'''public void removeRow(final RowRecord row)
'''
pass
def getCellValueIterator():
'''public Iterator<CellValueRecordInterface> getCellValueIterator()
'''
pass
def getNextRow():
'''public RowRecord getNextRow()
'''
pass
def getRow():
'''public RowRecord getRow(final int rownum)
'''
pass
def getDefaultColumnWidth():
'''public int getDefaultColumnWidth()
'''
pass
def isGridsPrinted():
'''public boolean isGridsPrinted()
'''
pass
def setGridsPrinted():
'''public void setGridsPrinted(final boolean value)
'''
pass
def setDefaultColumnWidth():
'''public void setDefaultColumnWidth(final int dcw)
'''
pass
def setDefaultRowHeight():
'''public void setDefaultRowHeight(final short dch)
'''
pass
def getDefaultRowHeight():
'''public short getDefaultRowHeight()
'''
pass
def getColumnWidth():
'''public int getColumnWidth(final int columnIndex)
'''
pass
def getXFIndexForColAt():
'''public short getXFIndexForColAt(final short columnIndex)
'''
pass
def setColumnWidth():
'''public void setColumnWidth(final int column, final int width)
'''
pass
def isColumnHidden():
'''public boolean isColumnHidden(final int columnIndex)
'''
pass
def setColumnHidden():
'''public void setColumnHidden(final int column, final boolean hidden)
'''
pass
def setDefaultColumnStyle():
'''public void setDefaultColumnStyle(final int column, final int styleIndex)
'''
pass
def groupColumnRange():
'''public void groupColumnRange(final int fromColumn, final int toColumn, final boolean indent)
'''
pass
def getTopRow():
'''public short getTopRow()
'''
pass
def setTopRow():
'''public void setTopRow(final short topRow)
'''
pass
def setLeftCol():
'''public void setLeftCol(final short leftCol)
'''
pass
def getLeftCol():
'''public short getLeftCol()
'''
pass
def getActiveCellRow():
'''public int getActiveCellRow()
'''
pass
def setActiveCellRow():
'''public void setActiveCellRow(final int row)
'''
pass
def getActiveCellCol():
'''public short getActiveCellCol()
'''
pass
def setActiveCellCol():
'''public void setActiveCellCol(final short col)
'''
pass
def getRecords():
'''public List<RecordBase> getRecords()
'''
pass
def getGridsetRecord():
'''public GridsetRecord getGridsetRecord()
'''
pass
def findFirstRecordBySid():
'''public Record findFirstRecordBySid(final short sid)
'''
pass
def setSCLRecord():
'''public void setSCLRecord(final SCLRecord sclRecord)
'''
pass
def findFirstRecordLocBySid():
'''public int findFirstRecordLocBySid(final short sid)
'''
pass
def getWindowTwo():
'''public WindowTwoRecord getWindowTwo()
'''
pass
def getPrintGridlines():
'''public PrintGridlinesRecord getPrintGridlines()
'''
pass
def setPrintGridlines():
'''public void setPrintGridlines(final PrintGridlinesRecord newPrintGridlines)
'''
pass
def getPrintHeaders():
'''public PrintHeadersRecord getPrintHeaders()
'''
pass
def setPrintHeaders():
'''public void setPrintHeaders(final PrintHeadersRecord newPrintHeaders)
'''
pass
def setSelected():
'''public void setSelected(final boolean sel)
'''
pass
def createFreezePane():
'''public void createFreezePane(final int colSplit, final int rowSplit, final int topRow, final int leftmostColumn)
'''
pass
def createSplitPane():
'''public void createSplitPane(final int xSplitPos, final int ySplitPos, final int topRow, final int leftmostColumn, final int activePane)
'''
pass
def getPaneInformation():
'''public PaneInformation getPaneInformation()
'''
pass
def getSelection():
'''public SelectionRecord getSelection()
'''
pass
def setSelection():
'''public void setSelection(final SelectionRecord selection)
'''
pass
def getProtectionBlock():
'''public WorksheetProtectionBlock getProtectionBlock()
'''
pass
def setDisplayGridlines():
'''public void setDisplayGridlines(final boolean show)
'''
pass
def isDisplayGridlines():
'''public boolean isDisplayGridlines()
'''
pass
def setDisplayFormulas():
'''public void setDisplayFormulas(final boolean show)
'''
pass
def isDisplayFormulas():
'''public boolean isDisplayFormulas()
'''
pass
def setDisplayRowColHeadings():
'''public void setDisplayRowColHeadings(final boolean show)
'''
pass
def isDisplayRowColHeadings():
'''public boolean isDisplayRowColHeadings()
'''
pass
def setPrintRowColHeadings():
'''public void setPrintRowColHeadings(final boolean show)
'''
pass
def isPrintRowColHeadings():
'''public boolean isPrintRowColHeadings()
'''
pass
def getUncalced():
'''public boolean getUncalced()
'''
pass
def setUncalced():
'''public void setUncalced(final boolean uncalced)
'''
pass
def aggregateDrawingRecords():
'''public int aggregateDrawingRecords(final DrawingManager2 drawingManager, final boolean createIfMissing)
'''
pass
def preSerialize():
'''public void preSerialize()
'''
pass
def getPageSettings():
'''public PageSettingsBlock getPageSettings()
'''
pass
def setColumnGroupCollapsed():
'''public void setColumnGroupCollapsed(final int columnNumber, final boolean collapsed)
'''
pass
def groupRowRange():
'''public void groupRowRange(final int fromRow, final int toRow, final boolean indent)
'''
pass
def getOrCreateDataValidityTable():
'''public DataValidityTable getOrCreateDataValidityTable()
'''
pass
def getNoteRecords():
'''public NoteRecord[] getNoteRecords()
'''
pass
def getColumnOutlineLevel():
'''public int getColumnOutlineLevel(final int columnIndex)
'''
pass
def getType():
'''public int getType()
'''
pass
def RecordCloner():
'''public RecordCloner(final List<Record> destList)
'''
pass
