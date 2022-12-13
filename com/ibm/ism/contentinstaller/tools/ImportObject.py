def ImportObject():
    '''public ImportObject()
    '''
def runExtension():
    '''public boolean runExtension(final String extensionNames, final int mode, final Connection con, final Element e)
    '''
def importObjectData():
    '''public void importObjectData(final Connection con, final Element objectElement)
    '''
def getColumnValue():
    '''public String getColumnValue(final Element elem)
    '''
def getColumnOriginalValue():
    '''public String getColumnOriginalValue(final Element elem)
    '''
def getValueText():
    '''public String getValueText(final Element elem, final String nodename)
    '''
def isNull():
    '''public static boolean isNull(final String a)
    '''
def replaceQuery():
    '''public void replaceQuery(final Connection conn, final Element element)
    '''
def executeSql():
    '''public void executeSql(final Connection conn, final Element element)
    '''
def deletion():
    '''public void deletion(final Connection conn, final Element element)
    '''
def importFile():
    '''public void importFile(final Connection c, final InputStream inputFile, final String filepath, final boolean validateXml)
    public int importFile(final ImportFileTag importFileTag, final MaximoResolver maximoResolver, final IProgressMonitor monitor)
    '''
def importDocument():
    '''public void importDocument(final Connection c, final Document doc)
    '''
def accept():
    '''public boolean accept(final File dir, final String name)
    '''
def importFiles():
    '''public void importFiles(final RootTag rootTag, final MaximoResolver maximoResolver, final IProgressMonitor monitor)
    '''
def importFromFile():
    '''public int importFromFile(final String filename, final boolean validateXml)
    public int importFromFile(final InputStream fileToImport, final String filepath, final ImportOptions options, final MaximoResolver maximoResolver)
    public int importFromFile(final InputStream fileToImport, final String filepath, final boolean validateXml, final MaximoResolver maximoResolver)
    '''
def importFromDirectory():
    '''public int importFromDirectory(final String importDirectory)
    '''
def importFromFileList():
    '''public int importFromFileList(final String importXmlFileList, final boolean validateXml)
    '''
def main():
    '''public static void main(final String[] args)
    '''
def setVerbose():
    '''public void setVerbose(final boolean shouldVerbose)
    '''
def setOutput():
    '''public void setOutput(final PrintStream newOutput)
    '''
def doReplacementLookup():
    '''public static final String doReplacementLookup(final String lookup)
    '''
def addColumnValueReplacements():
    '''public void addColumnValueReplacements(final Map<String, String> newColumnValueReplacements)
    '''
def resetOptionsToDefaults():
    '''public void resetOptionsToDefaults()
    '''
