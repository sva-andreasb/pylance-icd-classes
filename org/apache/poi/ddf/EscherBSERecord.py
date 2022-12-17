RECORD_ID = "short  -4089"
RECORD_DESCRIPTION = "String  \"MsofbtBSE\""
BT_ERROR = "byte  0"
BT_UNKNOWN = "byte  1"
BT_EMF = "byte  2"
BT_WMF = "byte  3"
BT_PICT = "byte  4"
BT_JPEG = "byte  5"
BT_PNG = "byte  6"
BT_DIB = "byte  7"
def ():
    '''returns EscherBSERecord\n\n
    ()\n
    '''
def fillFields():
    '''returns int\n\n
    fillFields(final byte[] data, final int offset, final EscherRecordFactory recordFactory)\n
    '''
def serialize():
    '''returns int\n\n
    serialize(final int offset, final byte[] data, final EscherSerializationListener listener)\n
    '''
def getRecordSize():
    '''returns int\n\n
    getRecordSize()\n
    '''
def getRecordName():
    '''returns String\n\n
    getRecordName()\n
    '''
def getBlipTypeWin32():
    '''returns byte\n\n
    getBlipTypeWin32()\n
    '''
def setBlipTypeWin32():
    '''returns None\n\n
    setBlipTypeWin32(final byte blipTypeWin32)\n
    '''
def getBlipTypeMacOS():
    '''returns byte\n\n
    getBlipTypeMacOS()\n
    '''
def setBlipTypeMacOS():
    '''returns None\n\n
    setBlipTypeMacOS(final byte blipTypeMacOS)\n
    '''
def getUid():
    '''returns byte[]\n\n
    getUid()\n
    '''
def setUid():
    '''returns None\n\n
    setUid(final byte[] uid)\n
    '''
def getTag():
    '''returns short\n\n
    getTag()\n
    '''
def setTag():
    '''returns None\n\n
    setTag(final short tag)\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def setSize():
    '''returns None\n\n
    setSize(final int size)\n
    '''
def getRef():
    '''returns int\n\n
    getRef()\n
    '''
def setRef():
    '''returns None\n\n
    setRef(final int ref)\n
    '''
def getOffset():
    '''returns int\n\n
    getOffset()\n
    '''
def setOffset():
    '''returns None\n\n
    setOffset(final int offset)\n
    '''
def getUsage():
    '''returns byte\n\n
    getUsage()\n
    '''
def setUsage():
    '''returns None\n\n
    setUsage(final byte usage)\n
    '''
def getName():
    '''returns byte\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final byte name)\n
    '''
def getUnused2():
    '''returns byte\n\n
    getUnused2()\n
    '''
def setUnused2():
    '''returns None\n\n
    setUnused2(final byte unused2)\n
    '''
def getUnused3():
    '''returns byte\n\n
    getUnused3()\n
    '''
def setUnused3():
    '''returns None\n\n
    setUnused3(final byte unused3)\n
    '''
def getBlipRecord():
    '''returns EscherBlipRecord\n\n
    getBlipRecord()\n
    '''
def setBlipRecord():
    '''returns None\n\n
    setBlipRecord(final EscherBlipRecord blipRecord)\n
    '''
def getRemainingData():
    '''returns byte[]\n\n
    getRemainingData()\n
    '''
def setRemainingData():
    '''returns None\n\n
    setRemainingData(final byte[] remainingData)\n
    '''
