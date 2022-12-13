LeftMargin = "short  0"
RightMargin = "short  1"
TopMargin = "short  2"
BottomMargin = "short  3"
PANE_LOWER_RIGHT = "byte  0"
PANE_UPPER_RIGHT = "byte  1"
PANE_LOWER_LEFT = "byte  2"
PANE_UPPER_LEFT = "byte  3"
def createSheet():
    '''    public static InternalSheet createSheet(final RecordStream rs)
    public static InternalSheet createSheet()
    '''
def visitRecord():
    '''    public void visitRecord(final Record r)
    public void visitRecord(final Record r)
    '''
def cloneSheet():
    '''    public InternalSheet cloneSheet()
    '''
def getRowsAggregate():
    '''    public RowRecordsAggregate getRowsAggregate()
    '''
def updateFormulasAfterCellShift():
    '''    public void updateFormulasAfterCellShift(final FormulaShifter shifter, final int externSheetIndex)
    '''
def addMergedRegion():
    '''    public int addMergedRegion(final int rowFrom, final int colFrom, final int rowTo, final int colTo)
    '''
def removeMergedRegion():
    '''    public void removeMergedRegion(final int index)
    '''
def getMergedRegionAt():
    '''    public CellRangeAddress getMergedRegionAt(final int index)
    '''
def getNumMergedRegions():
    '''    public int getNumMergedRegions()
    '''
def getConditionalFormattingTable():
    '''    public ConditionalFormattingTable getConditionalFormattingTable()
    '''
def setDimensions():
    '''    public void setDimensions(final int firstrow, final short firstcol, final int lastrow, final short lastcol)
    '''
def visitContainedRecords():
    '''    public void visitContainedRecords(final RecordAggregate.RecordVisitor rv, final int offset)
    '''
def addValueRecord():
    '''    public void addValueRecord(final int row, final CellValueRecordInterface col)
    '''
def removeValueRecord():
    '''    public void removeValueRecord(final int row, final CellValueRecordInterface col)
    '''
def replaceValueRecord():
    '''    public void replaceValueRecord(final CellValueRecordInterface newval)
    '''
def addRow():
    '''    public void addRow(final RowRecord row)
    '''
def removeRow():
    '''    public void removeRow(final RowRecord row)
    '''
def getCellValueIterator():
    '''    public Iterator<CellValueRecordInterface> getCellValueIterator()
    '''
def getNextRow():
    '''    public RowRecord getNextRow()
    '''
def getRow():
    '''    public RowRecord getRow(final int rownum)
    '''
def getDefaultColumnWidth():
    '''    public int getDefaultColumnWidth()
    '''
def isGridsPrinted():
    '''    public boolean isGridsPrinted()
    '''
def setGridsPrinted():
    '''    public void setGridsPrinted(final boolean value)
    '''
def setDefaultColumnWidth():
    '''    public void setDefaultColumnWidth(final int dcw)
    '''
def setDefaultRowHeight():
    '''    public void setDefaultRowHeight(final short dch)
    '''
def getDefaultRowHeight():
    '''    public short getDefaultRowHeight()
    '''
def getColumnWidth():
    '''    public int getColumnWidth(final int columnIndex)
    '''
def getXFIndexForColAt():
    '''    public short getXFIndexForColAt(final short columnIndex)
    '''
def setColumnWidth():
    '''    public void setColumnWidth(final int column, final int width)
    '''
def isColumnHidden():
    '''    public boolean isColumnHidden(final int columnIndex)
    '''
def setColumnHidden():
    '''    public void setColumnHidden(final int column, final boolean hidden)
    '''
def setDefaultColumnStyle():
    '''    public void setDefaultColumnStyle(final int column, final int styleIndex)
    '''
def groupColumnRange():
    '''    public void groupColumnRange(final int fromColumn, final int toColumn, final boolean indent)
    '''
def getTopRow():
    '''    public short getTopRow()
    '''
def setTopRow():
    '''    public void setTopRow(final short topRow)
    '''
def setLeftCol():
    '''    public void setLeftCol(final short leftCol)
    '''
def getLeftCol():
    '''    public short getLeftCol()
    '''
