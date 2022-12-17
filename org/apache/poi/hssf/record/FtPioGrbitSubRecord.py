sid = "short  8"
length = "short  2"
AUTO_PICT_BIT = "int  1"
DDE_BIT = "int  2"
PRINT_CALC_BIT = "int  4"
ICON_BIT = "int  8"
CTL_BIT = "int  16"
PRSTM_BIT = "int  32"
CAMERA_BIT = "int  128"
DEFAULT_SIZE_BIT = "int  256"
AUTO_LOAD_BIT = "int  512"
def ():
    '''returns FtPioGrbitSubRecord\n\n
    ()\n
    (final LittleEndianInput in, final int size)\n
    '''
def setFlagByBit():
    '''returns None\n\n
    setFlagByBit(final int bitmask, final boolean enabled)\n
    '''
def getFlagByBit():
    '''returns boolean\n\n
    getFlagByBit(final int bitmask)\n
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
    '''returns FtPioGrbitSubRecord\n\n
    clone()\n
    '''
def getFlags():
    '''returns short\n\n
    getFlags()\n
    '''
def setFlags():
    '''returns None\n\n
    setFlags(final short flags)\n
    '''
