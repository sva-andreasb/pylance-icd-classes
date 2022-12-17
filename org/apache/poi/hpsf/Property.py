DEFAULT_CODEPAGE = "int  1252"
def ():
    '''returns Property\n\n
    ()\n
    (final Property p)\n
    (final long id, final long type, final Object value)\n
    (final long id, final byte[] src, final long offset, final int length, final int codepage)\n
    (final long id, final LittleEndianByteArrayInputStream leis, final int length, final int codepage)\n
    '''
def getID():
    '''returns long\n\n
    getID()\n
    '''
def setID():
    '''returns None\n\n
    setID(final long id)\n
    '''
def getType():
    '''returns long\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final long type)\n
    '''
def getValue():
    '''returns Object\n\n
    getValue()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final Object value)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString(final int codepage, final PropertyIDMap idMap)\n
    '''
def write():
    '''returns int\n\n
    write(final OutputStream out, final int codepage)\n
    '''
