def PdfStamper():
    '''public PdfStamper(final PdfReader reader, final OutputStream os)
    public PdfStamper(final PdfReader reader, final OutputStream os, final char pdfVersion)
    public PdfStamper(final PdfReader reader, final OutputStream os, final char pdfVersion, final boolean append)
    '''
def getMoreInfo():
    '''public HashMap getMoreInfo()
    '''
def setMoreInfo():
    '''public void setMoreInfo(final HashMap moreInfo)
    '''
def insertPage():
    '''public void insertPage(final int pageNumber, final Rectangle mediabox)
    '''
def getSignatureAppearance():
    '''public PdfSignatureAppearance getSignatureAppearance()
    '''
def close():
    '''public void close()
    '''
def getUnderContent():
    '''public PdfContentByte getUnderContent(final int pageNum)
    '''
def getOverContent():
    '''public PdfContentByte getOverContent(final int pageNum)
    '''
def isRotateContents():
    '''public boolean isRotateContents()
    '''
def setRotateContents():
    '''public void setRotateContents(final boolean rotateContents)
    '''
def setEncryption():
    '''public void setEncryption(final byte[] userPassword, final byte[] ownerPassword, final int permissions, final boolean strength128Bits)
    public void setEncryption(final boolean strength, final String userPassword, final String ownerPassword, final int permissions)
    '''
def getImportedPage():
    '''public PdfImportedPage getImportedPage(final PdfReader reader, final int pageNumber)
    '''
def getWriter():
    '''public PdfWriter getWriter()
    '''
def getReader():
    '''public PdfReader getReader()
    '''
def getAcroFields():
    '''public AcroFields getAcroFields()
    '''
def setFormFlattening():
    '''public void setFormFlattening(final boolean flat)
    '''
def addAnnotation():
    '''public void addAnnotation(final PdfAnnotation annot, final int page)
    '''
def addComments():
    '''public void addComments(final FdfReader fdf)
    '''
def setOutlines():
    '''public void setOutlines(final List outlines)
    '''
def partialFormFlattening():
    '''public boolean partialFormFlattening(final String name)
    '''
def addJavaScript():
    '''public void addJavaScript(final String js)
    '''
def setViewerPreferences():
    '''public void setViewerPreferences(final int preferences)
    '''
def isFullCompression():
    '''public boolean isFullCompression()
    '''
def setFullCompression():
    '''public void setFullCompression()
    '''
def setPageAction():
    '''public void setPageAction(final PdfName actionType, final PdfAction action, final int page)
    '''
def setDuration():
    '''public void setDuration(final int seconds, final int page)
    '''
def setTransition():
    '''public void setTransition(final PdfTransition transition, final int page)
    '''
def createSignature():
    '''public static PdfStamper createSignature(final PdfReader reader, final OutputStream os, final char pdfVersion, File tempFile, final boolean append)
    public static PdfStamper createSignature(final PdfReader reader, final OutputStream os, final char pdfVersion)
    public static PdfStamper createSignature(final PdfReader reader, final OutputStream os, final char pdfVersion, final File tempFile)
    '''
