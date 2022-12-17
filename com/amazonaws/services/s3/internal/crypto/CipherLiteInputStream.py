def ():
    '''returns CipherLiteInputStream\n\n
    (final InputStream is, final CipherLite cipherLite)\n
    (final InputStream is, final CipherLite c, final int buffsize)\n
    (final InputStream is, final CipherLite c, final int buffsize, final boolean multipart, final boolean lastMultiPart)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b)\n
    read(final byte[] buf, final int off, final int target_len)\n
    '''
def skip():
    '''returns long\n\n
    skip(long n)\n
    '''
def available():
    '''returns int\n\n
    available()\n
    '''
def close():
    '''returns None\n\n
    close()\n
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
