DEFAULT_BUFFER_SIZE = "int  2048"
def ():
    '''returns Latin1Reader\n\n
    (final InputStream inputStream)\n
    (final InputStream inputStream, final int n)\n
    (final InputStream fInputStream, final byte[] fBuffer)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final char[] array, final int n, int length)\n
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
