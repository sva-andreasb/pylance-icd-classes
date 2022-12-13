def PdfStamper():
'''public PdfStamper(final PdfReader reader, final OutputStream os)
public PdfStamper(final PdfReader reader, final OutputStream os, final char pdfVersion)
public PdfStamper(final PdfReader reader, final OutputStream os, final char pdfVersion, final boolean append)
'''
pass
def getMoreInfo():
'''public HashMap getMoreInfo()
'''
pass
def setMoreInfo():
'''public void setMoreInfo(final HashMap moreInfo)
'''
pass
def insertPage():
'''public void insertPage(final int pageNumber, final Rectangle mediabox)
'''
pass
def getSignatureAppearance():
'''public PdfSignatureAppearance getSignatureAppearance()
'''
pass
def close():
'''public void close()
'''
pass
def getUnderContent():
'''public PdfContentByte getUnderContent(final int pageNum)
'''
pass
def getOverContent():
'''public PdfContentByte getOverContent(final int pageNum)
'''
pass
def isRotateContents():
'''public boolean isRotateContents()
'''
pass
def setRotateContents():
'''public void setRotateContents(final boolean rotateContents)
'''
pass
def setEncryption():
'''public void setEncryption(final byte[] userPassword, final byte[] ownerPassword, final int permissions, final boolean strength128Bits)
public void setEncryption(final boolean strength, final String userPassword, final String ownerPassword, final int permissions)
'''
pass
def getImportedPage():
'''public PdfImportedPage getImportedPage(final PdfReader reader, final int pageNumber)
'''
pass
def getWriter():
'''public PdfWriter getWriter()
'''
pass
def getReader():
'''public PdfReader getReader()
'''
pass
def getAcroFields():
'''public AcroFields getAcroFields()
'''
pass
def setFormFlattening():
'''public void setFormFlattening(final boolean flat)
'''
pass
def addAnnotation():
'''public void addAnnotation(final PdfAnnotation annot, final int page)
'''
pass
def addComments():
'''public void addComments(final FdfReader fdf)
'''
pass
def setOutlines():
'''public void setOutlines(final List outlines)
'''
pass
def partialFormFlattening():
'''public boolean partialFormFlattening(final String name)
'''
pass
def addJavaScript():
'''public void addJavaScript(final String js)
'''
pass
def setViewerPreferences():
'''public void setViewerPreferences(final int preferences)
'''
pass
def isFullCompression():
'''public boolean isFullCompression()
'''
pass
def setFullCompression():
'''public void setFullCompression()
'''
pass
def setPageAction():
'''public void setPageAction(final PdfName actionType, final PdfAction action, final int page)
'''
pass
def setDuration():
'''public void setDuration(final int seconds, final int page)
'''
pass
def setTransition():
'''public void setTransition(final PdfTransition transition, final int page)
'''
pass
def createSignature():
'''public static PdfStamper createSignature(final PdfReader reader, final OutputStream os, final char pdfVersion, File tempFile, final boolean append)
public static PdfStamper createSignature(final PdfReader reader, final OutputStream os, final char pdfVersion)
public static PdfStamper createSignature(final PdfReader reader, final OutputStream os, final char pdfVersion, final File tempFile)
'''
pass
