def getMaximoConnection():
    '''    public Connection getMaximoConnection(final MaximoResolver maximoResolver)
    '''
def addMonitor():
    '''    public void addMonitor(final IProgressMonitor newMonitor)
    '''
def removeMonitor():
    '''    public void removeMonitor(final IProgressMonitor monitor)
    '''
def importFromFile():
    '''    public void importFromFile(final File importXml, final ImportOptions options, final MaximoResolver maximoResolver, final PrintStream printStream)
    '''
def exportToFile():
    '''    public void exportToFile(final String exportXmlStructure, final String whereClause, final String outputFile, final ExportOptions options, final IProgressMonitor monitor, final MaximoResolver maximoResolver)
    '''
def exportFiles():
    '''    public void exportFiles(final RootTag rootTag, final MaximoResolver maximoResolver, final IProgressMonitor monitor)
    '''
def importFiles():
    '''    public void importFiles(final RootTag rootTag, final PrintStream printStream, final MaximoResolver maximoResolver, final IProgressMonitor monitor)
    '''
def exportObjectStructure():
    '''    public void exportObjectStructure(final MaximoResolver maximoResolver, final String objectName, final int maxDepth, final File outFileName, final boolean addKeyColumns)
    '''
def parseSingleImport():
    '''    public RootTag parseSingleImport(final InputStream singleImportStream, final IPackageResolver resolver)
    '''
def parsePackageImport():
    '''    public RootTag parsePackageImport(final URI pkgImportUri, final IPackageResolver resolver)
    '''
def parsePackageExport():
    '''    public RootTag parsePackageExport(final URI pkgExportUri, final IPackageResolver resolver)
    '''
def testConnection():
    '''    public boolean testConnection(final String dbDriver, final String dbUrl, final String dbUser, final String dbPassword, final String dbSchemaOwner)
    '''
def getKeyColumns():
    '''    public List<KeyColumn> getKeyColumns(final RootTag rootTag, final MaximoResolver maximoResolver)
    '''
