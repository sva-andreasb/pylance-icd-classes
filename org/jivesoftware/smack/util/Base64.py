NO_OPTIONS = "int  0"
ENCODE = "int  1"
DECODE = "int  0"
GZIP = "int  2"
DONT_BREAK_LINES = "int  8"
URL_SAFE = "int  16"
ORDERED = "int  32"
def ():
    '''returns OutputStream\n\n
    (final java.io.InputStream in)\n
    (final java.io.InputStream in, final int options)\n
    (final java.io.OutputStream out)\n
    (final java.io.OutputStream out, final int options)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] dest, final int off, final int len)\n
    '''
def write():
    '''returns None\n\n
    write(final int theByte)\n
    write(final byte[] theBytes, final int off, final int len)\n
    '''
def flushBase64():
    '''returns None\n\n
    flushBase64()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def suspendEncoding():
    '''returns None\n\n
    suspendEncoding()\n
    '''
def resumeEncoding():
    '''returns None\n\n
    resumeEncoding()\n
    '''
