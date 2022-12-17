DEFAULT_BUFFER_SIZE = "int  4096"
def ():
    '''returns UTF16Reader\n\n
    (final InputStream inputStream, final boolean b)\n
    (final InputStream inputStream, final boolean b, final MessageFormatter messageFormatter, final Locale locale)\n
    (final InputStream inputStream, final int n, final boolean b, final MessageFormatter messageFormatter, final Locale locale)\n
    (final InputStream fInputStream, final byte[] fBuffer, final boolean fIsBigEndian, final MessageFormatter fFormatter, final Locale fLocale)\n
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
    mark(final int n)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
