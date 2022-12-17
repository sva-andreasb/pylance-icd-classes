def ():
    '''returns ZipFile\n\n
    (final File f)\n
    (final String name)\n
    (final String name, final String encoding)\n
    (final File f, final String encoding)\n
    (final File f, final String encoding, final boolean useUnicodeExtraFields)\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getEntries():
    '''returns Enumeration\n\n
    getEntries()\n
    '''
def getEntry():
    '''returns ZipEntry\n\n
    getEntry(final String name)\n
    '''
def getInputStream():
    '''returns InputStream\n\n
    getInputStream(final ZipEntry ze)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, int len)\n
    '''
