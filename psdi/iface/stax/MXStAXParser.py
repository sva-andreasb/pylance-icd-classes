def getInstance():
'''public static final MXStAXParser getInstance()
'''
pass
def getRootElementName():
'''public QName getRootElementName(final byte[] data)
'''
pass
def parse():
'''public Map<QName, XMLElementValue> parse(final byte[] data, final Set<QName> tags)
public Map<QName, XMLElementValue> parse(final byte[] data, final Set<QName> tags, final boolean fetchAttrs)
public Map<QName, XMLElementValue> parse(final InputStream ip, final Set<QName> tags, final boolean fetchAttrs)
'''
pass
def evaluateXPath():
'''public List<String> evaluateXPath(final byte[] data, final String xpath, final Map<String, String> prefixNSMap)
public List<String> evaluateXPath(final InputStream xmlStream, final XPathExpression xpathExpr)
public List<String> evaluateXPath(final byte[] data, final XPathExpression xpathExpr)
'''
pass
def removeXMLComments():
'''public byte[] removeXMLComments(final byte[] xmlWithComments)
'''
pass
def getElementValue():
'''public String getElementValue()
'''
pass
def getAttrbuteValueMap():
'''public Map<QName, String> getAttrbuteValueMap()
'''
pass
