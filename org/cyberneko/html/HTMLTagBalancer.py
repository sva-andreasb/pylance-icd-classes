FRAGMENT_CONTEXT_STACK = "String  http://cyberneko.org/html/properties/balance-tags/fragment-context-stack""
def HTMLTagBalancer():
'''public HTMLTagBalancer()
'''
pass
def getFeatureDefault():
'''public Boolean getFeatureDefault(final String featureId)
'''
pass
def getPropertyDefault():
'''public Object getPropertyDefault(final String propertyId)
'''
pass
def getRecognizedFeatures():
'''public String[] getRecognizedFeatures()
'''
pass
def getRecognizedProperties():
'''public String[] getRecognizedProperties()
'''
pass
def reset():
'''public void reset(final XMLComponentManager manager)
'''
pass
def setFeature():
'''public void setFeature(final String featureId, final boolean state)
'''
pass
def setProperty():
'''public void setProperty(final String propertyId, final Object value)
'''
pass
def setDocumentHandler():
'''public void setDocumentHandler(final XMLDocumentHandler handler)
'''
pass
def getDocumentHandler():
'''public XMLDocumentHandler getDocumentHandler()
'''
pass
def startDocument():
'''public void startDocument(final XMLLocator locator, final String encoding, final NamespaceContext nscontext, final Augmentations augs)
public void startDocument(final XMLLocator locator, final String encoding, final Augmentations augs)
'''
pass
def xmlDecl():
'''public void xmlDecl(final String version, final String encoding, final String standalone, final Augmentations augs)
'''
pass
def doctypeDecl():
'''public void doctypeDecl(final String rootElementName, final String publicId, final String systemId, final Augmentations augs)
'''
pass
def endDocument():
'''public void endDocument(final Augmentations augs)
'''
pass
def comment():
'''public void comment(final XMLString text, final Augmentations augs)
'''
pass
def processingInstruction():
'''public void processingInstruction(final String target, final XMLString data, final Augmentations augs)
'''
pass
def startElement():
'''public void startElement(final QName elem, XMLAttributes attrs, final Augmentations augs)
'''
pass
def emptyElement():
'''public void emptyElement(final QName element, final XMLAttributes attrs, final Augmentations augs)
'''
pass
def startGeneralEntity():
'''public void startGeneralEntity(final String name, final XMLResourceIdentifier id, final String encoding, final Augmentations augs)
'''
pass
def textDecl():
'''public void textDecl(final String version, final String encoding, final Augmentations augs)
'''
pass
def endGeneralEntity():
'''public void endGeneralEntity(final String name, final Augmentations augs)
'''
pass
def startCDATA():
'''public void startCDATA(final Augmentations augs)
'''
pass
def endCDATA():
'''public void endCDATA(final Augmentations augs)
'''
pass
def characters():
'''public void characters(final XMLString text, final Augmentations augs)
'''
pass
def ignorableWhitespace():
'''public void ignorableWhitespace(final XMLString text, final Augmentations augs)
'''
pass
def endElement():
'''public void endElement(final QName element, final Augmentations augs)
'''
pass
def setDocumentSource():
'''public void setDocumentSource(final XMLDocumentSource source)
'''
pass
def getDocumentSource():
'''public XMLDocumentSource getDocumentSource()
'''
pass
def startPrefixMapping():
'''public void startPrefixMapping(final String prefix, final String uri, final Augmentations augs)
'''
pass
def endPrefixMapping():
'''public void endPrefixMapping(final String prefix, final Augmentations augs)
'''
pass
def Info():
'''public Info(final HTMLElements.Element element, final QName qname)
public Info(final HTMLElements.Element element, final QName qname, final XMLAttributes attributes)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def InfoStack():
'''public InfoStack()
'''
pass
def push():
'''public void push(final Info info)
'''
pass
def peek():
'''public Info peek()
'''
pass
def pop():
'''public Info pop()
'''
pass
