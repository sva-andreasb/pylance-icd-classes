def getMaximoConnection():
'''public Connection getMaximoConnection(final MaximoResolver maximoResolver)
'''
pass
def addMonitor():
'''public void addMonitor(final IProgressMonitor newMonitor)
'''
pass
def removeMonitor():
'''public void removeMonitor(final IProgressMonitor monitor)
'''
pass
def importFromFile():
'''public void importFromFile(final File importXml, final ImportOptions options, final MaximoResolver maximoResolver, final PrintStream printStream)
'''
pass
def exportToFile():
'''public void exportToFile(final String exportXmlStructure, final String whereClause, final String outputFile, final ExportOptions options, final IProgressMonitor monitor, final MaximoResolver maximoResolver)
'''
pass
def exportFiles():
'''public void exportFiles(final RootTag rootTag, final MaximoResolver maximoResolver, final IProgressMonitor monitor)
'''
pass
def importFiles():
'''public void importFiles(final RootTag rootTag, final PrintStream printStream, final MaximoResolver maximoResolver, final IProgressMonitor monitor)
'''
pass
def exportObjectStructure():
'''public void exportObjectStructure(final MaximoResolver maximoResolver, final String objectName, final int maxDepth, final File outFileName, final boolean addKeyColumns)
'''
pass
def parseSingleImport():
'''public RootTag parseSingleImport(final InputStream singleImportStream, final IPackageResolver resolver)
'''
pass
def parsePackageImport():
'''public RootTag parsePackageImport(final URI pkgImportUri, final IPackageResolver resolver)
'''
pass
def parsePackageExport():
'''public RootTag parsePackageExport(final URI pkgExportUri, final IPackageResolver resolver)
'''
pass
def testConnection():
'''public boolean testConnection(final String dbDriver, final String dbUrl, final String dbUser, final String dbPassword, final String dbSchemaOwner)
'''
pass
def getKeyColumns():
'''public List<KeyColumn> getKeyColumns(final RootTag rootTag, final MaximoResolver maximoResolver)
'''
pass
