sid = "short  146"
STANDARD_PALETTE_SIZE = "byte  56"
FIRST_COLOR_INDEX = "short  8"
ENCODED_SIZE = "short  4"
def ():
    '''returns PColor\n\n
    ()\n
    (final RecordInputStream in)\n
    (final int red, final int green, final int blue)\n
    (final RecordInputStream in)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final LittleEndianOutput out)\n
    serialize(final LittleEndianOutput out)\n
    '''
def getSid():
    '''returns short\n\n
    getSid()\n
    '''
def getColor():
    '''returns byte[]\n\n
    getColor(final int byteIndex)\n
    '''
def setColor():
    '''returns None\n\n
    setColor(final short byteIndex, final byte red, final byte green, final byte blue)\n
    '''
def getTriplet():
    '''returns byte[]\n\n
    getTriplet()\n
    '''
