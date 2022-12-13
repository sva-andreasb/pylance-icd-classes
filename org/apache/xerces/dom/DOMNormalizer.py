def DOMNormalizer():
'''public DOMNormalizer()
'''
pass
def isCDataWF():
'''public static final void isCDataWF(final DOMErrorHandler domErrorHandler, final DOMErrorImpl domErrorImpl, final DOMLocatorImpl domLocatorImpl, final String s, final boolean b)
'''
pass
def isXMLCharWF():
'''public static final void isXMLCharWF(final DOMErrorHandler domErrorHandler, final DOMErrorImpl domErrorImpl, final DOMLocatorImpl domLocatorImpl, final String s, final boolean b)
'''
pass
def isCommentWF():
'''public static final void isCommentWF(final DOMErrorHandler domErrorHandler, final DOMErrorImpl domErrorImpl, final DOMLocatorImpl domLocatorImpl, final String s, final boolean b)
'''
pass
def isAttrValueWF():
'''public static final void isAttrValueWF(final DOMErrorHandler domErrorHandler, final DOMErrorImpl domErrorImpl, final DOMLocatorImpl domLocatorImpl, final NamedNodeMap namedNodeMap, final Attr attr, final String s, final boolean b)
'''
pass
def reportDOMError():
'''public static final void reportDOMError(final DOMErrorHandler domErrorHandler, final DOMErrorImpl domErrorImpl, final DOMLocatorImpl fLocator, final String fMessage, final short fSeverity, final String fType)
'''
pass
def startDocument():
'''public void startDocument(final XMLLocator xmlLocator, final String s, final NamespaceContext namespaceContext, final Augmentations augmentations)
'''
pass
def xmlDecl():
'''public void xmlDecl(final String s, final String s2, final String s3, final Augmentations augmentations)
'''
pass
def doctypeDecl():
'''public void doctypeDecl(final String s, final String s2, final String s3, final Augmentations augmentations)
'''
pass
def comment():
'''public void comment(final XMLString xmlString, final Augmentations augmentations)
'''
pass
def processingInstruction():
'''public void processingInstruction(final String s, final XMLString xmlString, final Augmentations augmentations)
'''
pass
def startElement():
'''public void startElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)
'''
pass
def emptyElement():
'''public void emptyElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)
'''
pass
def startGeneralEntity():
'''public void startGeneralEntity(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)
'''
pass
def textDecl():
'''public void textDecl(final String s, final String s2, final Augmentations augmentations)
'''
pass
def endGeneralEntity():
'''public void endGeneralEntity(final String s, final Augmentations augmentations)
'''
pass
def characters():
'''public void characters(final XMLString xmlString, final Augmentations augmentations)
'''
pass
def ignorableWhitespace():
'''public void ignorableWhitespace(final XMLString xmlString, final Augmentations augmentations)
'''
pass
def endElement():
'''public void endElement(final QName qName, final Augmentations augmentations)
'''
pass
def startCDATA():
'''public void startCDATA(final Augmentations augmentations)
'''
pass
def endCDATA():
'''public void endCDATA(final Augmentations augmentations)
'''
pass
def endDocument():
'''public void endDocument(final Augmentations augmentations)
'''
pass
def setDocumentSource():
'''public void setDocumentSource(final XMLDocumentSource xmlDocumentSource)
'''
pass
def getDocumentSource():
'''public XMLDocumentSource getDocumentSource()
'''
pass
def fillInStackTrace():
'''public Throwable fillInStackTrace()
'''
pass
def setAttributes():
'''public void setAttributes(final AttributeMap fAttributes, final CoreDocumentImpl fDocument, final ElementImpl fElement)
'''
pass
def addAttribute():
'''public int addAttribute(final QName qName, final String obj, final String nodeValue)
'''
pass
def removeAllAttributes():
'''public void removeAllAttributes()
'''
pass
def removeAttributeAt():
'''public void removeAttributeAt(final int n)
'''
pass
def getLength():
'''public int getLength()
'''
pass
def getIndex():
'''public int getIndex(final String s)
public int getIndex(final String s, final String s2)
'''
pass
def setName():
'''public void setName(final int n, final QName qName)
'''
pass
def getName():
'''public void getName(final int n, final QName qName)
'''
pass
def getPrefix():
'''public String getPrefix(final int n)
'''
pass
def getURI():
'''public String getURI(final int n)
'''
pass
def getLocalName():
'''public String getLocalName(final int n)
'''
pass
def getQName():
'''public String getQName(final int n)
'''
pass
def setType():
'''public void setType(final int index, final String obj)
'''
pass
def getType():
'''public String getType(final int index)
public String getType(final String s)
public String getType(final String s, final String s2)
'''
pass
def setValue():
'''public void setValue(final int n, final String value)
'''
pass
def getValue():
'''public String getValue(final int n)
public String getValue(final String s)
public String getValue(final String s, final String s2)
'''
pass
def setNonNormalizedValue():
'''public void setNonNormalizedValue(final int n, final String s)
'''
pass
def getNonNormalizedValue():
'''public String getNonNormalizedValue(final int n)
'''
pass
def setSpecified():
'''public void setSpecified(final int n, final boolean specified)
'''
pass
def isSpecified():
'''public boolean isSpecified(final int n)
'''
pass
def getAugmentations():
'''public Augmentations getAugmentations(final int index)
public Augmentations getAugmentations(final String s, final String s2)
public Augmentations getAugmentations(final String s)
'''
pass
def setAugmentations():
'''public void setAugmentations(final int index, final Augmentations obj)
'''
pass
