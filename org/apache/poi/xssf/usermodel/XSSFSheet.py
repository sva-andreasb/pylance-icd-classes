TWIPS_PER_POINT = "int  20"
def getWorkbook():
    '''returns XSSFWorkbook\n\n
    getWorkbook()\n
    '''
def getCTWorksheet():
    '''returns CTWorksheet\n\n
    getCTWorksheet()\n
    '''
def getColumnHelper():
    '''returns ColumnHelper\n\n
    getColumnHelper()\n
    '''
def getSheetName():
    '''returns String\n\n
    getSheetName()\n
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
def autoSizeColumn():
    '''returns None\n\n
    autoSizeColumn(final int column)\n
    autoSizeColumn(final int column, final boolean useMergedCells)\n
    '''
def getDrawingPatriarch():
    '''returns XSSFDrawing\n\n
    getDrawingPatriarch()\n
    '''
def createDrawingPatriarch():
    '''returns XSSFDrawing\n\n
    createDrawingPatriarch()\n
    '''
def createFreezePane():
    '''returns None\n\n
    createFreezePane(final int colSplit, final int rowSplit)\n
    createFreezePane(final int colSplit, final int rowSplit, final int leftmostColumn, final int topRow)\n
    '''
def createRow():
    '''returns XSSFRow\n\n
    createRow(final int rownum)\n
    '''
def createSplitPane():
    '''returns None\n\n
    createSplitPane(final int xSplitPos, final int ySplitPos, final int leftmostColumn, final int topRow, final int activePane)\n
    '''
def getCellComment():
    '''returns XSSFComment\n\n
    getCellComment(final CellAddress address)\n
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
def getColumnBreaks():
    '''returns int[]\n\n
    getColumnBreaks()\n
    '''
def getColumnWidth():
    '''returns int\n\n
    getColumnWidth(final int columnIndex)\n
    '''
