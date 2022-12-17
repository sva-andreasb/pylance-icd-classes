DEFLATED = "int  8"
DEFAULT_COMPRESSION = "int  -1"
STORED = "int  0"
UFT8_NAMES_FLAG = "int  2048"
EFS_FLAG = "int  2048"
def ():
    '''returns ZipOutputStream\n\n
    (final OutputStream out)\n
    (final File file)\n
    '''
def isSeekable():
    '''returns boolean\n\n
    isSeekable()\n
    '''
def setEncoding():
    '''returns None\n\n
    setEncoding(final String encoding)\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def setUseLanguageEncodingFlag():
    '''returns None\n\n
    setUseLanguageEncodingFlag(final boolean b)\n
    '''
def setCreateUnicodeExtraFields():
    '''returns None\n\n
    setCreateUnicodeExtraFields(final UnicodeExtraFieldPolicy b)\n
    '''
def setFallbackToUTF8():
    '''returns None\n\n
    setFallbackToUTF8(final boolean b)\n
    '''
def finish():
    '''returns None\n\n
    finish()\n
    '''
def closeEntry():
    '''returns None\n\n
    closeEntry()\n
    '''
def putNextEntry():
    '''returns None\n\n
    putNextEntry(final ZipEntry ze)\n
    '''
def setComment():
    '''returns None\n\n
    setComment(final String comment)\n
    '''
def setLevel():
    '''returns None\n\n
    setLevel(final int level)\n
    '''
def setMethod():
    '''returns None\n\n
    setMethod(final int method)\n
    '''
def write():
    '''returns None\n\n
    write(final byte[] b, final int offset, final int length)\n
    write(final int b)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
