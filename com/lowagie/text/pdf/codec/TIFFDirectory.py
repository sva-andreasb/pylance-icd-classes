def ():
    '''returns TIFFDirectory\n\n
    (final RandomAccessFileOrArray stream, final int directory)\n
    (final RandomAccessFileOrArray stream, long ifd_offset, final int directory)\n
    '''
def getNumEntries():
    '''returns int\n\n
    getNumEntries()\n
    '''
def getField():
    '''returns TIFFField\n\n
    getField(final int tag)\n
    '''
def isTagPresent():
    '''returns boolean\n\n
    isTagPresent(final int tag)\n
    '''
def getTags():
    '''returns int[]\n\n
    getTags()\n
    '''
def getFields():
    '''returns TIFFField[]\n\n
    getFields()\n
    '''
def getFieldAsByte():
    '''returns byte\n\n
    getFieldAsByte(final int tag, final int index)\n
    getFieldAsByte(final int tag)\n
    '''
def getFieldAsLong():
    '''returns long\n\n
    getFieldAsLong(final int tag, final int index)\n
    getFieldAsLong(final int tag)\n
    '''
def getFieldAsFloat():
    '''returns float\n\n
    getFieldAsFloat(final int tag, final int index)\n
    getFieldAsFloat(final int tag)\n
    '''
def getFieldAsDouble():
    '''returns double\n\n
    getFieldAsDouble(final int tag, final int index)\n
    getFieldAsDouble(final int tag)\n
    '''
def isBigEndian():
    '''returns boolean\n\n
    isBigEndian()\n
    '''
def getIFDOffset():
    '''returns long\n\n
    getIFDOffset()\n
    '''
def getNextIFDOffset():
    '''returns long\n\n
    getNextIFDOffset()\n
    '''
