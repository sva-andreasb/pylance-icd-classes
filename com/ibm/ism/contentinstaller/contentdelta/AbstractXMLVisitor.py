def AbstractXMLVisitor():
    '''public AbstractXMLVisitor()
    '''
def parseAllXmlFilesInDirectory():
    '''public void parseAllXmlFilesInDirectory(final String directory)
    public void parseAllXmlFilesInDirectory(final String directory, final boolean allowXmlSnippets, final String[] excludeFileNames)
    '''
def setKeepRootElementsByFileName():
    '''public void setKeepRootElementsByFileName(final boolean keepRootElementsByFileName)
    '''
def getElementPathInXml():
    '''public static String getElementPathInXml(final Element element)
    '''
def getColumnValue():
    '''public static String getColumnValue(final Element element, final String columnName)
    '''
def getRootElementsByFileName():
    '''public SortedMap<String, Element> getRootElementsByFileName()
    '''
def XMLVisitorException():
    '''public XMLVisitorException(final String message, final Element element, final File file)
    '''
