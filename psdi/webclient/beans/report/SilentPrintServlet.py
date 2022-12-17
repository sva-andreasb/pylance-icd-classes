DOCLINK_PDFURL = "int  1"
DOCLINK_2PASSPDF = "int  3"
DOCLINK_2PDFSTAMP = "int  4"
DOCLINK_2PDFERROR = "int  5"
BIRT_PDF_REPORT = "int  11"
BIRT_PDF_PRINT = "int  33"
DOCLINK_GETTOKEN = "int  22"
VALIDATE_URL = "int  44"
PREPARE_DOC = "int  55"
securedDocPrefix = "String  \"securedAttachmentNonApplet=\""
def ():
    '''returns SilentPrintServlet\n\n
    ()\n
    '''
def doGet():
    '''returns None\n\n
    doGet(final HttpServletRequest requ, final HttpServletResponse resp)\n
    '''
def doPost():
    '''returns None\n\n
    doPost(final HttpServletRequest requ, final HttpServletResponse resp)\n
    '''
def doWork():
    '''returns None\n\n
    doWork(final HttpServletRequest requ, final HttpServletResponse resp)\n
    '''
def concatPDFFiles():
    '''returns boolean\n\n
    concatPDFFiles(final String outPutDirPath, final String outPutFilePath, final Vector<PathAndReportFlag> listOfFiles)\n
    '''