def getColumnWidthInPixels():
    '''returns float\n\n
    getColumnWidthInPixels(final int columnIndex)\n
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
def getColumnStyle():
    '''returns CellStyle\n\n
    getColumnStyle(final int column)\n
    '''
def setRightToLeft():
    '''returns None\n\n
    setRightToLeft(final boolean value)\n
    '''
def isRightToLeft():
    '''returns boolean\n\n
    isRightToLeft()\n
    '''
def getDisplayGuts():
    '''returns boolean\n\n
    getDisplayGuts()\n
    '''
def setDisplayGuts():
    '''returns None\n\n
    setDisplayGuts(final boolean value)\n
    '''
def isDisplayZeros():
    '''returns boolean\n\n
    isDisplayZeros()\n
    '''
def setDisplayZeros():
    '''returns None\n\n
    setDisplayZeros(final boolean value)\n
    '''
def getFirstRowNum():
    '''returns int\n\n
    getFirstRowNum()\n
    '''
def getFitToPage():
    '''returns boolean\n\n
    getFitToPage()\n
    '''
def getFooter():
    '''returns Footer\n\n
    getFooter()\n
    '''
def getHeader():
    '''returns Header\n\n
    getHeader()\n
    '''
def getOddFooter():
    '''returns Footer\n\n
    getOddFooter()\n
    '''
def getEvenFooter():
    '''returns Footer\n\n
    getEvenFooter()\n
    '''
def getFirstFooter():
    '''returns Footer\n\n
    getFirstFooter()\n
    '''
def getOddHeader():
    '''returns Header\n\n
    getOddHeader()\n
    '''
def getEvenHeader():
    '''returns Header\n\n
    getEvenHeader()\n
    '''
def getFirstHeader():
    '''returns Header\n\n
    getFirstHeader()\n
    '''
def getHorizontallyCenter():
    '''returns boolean\n\n
    getHorizontallyCenter()\n
    '''
def getLastRowNum():
    '''returns int\n\n
    getLastRowNum()\n
    '''
def getLeftCol():
    '''returns short\n\n
    getLeftCol()\n
    '''
def getMargin():
    '''returns double\n\n
    getMargin(final short margin)\n
    '''
def setMargin():
    '''returns None\n\n
    setMargin(final short margin, final double size)\n
    '''
def getMergedRegion():
    '''returns CellRangeAddress\n\n
    getMergedRegion(final int index)\n
    '''
def getMergedRegions():
    '''returns List<CellRangeAddress>\n\n
    getMergedRegions()\n
    '''
def getNumMergedRegions():
    '''returns int\n\n
    getNumMergedRegions()\n
    '''
def getNumHyperlinks():
    '''returns int\n\n
    getNumHyperlinks()\n
    '''
def getPaneInformation():
    '''returns PaneInformation\n\n
    getPaneInformation()\n
    '''
def getPhysicalNumberOfRows():
    '''returns int\n\n
    getPhysicalNumberOfRows()\n
    '''
def getPrintSetup():
    '''returns XSSFPrintSetup\n\n
    getPrintSetup()\n
    '''
def getProtect():
    '''returns boolean\n\n
    getProtect()\n
    '''
def protectSheet():
    '''returns None\n\n
    protectSheet(final String password)\n
    '''
def setSheetPassword():
    '''returns None\n\n
    setSheetPassword(final String password, final HashAlgorithm hashAlgo)\n
    '''
def validateSheetPassword():
    '''returns boolean\n\n
    validateSheetPassword(final String password)\n
    '''
def getRow():
    '''returns XSSFRow\n\n
    getRow(final int rownum)\n
    '''
def getRowBreaks():
    '''returns int[]\n\n
    getRowBreaks()\n
    '''
def getRowSumsBelow():
    '''returns boolean\n\n
    getRowSumsBelow()\n
    '''
def setRowSumsBelow():
    '''returns None\n\n
    setRowSumsBelow(final boolean value)\n
    '''
def getRowSumsRight():
    '''returns boolean\n\n
    getRowSumsRight()\n
    '''
def setRowSumsRight():
    '''returns None\n\n
    setRowSumsRight(final boolean value)\n
    '''
def getScenarioProtect():
    '''returns boolean\n\n
    getScenarioProtect()\n
    '''
def getTopRow():
    '''returns short\n\n
    getTopRow()\n
    '''
def getVerticallyCenter():
    '''returns boolean\n\n
    getVerticallyCenter()\n
    '''
def groupColumn():
    '''returns None\n\n
    groupColumn(final int fromColumn, final int toColumn)\n
    '''
def groupRow():
    '''returns None\n\n
    groupRow(final int fromRow, final int toRow)\n
    '''
def isColumnBroken():
    '''returns boolean\n\n
    isColumnBroken(final int column)\n
    '''
def isColumnHidden():
    '''returns boolean\n\n
    isColumnHidden(final int columnIndex)\n
    '''
def isDisplayFormulas():
    '''returns boolean\n\n
    isDisplayFormulas()\n
    '''
def isDisplayGridlines():
    '''returns boolean\n\n
    isDisplayGridlines()\n
    '''
def setDisplayGridlines():
    '''returns None\n\n
    setDisplayGridlines(final boolean show)\n
    '''
def isDisplayRowColHeadings():
    '''returns boolean\n\n
    isDisplayRowColHeadings()\n
    '''
def setDisplayRowColHeadings():
    '''returns None\n\n
    setDisplayRowColHeadings(final boolean show)\n
    '''
def isPrintGridlines():
    '''returns boolean\n\n
    isPrintGridlines()\n
    '''
def setPrintGridlines():
    '''returns None\n\n
    setPrintGridlines(final boolean value)\n
    '''
def isPrintRowAndColumnHeadings():
    '''returns boolean\n\n
    isPrintRowAndColumnHeadings()\n
    '''
def setPrintRowAndColumnHeadings():
    '''returns None\n\n
    setPrintRowAndColumnHeadings(final boolean value)\n
    '''
def isRowBroken():
    '''returns boolean\n\n
    isRowBroken(final int row)\n
    '''
def setRowBreak():
    '''returns None\n\n
    setRowBreak(final int row)\n
    '''
def removeColumnBreak():
    '''returns None\n\n
    removeColumnBreak(final int column)\n
    '''
def removeMergedRegion():
    '''returns None\n\n
    removeMergedRegion(final int index)\n
    '''
def removeMergedRegions():
    '''returns None\n\n
    removeMergedRegions(final Collection<Integer> indices)\n
    '''
def removeRow():
    '''returns None\n\n
    removeRow(final Row row)\n
    '''
def removeRowBreak():
    '''returns None\n\n
    removeRowBreak(final int row)\n
    '''
def setForceFormulaRecalculation():
    '''returns None\n\n
    setForceFormulaRecalculation(final boolean value)\n
    '''
def getForceFormulaRecalculation():
    '''returns boolean\n\n
    getForceFormulaRecalculation()\n
    '''
def rowIterator():
    '''returns Iterator<Row>\n\n
    rowIterator()\n
    '''
def iterator():
    '''returns Iterator<Row>\n\n
    iterator()\n
    '''
def getAutobreaks():
    '''returns boolean\n\n
    getAutobreaks()\n
    '''
def setAutobreaks():
    '''returns None\n\n
    setAutobreaks(final boolean value)\n
    '''
def setColumnBreak():
    '''returns None\n\n
    setColumnBreak(final int column)\n
    '''
def setColumnGroupCollapsed():
    '''returns None\n\n
    setColumnGroupCollapsed(final int columnNumber, final boolean collapsed)\n
    '''
def setColumnHidden():
    '''returns None\n\n
    setColumnHidden(final int columnIndex, final boolean hidden)\n
    '''
def setColumnWidth():
    '''returns None\n\n
    setColumnWidth(final int columnIndex, final int width)\n
    '''
def setDefaultColumnStyle():
    '''returns None\n\n
    setDefaultColumnStyle(final int column, final CellStyle style)\n
    '''
def setDefaultColumnWidth():
    '''returns None\n\n
    setDefaultColumnWidth(final int width)\n
    '''
def setDefaultRowHeight():
    '''returns None\n\n
    setDefaultRowHeight(final short height)\n
    '''
def setDefaultRowHeightInPoints():
    '''returns None\n\n
    setDefaultRowHeightInPoints(final float height)\n
    '''
def setDisplayFormulas():
    '''returns None\n\n
    setDisplayFormulas(final boolean show)\n
    '''
def setFitToPage():
    '''returns None\n\n
    setFitToPage(final boolean b)\n
    '''
def setHorizontallyCenter():
    '''returns None\n\n
    setHorizontallyCenter(final boolean value)\n
    '''
def setVerticallyCenter():
    '''returns None\n\n
    setVerticallyCenter(final boolean value)\n
    '''
def setRowGroupCollapsed():
    '''returns None\n\n
    setRowGroupCollapsed(final int rowIndex, final boolean collapse)\n
    '''
def findEndOfRowOutlineGroup():
    '''returns int\n\n
    findEndOfRowOutlineGroup(final int row)\n
    '''
def setZoom():
    '''returns None\n\n
    setZoom(final int scale)\n
    '''
def copyRows():
    '''returns None\n\n
    copyRows(final List<? extends Row> srcRows, final int destStartRow, final CellCopyPolicy policy)\n
    copyRows(final int srcStartRow, final int srcEndRow, final int destStartRow, final CellCopyPolicy cellCopyPolicy)\n
    '''
def shiftRows():
    '''returns None\n\n
    shiftRows(final int startRow, final int endRow, final int n)\n
    shiftRows(final int startRow, final int endRow, final int n, final boolean copyRowHeight, final boolean resetOriginalRowHeight)\n
    '''
def compare():
    '''returns int\n\n
    compare(final XSSFComment o1, final XSSFComment o2)\n
    '''
def showInPane():
    '''returns None\n\n
    showInPane(final int toprow, final int leftcol)\n
    '''
def ungroupColumn():
    '''returns None\n\n
    ungroupColumn(final int fromColumn, final int toColumn)\n
    '''
def ungroupRow():
    '''returns None\n\n
    ungroupRow(final int fromRow, final int toRow)\n
    '''
def isSelected():
    '''returns boolean\n\n
    isSelected()\n
    '''
def setSelected():
    '''returns None\n\n
    setSelected(final boolean value)\n
    '''
def addHyperlink():
    '''returns None\n\n
    addHyperlink(final XSSFHyperlink hyperlink)\n
    '''
def removeHyperlink():
    '''returns None\n\n
    removeHyperlink(final int row, final int column)\n
    '''
def getActiveCell():
    '''returns CellAddress\n\n
    getActiveCell()\n
    '''
def setActiveCell():
    '''returns None\n\n
    setActiveCell(final CellAddress address)\n
    '''
def hasComments():
    '''returns boolean\n\n
    hasComments()\n
    '''
def getSharedFormula():
    '''returns CTCellFormula\n\n
    getSharedFormula(final int sid)\n
    '''
def isAutoFilterLocked():
    '''returns boolean\n\n
    isAutoFilterLocked()\n
    '''
def isDeleteColumnsLocked():
    '''returns boolean\n\n
    isDeleteColumnsLocked()\n
    '''
def isDeleteRowsLocked():
    '''returns boolean\n\n
    isDeleteRowsLocked()\n
    '''
def isFormatCellsLocked():
    '''returns boolean\n\n
    isFormatCellsLocked()\n
    '''
def isFormatColumnsLocked():
    '''returns boolean\n\n
    isFormatColumnsLocked()\n
    '''
def isFormatRowsLocked():
    '''returns boolean\n\n
    isFormatRowsLocked()\n
    '''
def isInsertColumnsLocked():
    '''returns boolean\n\n
    isInsertColumnsLocked()\n
    '''
def isInsertHyperlinksLocked():
    '''returns boolean\n\n
    isInsertHyperlinksLocked()\n
    '''
def isInsertRowsLocked():
    '''returns boolean\n\n
    isInsertRowsLocked()\n
    '''
def isPivotTablesLocked():
    '''returns boolean\n\n
    isPivotTablesLocked()\n
    '''
def isSortLocked():
    '''returns boolean\n\n
    isSortLocked()\n
    '''
def isObjectsLocked():
    '''returns boolean\n\n
    isObjectsLocked()\n
    '''
def isScenariosLocked():
    '''returns boolean\n\n
    isScenariosLocked()\n
    '''
def isSelectLockedCellsLocked():
    '''returns boolean\n\n
    isSelectLockedCellsLocked()\n
    '''
def isSelectUnlockedCellsLocked():
    '''returns boolean\n\n
    isSelectUnlockedCellsLocked()\n
    '''
def isSheetLocked():
    '''returns boolean\n\n
    isSheetLocked()\n
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
def setArrayFormula():
    '''returns CellRange<XSSFCell>\n\n
    setArrayFormula(final String formula, final CellRangeAddress range)\n
    '''
