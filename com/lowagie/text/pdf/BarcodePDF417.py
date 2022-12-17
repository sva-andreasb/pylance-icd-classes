PDF417_USE_ASPECT_RATIO = "int  0"
PDF417_FIXED_RECTANGLE = "int  1"
PDF417_FIXED_COLUMNS = "int  2"
PDF417_FIXED_ROWS = "int  4"
PDF417_AUTO_ERROR_LEVEL = "int  0"
PDF417_USE_ERROR_LEVEL = "int  16"
PDF417_USE_RAW_CODEWORDS = "int  64"
PDF417_INVERT_BITMAP = "int  128"
def ():
    '''returns Segment\n\n
    ()\n
    (final char type, final int start, final int end)\n
    '''
def setDefaultParameters():
    '''returns None\n\n
    setDefaultParameters()\n
    '''
def paintCode():
    '''returns None\n\n
    paintCode()\n
    '''
def getImage():
    '''returns Image\n\n
    getImage()\n
    '''
def getOutBits():
    '''returns byte[]\n\n
    getOutBits()\n
    '''
def getBitColumns():
    '''returns int\n\n
    getBitColumns()\n
    '''
def getCodeRows():
    '''returns int\n\n
    getCodeRows()\n
    '''
def setCodeRows():
    '''returns None\n\n
    setCodeRows(final int codeRows)\n
    '''
def getCodeColumns():
    '''returns int\n\n
    getCodeColumns()\n
    '''
def setCodeColumns():
    '''returns None\n\n
    setCodeColumns(final int codeColumns)\n
    '''
def getCodewords():
    '''returns int[]\n\n
    getCodewords()\n
    '''
def getLenCodewords():
    '''returns int\n\n
    getLenCodewords()\n
    '''
def setLenCodewords():
    '''returns None\n\n
    setLenCodewords(final int lenCodewords)\n
    '''
def getErrorLevel():
    '''returns int\n\n
    getErrorLevel()\n
    '''
def setErrorLevel():
    '''returns None\n\n
    setErrorLevel(final int errorLevel)\n
    '''
def getText():
    '''returns byte[]\n\n
    getText()\n
    '''
def setText():
    '''returns None\n\n
    setText(final byte[] text)\n
    setText(final String s)\n
    '''
def getOptions():
    '''returns int\n\n
    getOptions()\n
    '''
def setOptions():
    '''returns None\n\n
    setOptions(final int options)\n
    '''
def getAspectRatio():
    '''returns float\n\n
    getAspectRatio()\n
    '''
def setAspectRatio():
    '''returns None\n\n
    setAspectRatio(final float aspectRatio)\n
    '''
def getYHeight():
    '''returns float\n\n
    getYHeight()\n
    '''
def setYHeight():
    '''returns None\n\n
    setYHeight(final float yHeight)\n
    '''
def add():
    '''returns None\n\n
    add(final char type, final int start, final int end)\n
    '''
def get():
    '''returns Segment\n\n
    get(final int idx)\n
    '''
def remove():
    '''returns None\n\n
    remove(final int idx)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
