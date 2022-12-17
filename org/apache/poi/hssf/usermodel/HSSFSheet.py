def getWorkbook():
    '''returns HSSFWorkbook\n\n
    getWorkbook()\n
    '''
def createRow():
    '''returns HSSFRow\n\n
    createRow(final int rownum)\n
    '''
def removeRow():
    '''returns None\n\n
    removeRow(final Row row)\n
    '''
def getRow():
    '''returns HSSFRow\n\n
    getRow(final int rowIndex)\n
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
def getDataValidations():
    '''returns List<HSSFDataValidation>\n\n
    getDataValidations()\n
    '''
def visitRecord():
    '''returns None\n\n
    visitRecord(final Record r)\n
    '''
def addValidationData():
    '''returns None\n\n
    addValidationData(final DataValidation dataValidation)\n
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
    getColumnWidthInPixels(final int column)\n
    '''
def getDefaultColumnWidth():
    '''returns int\n\n
    getDefaultColumnWidth()\n
    '''
def setDefaultColumnWidth():
    '''returns None\n\n
    setDefaultColumnWidth(final int width)\n
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
    '''returns HSSFCellStyle\n\n
    getColumnStyle(final int column)\n
    '''
def isGridsPrinted():
    '''returns boolean\n\n
    isGridsPrinted()\n
    '''
def setGridsPrinted():
    '''returns None\n\n
    setGridsPrinted(final boolean value)\n
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
def setForceFormulaRecalculation():
    '''returns None\n\n
    setForceFormulaRecalculation(final boolean value)\n
    '''
def getForceFormulaRecalculation():
    '''returns boolean\n\n
    getForceFormulaRecalculation()\n
    '''
def setVerticallyCenter():
    '''returns None\n\n
    setVerticallyCenter(final boolean value)\n
    '''
def getVerticallyCenter():
    '''returns boolean\n\n
    getVerticallyCenter()\n
    '''
def setHorizontallyCenter():
    '''returns None\n\n
    setHorizontallyCenter(final boolean value)\n
    '''
def getHorizontallyCenter():
    '''returns boolean\n\n
    getHorizontallyCenter()\n
    '''
def setRightToLeft():
    '''returns None\n\n
    setRightToLeft(final boolean value)\n
    '''
def isRightToLeft():
    '''returns boolean\n\n
    isRightToLeft()\n
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
def iterator():
    '''returns Iterator<Row>\n\n
    iterator()\n
    '''
def setAlternativeExpression():
    '''returns None\n\n
    setAlternativeExpression(final boolean b)\n
    '''
def setAlternativeFormula():
    '''returns None\n\n
    setAlternativeFormula(final boolean b)\n
    '''
def setAutobreaks():
    '''returns None\n\n
    setAutobreaks(final boolean b)\n
    '''
def setDialog():
    '''returns None\n\n
    setDialog(final boolean b)\n
    '''
def setDisplayGuts():
    '''returns None\n\n
    setDisplayGuts(final boolean b)\n
    '''
def setFitToPage():
    '''returns None\n\n
    setFitToPage(final boolean b)\n
    '''
def setRowSumsBelow():
    '''returns None\n\n
    setRowSumsBelow(final boolean b)\n
    '''
def setRowSumsRight():
    '''returns None\n\n
    setRowSumsRight(final boolean b)\n
    '''
def getAlternateExpression():
    '''returns boolean\n\n
    getAlternateExpression()\n
    '''
def getAlternateFormula():
    '''returns boolean\n\n
    getAlternateFormula()\n
    '''
def getAutobreaks():
    '''returns boolean\n\n
    getAutobreaks()\n
    '''
def getDialog():
    '''returns boolean\n\n
    getDialog()\n
    '''
def getDisplayGuts():
    '''returns boolean\n\n
    getDisplayGuts()\n
    '''
def isDisplayZeros():
    '''returns boolean\n\n
    isDisplayZeros()\n
    '''
