FIRSTPAGE = "int  1"
PREVPAGE = "int  2"
NEXTPAGE = "int  3"
LASTPAGE = "int  4"
PRINTDIALOG = "int  5"
SUBMIT_EXCLUDE = "int  1"
SUBMIT_INCLUDE_NO_VALUE_FIELDS = "int  2"
SUBMIT_HTML_FORMAT = "int  4"
SUBMIT_HTML_GET = "int  8"
SUBMIT_COORDINATES = "int  16"
SUBMIT_XFDF = "int  32"
SUBMIT_INCLUDE_APPEND_SAVES = "int  64"
SUBMIT_INCLUDE_ANNOTATIONS = "int  128"
SUBMIT_PDF = "int  256"
SUBMIT_CANONICAL_FORMAT = "int  512"
SUBMIT_EXCL_NON_USER_ANNOTS = "int  1024"
SUBMIT_EXCL_F_KEY = "int  2048"
SUBMIT_EMBED_FORM = "int  8196"
RESET_EXCLUDE = "int  1"
def PdfAction():
'''public PdfAction()
public PdfAction(final URL url)
public PdfAction(final URL url, final boolean isMap)
public PdfAction(final String url)
public PdfAction(final String url, final boolean isMap)
public PdfAction(final String filename, final String name)
public PdfAction(final String filename, final int page)
public PdfAction(final int named)
public PdfAction(final String application, final String parameters, final String operation, final String defaultDir)
'''
pass
def createLaunch():
'''public static PdfAction createLaunch(final String application, final String parameters, final String operation, final String defaultDir)
'''
pass
def rendition():
'''public static PdfAction rendition(final String file, final PdfFileSpecification fs, final String mimeType, final PdfIndirectReference ref)
'''
pass
def javaScript():
'''public static PdfAction javaScript(final String code, final PdfWriter writer, final boolean unicode)
public static PdfAction javaScript(final String code, final PdfWriter writer)
'''
pass
def createHide():
'''public static PdfAction createHide(final PdfAnnotation annot, final boolean hide)
public static PdfAction createHide(final String name, final boolean hide)
public static PdfAction createHide(final Object[] names, final boolean hide)
'''
pass
def createSubmitForm():
'''public static PdfAction createSubmitForm(final String file, final Object[] names, final int flags)
'''
pass
def createResetForm():
'''public static PdfAction createResetForm(final Object[] names, final int flags)
'''
pass
def createImportData():
'''public static PdfAction createImportData(final String file)
'''
pass
def next():
'''public void next(final PdfAction na)
'''
pass
def gotoLocalPage():
'''public static PdfAction gotoLocalPage(final int page, final PdfDestination dest, final PdfWriter writer)
public static PdfAction gotoLocalPage(final String dest, final boolean isName)
'''
pass
def gotoRemotePage():
'''public static PdfAction gotoRemotePage(final String filename, final String dest, final boolean isName, final boolean newWindow)
'''
pass
def setOCGstate():
'''public static PdfAction setOCGstate(final ArrayList state, final boolean preserveRB)
'''
pass
