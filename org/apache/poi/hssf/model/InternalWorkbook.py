OLD_WORKBOOK_DIR_ENTRY_NAME = "String  \"Book\""
def getSpecificBuiltinRecord():
    '''returns NameRecord\n\n
    getSpecificBuiltinRecord(final byte name, final int sheetNumber)\n
    '''
def removeBuiltinRecord():
    '''returns None\n\n
    removeBuiltinRecord(final byte name, final int sheetIndex)\n
    '''
def getNumRecords():
    '''returns int\n\n
    getNumRecords()\n
    '''
def getFontRecordAt():
    '''returns FontRecord\n\n
    getFontRecordAt(final int idx)\n
    '''
def getFontIndex():
    '''returns int\n\n
    getFontIndex(final FontRecord font)\n
    '''
def createNewFont():
    '''returns FontRecord\n\n
    createNewFont()\n
    '''
def removeFontRecord():
    '''returns None\n\n
    removeFontRecord(final FontRecord rec)\n
    '''
def getNumberOfFontRecords():
    '''returns int\n\n
    getNumberOfFontRecords()\n
    '''
def setSheetBof():
    '''returns None\n\n
    setSheetBof(final int sheetIndex, final int pos)\n
    '''
def getBackupRecord():
    '''returns BackupRecord\n\n
    getBackupRecord()\n
    '''
def setSheetName():
    '''returns None\n\n
    setSheetName(final int sheetnum, final String sheetname)\n
    '''
def doesContainsSheetName():
    '''returns boolean\n\n
    doesContainsSheetName(final String name, final int excludeSheetIdx)\n
    '''
def setSheetOrder():
    '''returns None\n\n
    setSheetOrder(final String sheetname, final int pos)\n
    '''
def getSheetName():
    '''returns String\n\n
    getSheetName(final int sheetIndex)\n
    '''
def isSheetHidden():
    '''returns boolean\n\n
    isSheetHidden(final int sheetnum)\n
    '''
def isSheetVeryHidden():
    '''returns boolean\n\n
    isSheetVeryHidden(final int sheetnum)\n
    '''
def getSheetVisibility():
    '''returns SheetVisibility\n\n
    getSheetVisibility(final int sheetnum)\n
    '''
def setSheetHidden():
    '''returns None\n\n
    setSheetHidden(final int sheetnum, final boolean hidden)\n
    setSheetHidden(final int sheetnum, final SheetVisibility visibility)\n
    '''
def getSheetIndex():
    '''returns int\n\n
    getSheetIndex(final String name)\n
    '''
def removeSheet():
    '''returns None\n\n
    removeSheet(final int sheetIndex)\n
    '''
def getNumSheets():
    '''returns int\n\n
    getNumSheets()\n
    '''
def getNumExFormats():
    '''returns int\n\n
    getNumExFormats()\n
    '''
def getExFormatAt():
    '''returns ExtendedFormatRecord\n\n
    getExFormatAt(final int index)\n
    '''
def removeExFormatRecord():
    '''returns None\n\n
    removeExFormatRecord(final ExtendedFormatRecord rec)\n
    removeExFormatRecord(final int index)\n
    '''
def createCellXF():
    '''returns ExtendedFormatRecord\n\n
    createCellXF()\n
    '''
def getStyleRecord():
    '''returns StyleRecord\n\n
    getStyleRecord(final int xfIndex)\n
    '''
def createStyleRecord():
    '''returns StyleRecord\n\n
    createStyleRecord(final int xfIndex)\n
    '''
def addSSTString():
    '''returns int\n\n
    addSSTString(final UnicodeString string)\n
    '''
def getSSTString():
    '''returns UnicodeString\n\n
    getSSTString(final int str)\n
    '''
def insertSST():
    '''returns None\n\n
    insertSST()\n
    '''
def serialize():
    '''returns int\n\n
    serialize(final int offset, final byte[] data)\n
    '''
