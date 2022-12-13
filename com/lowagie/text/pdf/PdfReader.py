def PdfReader():
    '''    public PdfReader(final String filename)
    public PdfReader(final String filename, final byte[] ownerPassword)
    public PdfReader(final byte[] pdfIn)
    public PdfReader(final byte[] pdfIn, final byte[] ownerPassword)
    public PdfReader(final URL url)
    public PdfReader(final URL url, final byte[] ownerPassword)
    public PdfReader(final InputStream is, final byte[] ownerPassword)
    public PdfReader(final InputStream is)
    public PdfReader(final PdfReader reader)
    '''
def getSafeFile():
    '''    public RandomAccessFileOrArray getSafeFile()
    '''
def getNumberOfPages():
    '''    public int getNumberOfPages()
    '''
def getCatalog():
    '''    public PdfDictionary getCatalog()
    '''
def getAcroForm():
    '''    public PRAcroForm getAcroForm()
    '''
def getPageRotation():
    '''    public int getPageRotation(final int index)
    '''
def getPageSizeWithRotation():
    '''    public Rectangle getPageSizeWithRotation(final int index)
    public Rectangle getPageSizeWithRotation(final PdfDictionary page)
    '''
def getPageSize():
    '''    public Rectangle getPageSize(final int index)
    public Rectangle getPageSize(final PdfDictionary page)
    '''
def getCropBox():
    '''    public Rectangle getCropBox(final int index)
    '''
def getBoxSize():
    '''    public Rectangle getBoxSize(final int index, final String boxName)
    '''
def getInfo():
    '''    public HashMap getInfo()
    '''
def getNormalizedRectangle():
    '''    public static Rectangle getNormalizedRectangle(final PdfArray box)
    '''
def getPdfObject():
    '''    public static PdfObject getPdfObject(PdfObject obj)
    public static PdfObject getPdfObject(PdfObject obj, final PdfObject parent)
    '''
def FlateDecode():
    '''    public static byte[] FlateDecode(final byte[] in)
    public static byte[] FlateDecode(final byte[] in, final boolean strict)
    '''
def decodePredictor():
    '''    public static byte[] decodePredictor(final byte[] in, final PdfObject dicPar)
    '''
def ASCIIHexDecode():
    '''    public static byte[] ASCIIHexDecode(final byte[] in)
    '''
def ASCII85Decode():
    '''    public static byte[] ASCII85Decode(final byte[] in)
    '''
def LZWDecode():
    '''    public static byte[] LZWDecode(final byte[] in)
    '''
def isRebuilt():
    '''    public boolean isRebuilt()
    '''
def getPageN():
    '''    public PdfDictionary getPageN(final int pageNum)
    '''
def getPageOrigRef():
    '''    public PRIndirectReference getPageOrigRef(final int pageNum)
    '''
def getPageContent():
    '''    public byte[] getPageContent(final int pageNum, final RandomAccessFileOrArray file)
    public byte[] getPageContent(final int pageNum)
    '''
def setPageContent():
    '''    public void setPageContent(final int pageNum, final byte[] content)
    '''
def getStreamBytes():
    '''    public static byte[] getStreamBytes(final PRStream stream, final RandomAccessFileOrArray file)
    public static byte[] getStreamBytes(final PRStream stream)
    '''
def eliminateSharedStreams():
    '''    public void eliminateSharedStreams()
    '''
def isTampered():
    '''    public boolean isTampered()
    '''
def setTampered():
    '''    public void setTampered(final boolean tampered)
    '''
def getMetadata():
    '''    public byte[] getMetadata()
    '''
def getLastXref():
    '''    public int getLastXref()
    '''
def getXrefSize():
    '''    public int getXrefSize()
    '''
def getEofPos():
    '''    public int getEofPos()
    '''
def getPdfVersion():
    '''    public char getPdfVersion()
    '''
def isEncrypted():
    '''    public boolean isEncrypted()
    '''
def getPermissions():
    '''    public int getPermissions()
    '''
def is128Key():
    '''    public boolean is128Key()
    '''
def getTrailer():
    '''    public PdfDictionary getTrailer()
    '''
def shuffleSubsetNames():
    '''    public int shuffleSubsetNames()
    '''
def createFakeFontSubsets():
    '''    public int createFakeFontSubsets()
    '''
def getNamedDestination():
    '''    public HashMap getNamedDestination()
    '''
def getNamedDestinationFromNames():
    '''    public HashMap getNamedDestinationFromNames()
    '''
def getNamedDestinationFromStrings():
    '''    public HashMap getNamedDestinationFromStrings()
    '''
def removeFields():
    '''    public void removeFields()
    '''
def removeAnnotations():
    '''    public void removeAnnotations()
    '''
def consolidateNamedDestinations():
    '''    public void consolidateNamedDestinations()
    '''
def removeUnusedObjects():
    '''    public int removeUnusedObjects()
    '''
def getAcroFields():
    '''    public AcroFields getAcroFields()
    '''
def getJavaScript():
    '''    public String getJavaScript(final RandomAccessFileOrArray file)
    public String getJavaScript()
    '''
def selectPages():
    '''    public void selectPages(final String ranges)
    public void selectPages(final List pagesToKeep)
    '''
def setViewerPreferences():
    '''    public static void setViewerPreferences(final int preferences, final PdfDictionary catalog)
    public void setViewerPreferences(final int preferences)
    '''
def getViewerPreferences():
    '''    public int getViewerPreferences()
    '''
def isAppendable():
    '''    public boolean isAppendable()
    '''
def setAppendable():
    '''    public void setAppendable(final boolean appendable)
    '''
def isNewXrefType():
    '''    public boolean isNewXrefType()
    '''
def getFileLength():
    '''    public int getFileLength()
    '''
def isHybridXref():
    '''    public boolean isHybridXref()
    '''
