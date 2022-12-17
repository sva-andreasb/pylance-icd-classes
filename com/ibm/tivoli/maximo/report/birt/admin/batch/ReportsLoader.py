LIBRARYFOLDER = "String  \"${libraryfolder}\""
def ():
    '''returns ReportsLoader\n\n
    ()\n
    (final MXLogger reportAdminServiceLogger)\n
    '''
def setLibraryFolder():
    '''returns None\n\n
    setLibraryFolder(final String folderName)\n
    '''
def loadReports():
    '''returns ArrayList<ReportInfo>\n\n
    loadReports(final String reportsXMLFile)\n
    loadReports(final String reportsXMLFile, final boolean createResourcesZip)\n
    '''
def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String publicId, final String systemId)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException e)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException e)\n
    '''
def warning():
    '''returns None\n\n
    warning(final SAXParseException exception)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final File pathname)\n
    '''
