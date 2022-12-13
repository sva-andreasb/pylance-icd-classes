def PdfReader():
'''public PdfReader(final String filename)
public PdfReader(final String filename, final byte[] ownerPassword)
public PdfReader(final byte[] pdfIn)
public PdfReader(final byte[] pdfIn, final byte[] ownerPassword)
public PdfReader(final URL url)
public PdfReader(final URL url, final byte[] ownerPassword)
public PdfReader(final InputStream is, final byte[] ownerPassword)
public PdfReader(final InputStream is)
public PdfReader(final PdfReader reader)
'''
pass
def getSafeFile():
'''public RandomAccessFileOrArray getSafeFile()
'''
pass
def getNumberOfPages():
'''public int getNumberOfPages()
'''
pass
def getCatalog():
'''public PdfDictionary getCatalog()
'''
pass
def getAcroForm():
'''public PRAcroForm getAcroForm()
'''
pass
def getPageRotation():
'''public int getPageRotation(final int index)
'''
pass
def getPageSizeWithRotation():
'''public Rectangle getPageSizeWithRotation(final int index)
public Rectangle getPageSizeWithRotation(final PdfDictionary page)
'''
pass
def getPageSize():
'''public Rectangle getPageSize(final int index)
public Rectangle getPageSize(final PdfDictionary page)
'''
pass
def getCropBox():
'''public Rectangle getCropBox(final int index)
'''
pass
def getBoxSize():
'''public Rectangle getBoxSize(final int index, final String boxName)
'''
pass
def getInfo():
'''public HashMap getInfo()
'''
pass
def getNormalizedRectangle():
'''public static Rectangle getNormalizedRectangle(final PdfArray box)
'''
pass
def getPdfObject():
'''public static PdfObject getPdfObject(PdfObject obj)
public static PdfObject getPdfObject(PdfObject obj, final PdfObject parent)
'''
pass
def FlateDecode():
'''public static byte[] FlateDecode(final byte[] in)
public static byte[] FlateDecode(final byte[] in, final boolean strict)
'''
pass
def decodePredictor():
'''public static byte[] decodePredictor(final byte[] in, final PdfObject dicPar)
'''
pass
def ASCIIHexDecode():
'''public static byte[] ASCIIHexDecode(final byte[] in)
'''
pass
def ASCII85Decode():
'''public static byte[] ASCII85Decode(final byte[] in)
'''
pass
def LZWDecode():
'''public static byte[] LZWDecode(final byte[] in)
'''
pass
def isRebuilt():
'''public boolean isRebuilt()
'''
pass
def getPageN():
'''public PdfDictionary getPageN(final int pageNum)
'''
pass
def getPageOrigRef():
'''public PRIndirectReference getPageOrigRef(final int pageNum)
'''
pass
def getPageContent():
'''public byte[] getPageContent(final int pageNum, final RandomAccessFileOrArray file)
public byte[] getPageContent(final int pageNum)
'''
pass
def setPageContent():
'''public void setPageContent(final int pageNum, final byte[] content)
'''
pass
def getStreamBytes():
'''public static byte[] getStreamBytes(final PRStream stream, final RandomAccessFileOrArray file)
public static byte[] getStreamBytes(final PRStream stream)
'''
pass
def eliminateSharedStreams():
'''public void eliminateSharedStreams()
'''
pass
def isTampered():
'''public boolean isTampered()
'''
pass
def setTampered():
'''public void setTampered(final boolean tampered)
'''
pass
def getMetadata():
'''public byte[] getMetadata()
'''
pass
def getLastXref():
'''public int getLastXref()
'''
pass
def getXrefSize():
'''public int getXrefSize()
'''
pass
def getEofPos():
'''public int getEofPos()
'''
pass
def getPdfVersion():
'''public char getPdfVersion()
'''
pass
def isEncrypted():
'''public boolean isEncrypted()
'''
pass
def getPermissions():
'''public int getPermissions()
'''
pass
def is128Key():
'''public boolean is128Key()
'''
pass
def getTrailer():
'''public PdfDictionary getTrailer()
'''
pass
def shuffleSubsetNames():
'''public int shuffleSubsetNames()
'''
pass
def createFakeFontSubsets():
'''public int createFakeFontSubsets()
'''
pass
def getNamedDestination():
'''public HashMap getNamedDestination()
'''
pass
def getNamedDestinationFromNames():
'''public HashMap getNamedDestinationFromNames()
'''
pass
def getNamedDestinationFromStrings():
'''public HashMap getNamedDestinationFromStrings()
'''
pass
def removeFields():
'''public void removeFields()
'''
pass
def removeAnnotations():
'''public void removeAnnotations()
'''
pass
def consolidateNamedDestinations():
'''public void consolidateNamedDestinations()
'''
pass
def removeUnusedObjects():
'''public int removeUnusedObjects()
'''
pass
def getAcroFields():
'''public AcroFields getAcroFields()
'''
pass
def getJavaScript():
'''public String getJavaScript(final RandomAccessFileOrArray file)
public String getJavaScript()
'''
pass
def selectPages():
'''public void selectPages(final String ranges)
public void selectPages(final List pagesToKeep)
'''
pass
def setViewerPreferences():
'''public static void setViewerPreferences(final int preferences, final PdfDictionary catalog)
public void setViewerPreferences(final int preferences)
'''
pass
def getViewerPreferences():
'''public int getViewerPreferences()
'''
pass
def isAppendable():
'''public boolean isAppendable()
'''
pass
def setAppendable():
'''public void setAppendable(final boolean appendable)
'''
pass
def isNewXrefType():
'''public boolean isNewXrefType()
'''
pass
def getFileLength():
'''public int getFileLength()
'''
pass
def isHybridXref():
'''public boolean isHybridXref()
'''
pass
