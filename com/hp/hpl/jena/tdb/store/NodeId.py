SIZE = "int  8"
NONE = "int  0"
INTEGER = "int  1"
DECIMAL = "int  2"
DATE = "int  3"
DATETIME = "int  4"
BOOLEAN = "int  5"
SHORT_STRING = "int  6"
SPECIAL = "int  255"
def ():
    '''returns NodeId\n\n
    (final long v)\n
    '''
def toByteBuffer():
    '''returns None\n\n
    toByteBuffer(final ByteBuffer b, final int idx)\n
    '''
def toBytes():
    '''returns None\n\n
    toBytes(final byte[] b, final int idx)\n
    '''
def isDirect():
    '''returns boolean\n\n
    isDirect()\n
    '''
def type():
    '''returns int\n\n
    type()\n
    '''
def getId():
    '''returns long\n\n
    getId()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
