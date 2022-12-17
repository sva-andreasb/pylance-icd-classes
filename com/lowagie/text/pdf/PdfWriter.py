PageLayoutSinglePage = "int  1"
PageLayoutOneColumn = "int  2"
PageLayoutTwoColumnLeft = "int  4"
PageLayoutTwoColumnRight = "int  8"
PageModeUseNone = "int  16"
PageModeUseOutlines = "int  32"
PageModeUseThumbs = "int  64"
PageModeFullScreen = "int  128"
PageModeUseOC = "int  1048576"
HideToolbar = "int  256"
HideMenubar = "int  512"
HideWindowUI = "int  1024"
FitWindow = "int  2048"
CenterWindow = "int  4096"
NonFullScreenPageModeUseNone = "int  8192"
NonFullScreenPageModeUseOutlines = "int  16384"
NonFullScreenPageModeUseThumbs = "int  32768"
NonFullScreenPageModeUseOC = "int  524288"
DirectionL2R = "int  65536"
DirectionR2L = "int  131072"
DisplayDocTitle = "int  262144"
AllowPrinting = "int  2052"
AllowModifyContents = "int  8"
AllowCopy = "int  16"
AllowModifyAnnotations = "int  32"
AllowFillIn = "int  256"
AllowScreenReaders = "int  512"
AllowAssembly = "int  1024"
AllowDegradedPrinting = "int  4"
STRENGTH40BITS = "boolean  false"
STRENGTH128BITS = "boolean  true"
SIGNATURE_EXISTS = "int  1"
SIGNATURE_APPEND_ONLY = "int  2"
VERSION_1_2 = "char  '2'"
VERSION_1_3 = "char  '3'"
VERSION_1_4 = "char  '4'"
VERSION_1_5 = "char  '5'"
VERSION_1_6 = "char  '6'"
PDFXNONE = "int  0"
PDFX1A2001 = "int  1"
PDFX32002 = "int  2"
SPACE_CHAR_RATIO_DEFAULT = "float  2.5f"
NO_SPACE_CHAR_RATIO = "float  1.0E7f"
RUN_DIRECTION_DEFAULT = "int  0"
RUN_DIRECTION_NO_BIDI = "int  1"
RUN_DIRECTION_LTR = "int  2"
RUN_DIRECTION_RTL = "int  3"
def open():
    '''returns None\n\n
    open()\n
    '''
def getTableBottom():
    '''returns float\n\n
    getTableBottom(final Table table)\n
    '''
def getPdfTable():
    '''returns PdfTable\n\n
    getPdfTable(final Table table)\n
    '''
def breakTableIfDoesntFit():
    '''returns boolean\n\n
    breakTableIfDoesntFit(final PdfTable table)\n
    '''
def fitsPage():
    '''returns boolean\n\n
    fitsPage(final Table table, final float margin)\n
    fitsPage(final Table table)\n
    fitsPage(final PdfPTable table, final float margin)\n
    fitsPage(final PdfPTable table)\n
    '''
def getVerticalPosition():
    '''returns float\n\n
    getVerticalPosition(final boolean ensureNewLine)\n
    '''
def getDirectContent():
    '''returns PdfContentByte\n\n
    getDirectContent()\n
    '''
def getDirectContentUnder():
    '''returns PdfContentByte\n\n
    getDirectContentUnder()\n
    '''
def getAcroForm():
    '''returns PdfAcroForm\n\n
    getAcroForm()\n
    '''
def getRootOutline():
    '''returns PdfOutline\n\n
    getRootOutline()\n
    '''
def getOs():
    '''returns OutputStreamCounter\n\n
    getOs()\n
    '''
def getPdfIndirectReference():
    '''returns PdfIndirectReference\n\n
    getPdfIndirectReference()\n
    '''
def setPageEvent():
    '''returns None\n\n
    setPageEvent(final PdfPageEvent pageEvent)\n
    '''
def getPageEvent():
    '''returns PdfPageEvent\n\n
    getPageEvent()\n
    '''
def getPageNumber():
    '''returns int\n\n
    getPageNumber()\n
    '''
def setViewerPreferences():
    '''returns None\n\n
    setViewerPreferences(final int preferences)\n
    '''
def setEncryption():
    '''returns None\n\n
    setEncryption(final byte[] userPassword, final byte[] ownerPassword, final int permissions, final boolean strength128Bits)\n
    setEncryption(final boolean strength, final String userPassword, final String ownerPassword, final int permissions)\n
    '''
def addToBody():
    '''returns PdfIndirectObject\n\n
    addToBody(final PdfObject object)\n
    addToBody(final PdfObject object, final boolean inObjStm)\n
    addToBody(final PdfObject object, final PdfIndirectReference ref)\n
    addToBody(final PdfObject object, final PdfIndirectReference ref, final boolean inObjStm)\n
    addToBody(final PdfObject object, final int refNumber)\n
    addToBody(final PdfObject object, final int refNumber, final boolean inObjStm)\n
    '''
