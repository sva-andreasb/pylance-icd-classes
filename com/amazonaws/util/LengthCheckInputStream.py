INCLUDE_SKIPPED_BYTES = "boolean  true"
EXCLUDE_SKIPPED_BYTES = "boolean  false"
def ():
    '''returns LengthCheckInputStream\n\n
    (final InputStream in, final long expectedLength, final boolean includeSkipped)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, final int len)\n
    '''
def mark():
    '''returns None\n\n
    mark(final int readlimit)\n
    '''
def reset():
    '''returns None\n\n
    reset()\n
    '''
def skip():
    '''returns long\n\n
    skip(final long n)\n
    '''
