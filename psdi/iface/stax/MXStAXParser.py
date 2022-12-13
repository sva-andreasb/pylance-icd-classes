def getInstance():
    '''    public static final MXStAXParser getInstance()
    '''
def getRootElementName():
    '''    public QName getRootElementName(final byte[] data)
    '''
def parse():
    '''    public Map<QName, XMLElementValue> parse(final byte[] data, final Set<QName> tags)
    public Map<QName, XMLElementValue> parse(final byte[] data, final Set<QName> tags, final boolean fetchAttrs)
    public Map<QName, XMLElementValue> parse(final InputStream ip, final Set<QName> tags, final boolean fetchAttrs)
    '''
def evaluateXPath():
    '''    public List<String> evaluateXPath(final byte[] data, final String xpath, final Map<String, String> prefixNSMap)
    public List<String> evaluateXPath(final InputStream xmlStream, final XPathExpression xpathExpr)
    public List<String> evaluateXPath(final byte[] data, final XPathExpression xpathExpr)
    '''
def removeXMLComments():
    '''    public byte[] removeXMLComments(final byte[] xmlWithComments)
    '''
def getElementValue():
    '''    public String getElementValue()
    '''
def getAttrbuteValueMap():
    '''    public Map<QName, String> getAttrbuteValueMap()
    '''
