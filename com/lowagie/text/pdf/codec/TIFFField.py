TIFF_BYTE = "int  1"
TIFF_ASCII = "int  2"
TIFF_SHORT = "int  3"
TIFF_LONG = "int  4"
TIFF_RATIONAL = "int  5"
TIFF_SBYTE = "int  6"
TIFF_UNDEFINED = "int  7"
TIFF_SSHORT = "int  8"
TIFF_SLONG = "int  9"
TIFF_SRATIONAL = "int  10"
TIFF_FLOAT = "int  11"
TIFF_DOUBLE = "int  12"
def TIFFField():
    '''    public TIFFField(final int tag, final int type, final int count, final Object data)
    '''
def getTag():
    '''    public int getTag()
    '''
def getType():
    '''    public int getType()
    '''
def getCount():
    '''    public int getCount()
    '''
def getAsBytes():
    '''    public byte[] getAsBytes()
    '''
def getAsChars():
    '''    public char[] getAsChars()
    '''
def getAsShorts():
    '''    public short[] getAsShorts()
    '''
def getAsInts():
    '''    public int[] getAsInts()
    '''
def getAsLongs():
    '''    public long[] getAsLongs()
    '''
def getAsFloats():
    '''    public float[] getAsFloats()
    '''
def getAsDoubles():
    '''    public double[] getAsDoubles()
    '''
def getAsSRationals():
    '''    public int[][] getAsSRationals()
    '''
def getAsRationals():
    '''    public long[][] getAsRationals()
    '''
def getAsInt():
    '''    public int getAsInt(final int index)
    '''
def getAsLong():
    '''    public long getAsLong(final int index)
    '''
def getAsFloat():
    '''    public float getAsFloat(final int index)
    '''
def getAsDouble():
    '''    public double getAsDouble(final int index)
    '''
def getAsString():
    '''    public String getAsString(final int index)
    '''
def getAsSRational():
    '''    public int[] getAsSRational(final int index)
    '''
def getAsRational():
    '''    public long[] getAsRational(final int index)
    '''
def compareTo():
    '''    public int compareTo(final Object o)
    '''
