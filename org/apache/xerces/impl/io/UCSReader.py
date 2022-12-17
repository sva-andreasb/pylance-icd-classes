DEFAULT_BUFFER_SIZE = "int  8192"
UCS2LE = "short  1"
UCS2BE = "short  2"
UCS4LE = "short  4"
UCS4BE = "short  8"
def ():
    '''returns UCSReader\n\n
    (final InputStream inputStream, final short n)\n
    (final InputStream inputStream, final int n, final short n2)\n
    (final InputStream fInputStream, final byte[] fBuffer, final short fEncoding)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final char[] array, final int n, final int n2)\n
    '''
def skip():
    '''returns long\n\n
    skip(final long n)\n
    '''
def ready():
    '''returns boolean\n\n
    ready()\n
    '''
def markSupported():
    '''returns boolean\n\n
    markSupported()\n
    '''
def mark():
    '''returns None\n\n
    mark(final int readlimit)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
