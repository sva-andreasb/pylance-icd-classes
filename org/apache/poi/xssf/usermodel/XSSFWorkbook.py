DEFAULT_CHARACTER_WIDTH = "float  7.0017f"
PICTURE_TYPE_GIF = "int  8"
PICTURE_TYPE_TIFF = "int  9"
PICTURE_TYPE_EPS = "int  10"
PICTURE_TYPE_BMP = "int  11"
PICTURE_TYPE_WPG = "int  12"
def ():
    '''returns SheetIterator\n\n
    ()\n
    (final XSSFWorkbookType workbookType)\n
    (final OPCPackage pkg)\n
    (final InputStream is)\n
    (final File file)\n
    (final String path)\n
    ()\n
    '''
def parseSheet():
    '''returns None\n\n
    parseSheet(final Map<String, XSSFSheet> shIdMap, final CTSheet ctSheet)\n
    '''
def getCTWorkbook():
    '''returns CTWorkbook\n\n
    getCTWorkbook()\n
    '''
def addPicture():
    '''returns int\n\n
    addPicture(final byte[] pictureData, final int format)\n
    addPicture(final InputStream is, final int format)\n
    '''
def cloneSheet():
    '''returns XSSFSheet\n\n
    cloneSheet(final int sheetNum)\n
    cloneSheet(final int sheetNum, String newName)\n
    '''
def createCellStyle():
    '''returns XSSFCellStyle\n\n
    createCellStyle()\n
    '''
def createDataFormat():
    '''returns XSSFDataFormat\n\n
    createDataFormat()\n
    '''
def createFont():
    '''returns XSSFFont\n\n
    createFont()\n
    '''
def createName():
    '''returns XSSFName\n\n
    createName()\n
    '''
def createSheet():
    '''returns XSSFSheet\n\n
    createSheet()\n
    createSheet(String sheetname)\n
    '''
def findFont():
    '''returns XSSFFont\n\n
    findFont(final boolean bold, final short color, final short fontHeight, final String name, final boolean italic, final boolean strikeout, final short typeOffset, final byte underline)\n
    '''
def getActiveSheetIndex():
    '''returns int\n\n
    getActiveSheetIndex()\n
    '''
def getAllPictures():
    '''returns List<XSSFPictureData>\n\n
    getAllPictures()\n
    '''
def getCellStyleAt():
    '''returns XSSFCellStyle\n\n
    getCellStyleAt(final int idx)\n
    '''
def getFontAt():
    '''returns XSSFFont\n\n
    getFontAt(final short idx)\n
    '''
def getName():
    '''returns XSSFName\n\n
    getName(final String name)\n
    '''
def getNames():
    '''returns List<XSSFName>\n\n
    getNames(final String name)\n
    '''
def getNameAt():
    '''returns XSSFName\n\n
    getNameAt(final int nameIndex)\n
    '''
def getAllNames():
    '''returns List<XSSFName>\n\n
    getAllNames()\n
    '''
def getNameIndex():
    '''returns int\n\n
    getNameIndex(final String name)\n
    '''
def getNumCellStyles():
    '''returns int\n\n
    getNumCellStyles()\n
    '''
def getNumberOfFonts():
    '''returns short\n\n
    getNumberOfFonts()\n
    '''
def getNumberOfNames():
    '''returns int\n\n
    getNumberOfNames()\n
    '''
def getNumberOfSheets():
    '''returns int\n\n
    getNumberOfSheets()\n
    '''
def getPrintArea():
    '''returns String\n\n
    getPrintArea(final int sheetIndex)\n
    '''
def getSheet():
    '''returns XSSFSheet\n\n
    getSheet(final String name)\n
    '''
def getSheetAt():
    '''returns XSSFSheet\n\n
    getSheetAt(final int index)\n
    '''
def getSheetIndex():
    '''returns int\n\n
    getSheetIndex(final String name)\n
    getSheetIndex(final Sheet sheet)\n
    '''
def getSheetName():
    '''returns String\n\n
    getSheetName(final int sheetIx)\n
    '''
def sheetIterator():
    '''returns Iterator<Sheet>\n\n
    sheetIterator()\n
    '''
def iterator():
    '''returns Iterator<Sheet>\n\n
    iterator()\n
    '''
def isMacroEnabled():
    '''returns boolean\n\n
    isMacroEnabled()\n
    '''
def removeName():
    '''returns None\n\n
    removeName(final int nameIndex)\n
    removeName(final String name)\n
    removeName(final Name name)\n
    '''
def removePrintArea():
    '''returns None\n\n
    removePrintArea(final int sheetIndex)\n
    '''
def removeSheetAt():
    '''returns None\n\n
    removeSheetAt(final int index)\n
    '''
