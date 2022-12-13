XHTML_1_0_URI = "String  http://www.w3.org/1999/xhtml""
XML_URI = "String  http://www.w3.org/XML/1998/namespace""
XMLNS_URI = "String  http://www.w3.org/2000/xmlns/""
def NamespaceBinder():
'''public NamespaceBinder()
'''
pass
def getRecognizedFeatures():
'''public String[] getRecognizedFeatures()
'''
pass
def getFeatureDefault():
'''public Boolean getFeatureDefault(final String featureId)
'''
pass
def getRecognizedProperties():
'''public String[] getRecognizedProperties()
'''
pass
def getPropertyDefault():
'''public Object getPropertyDefault(final String propertyId)
'''
pass
def reset():
'''public void reset(final XMLComponentManager manager)
public void reset()
'''
pass
def startDocument():
'''public void startDocument(final XMLLocator locator, final String encoding, final NamespaceContext nscontext, final Augmentations augs)
'''
pass
def startElement():
'''public void startElement(final QName element, final XMLAttributes attrs, final Augmentations augs)
'''
pass
def emptyElement():
'''public void emptyElement(final QName element, final XMLAttributes attrs, final Augmentations augs)
'''
pass
def endElement():
'''public void endElement(final QName element, final Augmentations augs)
'''
pass
def NamespaceSupport():
'''public NamespaceSupport()
'''
pass
def getURI():
'''public String getURI(final String prefix)
'''
pass
def getDeclaredPrefixCount():
'''public int getDeclaredPrefixCount()
'''
pass
def getDeclaredPrefixAt():
'''public String getDeclaredPrefixAt(final int index)
'''
pass
def getParentContext():
'''public NamespaceContext getParentContext()
'''
pass
def pushContext():
'''public void pushContext()
'''
pass
def popContext():
'''public void popContext()
'''
pass
def declarePrefix():
'''public boolean declarePrefix(final String prefix, final String uri)
'''
pass
def getPrefix():
'''public String getPrefix(final String uri)
'''
pass
def getAllPrefixes():
'''public Enumeration getAllPrefixes()
'''
pass
def Entry():
'''public Entry(final String prefix, final String uri)
'''
pass
