SYMBOL_TABLE = "String  \"http://apache.org/xml/properties/internal/symbol-table\""
ERROR_REPORTER = "String  \"http://apache.org/xml/properties/internal/error-reporter\""
ENTITY_RESOLVER = "String  \"http://apache.org/xml/properties/internal/entity-resolver\""
XMLGRAMMAR_POOL = "String  \"http://apache.org/xml/properties/internal/grammar-pool\""
def getRecognizedFeatures():
    '''returns String[]\n\n
    getRecognizedFeatures()\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final String s, final boolean b)\n
    '''
def getRecognizedProperties():
    '''returns String[]\n\n
    getRecognizedProperties()\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String s, final Object o)\n
    '''
def getFeatureDefault():
    '''returns Boolean\n\n
    getFeatureDefault(final String anObject)\n
    '''
def getPropertyDefault():
    '''returns Object\n\n
    getPropertyDefault(final String anObject)\n
    '''
def setDocumentHandler():
    '''returns None\n\n
    setDocumentHandler(final XMLDocumentHandler fDocumentHandler)\n
    '''
def getDocumentHandler():
    '''returns XMLDocumentHandler\n\n
    getDocumentHandler()\n
    '''
def setDocumentSource():
    '''returns None\n\n
    setDocumentSource(final XMLDocumentSource fDocumentSource)\n
    '''
def getDocumentSource():
    '''returns XMLDocumentSource\n\n
    getDocumentSource()\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument(final XMLLocator fLocator, final String s, final NamespaceContext namespaceSupport, final Augmentations augmentations)\n
    startDocument()\n
    '''
def xmlDecl():
    '''returns None\n\n
    xmlDecl(final String s, final String s2, final String s3, final Augmentations augmentations)\n
    '''
def doctypeDecl():
    '''returns None\n\n
    doctypeDecl(final String s, final String s2, final String s3, final Augmentations augmentations)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)\n
    startElement()\n
    '''
def emptyElement():
    '''returns None\n\n
    emptyElement(final QName qName, final XMLAttributes xmlAttributes, final Augmentations augmentations)\n
    '''
def characters():
    '''returns None\n\n
    characters(XMLString handleCharacters, final Augmentations augmentations)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final QName qName, final Augmentations augmentations)\n
    endElement()\n
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
    endDocument()\n
    endDocument()\n
    endDocument()\n
    '''
def characterData():
    '''returns boolean\n\n
    characterData(final String str, final Augmentations augmentations)\n
    '''
def elementDefault():
    '''returns None\n\n
    elementDefault(final String s)\n
    '''
def startGeneralEntity():
    '''returns None\n\n
    startGeneralEntity(final String s, final XMLResourceIdentifier xmlResourceIdentifier, final String s2, final Augmentations augmentations)\n
    '''
def textDecl():
    '''returns None\n\n
    textDecl(final String s, final String s2, final Augmentations augmentations)\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString xmlString, final Augmentations augmentations)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String s, final XMLString xmlString, final Augmentations augmentations)\n
    '''
def endGeneralEntity():
    '''returns None\n\n
    endGeneralEntity(final String s, final Augmentations augmentations)\n
    '''
def ():
    '''returns XPathMatcherStack\n\n
    ()\n
    ()\n
    (final int n)\n
    ()\n
    (final IdentityConstraint fId, final int fDepth)\n
    ()\n
    (final UniqueOrKey uniqueOrKey)\n
    (final UniqueOrKey uniqueOrKey)\n
    (final KeyRef keyRef, final KeyValueStore fKeyValueStore)\n
    ()\n
    '''
def reset():
    '''returns None\n\n
    reset(final XMLComponentManager xmlComponentManager)\n
    reset(final XMLErrorReporter fErrorReporter)\n
    '''
def startValueScopeFor():
    '''returns None\n\n
    startValueScopeFor(final IdentityConstraint identityConstraint, final int n)\n
    '''
def activateField():
    '''returns XPathMatcher\n\n
    activateField(final Field field, final int n)\n
    '''
def endValueScopeFor():
    '''returns None\n\n
    endValueScopeFor(final IdentityConstraint identityConstraint, final int n)\n
    '''
def getGlobalElementDecl():
    '''returns XSElementDecl\n\n
    getGlobalElementDecl(final QName qName)\n
    '''
def length():
    '''returns int\n\n
    length()\n
    '''
def add():
    '''returns None\n\n
    add(final short n)\n
    '''
def valueAt():
    '''returns short\n\n
    valueAt(final int n)\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    clear()\n
    clear()\n
    '''
def contains():
    '''returns int\n\n
    contains(final short n)\n
    contains()\n
    contains(final ValueStoreBase valueStoreBase)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def initValueStoresFor():
    '''returns None\n\n
    initValueStoresFor(final XSElementDecl xsElementDecl, final FieldActivator fieldActivator)\n
    '''
def getValueStoreFor():
    '''returns ValueStoreBase\n\n
    getValueStoreFor(final IdentityConstraint fId, final int fDepth)\n
    '''
def getGlobalValueStoreFor():
    '''returns ValueStoreBase\n\n
    getGlobalValueStoreFor(final IdentityConstraint key)\n
    '''
def transplant():
    '''returns None\n\n
    transplant(final IdentityConstraint identityConstraint, final int fDepth)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def append():
    '''returns None\n\n
    append(final ValueStoreBase valueStoreBase)\n
    '''
def startValueScope():
    '''returns None\n\n
    startValueScope()\n
    '''
def endValueScope():
    '''returns None\n\n
    endValueScope()\n
    '''
def endDocumentFragment():
    '''returns None\n\n
    endDocumentFragment()\n
    endDocumentFragment()\n
    '''
def reportError():
    '''returns None\n\n
    reportError(final String s, final Object[] array)\n
    reportError(final String s, final String obj, final Object[] array, final short n)\n
    reportError(final XMLLocator xmlLocator, final String s, final String obj, final Object[] array, final short n)\n
    '''
def addValue():
    '''returns None\n\n
    addValue(final Field field, final boolean b, final Object o, final short n, final ShortList list)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def getMatcherCount():
    '''returns int\n\n
    getMatcherCount()\n
    '''
def addMatcher():
    '''returns None\n\n
    addMatcher(final XPathMatcher xPathMatcher)\n
    '''
def getMatcherAt():
    '''returns XPathMatcher\n\n
    getMatcherAt(final int n)\n
    '''
def pushContext():
    '''returns None\n\n
    pushContext()\n
    pushContext()\n
    '''
def popContext():
    '''returns String[]\n\n
    popContext()\n
    popContext()\n
    '''
def mergeContext():
    '''returns String[]\n\n
    mergeContext()\n
    '''
