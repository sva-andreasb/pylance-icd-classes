INTLENGTH = "int  4"
def ():
    '''returns OutputStructuredFieldStream\n\n
    (final OutputStream outStream)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def writeHdr():
    '''returns None\n\n
    writeHdr(final byte b, final byte b2, final byte b3, final byte b4, final int n)\n
    writeHdr(final StructuredFieldHeader structuredFieldHeader, final int n)\n
    '''
def writeData():
    '''returns None\n\n
    writeData(final byte[] b)\n
    writeData(final byte b)\n
    writeData(final byte[] b, final int off, final int len)\n
    '''
def writeInt():
    '''returns None\n\n
    writeInt(final int n)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
