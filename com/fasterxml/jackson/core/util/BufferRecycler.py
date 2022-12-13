BYTE_READ_IO_BUFFER = "int  0"
BYTE_WRITE_ENCODING_BUFFER = "int  1"
BYTE_WRITE_CONCAT_BUFFER = "int  2"
BYTE_BASE64_CODEC_BUFFER = "int  3"
CHAR_TOKEN_BUFFER = "int  0"
CHAR_CONCAT_BUFFER = "int  1"
CHAR_TEXT_BUFFER = "int  2"
CHAR_NAME_COPY_BUFFER = "int  3"
def BufferRecycler():
    '''public BufferRecycler()
    '''
def allocByteBuffer():
    '''public final byte[] allocByteBuffer(final int ix)
    public byte[] allocByteBuffer(final int ix, int minSize)
    '''
def releaseByteBuffer():
    '''public void releaseByteBuffer(final int ix, final byte[] buffer)
    '''
def allocCharBuffer():
    '''public final char[] allocCharBuffer(final int ix)
    public char[] allocCharBuffer(final int ix, int minSize)
    '''
def releaseCharBuffer():
    '''public void releaseCharBuffer(final int ix, final char[] buffer)
    '''
