OLD_WORKBOOK_DIR_ENTRY_NAME = "String  \"Book\""
def createWorkbook():
    '''public static InternalWorkbook createWorkbook(final List<Record> recs)
    public static InternalWorkbook createWorkbook()
    '''
def getSpecificBuiltinRecord():
    '''public NameRecord getSpecificBuiltinRecord(final byte name, final int sheetNumber)
    '''
def removeBuiltinRecord():
    '''public void removeBuiltinRecord(final byte name, final int sheetIndex)
    '''
def getNumRecords():
    '''public int getNumRecords()
    '''
def getFontRecordAt():
    '''public FontRecord getFontRecordAt(final int idx)
    '''
def getFontIndex():
    '''public int getFontIndex(final FontRecord font)
    '''
def createNewFont():
    '''public FontRecord createNewFont()
    '''
def removeFontRecord():
    '''public void removeFontRecord(final FontRecord rec)
    '''
def getNumberOfFontRecords():
    '''public int getNumberOfFontRecords()
    '''
def setSheetBof():
    '''public void setSheetBof(final int sheetIndex, final int pos)
    '''
def getBackupRecord():
    '''public BackupRecord getBackupRecord()
    '''
def setSheetName():
    '''public void setSheetName(final int sheetnum, final String sheetname)
    '''
def doesContainsSheetName():
    '''public boolean doesContainsSheetName(final String name, final int excludeSheetIdx)
    '''
def setSheetOrder():
    '''public void setSheetOrder(final String sheetname, final int pos)
    '''
def getSheetName():
    '''public String getSheetName(final int sheetIndex)
    '''
def isSheetHidden():
    '''public boolean isSheetHidden(final int sheetnum)
    '''
def isSheetVeryHidden():
    '''public boolean isSheetVeryHidden(final int sheetnum)
    '''
def getSheetVisibility():
    '''public SheetVisibility getSheetVisibility(final int sheetnum)
    '''
def setSheetHidden():
    '''public void setSheetHidden(final int sheetnum, final boolean hidden)
    public void setSheetHidden(final int sheetnum, final SheetVisibility visibility)
    '''
def getSheetIndex():
    '''public int getSheetIndex(final String name)
    '''
def removeSheet():
    '''public void removeSheet(final int sheetIndex)
    '''
def getNumSheets():
    '''public int getNumSheets()
    '''
def getNumExFormats():
    '''public int getNumExFormats()
    '''
def getExFormatAt():
    '''public ExtendedFormatRecord getExFormatAt(final int index)
    '''
def removeExFormatRecord():
    '''public void removeExFormatRecord(final ExtendedFormatRecord rec)
    public void removeExFormatRecord(final int index)
    '''
def createCellXF():
    '''public ExtendedFormatRecord createCellXF()
    '''
def getStyleRecord():
    '''public StyleRecord getStyleRecord(final int xfIndex)
    '''
def createStyleRecord():
    '''public StyleRecord createStyleRecord(final int xfIndex)
    '''
def addSSTString():
    '''public int addSSTString(final UnicodeString string)
    '''
def getSSTString():
    '''public UnicodeString getSSTString(final int str)
    '''
def insertSST():
    '''public void insertSST()
    '''
def serialize():
    '''public int serialize(final int offset, final byte[] data)
    '''
def preSerialize():
    '''public void preSerialize()
    '''
def getSize():
    '''public int getSize()
    '''
def linkExternalWorkbook():
    '''public int linkExternalWorkbook(final String name, final Workbook externalWorkbook)
    '''
def findSheetFirstNameFromExternSheet():
    '''public String findSheetFirstNameFromExternSheet(final int externSheetIndex)
    '''
def findSheetLastNameFromExternSheet():
    '''public String findSheetLastNameFromExternSheet(final int externSheetIndex)
    '''
def getFirstSheetIndexFromExternSheetIndex():
    '''public int getFirstSheetIndexFromExternSheetIndex(final int externSheetNumber)
    '''
def getLastSheetIndexFromExternSheetIndex():
    '''public int getLastSheetIndexFromExternSheetIndex(final int externSheetNumber)
    '''
