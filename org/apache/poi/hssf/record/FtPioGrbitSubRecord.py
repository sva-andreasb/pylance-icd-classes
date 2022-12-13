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
pass
def setFlagByBit():
'''public void setFlagByBit(final int bitmask, final boolean enabled)
'''
pass
def getFlagByBit():
'''public boolean getFlagByBit(final int bitmask)
'''
pass
def toString():
'''public String toString()
'''
pass
def serialize():
'''public void serialize(final LittleEndianOutput out)
'''
pass
def getSid():
'''public short getSid()
'''
pass
def clone():
'''public FtPioGrbitSubRecord clone()
'''
pass
def getFlags():
'''public short getFlags()
'''
pass
def setFlags():
'''public void setFlags(final short flags)
'''
pass
