FULL_XML_STRING = "int  0"
MSS_XML_STRING = "int  1"
ME_XML_STRING = "int  2"
REL_XML_STRING = "int  3"
def IdmlObjects():
'''public IdmlObjects()
'''
pass
def parse():
'''public void parse(final InputSource is)
public void parse(final String xml, final int xmltype)
'''
pass
def getMssElements():
'''public List getMssElements()
'''
pass
def getManagedElements():
'''public List getManagedElements()
public List<Map<String, String>> getManagedElements(final String xml, final List<Map<String, String>> extendedAttr, final boolean addIdAndSuperior)
'''
pass
def getExtendedAttributes():
'''public List getExtendedAttributes()
'''
pass
def getRelationships():
'''public List getRelationships()
'''
pass
def IdmlNamespaceContext():
'''public IdmlNamespaceContext()
'''
pass
def getNamespaceURI():
'''public String getNamespaceURI(final String prefix)
'''
pass
def getPrefix():
'''public String getPrefix(final String namespaceURI)
'''
pass
def getPrefixes():
'''public Iterator getPrefixes(final String namespaceURI)
'''
pass
def warning():
'''public void warning(final SAXParseException spe)
'''
pass
def error():
'''public void error(final SAXParseException spe)
'''
pass
def fatalError():
'''public void fatalError(final SAXParseException spe)
'''
pass
