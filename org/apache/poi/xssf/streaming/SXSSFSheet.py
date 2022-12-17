def ():
    '''returns SXSSFSheet\n\n
    (final SXSSFWorkbook workbook, final XSSFSheet xSheet)\n
    '''
def getWorksheetXMLInputStream():
    '''returns InputStream\n\n
    getWorksheetXMLInputStream()\n
    '''
def iterator():
    '''returns Iterator<Row>\n\n
    iterator()\n
    '''
def createRow():
    '''returns SXSSFRow\n\n
    createRow(final int rownum)\n
    '''
def removeRow():
    '''returns None\n\n
    removeRow(final Row row)\n
    '''
def getRow():
    '''returns SXSSFRow\n\n
    getRow(final int rownum)\n
    '''
def getPhysicalNumberOfRows():
    '''returns int\n\n
    getPhysicalNumberOfRows()\n
    '''
def getFirstRowNum():
    '''returns int\n\n
    getFirstRowNum()\n
    '''
def getLastRowNum():
    '''returns int\n\n
    getLastRowNum()\n
    '''
def setColumnHidden():
    '''returns None\n\n
    setColumnHidden(final int columnIndex, final boolean hidden)\n
    '''
def isColumnHidden():
    '''returns boolean\n\n
    isColumnHidden(final int columnIndex)\n
    '''
def setColumnWidth():
    '''returns None\n\n
    setColumnWidth(final int columnIndex, final int width)\n
    '''
def getColumnWidth():
    '''returns int\n\n
    getColumnWidth(final int columnIndex)\n
    '''
def getColumnWidthInPixels():
    '''returns float\n\n
    getColumnWidthInPixels(final int columnIndex)\n
    '''
def setDefaultColumnWidth():
    '''returns None\n\n
    setDefaultColumnWidth(final int width)\n
    '''
def getDefaultColumnWidth():
    '''returns int\n\n
    getDefaultColumnWidth()\n
    '''
def getDefaultRowHeight():
    '''returns short\n\n
    getDefaultRowHeight()\n
    '''
def getDefaultRowHeightInPoints():
    '''returns float\n\n
    getDefaultRowHeightInPoints()\n
    '''
def setDefaultRowHeight():
    '''returns None\n\n
    setDefaultRowHeight(final short height)\n
    '''
def setDefaultRowHeightInPoints():
    '''returns None\n\n
    setDefaultRowHeightInPoints(final float height)\n
    '''
def getColumnStyle():
    '''returns CellStyle\n\n
    getColumnStyle(final int column)\n
    '''
def addMergedRegion():
    '''returns int\n\n
    addMergedRegion(final CellRangeAddress region)\n
    '''
def addMergedRegionUnsafe():
    '''returns int\n\n
    addMergedRegionUnsafe(final CellRangeAddress region)\n
    '''
def validateMergedRegions():
    '''returns None\n\n
    validateMergedRegions()\n
    '''
def setVerticallyCenter():
    '''returns None\n\n
    setVerticallyCenter(final boolean value)\n
    '''
def setHorizontallyCenter():
    '''returns None\n\n
    setHorizontallyCenter(final boolean value)\n
    '''
def getHorizontallyCenter():
    '''returns boolean\n\n
    getHorizontallyCenter()\n
    '''
def getVerticallyCenter():
    '''returns boolean\n\n
    getVerticallyCenter()\n
    '''
def removeMergedRegion():
    '''returns None\n\n
    removeMergedRegion(final int index)\n
    '''
def removeMergedRegions():
    '''returns None\n\n
    removeMergedRegions(final Collection<Integer> indices)\n
    '''
def getNumMergedRegions():
    '''returns int\n\n
    getNumMergedRegions()\n
    '''
def getMergedRegion():
    '''returns CellRangeAddress\n\n
    getMergedRegion(final int index)\n
    '''
def getMergedRegions():
    '''returns List<CellRangeAddress>\n\n
    getMergedRegions()\n
    '''
def rowIterator():
    '''returns Iterator<Row>\n\n
    rowIterator()\n
    '''
def setAutobreaks():
    '''returns None\n\n
    setAutobreaks(final boolean value)\n
    '''
