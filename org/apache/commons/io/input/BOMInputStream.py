def ():
    '''returns BOMInputStream\n\n
    (final InputStream delegate)\n
    (final InputStream delegate, final boolean include)\n
    (final InputStream delegate, final ByteOrderMark... boms)\n
    (final InputStream delegate, final boolean include, final ByteOrderMark... boms)\n
    '''
def hasBOM():
    '''returns boolean\n\n
    hasBOM()\n
    hasBOM(final ByteOrderMark bom)\n
    '''
def getBOM():
    '''returns ByteOrderMark\n\n
    getBOM()\n
    '''
def getBOMCharsetName():
    '''returns String\n\n
    getBOMCharsetName()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] buf, int off, int len)\n
    read(final byte[] buf)\n
    '''
def skip():
    '''returns long\n\n
    skip(final long n)\n
    '''
def compare():
    '''returns int\n\n
    compare(final ByteOrderMark bom1, final ByteOrderMark bom2)\n
    '''
