ALN = "int  0"
UPPER = "int  1"
LOWER = "int  2"
DATE = "int  3"
DATETIME = "int  4"
TIME = "int  5"
INTEGER = "int  6"
SMALLINT = "int  7"
FLOAT = "int  8"
DECIMAL = "int  9"
DURATION = "int  10"
AMOUNT = "int  11"
YORN = "int  12"
GL = "int  13"
LONGALN = "int  14"
CRYPTO = "int  15"
CRYPTOX = "int  16"
CLOB = "int  17"
BLOB = "int  18"
BIGINT = "int  19"
UDTYPE = "int  99"
DEFAULMAXLENGTH = "int  -1"
DEFAULTSCALE = "int  2"
def setMaxLength():
    '''public void setMaxLength(final int l)
    '''
def getMaxLength():
    '''public int getMaxLength()
    '''
def getScale():
    '''public int getScale()
    '''
def setScale():
    '''public void setScale(final int s)
    '''
def setValue():
    '''public void setValue(final Date value)
    public void setValue(final byte[] value)
    public void setValue(final double value)
    public void setValue(final float value)
    public void setValue(final int value)
    public void setValue(final long value)
    public void setValue(final boolean value)
    '''
def asDate():
    '''public Date asDate()
    '''
def asDouble():
    '''public double asDouble()
    '''
def asFloat():
    '''public float asFloat()
    '''
def asInt():
    '''public int asInt()
    '''
def asLong():
    '''public long asLong()
    '''
def asBoolean():
    '''public boolean asBoolean()
    '''
def asBytes():
    '''public byte[] asBytes()
    '''
def isNull():
    '''public boolean isNull()
    '''
def setValueNull():
    '''public void setValueNull()
    '''
def toString():
    '''public String toString()
    '''
def setAftercheckLengthAndScale():
    '''public void setAftercheckLengthAndScale(final String val)
    '''
def overrideStringData():
    '''public void overrideStringData(final String newValue)
    '''
def createMaxType():
    '''public static MaxType createMaxType(final Locale l, final TimeZone tz, final int type)
    public static MaxType createMaxType(final Locale l, final TimeZone tz, final int type, final int length, final int scale)
    '''
def getObjectName():
    '''public String getObjectName()
    '''
def setObjectName():
    '''public void setObjectName(final String objectName)
    '''
def getAttributeName():
    '''public String getAttributeName()
    '''
def setAttributeName():
    '''public void setAttributeName(final String attributeName)
    '''
