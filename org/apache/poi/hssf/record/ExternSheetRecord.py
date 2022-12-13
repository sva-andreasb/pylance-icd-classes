sid = "short  23"
ENCODED_SIZE = "int  6"
def ExternSheetRecord():
    '''    public ExternSheetRecord()
    public ExternSheetRecord(final RecordInputStream in)
    '''
def getNumOfRefs():
    '''    public int getNumOfRefs()
    '''
def addREFRecord():
    '''    public void addREFRecord(final RefSubRecord rec)
    '''
def getNumOfREFRecords():
    '''    public int getNumOfREFRecords()
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def serialize():
    '''    public void serialize(final LittleEndianOutput out)
    public void serialize(final LittleEndianOutput out)
    '''
def removeSheet():
    '''    public void removeSheet(final int sheetIdx)
    '''
def getSid():
    '''    public short getSid()
    '''
def getExtbookIndexFromRefIndex():
    '''    public int getExtbookIndexFromRefIndex(final int refIndex)
    '''
def findRefIndexFromExtBookIndex():
    '''    public int findRefIndexFromExtBookIndex(final int extBookIndex)
    '''
def getFirstSheetIndexFromRefIndex():
    '''    public int getFirstSheetIndexFromRefIndex(final int extRefIndex)
    '''
def getLastSheetIndexFromRefIndex():
    '''    public int getLastSheetIndexFromRefIndex(final int extRefIndex)
    '''
def addRef():
    '''    public int addRef(final int extBookIndex, final int firstSheetIndex, final int lastSheetIndex)
    '''
def getRefIxForSheet():
    '''    public int getRefIxForSheet(final int externalBookIndex, final int firstSheetIndex, final int lastSheetIndex)
    '''
def combine():
    '''    public static ExternSheetRecord combine(final ExternSheetRecord[] esrs)
    '''
def adjustIndex():
    '''    public void adjustIndex(final int offset)
    '''
def RefSubRecord():
    '''    public RefSubRecord(final int extBookIndex, final int firstSheetIndex, final int lastSheetIndex)
    public RefSubRecord(final RecordInputStream in)
    '''
def getExtBookIndex():
    '''    public int getExtBookIndex()
    '''
def getFirstSheetIndex():
    '''    public int getFirstSheetIndex()
    '''
def getLastSheetIndex():
    '''    public int getLastSheetIndex()
    '''
