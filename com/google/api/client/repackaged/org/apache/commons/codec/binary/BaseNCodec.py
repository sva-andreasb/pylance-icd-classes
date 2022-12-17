MIME_CHUNK_SIZE = "int  76"
PEM_CHUNK_SIZE = "int  64"
def encode():
    '''returns byte[]\n\n
    encode(final Object pObject)\n
    encode(final byte[] pArray)\n
    '''
def encodeToString():
    '''returns String\n\n
    encodeToString(final byte[] pArray)\n
    '''
def decode():
    '''returns byte[]\n\n
    decode(final Object pObject)\n
    decode(final String pArray)\n
    decode(final byte[] pArray)\n
    '''
def encodeAsString():
    '''returns String\n\n
    encodeAsString(final byte[] pArray)\n
    '''
def isInAlphabet():
    '''returns boolean\n\n
    isInAlphabet(final byte[] arrayOctet, final boolean allowWSPad)\n
    isInAlphabet(final String basen)\n
    '''
def getEncodedLength():
    '''returns long\n\n
    getEncodedLength(final byte[] pArray)\n
    '''
