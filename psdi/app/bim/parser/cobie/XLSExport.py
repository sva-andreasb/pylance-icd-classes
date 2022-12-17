H_ALIGN_CENTER = "short  1"
V_ALIGN_BOTTOM = "short  2"
BORDER_THIN = "short  1"
def ():
    '''returns XLSExport\n\n
    (final MessageLogger logger, final InputStream templateStream, final ExportFormat fileFormat)\n
    '''
def getLogger():
    '''returns MessageLogger\n\n
    getLogger()\n
    '''
def addRow():
    '''returns None\n\n
    addRow(final String[] columnValues)\n
    '''
def processPage():
    '''returns None\n\n
    processPage(final String pageName, final String[] colNames)\n
    '''
def getColumnNames():
    '''returns String[]\n\n
    getColumnNames()\n
    '''
def write():
    '''returns None\n\n
    write(final String fileName)\n
    '''
