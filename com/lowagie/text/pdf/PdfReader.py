def ():
    '''returns PdfReader\n\n
    (final String filename)\n
    (final String filename, final byte[] ownerPassword)\n
    (final byte[] pdfIn)\n
    (final byte[] pdfIn, final byte[] ownerPassword)\n
    (final URL url)\n
    (final URL url, final byte[] ownerPassword)\n
    (final InputStream is, final byte[] ownerPassword)\n
    (final InputStream is)\n
    (final PdfReader reader)\n
    '''
def getSafeFile():
    '''returns RandomAccessFileOrArray\n\n
    getSafeFile()\n
    '''
def getNumberOfPages():
    '''returns int\n\n
    getNumberOfPages()\n
    '''
def getCatalog():
    '''returns PdfDictionary\n\n
    getCatalog()\n
    '''
def getAcroForm():
    '''returns PRAcroForm\n\n
    getAcroForm()\n
    '''
def getPageRotation():
    '''returns int\n\n
    getPageRotation(final int index)\n
    '''
def getPageSizeWithRotation():
    '''returns Rectangle\n\n
    getPageSizeWithRotation(final int index)\n
    getPageSizeWithRotation(final PdfDictionary page)\n
    '''
def getPageSize():
    '''returns Rectangle\n\n
    getPageSize(final int index)\n
    getPageSize(final PdfDictionary page)\n
    '''
def getCropBox():
    '''returns Rectangle\n\n
    getCropBox(final int index)\n
    '''
def getBoxSize():
    '''returns Rectangle\n\n
    getBoxSize(final int index, final String boxName)\n
    '''
def getInfo():
    '''returns HashMap\n\n
    getInfo()\n
    '''
def isRebuilt():
    '''returns boolean\n\n
    isRebuilt()\n
    '''
def getPageN():
    '''returns PdfDictionary\n\n
    getPageN(final int pageNum)\n
    '''
def getPageOrigRef():
    '''returns PRIndirectReference\n\n
    getPageOrigRef(final int pageNum)\n
    '''
def getPageContent():
    '''returns byte[]\n\n
    getPageContent(final int pageNum, final RandomAccessFileOrArray file)\n
    getPageContent(final int pageNum)\n
    '''
def setPageContent():
    '''returns None\n\n
    setPageContent(final int pageNum, final byte[] content)\n
    '''
def eliminateSharedStreams():
    '''returns None\n\n
    eliminateSharedStreams()\n
    '''
def isTampered():
    '''returns boolean\n\n
    isTampered()\n
    '''
def setTampered():
    '''returns None\n\n
    setTampered(final boolean tampered)\n
    '''
def getMetadata():
    '''returns byte[]\n\n
    getMetadata()\n
    '''
def getLastXref():
    '''returns int\n\n
    getLastXref()\n
    '''
def getXrefSize():
    '''returns int\n\n
    getXrefSize()\n
    '''
def getEofPos():
    '''returns int\n\n
    getEofPos()\n
    '''
def getPdfVersion():
    '''returns char\n\n
    getPdfVersion()\n
    '''
def isEncrypted():
    '''returns boolean\n\n
    isEncrypted()\n
    '''
def getPermissions():
    '''returns int\n\n
    getPermissions()\n
    '''
def is128Key():
    '''returns boolean\n\n
    is128Key()\n
    '''
def getTrailer():
    '''returns PdfDictionary\n\n
    getTrailer()\n
    '''
def shuffleSubsetNames():
    '''returns int\n\n
    shuffleSubsetNames()\n
    '''
def createFakeFontSubsets():
    '''returns int\n\n
    createFakeFontSubsets()\n
    '''
def getNamedDestination():
    '''returns HashMap\n\n
    getNamedDestination()\n
    '''
def getNamedDestinationFromNames():
    '''returns HashMap\n\n
    getNamedDestinationFromNames()\n
    '''
def getNamedDestinationFromStrings():
    '''returns HashMap\n\n
    getNamedDestinationFromStrings()\n
    '''
def removeFields():
    '''returns None\n\n
    removeFields()\n
    '''
def removeAnnotations():
    '''returns None\n\n
    removeAnnotations()\n
    '''
def consolidateNamedDestinations():
    '''returns None\n\n
    consolidateNamedDestinations()\n
    '''
def removeUnusedObjects():
    '''returns int\n\n
    removeUnusedObjects()\n
    '''
def getAcroFields():
    '''returns AcroFields\n\n
    getAcroFields()\n
    '''
def getJavaScript():
    '''returns String\n\n
    getJavaScript(final RandomAccessFileOrArray file)\n
    getJavaScript()\n
    '''
def selectPages():
    '''returns None\n\n
    selectPages(final String ranges)\n
    selectPages(final List pagesToKeep)\n
    '''
def setViewerPreferences():
    '''returns None\n\n
    setViewerPreferences(final int preferences)\n
    '''
def getViewerPreferences():
    '''returns int\n\n
    getViewerPreferences()\n
    '''
def isAppendable():
    '''returns boolean\n\n
    isAppendable()\n
    '''
def setAppendable():
    '''returns None\n\n
    setAppendable(final boolean appendable)\n
    '''
def isNewXrefType():
    '''returns boolean\n\n
    isNewXrefType()\n
    '''
def getFileLength():
    '''returns int\n\n
    getFileLength()\n
    '''
def isHybridXref():
    '''returns boolean\n\n
    isHybridXref()\n
    '''
