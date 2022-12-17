BYTE_READ_IO_BUFFER = "int  0"
BYTE_WRITE_ENCODING_BUFFER = "int  1"
BYTE_WRITE_CONCAT_BUFFER = "int  2"
BYTE_BASE64_CODEC_BUFFER = "int  3"
CHAR_TOKEN_BUFFER = "int  0"
CHAR_CONCAT_BUFFER = "int  1"
CHAR_TEXT_BUFFER = "int  2"
CHAR_NAME_COPY_BUFFER = "int  3"
def ():
    '''returns BufferRecycler\n\n
    ()\n
    '''
def allocByteBuffer():
    '''returns byte[]\n\n
    allocByteBuffer(final int ix, int minSize)\n
    '''
def releaseByteBuffer():
    '''returns None\n\n
    releaseByteBuffer(final int ix, final byte[] buffer)\n
    '''
def allocCharBuffer():
    '''returns char[]\n\n
    allocCharBuffer(final int ix, int minSize)\n
    '''
def releaseCharBuffer():
    '''returns None\n\n
    releaseCharBuffer(final int ix, final char[] buffer)\n
    '''
