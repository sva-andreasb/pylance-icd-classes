sid = "short  146"
STANDARD_PALETTE_SIZE = "byte  56"
FIRST_COLOR_INDEX = "short  8"
ENCODED_SIZE = "short  4"
def PaletteRecord():
    '''public PaletteRecord()
    public PaletteRecord(final RecordInputStream in)
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def serialize():
    '''public void serialize(final LittleEndianOutput out)
    public void serialize(final LittleEndianOutput out)
    '''
def getSid():
    '''public short getSid()
    '''
def getColor():
    '''public byte[] getColor(final int byteIndex)
    '''
def setColor():
    '''public void setColor(final short byteIndex, final byte red, final byte green, final byte blue)
    '''
def PColor():
    '''public PColor(final int red, final int green, final int blue)
    public PColor(final RecordInputStream in)
    '''
def getTriplet():
    '''public byte[] getTriplet()
    '''
