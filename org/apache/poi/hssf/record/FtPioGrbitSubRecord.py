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
def FtPioGrbitSubRecord():
    '''public FtPioGrbitSubRecord()
    public FtPioGrbitSubRecord(final LittleEndianInput in, final int size)
    '''
def setFlagByBit():
    '''public void setFlagByBit(final int bitmask, final boolean enabled)
    '''
def getFlagByBit():
    '''public boolean getFlagByBit(final int bitmask)
    '''
def toString():
    '''public String toString()
    '''
def serialize():
    '''public void serialize(final LittleEndianOutput out)
    '''
def getSid():
    '''public short getSid()
    '''
def clone():
    '''public FtPioGrbitSubRecord clone()
    '''
def getFlags():
    '''public short getFlags()
    '''
def setFlags():
    '''public void setFlags(final short flags)
    '''
