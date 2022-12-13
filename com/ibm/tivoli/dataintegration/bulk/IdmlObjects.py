FULL_XML_STRING = "int  0"
MSS_XML_STRING = "int  1"
ME_XML_STRING = "int  2"
REL_XML_STRING = "int  3"
def IdmlObjects():
    '''    public IdmlObjects()
    '''
def parse():
    '''    public void parse(final InputSource is)
    public void parse(final String xml, final int xmltype)
    '''
def getMssElements():
    '''    public List getMssElements()
    '''
def getManagedElements():
    '''    public List getManagedElements()
    public List<Map<String, String>> getManagedElements(final String xml, final List<Map<String, String>> extendedAttr, final boolean addIdAndSuperior)
    '''
def getExtendedAttributes():
    '''    public List getExtendedAttributes()
    '''
def getRelationships():
    '''    public List getRelationships()
    '''
def IdmlNamespaceContext():
    '''    public IdmlNamespaceContext()
    '''
def getNamespaceURI():
    '''    public String getNamespaceURI(final String prefix)
    '''
def getPrefix():
    '''    public String getPrefix(final String namespaceURI)
    '''
def getPrefixes():
    '''    public Iterator getPrefixes(final String namespaceURI)
    '''
def warning():
    '''    public void warning(final SAXParseException spe)
    '''
def error():
    '''    public void error(final SAXParseException spe)
    '''
def fatalError():
    '''    public void fatalError(final SAXParseException spe)
    '''
