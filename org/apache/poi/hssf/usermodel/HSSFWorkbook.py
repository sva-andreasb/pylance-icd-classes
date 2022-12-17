def ():
    '''returns SheetRecordCollector\n\n
    ()\n
    (final POIFSFileSystem fs)\n
    (final NPOIFSFileSystem fs)\n
    (final POIFSFileSystem fs, final boolean preserveNodes)\n
    (final DirectoryNode directory, final POIFSFileSystem fs, final boolean preserveNodes)\n
    (final DirectoryNode directory, final boolean preserveNodes)\n
    (final InputStream s)\n
    (final InputStream s, final boolean preserveNodes)\n
    ()\n
    ()\n
    '''
def setMissingCellPolicy():
    '''returns None\n\n
    setMissingCellPolicy(final Row.MissingCellPolicy missingCellPolicy)\n
    '''
def setSheetOrder():
    '''returns None\n\n
    setSheetOrder(final String sheetname, final int pos)\n
    '''
def setSelectedTab():
    '''returns None\n\n
    setSelectedTab(final int index)\n
    '''
def setSelectedTabs():
    '''returns None\n\n
    setSelectedTabs(final int[] indexes)\n
    setSelectedTabs(final Collection<Integer> indexes)\n
    '''
def getSelectedTabs():
    '''returns Collection<Integer>\n\n
    getSelectedTabs()\n
    '''
def setActiveSheet():
    '''returns None\n\n
    setActiveSheet(final int index)\n
    '''
def getActiveSheetIndex():
    '''returns int\n\n
    getActiveSheetIndex()\n
    '''
def setFirstVisibleTab():
    '''returns None\n\n
    setFirstVisibleTab(final int index)\n
    '''
def getFirstVisibleTab():
    '''returns int\n\n
    getFirstVisibleTab()\n
    '''
def setSheetName():
    '''returns None\n\n
    setSheetName(final int sheetIx, final String name)\n
    '''
def getSheetName():
    '''returns String\n\n
    getSheetName(final int sheetIndex)\n
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
def getSheetIndex():
    '''returns int\n\n
    getSheetIndex(final String name)\n
    getSheetIndex(final Sheet sheet)\n
    '''
def createSheet():
    '''returns HSSFSheet\n\n
    createSheet()\n
    createSheet(final String sheetname)\n
    '''
def cloneSheet():
    '''returns HSSFSheet\n\n
    cloneSheet(final int sheetIndex)\n
    '''
def sheetIterator():
    '''returns Iterator<Sheet>\n\n
    sheetIterator()\n
    '''
def iterator():
    '''returns Iterator<Sheet>\n\n
    iterator()\n
    '''
def getNumberOfSheets():
    '''returns int\n\n
    getNumberOfSheets()\n
    '''
def getSheetAt():
    '''returns HSSFSheet\n\n
    getSheetAt(final int index)\n
    '''
def getSheet():
    '''returns HSSFSheet\n\n
    getSheet(final String name)\n
    '''
def removeSheetAt():
    '''returns None\n\n
    removeSheetAt(final int index)\n
    '''
def setBackupFlag():
    '''returns None\n\n
    setBackupFlag(final boolean backupValue)\n
    '''
def getBackupFlag():
    '''returns boolean\n\n
    getBackupFlag()\n
    '''
def createFont():
    '''returns HSSFFont\n\n
    createFont()\n
    '''
def findFont():
    '''returns HSSFFont\n\n
    findFont(final boolean bold, final short color, final short fontHeight, final String name, final boolean italic, final boolean strikeout, final short typeOffset, final byte underline)\n
    '''
def getNumberOfFonts():
    '''returns short\n\n
    getNumberOfFonts()\n
    '''
def getFontAt():
    '''returns HSSFFont\n\n
    getFontAt(final short idx)\n
    '''
def createCellStyle():
    '''returns HSSFCellStyle\n\n
    createCellStyle()\n
    '''
def getNumCellStyles():
    '''returns int\n\n
    getNumCellStyles()\n
    '''
def getCellStyleAt():
    '''returns HSSFCellStyle\n\n
    getCellStyleAt(final int idx)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def write():
    '''returns None\n\n
    write()\n
    write(final File newFile)\n
    write(final OutputStream stream)\n
    '''
def getBytes():
    '''returns byte[]\n\n
    getBytes()\n
    '''
def getNumberOfNames():
    '''returns int\n\n
    getNumberOfNames()\n
    '''
def getName():
    '''returns HSSFName\n\n
    getName(final String name)\n
    '''
def getNames():
    '''returns List<HSSFName>\n\n
    getNames(final String name)\n
    '''
def getNameAt():
    '''returns HSSFName\n\n
    getNameAt(final int nameIndex)\n
    '''
def getAllNames():
    '''returns List<HSSFName>\n\n
    getAllNames()\n
    '''
def getNameRecord():
    '''returns NameRecord\n\n
    getNameRecord(final int nameIndex)\n
    '''
def getNameName():
    '''returns String\n\n
    getNameName(final int index)\n
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
def createName():
    '''returns HSSFName\n\n
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
def createDataFormat():
    '''returns HSSFDataFormat\n\n
    createDataFormat()\n
    '''
def getCustomPalette():
    '''returns HSSFPalette\n\n
    getCustomPalette()\n
    '''
def insertChartRecord():
    '''returns None\n\n
    insertChartRecord()\n
    '''
def dumpDrawingGroupRecords():
    '''returns None\n\n
    dumpDrawingGroupRecords(final boolean fat)\n
    '''
def addPicture():
    '''returns int\n\n
    addPicture(byte[] pictureData, final int format)\n
    '''
def getAllPictures():
    '''returns List<HSSFPictureData>\n\n
    getAllPictures()\n
    '''
def addOlePackage():
    '''returns int\n\n
    addOlePackage(final POIFSFileSystem poiData, final String label, final String fileName, final String command)\n
    addOlePackage(final byte[] oleData, final String label, final String fileName, final String command)\n
    '''
def linkExternalWorkbook():
    '''returns int\n\n
    linkExternalWorkbook(final String name, final Workbook workbook)\n
    '''
def isWriteProtected():
    '''returns boolean\n\n
    isWriteProtected()\n
    '''
def writeProtectWorkbook():
    '''returns None\n\n
    writeProtectWorkbook(final String password, final String username)\n
    '''
def unwriteProtectWorkbook():
    '''returns None\n\n
    unwriteProtectWorkbook()\n
    '''
def getAllEmbeddedObjects():
    '''returns List<HSSFObjectData>\n\n
    getAllEmbeddedObjects()\n
    '''
def getCreationHelper():
    '''returns HSSFCreationHelper\n\n
    getCreationHelper()\n
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
def changeExternalReference():
    '''returns boolean\n\n
    changeExternalReference(final String oldUrl, final String newUrl)\n
    '''
def getRootDirectory():
    '''returns DirectoryNode\n\n
    getRootDirectory()\n
    '''
def getInternalWorkbook():
    '''returns InternalWorkbook\n\n
    getInternalWorkbook()\n
    '''
def getSpreadsheetVersion():
    '''returns SpreadsheetVersion\n\n
    getSpreadsheetVersion()\n
    '''
def getEncryptionInfo():
    '''returns EncryptionInfo\n\n
    getEncryptionInfo()\n
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
def getTotalSize():
    '''returns int\n\n
    getTotalSize()\n
    '''
def visitRecord():
    '''returns None\n\n
    visitRecord(final Record r)\n
    '''
def serialize():
    '''returns int\n\n
    serialize(final int offset, final byte[] data)\n
    '''
