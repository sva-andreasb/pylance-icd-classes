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
'''public static PdfWriter getInstance(final Document document, final OutputStream os)
public static PdfWriter getInstance(final Document document, final OutputStream os, final DocListener listener)
'''
pass
def open():
'''public void open()
'''
pass
def close():
'''public synchronized void close()
'''
pass
def getTableBottom():
'''public float getTableBottom(final Table table)
'''
pass
def getPdfTable():
'''public PdfTable getPdfTable(final Table table)
'''
pass
def breakTableIfDoesntFit():
'''public boolean breakTableIfDoesntFit(final PdfTable table)
'''
pass
def fitsPage():
'''public boolean fitsPage(final Table table, final float margin)
public boolean fitsPage(final Table table)
public boolean fitsPage(final PdfPTable table, final float margin)
public boolean fitsPage(final PdfPTable table)
'''
pass
def getVerticalPosition():
'''public float getVerticalPosition(final boolean ensureNewLine)
'''
pass
def getDirectContent():
'''public PdfContentByte getDirectContent()
'''
pass
def getDirectContentUnder():
'''public PdfContentByte getDirectContentUnder()
'''
pass
def getAcroForm():
'''public PdfAcroForm getAcroForm()
'''
pass
def getRootOutline():
'''public PdfOutline getRootOutline()
'''
pass
def getOs():
'''public OutputStreamCounter getOs()
'''
pass
def getPdfIndirectReference():
'''public PdfIndirectReference getPdfIndirectReference()
'''
pass
def setPageEvent():
'''public void setPageEvent(final PdfPageEvent pageEvent)
'''
pass
def getPageEvent():
'''public PdfPageEvent getPageEvent()
'''
pass
def getPageNumber():
'''public int getPageNumber()
'''
pass
def setViewerPreferences():
'''public void setViewerPreferences(final int preferences)
'''
pass
def setEncryption():
'''public void setEncryption(final byte[] userPassword, final byte[] ownerPassword, final int permissions, final boolean strength128Bits)
public void setEncryption(final boolean strength, final String userPassword, final String ownerPassword, final int permissions)
'''
pass
def addToBody():
'''public PdfIndirectObject addToBody(final PdfObject object)
public PdfIndirectObject addToBody(final PdfObject object, final boolean inObjStm)
public PdfIndirectObject addToBody(final PdfObject object, final PdfIndirectReference ref)
public PdfIndirectObject addToBody(final PdfObject object, final PdfIndirectReference ref, final boolean inObjStm)
public PdfIndirectObject addToBody(final PdfObject object, final int refNumber)
public PdfIndirectObject addToBody(final PdfObject object, final int refNumber, final boolean inObjStm)
'''
pass
def setOpenAction():
'''public void setOpenAction(final String name)
public void setOpenAction(final PdfAction action)
'''
pass
def setAdditionalAction():
'''public void setAdditionalAction(final PdfName actionType, final PdfAction action)
'''
pass
def setPageLabels():
'''public void setPageLabels(final PdfPageLabels pageLabels)
'''
pass
def getImportedPage():
'''public PdfImportedPage getImportedPage(final PdfReader reader, final int pageNumber)
'''
pass
def addJavaScript():
'''public void addJavaScript(final PdfAction js)
public void addJavaScript(final String code, final boolean unicode)
public void addJavaScript(final String code)
'''
pass
def setCropBoxSize():
'''public void setCropBoxSize(final Rectangle crop)
'''
pass
def getPageReference():
'''public PdfIndirectReference getPageReference(int page)
'''
pass
def addCalculationOrder():
'''public void addCalculationOrder(final PdfFormField annot)
'''
pass
def setSigFlags():
'''public void setSigFlags(final int f)
'''
pass
def addAnnotation():
'''public void addAnnotation(final PdfAnnotation annot)
'''
pass
def setPdfVersion():
'''public void setPdfVersion(final char version)
'''
pass
def reorderPages():
'''public int reorderPages(final int[] order)
'''
pass
def getSpaceCharRatio():
'''public float getSpaceCharRatio()
'''
pass
def setSpaceCharRatio():
'''public void setSpaceCharRatio(final float spaceCharRatio)
'''
pass
def setRunDirection():
'''public void setRunDirection(final int runDirection)
'''
pass
def getRunDirection():
'''public int getRunDirection()
'''
pass
def setDuration():
'''public void setDuration(final int seconds)
'''
pass
def setTransition():
'''public void setTransition(final PdfTransition transition)
'''
pass
def freeReader():
'''public void freeReader(final PdfReader reader)
'''
pass
def setPageAction():
'''public void setPageAction(final PdfName actionType, final PdfAction action)
'''
pass
def getCurrentDocumentSize():
'''public int getCurrentDocumentSize()
'''
pass
def isStrictImageSequence():
'''public boolean isStrictImageSequence()
'''
pass
def setStrictImageSequence():
'''public void setStrictImageSequence(final boolean strictImageSequence)
'''
pass
def setPageEmpty():
'''public void setPageEmpty(final boolean pageEmpty)
'''
pass
def getInfo():
'''public PdfDictionary getInfo()
'''
pass
def getExtraCatalog():
'''public PdfDictionary getExtraCatalog()
'''
pass
def setLinearPageMode():
'''public void setLinearPageMode()
'''
pass
def getGroup():
'''public PdfDictionary getGroup()
'''
pass
def setGroup():
'''public void setGroup(final PdfDictionary group)
'''
pass
def setPDFXConformance():
'''public void setPDFXConformance(final int pdfxConformance)
'''
pass
def getPDFXConformance():
'''public int getPDFXConformance()
'''
pass
def setOutputIntents():
'''public void setOutputIntents(final String outputConditionIdentifier, final String outputCondition, final String registryName, final String info, final byte[] destOutputProfile)
public boolean setOutputIntents(final PdfReader reader, final boolean checkExistence)
'''
pass
def setBoxSize():
'''public void setBoxSize(final String boxName, final Rectangle size)
'''
pass
def getDefaultColorspace():
'''public PdfDictionary getDefaultColorspace()
'''
pass
def setDefaultColorspace():
'''public void setDefaultColorspace(final PdfName key, final PdfObject cs)
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
def getOCProperties():
'''public PdfOCProperties getOCProperties()
'''
pass
def addOCGRadioGroup():
'''public void addOCGRadioGroup(final ArrayList group)
'''
pass
def toPdf():
'''public void toPdf(final OutputStream os)
public void toPdf(int midSize, final OutputStream os)
public void toPdf(final PdfWriter writer, final OutputStream os)
'''
pass
def compareTo():
'''public int compareTo(final Object o)
'''
pass
def equals():
'''public boolean equals(final Object obj)
'''
pass
