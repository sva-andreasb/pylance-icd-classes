def getMaximoConnection():
    '''returns Connection\n\n
    getMaximoConnection(final MaximoResolver maximoResolver)\n
    '''
def addMonitor():
    '''returns None\n\n
    addMonitor(final IProgressMonitor newMonitor)\n
    '''
def removeMonitor():
    '''returns None\n\n
    removeMonitor(final IProgressMonitor monitor)\n
    '''
def importFromFile():
    '''returns None\n\n
    importFromFile(final File importXml, final ImportOptions options, final MaximoResolver maximoResolver, final PrintStream printStream)\n
    '''
def exportToFile():
    '''returns None\n\n
    exportToFile(final String exportXmlStructure, final String whereClause, final String outputFile, final ExportOptions options, final IProgressMonitor monitor, final MaximoResolver maximoResolver)\n
    '''
def exportFiles():
    '''returns None\n\n
    exportFiles(final RootTag rootTag, final MaximoResolver maximoResolver, final IProgressMonitor monitor)\n
    '''
def importFiles():
    '''returns None\n\n
    importFiles(final RootTag rootTag, final PrintStream printStream, final MaximoResolver maximoResolver, final IProgressMonitor monitor)\n
    '''
def exportObjectStructure():
    '''returns None\n\n
    exportObjectStructure(final MaximoResolver maximoResolver, final String objectName, final int maxDepth, final File outFileName, final boolean addKeyColumns)\n
    '''
def parseSingleImport():
    '''returns RootTag\n\n
    parseSingleImport(final InputStream singleImportStream, final IPackageResolver resolver)\n
    '''
def parsePackageImport():
    '''returns RootTag\n\n
    parsePackageImport(final URI pkgImportUri, final IPackageResolver resolver)\n
    '''
def parsePackageExport():
    '''returns RootTag\n\n
    parsePackageExport(final URI pkgExportUri, final IPackageResolver resolver)\n
    '''
def testConnection():
    '''returns boolean\n\n
    testConnection(final String dbDriver, final String dbUrl, final String dbUser, final String dbPassword, final String dbSchemaOwner)\n
    '''
def getKeyColumns():
    '''returns List<KeyColumn>\n\n
    getKeyColumns(final RootTag rootTag, final MaximoResolver maximoResolver)\n
    '''
