def ():
    '''returns PdfCopyFields\n\n
    (final OutputStream os)\n
    (final OutputStream os, final char pdfVersion)\n
    '''
def addDocument():
    '''returns None\n\n
    addDocument(final PdfReader reader)\n
    addDocument(final PdfReader reader, final List pagesToKeep)\n
    addDocument(final PdfReader reader, final String ranges)\n
    '''
def setEncryption():
    '''returns None\n\n
    setEncryption(final byte[] userPassword, final byte[] ownerPassword, final int permissions, final boolean strength128Bits)\n
    setEncryption(final boolean strength, final String userPassword, final String ownerPassword, final int permissions)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def open():
    '''returns None\n\n
    open()\n
    '''
def addJavaScript():
    '''returns None\n\n
    addJavaScript(final String js)\n
    '''
def setOutlines():
    '''returns None\n\n
    setOutlines(final List outlines)\n
    '''
def getWriter():
    '''returns PdfWriter\n\n
    getWriter()\n
    '''
def isFullCompression():
    '''returns boolean\n\n
    isFullCompression()\n
    '''
def setFullCompression():
    '''returns None\n\n
    setFullCompression()\n
    '''