def setDisplayZeros():
    '''returns None\n\n
    setDisplayZeros(final boolean value)\n
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
    '''returns HSSFPrintSetup\n\n
    getPrintSetup()\n
    '''
def getHeader():
    '''returns HSSFHeader\n\n
    getHeader()\n
    '''
def getFooter():
    '''returns HSSFFooter\n\n
    getFooter()\n
    '''
def isSelected():
    '''returns boolean\n\n
    isSelected()\n
    '''
def setSelected():
    '''returns None\n\n
    setSelected(final boolean sel)\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive()\n
    '''
def setActive():
    '''returns None\n\n
    setActive(final boolean sel)\n
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
def getPassword():
    '''returns short\n\n
    getPassword()\n
    '''
def getObjectProtect():
    '''returns boolean\n\n
    getObjectProtect()\n
    '''
def getScenarioProtect():
    '''returns boolean\n\n
    getScenarioProtect()\n
    '''
def protectSheet():
    '''returns None\n\n
    protectSheet(final String password)\n
    '''
def setZoom():
    '''returns None\n\n
    setZoom(final int numerator, final int denominator)\n
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
def shiftRows():
    '''returns None\n\n
    shiftRows(final int startRow, final int endRow, final int n)\n
    shiftRows(final int startRow, final int endRow, final int n, final boolean copyRowHeight, final boolean resetOriginalRowHeight)\n
    shiftRows(final int startRow, final int endRow, final int n, final boolean copyRowHeight, final boolean resetOriginalRowHeight, final boolean moveComments)\n
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
def dumpDrawingRecords():
    '''returns None\n\n
    dumpDrawingRecords(final boolean fat, final PrintWriter pw)\n
    '''
def getDrawingEscherAggregate():
    '''returns EscherAggregate\n\n
    getDrawingEscherAggregate()\n
    '''
def getDrawingPatriarch():
    '''returns HSSFPatriarch\n\n
    getDrawingPatriarch()\n
    '''
def createDrawingPatriarch():
    '''returns HSSFPatriarch\n\n
    createDrawingPatriarch()\n
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
def ungroupRow():
    '''returns None\n\n
    ungroupRow(final int fromRow, final int toRow)\n
    '''
def setRowGroupCollapsed():
    '''returns None\n\n
    setRowGroupCollapsed(final int rowIndex, final boolean collapse)\n
    '''
def setDefaultColumnStyle():
    '''returns None\n\n
    setDefaultColumnStyle(final int column, final CellStyle style)\n
    '''
def autoSizeColumn():
    '''returns None\n\n
    autoSizeColumn(final int column)\n
    autoSizeColumn(final int column, final boolean useMergedCells)\n
    '''
def getCellComment():
    '''returns HSSFComment\n\n
    getCellComment(final CellAddress ref)\n
    '''
def getHyperlink():
    '''returns HSSFHyperlink\n\n
    getHyperlink(final int row, final int column)\n
    getHyperlink(final CellAddress addr)\n
    '''
def getHyperlinkList():
    '''returns List<HSSFHyperlink>\n\n
    getHyperlinkList()\n
    '''
def getSheetConditionalFormatting():
    '''returns HSSFSheetConditionalFormatting\n\n
    getSheetConditionalFormatting()\n
    '''
def getSheetName():
    '''returns String\n\n
    getSheetName()\n
    '''
def setArrayFormula():
    '''returns CellRange<HSSFCell>\n\n
    setArrayFormula(final String formula, final CellRangeAddress range)\n
    '''
def removeArrayFormula():
    '''returns CellRange<HSSFCell>\n\n
    removeArrayFormula(final Cell cell)\n
    '''
def getDataValidationHelper():
    '''returns DataValidationHelper\n\n
    getDataValidationHelper()\n
    '''
def setAutoFilter():
    '''returns HSSFAutoFilter\n\n
    setAutoFilter(final CellRangeAddress range)\n
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
