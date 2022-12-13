PDF417_USE_ASPECT_RATIO = "int  0"
PDF417_FIXED_RECTANGLE = "int  1"
PDF417_FIXED_COLUMNS = "int  2"
PDF417_FIXED_ROWS = "int  4"
PDF417_AUTO_ERROR_LEVEL = "int  0"
PDF417_USE_ERROR_LEVEL = "int  16"
PDF417_USE_RAW_CODEWORDS = "int  64"
PDF417_INVERT_BITMAP = "int  128"
def BarcodePDF417():
    '''public BarcodePDF417()
    '''
def setDefaultParameters():
    '''public void setDefaultParameters()
    '''
def paintCode():
    '''public void paintCode()
    '''
def getImage():
    '''public Image getImage()
    '''
def getOutBits():
    '''public byte[] getOutBits()
    '''
def getBitColumns():
    '''public int getBitColumns()
    '''
def getCodeRows():
    '''public int getCodeRows()
    '''
def setCodeRows():
    '''public void setCodeRows(final int codeRows)
    '''
def getCodeColumns():
    '''public int getCodeColumns()
    '''
def setCodeColumns():
    '''public void setCodeColumns(final int codeColumns)
    '''
def getCodewords():
    '''public int[] getCodewords()
    '''
def getLenCodewords():
    '''public int getLenCodewords()
    '''
def setLenCodewords():
    '''public void setLenCodewords(final int lenCodewords)
    '''
def getErrorLevel():
    '''public int getErrorLevel()
    '''
def setErrorLevel():
    '''public void setErrorLevel(final int errorLevel)
    '''
def getText():
    '''public byte[] getText()
    '''
def setText():
    '''public void setText(final byte[] text)
    public void setText(final String s)
    '''
def getOptions():
    '''public int getOptions()
    '''
def setOptions():
    '''public void setOptions(final int options)
    '''
def getAspectRatio():
    '''public float getAspectRatio()
    '''
def setAspectRatio():
    '''public void setAspectRatio(final float aspectRatio)
    '''
def getYHeight():
    '''public float getYHeight()
    '''
def setYHeight():
    '''public void setYHeight(final float yHeight)
    '''
def Segment():
    '''public Segment(final char type, final int start, final int end)
    '''
def add():
    '''public void add(final char type, final int start, final int end)
    '''
def get():
    '''public Segment get(final int idx)
    '''
def remove():
    '''public void remove(final int idx)
    '''
def size():
    '''public int size()
    '''
