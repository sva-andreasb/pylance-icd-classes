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
def BOFRecord():
'''public BOFRecord()
public BOFRecord(final RecordInputStream in)
'''
pass
def createSheetBOF():
'''public static BOFRecord createSheetBOF()
'''
pass
def setVersion():
'''public void setVersion(final int version)
'''
pass
def setType():
'''public void setType(final int type)
'''
pass
def setBuild():
'''public void setBuild(final int build)
'''
pass
def setBuildYear():
'''public void setBuildYear(final int year)
'''
pass
def setHistoryBitMask():
'''public void setHistoryBitMask(final int bitmask)
'''
pass
def setRequiredVersion():
'''public void setRequiredVersion(final int version)
'''
pass
def getVersion():
'''public int getVersion()
'''
pass
def getType():
'''public int getType()
'''
pass
def getBuild():
'''public int getBuild()
'''
pass
def getBuildYear():
'''public int getBuildYear()
'''
pass
def getHistoryBitMask():
'''public int getHistoryBitMask()
'''
pass
def getRequiredVersion():
'''public int getRequiredVersion()
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
'''public BOFRecord clone()
'''
pass
