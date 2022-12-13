OLD_WORKBOOK_DIR_ENTRY_NAME = "String  Book""
def createWorkbook():
'''public static InternalWorkbook createWorkbook(final List<Record> recs)
public static InternalWorkbook createWorkbook()
'''
pass
def getSpecificBuiltinRecord():
'''public NameRecord getSpecificBuiltinRecord(final byte name, final int sheetNumber)
'''
pass
def removeBuiltinRecord():
'''public void removeBuiltinRecord(final byte name, final int sheetIndex)
'''
pass
def getNumRecords():
'''public int getNumRecords()
'''
pass
def getFontRecordAt():
'''public FontRecord getFontRecordAt(final int idx)
'''
pass
def getFontIndex():
'''public int getFontIndex(final FontRecord font)
'''
pass
def createNewFont():
'''public FontRecord createNewFont()
'''
pass
def removeFontRecord():
'''public void removeFontRecord(final FontRecord rec)
'''
pass
def getNumberOfFontRecords():
'''public int getNumberOfFontRecords()
'''
pass
def setSheetBof():
'''public void setSheetBof(final int sheetIndex, final int pos)
'''
pass
def getBackupRecord():
'''public BackupRecord getBackupRecord()
'''
pass
def setSheetName():
'''public void setSheetName(final int sheetnum, final String sheetname)
'''
pass
def doesContainsSheetName():
'''public boolean doesContainsSheetName(final String name, final int excludeSheetIdx)
'''
pass
def setSheetOrder():
'''public void setSheetOrder(final String sheetname, final int pos)
'''
pass
def getSheetName():
'''public String getSheetName(final int sheetIndex)
'''
pass
def isSheetHidden():
'''public boolean isSheetHidden(final int sheetnum)
'''
pass
def isSheetVeryHidden():
'''public boolean isSheetVeryHidden(final int sheetnum)
'''
pass
def getSheetVisibility():
'''public SheetVisibility getSheetVisibility(final int sheetnum)
'''
pass
def setSheetHidden():
'''public void setSheetHidden(final int sheetnum, final boolean hidden)
public void setSheetHidden(final int sheetnum, final SheetVisibility visibility)
'''
pass
def getSheetIndex():
'''public int getSheetIndex(final String name)
'''
pass
def removeSheet():
'''public void removeSheet(final int sheetIndex)
'''
pass
def getNumSheets():
'''public int getNumSheets()
'''
pass
def getNumExFormats():
'''public int getNumExFormats()
'''
pass
def getExFormatAt():
'''public ExtendedFormatRecord getExFormatAt(final int index)
'''
pass
def removeExFormatRecord():
'''public void removeExFormatRecord(final ExtendedFormatRecord rec)
public void removeExFormatRecord(final int index)
'''
pass
def createCellXF():
'''public ExtendedFormatRecord createCellXF()
'''
pass
def getStyleRecord():
'''public StyleRecord getStyleRecord(final int xfIndex)
'''
pass
def createStyleRecord():
'''public StyleRecord createStyleRecord(final int xfIndex)
'''
pass
def addSSTString():
'''public int addSSTString(final UnicodeString string)
'''
pass
def getSSTString():
'''public UnicodeString getSSTString(final int str)
'''
pass
def insertSST():
'''public void insertSST()
'''
pass
def serialize():
'''public int serialize(final int offset, final byte[] data)
'''
pass
def preSerialize():
'''public void preSerialize()
'''
pass
def getSize():
'''public int getSize()
'''
pass
def linkExternalWorkbook():
'''public int linkExternalWorkbook(final String name, final Workbook externalWorkbook)
'''
pass
def findSheetFirstNameFromExternSheet():
'''public String findSheetFirstNameFromExternSheet(final int externSheetIndex)
'''
pass
def findSheetLastNameFromExternSheet():
'''public String findSheetLastNameFromExternSheet(final int externSheetIndex)
'''
pass
def getFirstSheetIndexFromExternSheetIndex():
'''public int getFirstSheetIndexFromExternSheetIndex(final int externSheetNumber)
'''
pass
def getLastSheetIndexFromExternSheetIndex():
'''public int getLastSheetIndexFromExternSheetIndex(final int externSheetNumber)
'''
pass
def checkExternSheet():
'''public short checkExternSheet(final int sheetNumber)
public short checkExternSheet(final int firstSheetNumber, final int lastSheetNumber)
'''
pass
def getExternalSheetIndex():
'''public int getExternalSheetIndex(final String workbookName, final String sheetName)
public int getExternalSheetIndex(final String workbookName, final String firstSheetName, final String lastSheetName)
'''
pass
def getNumNames():
'''public int getNumNames()
'''
pass
def getNameRecord():
'''public NameRecord getNameRecord(final int index)
'''
pass
def getNameCommentRecord():
'''public NameCommentRecord getNameCommentRecord(final NameRecord nameRecord)
'''
pass
def createName():
'''public NameRecord createName()
'''
pass
def addName():
'''public NameRecord addName(final NameRecord name)
'''
pass
def createBuiltInName():
'''public NameRecord createBuiltInName(final byte builtInName, final int sheetNumber)
'''
pass
def removeName():
'''public void removeName(final int nameIndex)
'''
pass
def updateNameCommentRecordCache():
'''public void updateNameCommentRecordCache(final NameCommentRecord commentRecord)
'''
pass
def getFormat():
'''public short getFormat(final String format, final boolean createIfNotFound)
'''
pass
def getFormats():
'''public List<FormatRecord> getFormats()
'''
pass
def createFormat():
'''public int createFormat(final String formatString)
'''
pass
def findFirstRecordBySid():
'''public Record findFirstRecordBySid(final short sid)
'''
pass
def findFirstRecordLocBySid():
'''public int findFirstRecordLocBySid(final short sid)
'''
pass
def findNextRecordBySid():
'''public Record findNextRecordBySid(final short sid, final int pos)
'''
pass
def getHyperlinks():
'''public List<HyperlinkRecord> getHyperlinks()
'''
pass
def getRecords():
'''public List<Record> getRecords()
'''
pass
def isUsing1904DateWindowing():
'''public boolean isUsing1904DateWindowing()
'''
pass
def getCustomPalette():
'''public PaletteRecord getCustomPalette()
'''
pass
def findDrawingGroup():
'''public DrawingManager2 findDrawingGroup()
'''
pass
def createDrawingGroup():
'''public void createDrawingGroup()
'''
pass
def getWindowOne():
'''public WindowOneRecord getWindowOne()
'''
pass
def getBSERecord():
'''public EscherBSERecord getBSERecord(final int pictureIndex)
'''
pass
def addBSERecord():
'''public int addBSERecord(final EscherBSERecord e)
'''
pass
def getDrawingManager():
'''public DrawingManager2 getDrawingManager()
'''
pass
def getWriteProtect():
'''public WriteProtectRecord getWriteProtect()
'''
pass
def getWriteAccess():
'''public WriteAccessRecord getWriteAccess()
'''
pass
def getFileSharing():
'''public FileSharingRecord getFileSharing()
'''
pass
def isWriteProtected():
'''public boolean isWriteProtected()
'''
pass
def writeProtectWorkbook():
'''public void writeProtectWorkbook(final String password, final String username)
'''
pass
def unwriteProtectWorkbook():
'''public void unwriteProtectWorkbook()
'''
pass
def resolveNameXText():
'''public String resolveNameXText(final int refIndex, final int definedNameIndex)
'''
pass
def getNameXPtg():
'''public NameXPtg getNameXPtg(final String name, final int sheetRefIndex, final UDFFinder udf)
public NameXPtg getNameXPtg(final String name, final UDFFinder udf)
'''
pass
def cloneDrawings():
'''public void cloneDrawings(final InternalSheet sheet)
'''
pass
def cloneFilter():
'''public NameRecord cloneFilter(final int filterDbNameIndex, final int newSheetIndex)
'''
pass
def updateNamesAfterCellShift():
'''public void updateNamesAfterCellShift(final FormulaShifter shifter)
'''
pass
def getRecalcId():
'''public RecalcIdRecord getRecalcId()
'''
pass
def changeExternalReference():
'''public boolean changeExternalReference(final String oldUrl, final String newUrl)
'''
pass
def getWorkbookRecordList():
'''public WorkbookRecordList getWorkbookRecordList()
'''
pass
