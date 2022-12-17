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
def ():
    '''returns PdfAction\n\n
    ()\n
    (final URL url)\n
    (final URL url, final boolean isMap)\n
    (final String url)\n
    (final String url, final boolean isMap)\n
    (final String filename, final String name)\n
    (final String filename, final int page)\n
    (final int named)\n
    (final String application, final String parameters, final String operation, final String defaultDir)\n
    '''
def next():
    '''returns None\n\n
    next(final PdfAction na)\n
    '''