def setDisplayGuts():
    '''returns None\n\n
    setDisplayGuts(final boolean value)\n
    '''
def setDisplayZeros():
    '''returns None\n\n
    setDisplayZeros(final boolean value)\n
    '''
def isDisplayZeros():
    '''returns boolean\n\n
    isDisplayZeros()\n
    '''
def setRightToLeft():
    '''returns None\n\n
    setRightToLeft(final boolean value)\n
    '''
def isRightToLeft():
    '''returns boolean\n\n
    isRightToLeft()\n
    '''
def setFitToPage():
    '''returns None\n\n
    setFitToPage(final boolean value)\n
    '''
def setRowSumsBelow():
    '''returns None\n\n
    setRowSumsBelow(final boolean value)\n
    '''
def setRowSumsRight():
    '''returns None\n\n
    setRowSumsRight(final boolean value)\n
    '''
def getAutobreaks():
    '''returns boolean\n\n
    getAutobreaks()\n
    '''
def getDisplayGuts():
    '''returns boolean\n\n
    getDisplayGuts()\n
    '''
def getFitToPage():
    '''returns boolean\n\n
    getFitToPage()\n
    '''
def getRowSumsBelow():
    '''returns boolean\n\n
    getRowSumsBelow()\n
    '''
def getRowSumsRight():
    '''returns boolean\n\n
    getRowSumsRight()\n
    '''
def isPrintGridlines():
    '''returns boolean\n\n
    isPrintGridlines()\n
    '''
def setPrintGridlines():
    '''returns None\n\n
    setPrintGridlines(final boolean show)\n
    '''
def isPrintRowAndColumnHeadings():
    '''returns boolean\n\n
    isPrintRowAndColumnHeadings()\n
    '''
def setPrintRowAndColumnHeadings():
    '''returns None\n\n
    setPrintRowAndColumnHeadings(final boolean show)\n
    '''
def getPrintSetup():
    '''returns PrintSetup\n\n
    getPrintSetup()\n
    '''
def getHeader():
    '''returns Header\n\n
    getHeader()\n
    '''
def getFooter():
    '''returns Footer\n\n
    getFooter()\n
    '''
def setSelected():
    '''returns None\n\n
    setSelected(final boolean value)\n
    '''
def getMargin():
    '''returns double\n\n
    getMargin(final short margin)\n
    '''
def setMargin():
    '''returns None\n\n
    setMargin(final short margin, final double size)\n
    '''
def getProtect():
    '''returns boolean\n\n
    getProtect()\n
    '''
def protectSheet():
    '''returns None\n\n
    protectSheet(final String password)\n
    '''
def getScenarioProtect():
    '''returns boolean\n\n
    getScenarioProtect()\n
    '''
def setZoom():
    '''returns None\n\n
    setZoom(final int scale)\n
    '''
def getTopRow():
    '''returns short\n\n
    getTopRow()\n
    '''
def getLeftCol():
    '''returns short\n\n
    getLeftCol()\n
    '''
def showInPane():
    '''returns None\n\n
    showInPane(final int toprow, final int leftcol)\n
    '''
def setForceFormulaRecalculation():
    '''returns None\n\n
    setForceFormulaRecalculation(final boolean value)\n
    '''
def getForceFormulaRecalculation():
    '''returns boolean\n\n
    getForceFormulaRecalculation()\n
    '''
def shiftRows():
    '''returns None\n\n
    shiftRows(final int startRow, final int endRow, final int n)\n
    shiftRows(final int startRow, final int endRow, final int n, final boolean copyRowHeight, final boolean resetOriginalRowHeight)\n
    '''
def createFreezePane():
    '''returns None\n\n
    createFreezePane(final int colSplit, final int rowSplit, final int leftmostColumn, final int topRow)\n
    createFreezePane(final int colSplit, final int rowSplit)\n
    '''
def createSplitPane():
    '''returns None\n\n
    createSplitPane(final int xSplitPos, final int ySplitPos, final int leftmostColumn, final int topRow, final int activePane)\n
    '''