def preSerialize():
    '''returns None\n\n
    preSerialize()\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def linkExternalWorkbook():
    '''returns int\n\n
    linkExternalWorkbook(final String name, final Workbook externalWorkbook)\n
    '''
def findSheetFirstNameFromExternSheet():
    '''returns String\n\n
    findSheetFirstNameFromExternSheet(final int externSheetIndex)\n
    '''
def findSheetLastNameFromExternSheet():
    '''returns String\n\n
    findSheetLastNameFromExternSheet(final int externSheetIndex)\n
    '''
def getFirstSheetIndexFromExternSheetIndex():
    '''returns int\n\n
    getFirstSheetIndexFromExternSheetIndex(final int externSheetNumber)\n
    '''
def getLastSheetIndexFromExternSheetIndex():
    '''returns int\n\n
    getLastSheetIndexFromExternSheetIndex(final int externSheetNumber)\n
    '''
def checkExternSheet():
    '''returns short\n\n
    checkExternSheet(final int sheetNumber)\n
    checkExternSheet(final int firstSheetNumber, final int lastSheetNumber)\n
    '''
def getExternalSheetIndex():
    '''returns int\n\n
    getExternalSheetIndex(final String workbookName, final String sheetName)\n
    getExternalSheetIndex(final String workbookName, final String firstSheetName, final String lastSheetName)\n
    '''
def getNumNames():
    '''returns int\n\n
    getNumNames()\n
    '''
def getNameRecord():
    '''returns NameRecord\n\n
    getNameRecord(final int index)\n
    '''
def getNameCommentRecord():
    '''returns NameCommentRecord\n\n
    getNameCommentRecord(final NameRecord nameRecord)\n
    '''
def createName():
    '''returns NameRecord\n\n
    createName()\n
    '''
def addName():
    '''returns NameRecord\n\n
    addName(final NameRecord name)\n
    '''
def createBuiltInName():
    '''returns NameRecord\n\n
    createBuiltInName(final byte builtInName, final int sheetNumber)\n
    '''
def removeName():
    '''returns None\n\n
    removeName(final int nameIndex)\n
    '''
def updateNameCommentRecordCache():
    '''returns None\n\n
    updateNameCommentRecordCache(final NameCommentRecord commentRecord)\n
    '''
def getFormat():
    '''returns short\n\n
    getFormat(final String format, final boolean createIfNotFound)\n
    '''
def getFormats():
    '''returns List<FormatRecord>\n\n
    getFormats()\n
    '''
def createFormat():
    '''returns int\n\n
    createFormat(final String formatString)\n
    '''
def findFirstRecordBySid():
    '''returns Record\n\n
    findFirstRecordBySid(final short sid)\n
    '''
def findFirstRecordLocBySid():
    '''returns int\n\n
    findFirstRecordLocBySid(final short sid)\n
    '''
def findNextRecordBySid():
    '''returns Record\n\n
    findNextRecordBySid(final short sid, final int pos)\n
    '''
def getHyperlinks():
    '''returns List<HyperlinkRecord>\n\n
    getHyperlinks()\n
    '''
def getRecords():
    '''returns List<Record>\n\n
    getRecords()\n
    '''
def isUsing1904DateWindowing():
    '''returns boolean\n\n
    isUsing1904DateWindowing()\n
    '''
def getCustomPalette():
    '''returns PaletteRecord\n\n
    getCustomPalette()\n
    '''
def findDrawingGroup():
    '''returns DrawingManager2\n\n
    findDrawingGroup()\n
    '''
def createDrawingGroup():
    '''returns None\n\n
    createDrawingGroup()\n
    '''
def getWindowOne():
    '''returns WindowOneRecord\n\n
    getWindowOne()\n
    '''
def getBSERecord():
    '''returns EscherBSERecord\n\n
    getBSERecord(final int pictureIndex)\n
    '''
def addBSERecord():
    '''returns int\n\n
    addBSERecord(final EscherBSERecord e)\n
    '''
def getDrawingManager():
    '''returns DrawingManager2\n\n
    getDrawingManager()\n
    '''
def getWriteProtect():
    '''returns WriteProtectRecord\n\n
    getWriteProtect()\n
    '''
def getWriteAccess():
    '''returns WriteAccessRecord\n\n
    getWriteAccess()\n
    '''
def getFileSharing():
    '''returns FileSharingRecord\n\n
    getFileSharing()\n
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
def resolveNameXText():
    '''returns String\n\n
    resolveNameXText(final int refIndex, final int definedNameIndex)\n
    '''
def getNameXPtg():
    '''returns NameXPtg\n\n
    getNameXPtg(final String name, final int sheetRefIndex, final UDFFinder udf)\n
    getNameXPtg(final String name, final UDFFinder udf)\n
    '''
def cloneDrawings():
    '''returns None\n\n
    cloneDrawings(final InternalSheet sheet)\n
    '''
def cloneFilter():
    '''returns NameRecord\n\n
    cloneFilter(final int filterDbNameIndex, final int newSheetIndex)\n
    '''
def updateNamesAfterCellShift():
    '''returns None\n\n
    updateNamesAfterCellShift(final FormulaShifter shifter)\n
    '''
def getRecalcId():
    '''returns RecalcIdRecord\n\n
    getRecalcId()\n
    '''
def changeExternalReference():
    '''returns boolean\n\n
    changeExternalReference(final String oldUrl, final String newUrl)\n
    '''
def getWorkbookRecordList():
    '''returns WorkbookRecordList\n\n
    getWorkbookRecordList()\n
    '''