def getActiveCellRow():
    '''    public int getActiveCellRow()
    '''
def setActiveCellRow():
    '''    public void setActiveCellRow(final int row)
    '''
def getActiveCellCol():
    '''    public short getActiveCellCol()
    '''
def setActiveCellCol():
    '''    public void setActiveCellCol(final short col)
    '''
def getRecords():
    '''    public List<RecordBase> getRecords()
    '''
def getGridsetRecord():
    '''    public GridsetRecord getGridsetRecord()
    '''
def findFirstRecordBySid():
    '''    public Record findFirstRecordBySid(final short sid)
    '''
def setSCLRecord():
    '''    public void setSCLRecord(final SCLRecord sclRecord)
    '''
def findFirstRecordLocBySid():
    '''    public int findFirstRecordLocBySid(final short sid)
    '''
def getWindowTwo():
    '''    public WindowTwoRecord getWindowTwo()
    '''
def getPrintGridlines():
    '''    public PrintGridlinesRecord getPrintGridlines()
    '''
def setPrintGridlines():
    '''    public void setPrintGridlines(final PrintGridlinesRecord newPrintGridlines)
    '''
def getPrintHeaders():
    '''    public PrintHeadersRecord getPrintHeaders()
    '''
def setPrintHeaders():
    '''    public void setPrintHeaders(final PrintHeadersRecord newPrintHeaders)
    '''
def setSelected():
    '''    public void setSelected(final boolean sel)
    '''
def createFreezePane():
    '''    public void createFreezePane(final int colSplit, final int rowSplit, final int topRow, final int leftmostColumn)
    '''
def createSplitPane():
    '''    public void createSplitPane(final int xSplitPos, final int ySplitPos, final int topRow, final int leftmostColumn, final int activePane)
    '''
def getPaneInformation():
    '''    public PaneInformation getPaneInformation()
    '''
def getSelection():
    '''    public SelectionRecord getSelection()
    '''
def setSelection():
    '''    public void setSelection(final SelectionRecord selection)
    '''
def getProtectionBlock():
    '''    public WorksheetProtectionBlock getProtectionBlock()
    '''
def setDisplayGridlines():
    '''    public void setDisplayGridlines(final boolean show)
    '''
def isDisplayGridlines():
    '''    public boolean isDisplayGridlines()
    '''
def setDisplayFormulas():
    '''    public void setDisplayFormulas(final boolean show)
    '''
def isDisplayFormulas():
    '''    public boolean isDisplayFormulas()
    '''
def setDisplayRowColHeadings():
    '''    public void setDisplayRowColHeadings(final boolean show)
    '''
def isDisplayRowColHeadings():
    '''    public boolean isDisplayRowColHeadings()
    '''
def setPrintRowColHeadings():
    '''    public void setPrintRowColHeadings(final boolean show)
    '''
def isPrintRowColHeadings():
    '''    public boolean isPrintRowColHeadings()
    '''
def getUncalced():
    '''    public boolean getUncalced()
    '''
def setUncalced():
    '''    public void setUncalced(final boolean uncalced)
    '''
def aggregateDrawingRecords():
    '''    public int aggregateDrawingRecords(final DrawingManager2 drawingManager, final boolean createIfMissing)
    '''
def preSerialize():
    '''    public void preSerialize()
    '''
def getPageSettings():
    '''    public PageSettingsBlock getPageSettings()
    '''
def setColumnGroupCollapsed():
    '''    public void setColumnGroupCollapsed(final int columnNumber, final boolean collapsed)
    '''
def groupRowRange():
    '''    public void groupRowRange(final int fromRow, final int toRow, final boolean indent)
    '''
def getOrCreateDataValidityTable():
    '''    public DataValidityTable getOrCreateDataValidityTable()
    '''
def getNoteRecords():
    '''    public NoteRecord[] getNoteRecords()
    '''
def getColumnOutlineLevel():
    '''    public int getColumnOutlineLevel(final int columnIndex)
    '''
def getType():
    '''    public int getType()
    '''
def RecordCloner():
    '''    public RecordCloner(final List<Record> destList)
    '''
