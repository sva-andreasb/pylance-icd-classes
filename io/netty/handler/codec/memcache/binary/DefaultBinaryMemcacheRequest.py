REQUEST_MAGIC_BYTE = "byte  Byte.MIN_VALUE"
def ():
    '''returns DefaultBinaryMemcacheRequest\n\n
    ()\n
    (final ByteBuf key)\n
    (final ByteBuf key, final ByteBuf extras)\n
    '''
def reserved():
    '''returns short\n\n
    reserved()\n
    '''
def setReserved():
    '''returns BinaryMemcacheRequest\n\n
    setReserved(final short reserved)\n
    '''
def retain():
    '''returns BinaryMemcacheRequest\n\n
    retain()\n
    retain(final int increment)\n
    '''
def touch():
    '''returns BinaryMemcacheRequest\n\n
    touch()\n
    touch(final Object hint)\n
    '''