def removeArrayFormula():
    '''returns CellRange<XSSFCell>\n\n
    removeArrayFormula(final Cell cell)\n
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
    '''returns XSSFAutoFilter\n\n
    setAutoFilter(final CellRangeAddress range)\n
    '''
def createTable():
    '''returns XSSFTable\n\n
    createTable()\n
    '''
def getTables():
    '''returns List<XSSFTable>\n\n
    getTables()\n
    '''
def removeTable():
    '''returns None\n\n
    removeTable(final XSSFTable t)\n
    '''
def getSheetConditionalFormatting():
    '''returns XSSFSheetConditionalFormatting\n\n
    getSheetConditionalFormatting()\n
    '''
def getTabColor():
    '''returns XSSFColor\n\n
    getTabColor()\n
    '''
def setTabColor():
    '''returns None\n\n
    setTabColor(final XSSFColor color)\n
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
def createPivotTable():
    '''returns XSSFPivotTable\n\n
    createPivotTable(final AreaReference source, final CellReference position, final Sheet sourceSheet)\n
    createPivotTable(final AreaReference source, final CellReference position)\n
    createPivotTable(final Name source, final CellReference position, final Sheet sourceSheet)\n
    createPivotTable(final Name source, final CellReference position)\n
    createPivotTable(final Table source, final CellReference position)\n
    '''
def configureReference():
    '''returns None\n\n
    configureReference(final CTWorksheetSource wsSource)\n
    configureReference(final CTWorksheetSource wsSource)\n
    configureReference(final CTWorksheetSource wsSource)\n
    '''
def getPivotTables():
    '''returns List<XSSFPivotTable>\n\n
    getPivotTables()\n
    '''
def getColumnOutlineLevel():
    '''returns int\n\n
    getColumnOutlineLevel(final int columnIndex)\n
    '''
def addIgnoredErrors():
    '''returns None\n\n
    addIgnoredErrors(final CellReference cell, final IgnoredErrorType... ignoredErrorTypes)\n
    addIgnoredErrors(final CellRangeAddress region, final IgnoredErrorType... ignoredErrorTypes)\n
    '''