def getPaneInformation():
    '''returns PaneInformation\n\n
    getPaneInformation()\n
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
def setRowBreak():
    '''returns None\n\n
    setRowBreak(final int row)\n
    '''
def isRowBroken():
    '''returns boolean\n\n
    isRowBroken(final int row)\n
    '''
def removeRowBreak():
    '''returns None\n\n
    removeRowBreak(final int row)\n
    '''
def getRowBreaks():
    '''returns int[]\n\n
    getRowBreaks()\n
    '''
def getColumnBreaks():
    '''returns int[]\n\n
    getColumnBreaks()\n
    '''
def setColumnBreak():
    '''returns None\n\n
    setColumnBreak(final int column)\n
    '''
def isColumnBroken():
    '''returns boolean\n\n
    isColumnBroken(final int column)\n
    '''
def removeColumnBreak():
    '''returns None\n\n
    removeColumnBreak(final int column)\n
    '''
def setColumnGroupCollapsed():
    '''returns None\n\n
    setColumnGroupCollapsed(final int columnNumber, final boolean collapsed)\n
    '''
def groupColumn():
    '''returns None\n\n
    groupColumn(final int fromColumn, final int toColumn)\n
    '''
def ungroupColumn():
    '''returns None\n\n
    ungroupColumn(final int fromColumn, final int toColumn)\n
    '''
def groupRow():
    '''returns None\n\n
    groupRow(final int fromRow, final int toRow)\n
    '''
def setRowOutlineLevel():
    '''returns None\n\n
    setRowOutlineLevel(final int rownum, final int level)\n
    '''
def ungroupRow():
    '''returns None\n\n
    ungroupRow(final int fromRow, final int toRow)\n
    '''
def setRowGroupCollapsed():
    '''returns None\n\n
    setRowGroupCollapsed(final int row, final boolean collapse)\n
    '''
def setDefaultColumnStyle():
    '''returns None\n\n
    setDefaultColumnStyle(final int column, final CellStyle style)\n
    '''
def trackColumnForAutoSizing():
    '''returns None\n\n
    trackColumnForAutoSizing(final int column)\n
    '''
def trackColumnsForAutoSizing():
    '''returns None\n\n
    trackColumnsForAutoSizing(final Collection<Integer> columns)\n
    '''
def trackAllColumnsForAutoSizing():
    '''returns None\n\n
    trackAllColumnsForAutoSizing()\n
    '''
def untrackColumnForAutoSizing():
    '''returns boolean\n\n
    untrackColumnForAutoSizing(final int column)\n
    '''
def untrackColumnsForAutoSizing():
    '''returns boolean\n\n
    untrackColumnsForAutoSizing(final Collection<Integer> columns)\n
    '''
def untrackAllColumnsForAutoSizing():
    '''returns None\n\n
    untrackAllColumnsForAutoSizing()\n
    '''
def isColumnTrackedForAutoSizing():
    '''returns boolean\n\n
    isColumnTrackedForAutoSizing(final int column)\n
    '''
def getTrackedColumnsForAutoSizing():
    '''returns Set<Integer>\n\n
    getTrackedColumnsForAutoSizing()\n
    '''
def autoSizeColumn():
    '''returns None\n\n
    autoSizeColumn(final int column)\n
    autoSizeColumn(final int column, final boolean useMergedCells)\n
    '''
def getCellComment():
    '''returns XSSFComment\n\n
    getCellComment(final CellAddress ref)\n
    '''
def getHyperlink():
    '''returns XSSFHyperlink\n\n
    getHyperlink(final int row, final int column)\n
    getHyperlink(final CellAddress addr)\n
    '''
def getHyperlinkList():
    '''returns List<XSSFHyperlink>\n\n
    getHyperlinkList()\n
    '''
def getDrawingPatriarch():
    '''returns XSSFDrawing\n\n
    getDrawingPatriarch()\n
    '''
def createDrawingPatriarch():
    '''returns SXSSFDrawing\n\n
    createDrawingPatriarch()\n
    '''
def getWorkbook():
    '''returns SXSSFWorkbook\n\n
    getWorkbook()\n
    '''
def getSheetName():
    '''returns String\n\n
    getSheetName()\n
    '''
def isSelected():
    '''returns boolean\n\n
    isSelected()\n
    '''
def getDataValidationHelper():
    '''returns DataValidationHelper\n\n
    getDataValidationHelper()\n
    '''
def getDataValidations():
    '''returns List<XSSFDataValidation>\n\n
    getDataValidations()\n
    '''
def addValidationData():
    '''returns None\n\n
    addValidationData(final DataValidation dataValidation)\n
    '''
def setAutoFilter():
    '''returns AutoFilter\n\n
    setAutoFilter(final CellRangeAddress range)\n
    '''
def getSheetConditionalFormatting():
    '''returns SheetConditionalFormatting\n\n
    getSheetConditionalFormatting()\n
    '''
def getRepeatingRows():
    '''returns CellRangeAddress\n\n
    getRepeatingRows()\n
    '''
def getRepeatingColumns():
    '''returns CellRangeAddress\n\n
    getRepeatingColumns()\n
    '''
def setRepeatingRows():
    '''returns None\n\n
    setRepeatingRows(final CellRangeAddress rowRangeRef)\n
    '''
def setRepeatingColumns():
    '''returns None\n\n
    setRepeatingColumns(final CellRangeAddress columnRangeRef)\n
    '''
def setRandomAccessWindowSize():
    '''returns None\n\n
    setRandomAccessWindowSize(final int value)\n
    '''
def areAllRowsFlushed():
    '''returns boolean\n\n
    areAllRowsFlushed()\n
    '''
def getLastFlushedRowNum():
    '''returns int\n\n
    getLastFlushedRowNum()\n
    '''
def flushRows():
    '''returns None\n\n
    flushRows(final int remaining)\n
    flushRows()\n
    '''
def changeRowNum():
    '''returns None\n\n
    changeRowNum(final SXSSFRow row, final int newRowNum)\n
    '''
def getRowNum():
    '''returns int\n\n
    getRowNum(final SXSSFRow row)\n
    '''
def getColumnOutlineLevel():
    '''returns int\n\n
    getColumnOutlineLevel(final int columnIndex)\n
    '''
def getActiveCell():
    '''returns CellAddress\n\n
    getActiveCell()\n
    '''
def setActiveCell():
    '''returns None\n\n
    setActiveCell(final CellAddress address)\n
    '''
def getTabColor():
    '''returns XSSFColor\n\n
    getTabColor()\n
    '''
def setTabColor():
    '''returns None\n\n
    setTabColor(final XSSFColor color)\n
    setTabColor(final int colorIndex)\n
    '''
def enableLocking():
    '''returns None\n\n
    enableLocking()\n
    '''
def disableLocking():
    '''returns None\n\n
    disableLocking()\n
    '''
def lockAutoFilter():
    '''returns None\n\n
    lockAutoFilter(final boolean enabled)\n
    '''
def lockDeleteColumns():
    '''returns None\n\n
    lockDeleteColumns(final boolean enabled)\n
    '''
def lockDeleteRows():
    '''returns None\n\n
    lockDeleteRows(final boolean enabled)\n
    '''
def lockFormatCells():
    '''returns None\n\n
    lockFormatCells(final boolean enabled)\n
    '''
def lockFormatColumns():
    '''returns None\n\n
    lockFormatColumns(final boolean enabled)\n
    '''
def lockFormatRows():
    '''returns None\n\n
    lockFormatRows(final boolean enabled)\n
    '''
def lockInsertColumns():
    '''returns None\n\n
    lockInsertColumns(final boolean enabled)\n
    '''
def lockInsertHyperlinks():
    '''returns None\n\n
    lockInsertHyperlinks(final boolean enabled)\n
    '''
def lockInsertRows():
    '''returns None\n\n
    lockInsertRows(final boolean enabled)\n
    '''
def lockPivotTables():
    '''returns None\n\n
    lockPivotTables(final boolean enabled)\n
    '''
def lockSort():
    '''returns None\n\n
    lockSort(final boolean enabled)\n
    '''
def lockObjects():
    '''returns None\n\n
    lockObjects(final boolean enabled)\n
    '''
def lockScenarios():
    '''returns None\n\n
    lockScenarios(final boolean enabled)\n
    '''
def lockSelectLockedCells():
    '''returns None\n\n
    lockSelectLockedCells(final boolean enabled)\n
    '''
def lockSelectUnlockedCells():
    '''returns None\n\n
    lockSelectUnlockedCells(final boolean enabled)\n
    '''
