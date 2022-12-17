def ():
    '''returns SimpleRecord\n\n
    (final long timestamp, final ByteBuffer key, final ByteBuffer value, final Header[] headers)\n
    (final long timestamp, final byte[] key, final byte[] value, final Header[] headers)\n
    (final long timestamp, final ByteBuffer key, final ByteBuffer value)\n
    (final long timestamp, final byte[] key, final byte[] value)\n
    (final long timestamp, final byte[] value)\n
    (final byte[] value)\n
    (final byte[] key, final byte[] value)\n
    (final Record record)\n
    '''
def key():
    '''returns ByteBuffer\n\n
    key()\n
    '''
def value():
    '''returns ByteBuffer\n\n
    value()\n
    '''
def timestamp():
    '''returns long\n\n
    timestamp()\n
    '''
def headers():
    '''returns Header[]\n\n
    headers()\n
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
    '''
