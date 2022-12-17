def ():
    '''returns ImportObject\n\n
    ()\n
    '''
def runExtension():
    '''returns boolean\n\n
    runExtension(final String extensionNames, final int mode, final Connection con, final Element e)\n
    '''
def importObjectData():
    '''returns None\n\n
    importObjectData(final Connection con, final Element objectElement)\n
    '''
def getColumnValue():
    '''returns String\n\n
    getColumnValue(final Element elem)\n
    '''
def getColumnOriginalValue():
    '''returns String\n\n
    getColumnOriginalValue(final Element elem)\n
    '''
def getValueText():
    '''returns String\n\n
    getValueText(final Element elem, final String nodename)\n
    '''
def replaceQuery():
    '''returns None\n\n
    replaceQuery(final Connection conn, final Element element)\n
    '''
def executeSql():
    '''returns None\n\n
    executeSql(final Connection conn, final Element element)\n
    '''
def deletion():
    '''returns None\n\n
    deletion(final Connection conn, final Element element)\n
    '''
def importFile():
    '''returns int\n\n
    importFile(final Connection c, final InputStream inputFile, final String filepath, final boolean validateXml)\n
    importFile(final ImportFileTag importFileTag, final MaximoResolver maximoResolver, final IProgressMonitor monitor)\n
    '''
def importDocument():
    '''returns None\n\n
    importDocument(final Connection c, final Document doc)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final File dir, final String name)\n
    '''
def importFiles():
    '''returns None\n\n
    importFiles(final RootTag rootTag, final MaximoResolver maximoResolver, final IProgressMonitor monitor)\n
    '''
def importFromFile():
    '''returns int\n\n
    importFromFile(final String filename, final boolean validateXml)\n
    importFromFile(final InputStream fileToImport, final String filepath, final ImportOptions options, final MaximoResolver maximoResolver)\n
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
def setVerbose():
    '''returns None\n\n
    setVerbose(final boolean shouldVerbose)\n
    '''
def setOutput():
    '''returns None\n\n
    setOutput(final PrintStream newOutput)\n
    '''
def addColumnValueReplacements():
    '''returns None\n\n
    addColumnValueReplacements(final Map<String, String> newColumnValueReplacements)\n
    '''
def resetOptionsToDefaults():
    '''returns None\n\n
    resetOptionsToDefaults()\n
    '''
