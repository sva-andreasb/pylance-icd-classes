IMPORT_CALLER_CMD_LINE = "int  1"
IMPORT_CALLER_CONTENT_INSTALLER = "int  2"
def ():
    '''returns ImportSAXObject\n\n
    ()\n
    '''
def runExtension():
    '''returns boolean\n\n
    runExtension(final String extensionNames, final int mode, final Connection con, final Element e)\n
    '''
def importFile():
    '''returns None\n\n
    importFile(final Connection c, final InputStream inputFile, final String filepath, final boolean validateXml)\n
    importFile(final Connection c, final InputStream inputFile)\n
    importFile(final Connection c, final InputStream inputFile, final Map<String, String[]> replacementColumns)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final File dir, final String name)\n
    '''
def importFromFile():
    '''returns int\n\n
    importFromFile(final String filename, final boolean validateXml)\n
    importFromFile(final InputStream fileToImport, final String filepath, final boolean validateXml, final MaximoResolver maximoResolver)\n
    '''
def importFromDirectory():
    '''returns int\n\n
    importFromDirectory(final String importDirectory)\n
    '''
def importFromFileList():
    '''returns int\n\n
    importFromFileList(final String importXmlFileList, final boolean validateXml)\n
    '''
def setProgressMonitor():
    '''returns None\n\n
    setProgressMonitor(final IProgressMonitor monitor)\n
    '''
def setOutput():
    '''returns None\n\n
    setOutput(final PrintStream newOutput)\n
    '''
def addColumnValueReplacements():
    '''returns None\n\n
    addColumnValueReplacements(final Map<String, String[]> newColumnValueReplacements)\n
    '''
def resetOptionsToDefaults():
    '''returns None\n\n
    resetOptionsToDefaults()\n
    '''
