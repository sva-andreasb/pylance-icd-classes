MIN_BLOCKSIZE = "int  1"
MAX_BLOCKSIZE = "int  9"
def ():
    '''returns CBZip2OutputStream\n\n
    (final OutputStream out)\n
    (final OutputStream out, final int blockSize)\n
    '''
def write():
    '''returns None\n\n
    write(final int b)\n
    write(final byte[] buf, int offs, final int len)\n
    '''
def finish():
    '''returns None\n\n
    finish()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
