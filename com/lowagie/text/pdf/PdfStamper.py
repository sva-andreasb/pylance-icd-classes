def ():
    '''returns PdfStamper\n\n
    (final PdfReader reader, final OutputStream os)\n
    (final PdfReader reader, final OutputStream os, final char pdfVersion)\n
    (final PdfReader reader, final OutputStream os, final char pdfVersion, final boolean append)\n
    '''
def getMoreInfo():
    '''returns HashMap\n\n
    getMoreInfo()\n
    '''
def setMoreInfo():
    '''returns None\n\n
    setMoreInfo(final HashMap moreInfo)\n
    '''
def insertPage():
    '''returns None\n\n
    insertPage(final int pageNumber, final Rectangle mediabox)\n
    '''
def getSignatureAppearance():
    '''returns PdfSignatureAppearance\n\n
    getSignatureAppearance()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getUnderContent():
    '''returns PdfContentByte\n\n
    getUnderContent(final int pageNum)\n
    '''
def getOverContent():
    '''returns PdfContentByte\n\n
    getOverContent(final int pageNum)\n
    '''
def isRotateContents():
    '''returns boolean\n\n
    isRotateContents()\n
    '''
def setRotateContents():
    '''returns None\n\n
    setRotateContents(final boolean rotateContents)\n
    '''
def setEncryption():
    '''returns None\n\n
    setEncryption(final byte[] userPassword, final byte[] ownerPassword, final int permissions, final boolean strength128Bits)\n
    setEncryption(final boolean strength, final String userPassword, final String ownerPassword, final int permissions)\n
    '''
def getImportedPage():
    '''returns PdfImportedPage\n\n
    getImportedPage(final PdfReader reader, final int pageNumber)\n
    '''
def getWriter():
    '''returns PdfWriter\n\n
    getWriter()\n
    '''
def getReader():
    '''returns PdfReader\n\n
    getReader()\n
    '''
def getAcroFields():
    '''returns AcroFields\n\n
    getAcroFields()\n
    '''
def setFormFlattening():
    '''returns None\n\n
    setFormFlattening(final boolean flat)\n
    '''
def addAnnotation():
    '''returns None\n\n
    addAnnotation(final PdfAnnotation annot, final int page)\n
    '''
def addComments():
    '''returns None\n\n
    addComments(final FdfReader fdf)\n
    '''
def setOutlines():
    '''returns None\n\n
    setOutlines(final List outlines)\n
    '''
def partialFormFlattening():
    '''returns boolean\n\n
    partialFormFlattening(final String name)\n
    '''
def addJavaScript():
    '''returns None\n\n
    addJavaScript(final String js)\n
    '''
def setViewerPreferences():
    '''returns None\n\n
    setViewerPreferences(final int preferences)\n
    '''
def isFullCompression():
    '''returns boolean\n\n
    isFullCompression()\n
    '''
def setFullCompression():
    '''returns None\n\n
    setFullCompression()\n
    '''
def setPageAction():
    '''returns None\n\n
    setPageAction(final PdfName actionType, final PdfAction action, final int page)\n
    '''
def setDuration():
    '''returns None\n\n
    setDuration(final int seconds, final int page)\n
    '''
def setTransition():
    '''returns None\n\n
    setTransition(final PdfTransition transition, final int page)\n
    '''
