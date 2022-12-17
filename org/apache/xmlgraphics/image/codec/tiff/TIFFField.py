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
def ():
    '''returns TIFFField\n\n
    (final int tag, final int type, final int count, final Object data)\n
    '''
def getTag():
    '''returns int\n\n
    getTag()\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    '''
def getCount():
    '''returns int\n\n
    getCount()\n
    '''
def getAsBytes():
    '''returns byte[]\n\n
    getAsBytes()\n
    '''
def getAsChars():
    '''returns char[]\n\n
    getAsChars()\n
    '''
def getAsShorts():
    '''returns short[]\n\n
    getAsShorts()\n
    '''
def getAsInts():
    '''returns int[]\n\n
    getAsInts()\n
    '''
def getAsLongs():
    '''returns long[]\n\n
    getAsLongs()\n
    '''
def getAsFloats():
    '''returns float[]\n\n
    getAsFloats()\n
    '''
def getAsDoubles():
    '''returns double[]\n\n
    getAsDoubles()\n
    '''
def getAsSRationals():
    '''returns int[][]\n\n
    getAsSRationals()\n
    '''
def getAsRationals():
    '''returns long[][]\n\n
    getAsRationals()\n
    '''
def getAsInt():
    '''returns int\n\n
    getAsInt(final int index)\n
    '''
def getAsLong():
    '''returns long\n\n
    getAsLong(final int index)\n
    '''
def getAsFloat():
    '''returns float\n\n
    getAsFloat(final int index)\n
    '''
def getAsDouble():
    '''returns double\n\n
    getAsDouble(final int index)\n
    '''
def getAsString():
    '''returns String\n\n
    getAsString(final int index)\n
    '''
def getAsSRational():
    '''returns int[]\n\n
    getAsSRational(final int index)\n
    '''
def getAsRational():
    '''returns long[]\n\n
    getAsRational(final int index)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object o)\n
    '''
