sid = "short  2057"
biff2_sid = "short  9"
biff3_sid = "short  521"
biff4_sid = "short  1033"
biff5_sid = "short  2057"
VERSION = "int  1536"
BUILD = "int  4307"
BUILD_YEAR = "int  1996"
HISTORY_MASK = "int  65"
TYPE_WORKBOOK = "int  5"
TYPE_VB_MODULE = "int  6"
TYPE_WORKSHEET = "int  16"
TYPE_CHART = "int  32"
TYPE_EXCEL_4_MACRO = "int  64"
TYPE_WORKSPACE_FILE = "int  256"
def ():
    '''returns BOFRecord\n\n
    ()\n
    (final RecordInputStream in)\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final int version)\n
    '''
def setType():
    '''returns None\n\n
    setType(final int type)\n
    '''
def setBuild():
    '''returns None\n\n
    setBuild(final int build)\n
    '''
def setBuildYear():
    '''returns None\n\n
    setBuildYear(final int year)\n
    '''
def setHistoryBitMask():
    '''returns None\n\n
    setHistoryBitMask(final int bitmask)\n
    '''
def setRequiredVersion():
    '''returns None\n\n
    setRequiredVersion(final int version)\n
    '''
def getVersion():
    '''returns int\n\n
    getVersion()\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def getBuild():
    '''returns int\n\n
    getBuild()\n
    '''
def getBuildYear():
    '''returns int\n\n
    getBuildYear()\n
    '''
def getHistoryBitMask():
    '''returns int\n\n
    getHistoryBitMask()\n
    '''
def getRequiredVersion():
    '''returns int\n\n
    getRequiredVersion()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final LittleEndianOutput out)\n
    '''
def getSid():
    '''returns short\n\n
    getSid()\n
    '''
def clone():
    '''returns BOFRecord\n\n
    clone()\n
    '''
