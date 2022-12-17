DEFAULT_WINDOW_SIZE = "int  100"
def ():
    '''returns SheetIterator\n\n
    ()\n
    (final XSSFWorkbook workbook)\n
    (final XSSFWorkbook workbook, final int rowAccessWindowSize)\n
    (final XSSFWorkbook workbook, final int rowAccessWindowSize, final boolean compressTmpFiles)\n
    (final XSSFWorkbook workbook, final int rowAccessWindowSize, final boolean compressTmpFiles, final boolean useSharedStringsTable)\n
    (final int rowAccessWindowSize)\n
    ()\n
    '''
def getRandomAccessWindowSize():
    '''returns int\n\n
    getRandomAccessWindowSize()\n
    '''
def isCompressTempFiles():
    '''returns boolean\n\n
    isCompressTempFiles()\n
    '''
def setCompressTempFiles():
    '''returns None\n\n
    setCompressTempFiles(final boolean compress)\n
    '''
def getXSSFWorkbook():
    '''returns XSSFWorkbook\n\n
    getXSSFWorkbook()\n
    '''
def getActiveSheetIndex():
    '''returns int\n\n
    getActiveSheetIndex()\n
    '''
def setActiveSheet():
    '''returns None\n\n
    setActiveSheet(final int sheetIndex)\n
    '''
def getFirstVisibleTab():
    '''returns int\n\n
    getFirstVisibleTab()\n
    '''
def setFirstVisibleTab():
    '''returns None\n\n
    setFirstVisibleTab(final int sheetIndex)\n
    '''
def setSheetOrder():
    '''returns None\n\n
    setSheetOrder(final String sheetname, final int pos)\n
    '''
def setSelectedTab():
    '''returns None\n\n
    setSelectedTab(final int index)\n
    '''
def setSheetName():
    '''returns None\n\n
    setSheetName(final int sheet, final String name)\n
    '''
def getSheetName():
    '''returns String\n\n
    getSheetName(final int sheet)\n
    '''
def getSheetIndex():
    '''returns int\n\n
    getSheetIndex(final String name)\n
    getSheetIndex(final Sheet sheet)\n
    '''
def createSheet():
    '''returns SXSSFSheet\n\n
    createSheet()\n
    createSheet(final String sheetname)\n
    '''
def cloneSheet():
    '''returns Sheet\n\n
    cloneSheet(final int sheetNum)\n
    '''
def getNumberOfSheets():
    '''returns int\n\n
    getNumberOfSheets()\n
    '''
def sheetIterator():
    '''returns Iterator<Sheet>\n\n
    sheetIterator()\n
    '''
def iterator():
    '''returns Iterator<Sheet>\n\n
    iterator()\n
    '''
def getSheetAt():
    '''returns SXSSFSheet\n\n
    getSheetAt(final int index)\n
    '''
def getSheet():
    '''returns SXSSFSheet\n\n
    getSheet(final String name)\n
    '''
def removeSheetAt():
    '''returns None\n\n
    removeSheetAt(final int index)\n
    '''
def createFont():
    '''returns Font\n\n
    createFont()\n
    '''
def findFont():
    '''returns Font\n\n
    findFont(final boolean bold, final short color, final short fontHeight, final String name, final boolean italic, final boolean strikeout, final short typeOffset, final byte underline)\n
    '''
def getNumberOfFonts():
    '''returns short\n\n
    getNumberOfFonts()\n
    '''
def getFontAt():
    '''returns Font\n\n
    getFontAt(final short idx)\n
    '''
def createCellStyle():
    '''returns CellStyle\n\n
    createCellStyle()\n
    '''
def getNumCellStyles():
    '''returns int\n\n
    getNumCellStyles()\n
    '''
def getCellStyleAt():
    '''returns CellStyle\n\n
    getCellStyleAt(final int idx)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def write():
    '''returns None\n\n
    write(final OutputStream stream)\n
    '''
def dispose():
    '''returns boolean\n\n
    dispose()\n
    '''
def getNumberOfNames():
    '''returns int\n\n
    getNumberOfNames()\n
    '''
def getName():
    '''returns Name\n\n
    getName(final String name)\n
    '''
def getNameAt():
    '''returns Name\n\n
    getNameAt(final int nameIndex)\n
    '''
def createName():
    '''returns Name\n\n
    createName()\n
    '''
def getNameIndex():
    '''returns int\n\n
    getNameIndex(final String name)\n
    '''
def removeName():
    '''returns None\n\n
    removeName(final int index)\n
    removeName(final String name)\n
    removeName(final Name name)\n
    '''
def setPrintArea():
    '''returns None\n\n
    setPrintArea(final int sheetIndex, final String reference)\n
    setPrintArea(final int sheetIndex, final int startColumn, final int endColumn, final int startRow, final int endRow)\n
    '''
def getPrintArea():
    '''returns String\n\n
    getPrintArea(final int sheetIndex)\n
    '''
def removePrintArea():
    '''returns None\n\n
    removePrintArea(final int sheetIndex)\n
    '''
def setMissingCellPolicy():
    '''returns None\n\n
    setMissingCellPolicy(final Row.MissingCellPolicy missingCellPolicy)\n
    '''
def createDataFormat():
    '''returns DataFormat\n\n
    createDataFormat()\n
    '''
def addPicture():
    '''returns int\n\n
    addPicture(final byte[] pictureData, final int format)\n
    '''
def getCreationHelper():
    '''returns CreationHelper\n\n
    getCreationHelper()\n
    '''
def isHidden():
    '''returns boolean\n\n
    isHidden()\n
    '''
def setHidden():
    '''returns None\n\n
    setHidden(final boolean hiddenFlag)\n
    '''
def isSheetHidden():
    '''returns boolean\n\n
    isSheetHidden(final int sheetIx)\n
    '''
def isSheetVeryHidden():
    '''returns boolean\n\n
    isSheetVeryHidden(final int sheetIx)\n
    '''
def getSheetVisibility():
    '''returns SheetVisibility\n\n
    getSheetVisibility(final int sheetIx)\n
    '''
def setSheetHidden():
    '''returns None\n\n
    setSheetHidden(final int sheetIx, final boolean hidden)\n
    setSheetHidden(final int sheetIx, final int hidden)\n
    '''
def setSheetVisibility():
    '''returns None\n\n
    setSheetVisibility(final int sheetIx, final SheetVisibility visibility)\n
    '''
def linkExternalWorkbook():
    '''returns int\n\n
    linkExternalWorkbook(final String name, final Workbook workbook)\n
    '''
def addToolPack():
    '''returns None\n\n
    addToolPack(final UDFFinder toopack)\n
    '''
def setForceFormulaRecalculation():
    '''returns None\n\n
    setForceFormulaRecalculation(final boolean value)\n
    '''
def getForceFormulaRecalculation():
    '''returns boolean\n\n
    getForceFormulaRecalculation()\n
    '''
def getSpreadsheetVersion():
    '''returns SpreadsheetVersion\n\n
    getSpreadsheetVersion()\n
    '''
def addOlePackage():
    '''returns int\n\n
    addOlePackage(final byte[] oleData, final String label, final String fileName, final String command)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns T\n\n
    next()\n
    '''
def remove():
    '''returns None\n\n
    remove()\n
    '''
