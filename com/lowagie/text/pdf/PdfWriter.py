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
def getInstance():
    '''    public static PdfWriter getInstance(final Document document, final OutputStream os)
    public static PdfWriter getInstance(final Document document, final OutputStream os, final DocListener listener)
    '''
def open():
    '''    public void open()
    '''
def close():
    '''    public synchronized void close()
    '''
def getTableBottom():
    '''    public float getTableBottom(final Table table)
    '''
def getPdfTable():
    '''    public PdfTable getPdfTable(final Table table)
    '''
def breakTableIfDoesntFit():
    '''    public boolean breakTableIfDoesntFit(final PdfTable table)
    '''
def fitsPage():
    '''    public boolean fitsPage(final Table table, final float margin)
    public boolean fitsPage(final Table table)
    public boolean fitsPage(final PdfPTable table, final float margin)
    public boolean fitsPage(final PdfPTable table)
    '''
def getVerticalPosition():
    '''    public float getVerticalPosition(final boolean ensureNewLine)
    '''
def getDirectContent():
    '''    public PdfContentByte getDirectContent()
    '''
def getDirectContentUnder():
    '''    public PdfContentByte getDirectContentUnder()
    '''
def getAcroForm():
    '''    public PdfAcroForm getAcroForm()
    '''
def getRootOutline():
    '''    public PdfOutline getRootOutline()
    '''
def getOs():
    '''    public OutputStreamCounter getOs()
    '''
def getPdfIndirectReference():
    '''    public PdfIndirectReference getPdfIndirectReference()
    '''
def setPageEvent():
    '''    public void setPageEvent(final PdfPageEvent pageEvent)
    '''
def getPageEvent():
    '''    public PdfPageEvent getPageEvent()
    '''
def getPageNumber():
    '''    public int getPageNumber()
    '''
def setViewerPreferences():
    '''    public void setViewerPreferences(final int preferences)
    '''
def setEncryption():
    '''    public void setEncryption(final byte[] userPassword, final byte[] ownerPassword, final int permissions, final boolean strength128Bits)
    public void setEncryption(final boolean strength, final String userPassword, final String ownerPassword, final int permissions)
    '''
def addToBody():
    '''    public PdfIndirectObject addToBody(final PdfObject object)
    public PdfIndirectObject addToBody(final PdfObject object, final boolean inObjStm)
    public PdfIndirectObject addToBody(final PdfObject object, final PdfIndirectReference ref)
    public PdfIndirectObject addToBody(final PdfObject object, final PdfIndirectReference ref, final boolean inObjStm)
    public PdfIndirectObject addToBody(final PdfObject object, final int refNumber)
    public PdfIndirectObject addToBody(final PdfObject object, final int refNumber, final boolean inObjStm)
    '''
def setOpenAction():
    '''    public void setOpenAction(final String name)
    public void setOpenAction(final PdfAction action)
    '''
def setAdditionalAction():
    '''    public void setAdditionalAction(final PdfName actionType, final PdfAction action)
    '''
def setPageLabels():
    '''    public void setPageLabels(final PdfPageLabels pageLabels)
    '''
def getImportedPage():
    '''    public PdfImportedPage getImportedPage(final PdfReader reader, final int pageNumber)
    '''
def addJavaScript():
    '''    public void addJavaScript(final PdfAction js)
    public void addJavaScript(final String code, final boolean unicode)
    public void addJavaScript(final String code)
    '''
def setCropBoxSize():
    '''    public void setCropBoxSize(final Rectangle crop)
    '''
def getPageReference():
    '''    public PdfIndirectReference getPageReference(int page)
    '''
def addCalculationOrder():
    '''    public void addCalculationOrder(final PdfFormField annot)
    '''
def setSigFlags():
    '''    public void setSigFlags(final int f)
    '''
def addAnnotation():
    '''    public void addAnnotation(final PdfAnnotation annot)
    '''
def setPdfVersion():
    '''    public void setPdfVersion(final char version)
    '''
def reorderPages():
    '''    public int reorderPages(final int[] order)
    '''
def getSpaceCharRatio():
    '''    public float getSpaceCharRatio()
    '''
def setSpaceCharRatio():
    '''    public void setSpaceCharRatio(final float spaceCharRatio)
    '''
def setRunDirection():
    '''    public void setRunDirection(final int runDirection)
    '''
def getRunDirection():
    '''    public int getRunDirection()
    '''
def setDuration():
    '''    public void setDuration(final int seconds)
    '''
def setTransition():
    '''    public void setTransition(final PdfTransition transition)
    '''
def freeReader():
    '''    public void freeReader(final PdfReader reader)
    '''
def setPageAction():
    '''    public void setPageAction(final PdfName actionType, final PdfAction action)
    '''
def getCurrentDocumentSize():
    '''    public int getCurrentDocumentSize()
    '''
def isStrictImageSequence():
    '''    public boolean isStrictImageSequence()
    '''
def setStrictImageSequence():
    '''    public void setStrictImageSequence(final boolean strictImageSequence)
    '''
def setPageEmpty():
    '''    public void setPageEmpty(final boolean pageEmpty)
    '''
def getInfo():
    '''    public PdfDictionary getInfo()
    '''
def getExtraCatalog():
    '''    public PdfDictionary getExtraCatalog()
    '''
def setLinearPageMode():
    '''    public void setLinearPageMode()
    '''
def getGroup():
    '''    public PdfDictionary getGroup()
    '''
def setGroup():
    '''    public void setGroup(final PdfDictionary group)
    '''
def setPDFXConformance():
    '''    public void setPDFXConformance(final int pdfxConformance)
    '''
def getPDFXConformance():
    '''    public int getPDFXConformance()
    '''
def setOutputIntents():
    '''    public void setOutputIntents(final String outputConditionIdentifier, final String outputCondition, final String registryName, final String info, final byte[] destOutputProfile)
    public boolean setOutputIntents(final PdfReader reader, final boolean checkExistence)
    '''
def setBoxSize():
    '''    public void setBoxSize(final String boxName, final Rectangle size)
    '''
def getDefaultColorspace():
    '''    public PdfDictionary getDefaultColorspace()
    '''
def setDefaultColorspace():
    '''    public void setDefaultColorspace(final PdfName key, final PdfObject cs)
    '''
def isFullCompression():
    '''    public boolean isFullCompression()
    '''
def setFullCompression():
    '''    public void setFullCompression()
    '''
def getOCProperties():
    '''    public PdfOCProperties getOCProperties()
    '''
def addOCGRadioGroup():
    '''    public void addOCGRadioGroup(final ArrayList group)
    '''
def toPdf():
    '''    public void toPdf(final OutputStream os)
    public void toPdf(int midSize, final OutputStream os)
    public void toPdf(final PdfWriter writer, final OutputStream os)
    '''
def compareTo():
    '''    public int compareTo(final Object o)
    '''
def equals():
    '''    public boolean equals(final Object obj)
    '''
