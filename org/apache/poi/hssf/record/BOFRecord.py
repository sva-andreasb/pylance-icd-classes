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
    '''    public BOFRecord()
    public BOFRecord(final RecordInputStream in)
    '''
def createSheetBOF():
    '''    public static BOFRecord createSheetBOF()
    '''
def setVersion():
    '''    public void setVersion(final int version)
    '''
def setType():
    '''    public void setType(final int type)
    '''
def setBuild():
    '''    public void setBuild(final int build)
    '''
def setBuildYear():
    '''    public void setBuildYear(final int year)
    '''
def setHistoryBitMask():
    '''    public void setHistoryBitMask(final int bitmask)
    '''
def setRequiredVersion():
    '''    public void setRequiredVersion(final int version)
    '''
def getVersion():
    '''    public int getVersion()
    '''
def getType():
    '''    public int getType()
    '''
def getBuild():
    '''    public int getBuild()
    '''
def getBuildYear():
    '''    public int getBuildYear()
    '''
def getHistoryBitMask():
    '''    public int getHistoryBitMask()
    '''
def getRequiredVersion():
    '''    public int getRequiredVersion()
    '''
def toString():
    '''    public String toString()
    '''
def serialize():
    '''    public void serialize(final LittleEndianOutput out)
    '''
def getSid():
    '''    public short getSid()
    '''
def clone():
    '''    public BOFRecord clone()
    '''
