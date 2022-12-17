sid = "short  23"
ENCODED_SIZE = "int  6"
def ():
    '''returns RefSubRecord\n\n
    ()\n
    (final RecordInputStream in)\n
    (final int extBookIndex, final int firstSheetIndex, final int lastSheetIndex)\n
    (final RecordInputStream in)\n
    '''
def getNumOfRefs():
    '''returns int\n\n
    getNumOfRefs()\n
    '''
def addREFRecord():
    '''returns None\n\n
    addREFRecord(final RefSubRecord rec)\n
    '''
def getNumOfREFRecords():
    '''returns int\n\n
    getNumOfREFRecords()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final LittleEndianOutput out)\n
    serialize(final LittleEndianOutput out)\n
    '''
def removeSheet():
    '''returns None\n\n
    removeSheet(final int sheetIdx)\n
    '''
def getSid():
    '''returns short\n\n
    getSid()\n
    '''
def getExtbookIndexFromRefIndex():
    '''returns int\n\n
    getExtbookIndexFromRefIndex(final int refIndex)\n
    '''
def findRefIndexFromExtBookIndex():
    '''returns int\n\n
    findRefIndexFromExtBookIndex(final int extBookIndex)\n
    '''
def getFirstSheetIndexFromRefIndex():
    '''returns int\n\n
    getFirstSheetIndexFromRefIndex(final int extRefIndex)\n
    '''
def getLastSheetIndexFromRefIndex():
    '''returns int\n\n
    getLastSheetIndexFromRefIndex(final int extRefIndex)\n
    '''
def addRef():
    '''returns int\n\n
    addRef(final int extBookIndex, final int firstSheetIndex, final int lastSheetIndex)\n
    '''
def getRefIxForSheet():
    '''returns int\n\n
    getRefIxForSheet(final int externalBookIndex, final int firstSheetIndex, final int lastSheetIndex)\n
    '''
def adjustIndex():
    '''returns None\n\n
    adjustIndex(final int offset)\n
    '''
def getExtBookIndex():
    '''returns int\n\n
    getExtBookIndex()\n
    '''
def getFirstSheetIndex():
    '''returns int\n\n
    getFirstSheetIndex()\n
    '''
def getLastSheetIndex():
    '''returns int\n\n
    getLastSheetIndex()\n
    '''