def setOpenAction():
    '''returns None\n\n
    setOpenAction(final String name)\n
    setOpenAction(final PdfAction action)\n
    '''
def setAdditionalAction():
    '''returns None\n\n
    setAdditionalAction(final PdfName actionType, final PdfAction action)\n
    '''
def setPageLabels():
    '''returns None\n\n
    setPageLabels(final PdfPageLabels pageLabels)\n
    '''
def getImportedPage():
    '''returns PdfImportedPage\n\n
    getImportedPage(final PdfReader reader, final int pageNumber)\n
    '''
def addJavaScript():
    '''returns None\n\n
    addJavaScript(final PdfAction js)\n
    addJavaScript(final String code, final boolean unicode)\n
    addJavaScript(final String code)\n
    '''
def setCropBoxSize():
    '''returns None\n\n
    setCropBoxSize(final Rectangle crop)\n
    '''
def getPageReference():
    '''returns PdfIndirectReference\n\n
    getPageReference(int page)\n
    '''
def addCalculationOrder():
    '''returns None\n\n
    addCalculationOrder(final PdfFormField annot)\n
    '''
def setSigFlags():
    '''returns None\n\n
    setSigFlags(final int f)\n
    '''
def addAnnotation():
    '''returns None\n\n
    addAnnotation(final PdfAnnotation annot)\n
    '''
def setPdfVersion():
    '''returns None\n\n
    setPdfVersion(final char version)\n
    '''
def reorderPages():
    '''returns int\n\n
    reorderPages(final int[] order)\n
    '''
def getSpaceCharRatio():
    '''returns float\n\n
    getSpaceCharRatio()\n
    '''
def setSpaceCharRatio():
    '''returns None\n\n
    setSpaceCharRatio(final float spaceCharRatio)\n
    '''
def setRunDirection():
    '''returns None\n\n
    setRunDirection(final int runDirection)\n
    '''
def getRunDirection():
    '''returns int\n\n
    getRunDirection()\n
    '''
def setDuration():
    '''returns None\n\n
    setDuration(final int seconds)\n
    '''
def setTransition():
    '''returns None\n\n
    setTransition(final PdfTransition transition)\n
    '''
def freeReader():
    '''returns None\n\n
    freeReader(final PdfReader reader)\n
    '''
def setPageAction():
    '''returns None\n\n
    setPageAction(final PdfName actionType, final PdfAction action)\n
    '''
def getCurrentDocumentSize():
    '''returns int\n\n
    getCurrentDocumentSize()\n
    '''
def isStrictImageSequence():
    '''returns boolean\n\n
    isStrictImageSequence()\n
    '''
def setStrictImageSequence():
    '''returns None\n\n
    setStrictImageSequence(final boolean strictImageSequence)\n
    '''
def setPageEmpty():
    '''returns None\n\n
    setPageEmpty(final boolean pageEmpty)\n
    '''
def getInfo():
    '''returns PdfDictionary\n\n
    getInfo()\n
    '''
def getExtraCatalog():
    '''returns PdfDictionary\n\n
    getExtraCatalog()\n
    '''
def setLinearPageMode():
    '''returns None\n\n
    setLinearPageMode()\n
    '''
def getGroup():
    '''returns PdfDictionary\n\n
    getGroup()\n
    '''
def setGroup():
    '''returns None\n\n
    setGroup(final PdfDictionary group)\n
    '''
def setPDFXConformance():
    '''returns None\n\n
    setPDFXConformance(final int pdfxConformance)\n
    '''
def getPDFXConformance():
    '''returns int\n\n
    getPDFXConformance()\n
    '''
def setOutputIntents():
    '''returns boolean\n\n
    setOutputIntents(final String outputConditionIdentifier, final String outputCondition, final String registryName, final String info, final byte[] destOutputProfile)\n
    setOutputIntents(final PdfReader reader, final boolean checkExistence)\n
    '''
def setBoxSize():
    '''returns None\n\n
    setBoxSize(final String boxName, final Rectangle size)\n
    '''
def getDefaultColorspace():
    '''returns PdfDictionary\n\n
    getDefaultColorspace()\n
    '''
def setDefaultColorspace():
    '''returns None\n\n
    setDefaultColorspace(final PdfName key, final PdfObject cs)\n
    '''
def isFullCompression():
    '''returns boolean\n\n
    isFullCompression()\n
    '''
def setFullCompression():
    '''returns None\n\n
    setFullCompression()\n
    '''
def getOCProperties():
    '''returns PdfOCProperties\n\n
    getOCProperties()\n
    '''
def addOCGRadioGroup():
    '''returns None\n\n
    addOCGRadioGroup(final ArrayList group)\n
    '''
def toPdf():
    '''returns None\n\n
    toPdf(final OutputStream os)\n
    toPdf(int midSize, final OutputStream os)\n
    toPdf(final PdfWriter writer, final OutputStream os)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Object o)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
