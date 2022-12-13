def DOMNormalizer():
    '''    public DOMNormalizer()
    '''
def isCDataWF():
    '''    public static final void isCDataWF(final DOMErrorHandler domErrorHandler, final DOMErrorImpl domErrorImpl, final DOMLocatorImpl domLocatorImpl, final String s, final boolean b)
    '''
def isXMLCharWF():
    '''    public static final void isXMLCharWF(final DOMErrorHandler domErrorHandler, final DOMErrorImpl domErrorImpl, final DOMLocatorImpl domLocatorImpl, final String s, final boolean b)
    '''
def isCommentWF():
    '''    public static final void isCommentWF(final DOMErrorHandler domErrorHandler, final DOMErrorImpl domErrorImpl, final DOMLocatorImpl domLocatorImpl, final String s, final boolean b)
    '''
def isAttrValueWF():
    '''    public static final void isAttrValueWF(final DOMErrorHandler domErrorHandler, final DOMErrorImpl domErrorImpl, final DOMLocatorImpl domLocatorImpl, final NamedNodeMap namedNodeMap, final Attr attr, final String s, final boolean b)
    '''
def reportDOMError():
    '''    public static final void reportDOMError(final DOMErrorHandler domErrorHandler, final DOMErrorImpl domErrorImpl, final DOMLocatorImpl fLocator, final String fMessage, final short fSeverity, final String fType)
    '''
def startDocument():
    '''    public void startDocument(final XMLLocator xmlLocator, final String s, final NamespaceContext namespaceContext, final Augmentations augmentations)
    '''
def xmlDecl():
    '''    public void xmlDecl(final String s, final String s2, final String s3, final Augmentations augmentations)
    '''
def doctypeDecl():
    '''    public void doctypeDecl(final String s, final String s2, final String s3, final Augmentations augmentations)
    '''
def comment():
    '''    public void comment(final XMLString xmlString, final Augmentations augmentations)
    '''
def processingInstruction():
    '''    public void processingInstruction(final String s, final XMLString xmlString, final Augmentations augmentations)
    '''
def startElement():
    '''    public void startElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)
    '''
def emptyElement():
    '''    public void emptyElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)
    '''
def startGeneralEntity():
    '''    public void startGeneralEntity(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)
    '''
def textDecl():
    '''    public void textDecl(final String s, final String s2, final Augmentations augmentations)
    '''
def endGeneralEntity():
    '''    public void endGeneralEntity(final String s, final Augmentations augmentations)
    '''
def characters():
    '''    public void characters(final XMLString xmlString, final Augmentations augmentations)
    '''
def ignorableWhitespace():
    '''    public void ignorableWhitespace(final XMLString xmlString, final Augmentations augmentations)
    '''
def endElement():
    '''    public void endElement(final QName qName, final Augmentations augmentations)
    '''
def startCDATA():
    '''    public void startCDATA(final Augmentations augmentations)
    '''
def endCDATA():
    '''    public void endCDATA(final Augmentations augmentations)
    '''
def endDocument():
    '''    public void endDocument(final Augmentations augmentations)
    '''
def setDocumentSource():
    '''    public void setDocumentSource(final XMLDocumentSource xmlDocumentSource)
    '''
def getDocumentSource():
    '''    public XMLDocumentSource getDocumentSource()
    '''
def fillInStackTrace():
    '''    public Throwable fillInStackTrace()
    '''
def setAttributes():
    '''    public void setAttributes(final AttributeMap fAttributes, final CoreDocumentImpl fDocument, final ElementImpl fElement)
    '''
def addAttribute():
    '''    public int addAttribute(final QName qName, final String obj, final String nodeValue)
    '''
def removeAllAttributes():
    '''    public void removeAllAttributes()
    '''
def removeAttributeAt():
    '''    public void removeAttributeAt(final int n)
    '''
def getLength():
    '''    public int getLength()
    '''
def getIndex():
    '''    public int getIndex(final String s)
    public int getIndex(final String s, final String s2)
    '''
def setName():
    '''    public void setName(final int n, final QName qName)
    '''
def getName():
    '''    public void getName(final int n, final QName qName)
    '''
def getPrefix():
    '''    public String getPrefix(final int n)
    '''
def getURI():
    '''    public String getURI(final int n)
    '''
def getLocalName():
    '''    public String getLocalName(final int n)
    '''
def getQName():
    '''    public String getQName(final int n)
    '''
def setType():
    '''    public void setType(final int index, final String obj)
    '''
def getType():
    '''    public String getType(final int index)
    public String getType(final String s)
    public String getType(final String s, final String s2)
    '''
def setValue():
    '''    public void setValue(final int n, final String value)
    '''
def getValue():
    '''    public String getValue(final int n)
    public String getValue(final String s)
    public String getValue(final String s, final String s2)
    '''
def setNonNormalizedValue():
    '''    public void setNonNormalizedValue(final int n, final String s)
    '''
def getNonNormalizedValue():
    '''    public String getNonNormalizedValue(final int n)
    '''
def setSpecified():
    '''    public void setSpecified(final int n, final boolean specified)
    '''
def isSpecified():
    '''    public boolean isSpecified(final int n)
    '''
def getAugmentations():
    '''    public Augmentations getAugmentations(final int index)
    public Augmentations getAugmentations(final String s, final String s2)
    public Augmentations getAugmentations(final String s)
    '''
def setAugmentations():
    '''    public void setAugmentations(final int index, final Augmentations obj)
    '''