def checkExternSheet():
    '''public short checkExternSheet(final int sheetNumber)
    public short checkExternSheet(final int firstSheetNumber, final int lastSheetNumber)
    '''
def getExternalSheetIndex():
    '''public int getExternalSheetIndex(final String workbookName, final String sheetName)
    public int getExternalSheetIndex(final String workbookName, final String firstSheetName, final String lastSheetName)
    '''
def getNumNames():
    '''public int getNumNames()
    '''
def getNameRecord():
    '''public NameRecord getNameRecord(final int index)
    '''
def getNameCommentRecord():
    '''public NameCommentRecord getNameCommentRecord(final NameRecord nameRecord)
    '''
def createName():
    '''public NameRecord createName()
    '''
def addName():
    '''public NameRecord addName(final NameRecord name)
    '''
def createBuiltInName():
    '''public NameRecord createBuiltInName(final byte builtInName, final int sheetNumber)
    '''
def removeName():
    '''public void removeName(final int nameIndex)
    '''
def updateNameCommentRecordCache():
    '''public void updateNameCommentRecordCache(final NameCommentRecord commentRecord)
    '''
def getFormat():
    '''public short getFormat(final String format, final boolean createIfNotFound)
    '''
def getFormats():
    '''public List<FormatRecord> getFormats()
    '''
def createFormat():
    '''public int createFormat(final String formatString)
    '''
def findFirstRecordBySid():
    '''public Record findFirstRecordBySid(final short sid)
    '''
def findFirstRecordLocBySid():
    '''public int findFirstRecordLocBySid(final short sid)
    '''
def findNextRecordBySid():
    '''public Record findNextRecordBySid(final short sid, final int pos)
    '''
def getHyperlinks():
    '''public List<HyperlinkRecord> getHyperlinks()
    '''
def getRecords():
    '''public List<Record> getRecords()
    '''
def isUsing1904DateWindowing():
    '''public boolean isUsing1904DateWindowing()
    '''
def getCustomPalette():
    '''public PaletteRecord getCustomPalette()
    '''
def findDrawingGroup():
    '''public DrawingManager2 findDrawingGroup()
    '''
def createDrawingGroup():
    '''public void createDrawingGroup()
    '''
def getWindowOne():
    '''public WindowOneRecord getWindowOne()
    '''
def getBSERecord():
    '''public EscherBSERecord getBSERecord(final int pictureIndex)
    '''
def addBSERecord():
    '''public int addBSERecord(final EscherBSERecord e)
    '''
def getDrawingManager():
    '''public DrawingManager2 getDrawingManager()
    '''
def getWriteProtect():
    '''public WriteProtectRecord getWriteProtect()
    '''
def getWriteAccess():
    '''public WriteAccessRecord getWriteAccess()
    '''
def getFileSharing():
    '''public FileSharingRecord getFileSharing()
    '''
def isWriteProtected():
    '''public boolean isWriteProtected()
    '''
def writeProtectWorkbook():
    '''public void writeProtectWorkbook(final String password, final String username)
    '''
def unwriteProtectWorkbook():
    '''public void unwriteProtectWorkbook()
    '''
def resolveNameXText():
    '''public String resolveNameXText(final int refIndex, final int definedNameIndex)
    '''
def getNameXPtg():
    '''public NameXPtg getNameXPtg(final String name, final int sheetRefIndex, final UDFFinder udf)
    public NameXPtg getNameXPtg(final String name, final UDFFinder udf)
    '''
def cloneDrawings():
    '''public void cloneDrawings(final InternalSheet sheet)
    '''
def cloneFilter():
    '''public NameRecord cloneFilter(final int filterDbNameIndex, final int newSheetIndex)
    '''
def updateNamesAfterCellShift():
    '''public void updateNamesAfterCellShift(final FormulaShifter shifter)
    '''
def getRecalcId():
    '''public RecalcIdRecord getRecalcId()
    '''
def changeExternalReference():
    '''public boolean changeExternalReference(final String oldUrl, final String newUrl)
    '''
def getWorkbookRecordList():
    '''public WorkbookRecordList getWorkbookRecordList()
    '''
