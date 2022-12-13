sid = "short  23"
ENCODED_SIZE = "int  6"
def ExternSheetRecord():
'''public ExternSheetRecord()
public ExternSheetRecord(final RecordInputStream in)
'''
pass
def getNumOfRefs():
'''public int getNumOfRefs()
'''
pass
def addREFRecord():
'''public void addREFRecord(final RefSubRecord rec)
'''
pass
def getNumOfREFRecords():
'''public int getNumOfREFRecords()
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def serialize():
'''public void serialize(final LittleEndianOutput out)
public void serialize(final LittleEndianOutput out)
'''
pass
def removeSheet():
'''public void removeSheet(final int sheetIdx)
'''
pass
def getSid():
'''public short getSid()
'''
pass
def getExtbookIndexFromRefIndex():
'''public int getExtbookIndexFromRefIndex(final int refIndex)
'''
pass
def findRefIndexFromExtBookIndex():
'''public int findRefIndexFromExtBookIndex(final int extBookIndex)
'''
pass
def getFirstSheetIndexFromRefIndex():
'''public int getFirstSheetIndexFromRefIndex(final int extRefIndex)
'''
pass
def getLastSheetIndexFromRefIndex():
'''public int getLastSheetIndexFromRefIndex(final int extRefIndex)
'''
pass
def addRef():
'''public int addRef(final int extBookIndex, final int firstSheetIndex, final int lastSheetIndex)
'''
pass
def getRefIxForSheet():
'''public int getRefIxForSheet(final int externalBookIndex, final int firstSheetIndex, final int lastSheetIndex)
'''
pass
def combine():
'''public static ExternSheetRecord combine(final ExternSheetRecord[] esrs)
'''
pass
def adjustIndex():
'''public void adjustIndex(final int offset)
'''
pass
def RefSubRecord():
'''public RefSubRecord(final int extBookIndex, final int firstSheetIndex, final int lastSheetIndex)
public RefSubRecord(final RecordInputStream in)
'''
pass
def getExtBookIndex():
'''public int getExtBookIndex()
'''
pass
def getFirstSheetIndex():
'''public int getFirstSheetIndex()
'''
pass
def getLastSheetIndex():
'''public int getLastSheetIndex()
'''
pass
