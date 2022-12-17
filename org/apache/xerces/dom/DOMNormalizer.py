def ():
    '''returns DOMNormalizer\n\n
    ()\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument(final XMLLocator xmlLocator, final String s, final NamespaceContext namespaceContext, final Augmentations augmentations)\n
    '''
def xmlDecl():
    '''returns None\n\n
    xmlDecl(final String s, final String s2, final String s3, final Augmentations augmentations)\n
    '''
def doctypeDecl():
    '''returns None\n\n
    doctypeDecl(final String s, final String s2, final String s3, final Augmentations augmentations)\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String s, final XMLString xmlString, final Augmentations augmentations)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)\n
    '''
def emptyElement():
    '''returns None\n\n
    emptyElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)\n
    '''
def startGeneralEntity():
    '''returns None\n\n
    startGeneralEntity(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)\n
    '''
def textDecl():
    '''returns None\n\n
    textDecl(final String s, final String s2, final Augmentations augmentations)\n
    '''
def endGeneralEntity():
    '''returns None\n\n
    endGeneralEntity(final String s, final Augmentations augmentations)\n
    '''
def characters():
    '''returns None\n\n
    characters(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final QName qName, final Augmentations augmentations)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA(final Augmentations augmentations)\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA(final Augmentations augmentations)\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument(final Augmentations augmentations)\n
    '''
def setDocumentSource():
    '''returns None\n\n
    setDocumentSource(final XMLDocumentSource xmlDocumentSource)\n
    '''
def getDocumentSource():
    '''returns XMLDocumentSource\n\n
    getDocumentSource()\n
    '''
def fillInStackTrace():
    '''returns Throwable\n\n
    fillInStackTrace()\n
    '''
def setAttributes():
    '''returns None\n\n
    setAttributes(final AttributeMap fAttributes, final CoreDocumentImpl fDocument, final ElementImpl fElement)\n
    '''
def addAttribute():
    '''returns int\n\n
    addAttribute(final QName qName, final String obj, final String nodeValue)\n
    '''
def removeAllAttributes():
    '''returns None\n\n
    removeAllAttributes()\n
    '''
def removeAttributeAt():
    '''returns None\n\n
    removeAttributeAt(final int n)\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def getIndex():
    '''returns int\n\n
    getIndex(final String s)\n
    getIndex(final String s, final String s2)\n
    '''
def setName():
    '''returns None\n\n
    setName(final int n, final QName qName)\n
    '''
def getName():
    '''returns None\n\n
    getName(final int n, final QName qName)\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix(final int n)\n
    '''
def getURI():
    '''returns String\n\n
    getURI(final int n)\n
    '''
def getLocalName():
    '''returns String\n\n
    getLocalName(final int n)\n
    '''
def getQName():
    '''returns String\n\n
    getQName(final int n)\n
    '''
def setType():
    '''returns None\n\n
    setType(final int index, final String obj)\n
    '''
def getType():
    '''returns String\n\n
    getType(final int index)\n
    getType(final String s)\n
    getType(final String s, final String s2)\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final int n, final String value)\n
    '''
def getValue():
    '''returns String\n\n
    getValue(final int n)\n
    getValue(final String s)\n
    getValue(final String s, final String s2)\n
    '''
def setNonNormalizedValue():
    '''returns None\n\n
    setNonNormalizedValue(final int n, final String s)\n
    '''
def getNonNormalizedValue():
    '''returns String\n\n
    getNonNormalizedValue(final int n)\n
    '''
def setSpecified():
    '''returns None\n\n
    setSpecified(final int n, final boolean specified)\n
    '''
def isSpecified():
    '''returns boolean\n\n
    isSpecified(final int n)\n
    '''
def getAugmentations():
    '''returns Augmentations\n\n
    getAugmentations(final int index)\n
    getAugmentations(final String s, final String s2)\n
    getAugmentations(final String s)\n
    '''
def setAugmentations():
    '''returns None\n\n
    setAugmentations(final int index, final Augmentations obj)\n
    '''