def setMissingCellPolicy():
    '''returns None\n\n
    setMissingCellPolicy(final Row.MissingCellPolicy missingCellPolicy)\n
    '''
def setActiveSheet():
    '''returns None\n\n
    setActiveSheet(final int index)\n
    '''
def getFirstVisibleTab():
    '''returns int\n\n
    getFirstVisibleTab()\n
    '''
def setFirstVisibleTab():
    '''returns None\n\n
    setFirstVisibleTab(final int index)\n
    '''
def setPrintArea():
    '''returns None\n\n
    setPrintArea(final int sheetIndex, final String reference)\n
    setPrintArea(final int sheetIndex, final int startColumn, final int endColumn, final int startRow, final int endRow)\n
    '''
def setSelectedTab():
    '''returns None\n\n
    setSelectedTab(final int index)\n
    '''
def setSheetName():
    '''returns None\n\n
    setSheetName(final int sheetIndex, String sheetname)\n
    '''
def setSheetOrder():
    '''returns None\n\n
    setSheetOrder(final String sheetname, final int pos)\n
    '''
def getSharedStringSource():
    '''returns SharedStringsTable\n\n
    getSharedStringSource()\n
    '''
def getStylesSource():
    '''returns StylesTable\n\n
    getStylesSource()\n
    '''
def getTheme():
    '''returns ThemesTable\n\n
    getTheme()\n
    '''
def getCreationHelper():
    '''returns XSSFCreationHelper\n\n
    getCreationHelper()\n
    '''
def isDate1904():
    '''returns boolean\n\n
    isDate1904()\n
    '''
def getAllEmbedds():
    '''returns List<PackagePart>\n\n
    getAllEmbedds()\n
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
    setSheetHidden(final int sheetIx, final int state)\n
    '''
def setSheetVisibility():
    '''returns None\n\n
    setSheetVisibility(final int sheetIx, final SheetVisibility visibility)\n
    '''
def getCalculationChain():
    '''returns CalculationChain\n\n
    getCalculationChain()\n
    '''
def getExternalLinksTable():
    '''returns List<ExternalLinksTable>\n\n
    getExternalLinksTable()\n
    '''
def getCustomXMLMappings():
    '''returns Collection<XSSFMap>\n\n
    getCustomXMLMappings()\n
    '''
def getMapInfo():
    '''returns MapInfo\n\n
    getMapInfo()\n
    '''
def linkExternalWorkbook():
    '''returns int\n\n
    linkExternalWorkbook(final String name, final Workbook workbook)\n
    '''
def isStructureLocked():
    '''returns boolean\n\n
    isStructureLocked()\n
    '''
def isWindowsLocked():
    '''returns boolean\n\n
    isWindowsLocked()\n
    '''
def isRevisionLocked():
    '''returns boolean\n\n
    isRevisionLocked()\n
    '''
def lockStructure():
    '''returns None\n\n
    lockStructure()\n
    '''
def unLockStructure():
    '''returns None\n\n
    unLockStructure()\n
    '''
def lockWindows():
    '''returns None\n\n
    lockWindows()\n
    '''
def unLockWindows():
    '''returns None\n\n
    unLockWindows()\n
    '''
def lockRevision():
    '''returns None\n\n
    lockRevision()\n
    '''
def unLockRevision():
    '''returns None\n\n
    unLockRevision()\n
    '''
def setWorkbookPassword():
    '''returns None\n\n
    setWorkbookPassword(final String password, final HashAlgorithm hashAlgo)\n
    '''
def validateWorkbookPassword():
    '''returns boolean\n\n
    validateWorkbookPassword(final String password)\n
    '''
def setRevisionsPassword():
    '''returns None\n\n
    setRevisionsPassword(final String password, final HashAlgorithm hashAlgo)\n
    '''
def validateRevisionsPassword():
    '''returns boolean\n\n
    validateRevisionsPassword(final String password)\n
    '''
def unLock():
    '''returns None\n\n
    unLock()\n
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
def getPivotTables():
    '''returns List<XSSFPivotTable>\n\n
    getPivotTables()\n
    '''
def getWorkbookType():
    '''returns XSSFWorkbookType\n\n
    getWorkbookType()\n
    '''
def setWorkbookType():
    '''returns None\n\n
    setWorkbookType(final XSSFWorkbookType type)\n
    '''
def setVBAProject():
    '''returns None\n\n
    setVBAProject(final InputStream vbaProjectStream)\n
    setVBAProject(final XSSFWorkbook macroWorkbook)\n
    '''
def getSpreadsheetVersion():
    '''returns SpreadsheetVersion\n\n
    getSpreadsheetVersion()\n
    '''
def getTable():
    '''returns XSSFTable\n\n
    getTable(final String name)\n
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
