def ():
    '''returns ExtensionEvent\n\n
    ()\n
    (final DocumentEntityScanner documentEntityScanner, final DataBufferFactory dataBufferFactory)\n
    (final DocumentEntityScanner fDocumentEntityScanner, final DataBufferFactory fBufferFactory, final SymbolTable fSymbolTable)\n
    (final int n)\n
    (final int n)\n
    ()\n
    ()\n
    ()\n
    ()\n
    (final int n)\n
    (final int n)\n
    ()\n
    ()\n
    (final int n)\n
    (final int n)\n
    (final int n)\n
    (final int n)\n
    ()\n
    ()\n
    ()\n
    ()\n
    (final int n)\n
    (final int n)\n
    (final int n)\n
    (final int n)\n
    ()\n
    '''
def reset():
    '''returns None\n\n
    reset(final boolean b)\n
    '''
def setEventConsumer():
    '''returns None\n\n
    setEventConsumer(final ScannerEventConsumer fEventConsumer)\n
    '''
def setNamespaceAwareness():
    '''returns None\n\n
    setNamespaceAwareness(final boolean fIsNamespaceAware)\n
    '''
def symbolTable():
    '''returns SymbolTable\n\n
    symbolTable()\n
    '''
def namespaceContext():
    '''returns NamespaceContext\n\n
    namespaceContext()\n
    '''
def parseDocumentEntity():
    '''returns None\n\n
    parseDocumentEntity(final ParsedEntity documentEntity)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def runConsumers():
    '''returns boolean\n\n
    runConsumers()\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
def reportWarning():
    '''returns boolean\n\n
    reportWarning(final String s, final int n)\n
    '''
def reportRecoverableError():
    '''returns boolean\n\n
    reportRecoverableError(final String s, final int n)\n
    '''
def reportFatalError():
    '''returns boolean\n\n
    reportFatalError(final String s, final int n)\n
    '''
def setParameter():
    '''returns None\n\n
    setParameter(final int n, final String s)\n
    setParameter(final int n, final int n2)\n
    setParameter(final int n, final QName qName)\n
    setParameter(final int n, final XMLString values)\n
    '''
def setInvalidCharParameter():
    '''returns None\n\n
    setInvalidCharParameter(final int n, final int i)\n
    '''
def produceExtensionEvent():
    '''returns boolean\n\n
    produceExtensionEvent(final Object o)\n
    '''
def scanQName():
    '''returns int\n\n
    scanQName(final ParsedEntity parsedEntity, final QName qName)\n
    '''
def scanNCName():
    '''returns int\n\n
    scanNCName(final ParsedEntity parsedEntity, final XMLString xmlString)\n
    '''
def scanAttrValueBuffered():
    '''returns boolean\n\n
    scanAttrValueBuffered(final ParsedEntity parsedEntity, final XMLString xmlString, final int n)\n
    '''
def scanAttrValueUnbuffered():
    '''returns boolean\n\n
    scanAttrValueUnbuffered(final ParsedEntity parsedEntity, final XMLString xmlString, final int n)\n
    '''
def scanNamespaceURIBuffered():
    '''returns boolean\n\n
    scanNamespaceURIBuffered(final ParsedEntity parsedEntity, final XMLString xmlString, final int n)\n
    '''
def scanNamespaceURIUnbuffered():
    '''returns boolean\n\n
    scanNamespaceURIUnbuffered(final ParsedEntity parsedEntity, final XMLString xmlString, final int n)\n
    '''
def setupStartElement():
    '''returns QName\n\n
    setupStartElement()\n
    '''
def currentElementType():
    '''returns QName\n\n
    currentElementType()\n
    '''
def currentAttributeName():
    '''returns QName\n\n
    currentAttributeName()\n
    '''
def setupSpecifiedAttribute():
    '''returns XMLString\n\n
    setupSpecifiedAttribute()\n
    '''
def addSpecifiedAttribute():
    '''returns boolean\n\n
    addSpecifiedAttribute()\n
    '''
def setAttributeType():
    '''returns None\n\n
    setAttributeType(final int n, final int n2)\n
    '''
def attributeValueCharacter():
    '''returns None\n\n
    attributeValueCharacter(final int n, final boolean b)\n
    '''
def saveSpecifiedAttValue():
    '''returns boolean\n\n
    saveSpecifiedAttValue()\n
    '''
def saveSpecifiedNamespaceURI():
    '''returns boolean\n\n
    saveSpecifiedNamespaceURI()\n
    '''
def finishElement():
    '''returns boolean\n\n
    finishElement()\n
    '''
def finishEmptyElement():
    '''returns boolean\n\n
    finishEmptyElement()\n
    '''
def finishStartElement():
    '''returns boolean\n\n
    finishStartElement()\n
    '''
def setNamespaceURI():
    '''returns boolean\n\n
    setNamespaceURI(final QName qName)\n
    '''
def elementDepth():
    '''returns int\n\n
    elementDepth()\n
    '''
def popElement():
    '''returns QName\n\n
    popElement()\n
    '''
def topElement():
    '''returns QName\n\n
    topElement()\n
    '''
def continueAfterEndOfEntity():
    '''returns boolean\n\n
    continueAfterEndOfEntity()\n
    '''
def scanStartElementBuffered():
    '''returns boolean\n\n
    scanStartElementBuffered(final ParsedEntity parsedEntity)\n
    '''
def scanStartElementUnbuffered():
    '''returns boolean\n\n
    scanStartElementUnbuffered(final ParsedEntity parsedEntity)\n
    '''
def scanEndElementBuffered():
    '''returns boolean\n\n
    scanEndElementBuffered(final ParsedEntity parsedEntity)\n
    '''
def scanEndElementUnbuffered():
    '''returns boolean\n\n
    scanEndElementUnbuffered(final ParsedEntity parsedEntity)\n
    '''
def setInElementContent():
    '''returns None\n\n
    setInElementContent(final boolean fInElementContent)\n
    '''
def scanContentBuffered():
    '''returns boolean\n\n
    scanContentBuffered(final ParsedEntity parsedEntity)\n
    '''
def scanContentUnbuffered():
    '''returns boolean\n\n
    scanContentUnbuffered(final ParsedEntity parsedEntity)\n
    '''
def version():
    '''returns XMLString\n\n
    version()\n
    version()\n
    version()\n
    version()\n
    '''
def encName():
    '''returns XMLString\n\n
    encName()\n
    encName()\n
    encName()\n
    encName()\n
    '''
def standalone():
    '''returns XMLString\n\n
    standalone()\n
    standalone()\n
    '''
def nsContext():
    '''returns int\n\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    nsContext()\n
    '''
def elementType():
    '''returns QName\n\n
    elementType()\n
    elementType()\n
    elementType()\n
    elementType()\n
    '''
def nsDecls():
    '''returns NSDeclList\n\n
    nsDecls()\n
    nsDecls()\n
    nsDecls()\n
    nsDecls()\n
    '''
def attributes():
    '''returns AttrList\n\n
    attributes()\n
    attributes()\n
    '''
def elementValue():
    '''returns XMLString\n\n
    elementValue()\n
    elementValue()\n
    '''
def nsDeclCount():
    '''returns int\n\n
    nsDeclCount()\n
    nsDeclCount()\n
    nsDeclCount()\n
    nsDeclCount()\n
    '''
def nsDeclPrefix():
    '''returns int\n\n
    nsDeclPrefix(final int n)\n
    nsDeclPrefix(final int n)\n
    nsDeclPrefix(final int n)\n
    nsDeclPrefix(final int n)\n
    '''
def nsDeclURI():
    '''returns int\n\n
    nsDeclURI(final int n)\n
    nsDeclURI(final int n)\n
    nsDeclURI(final int n)\n
    nsDeclURI(final int n)\n
    '''
def nsDeclQName():
    '''returns int\n\n
    nsDeclQName(final int n)\n
    nsDeclQName(final int n)\n
    nsDeclQName(final int n)\n
    nsDeclQName(final int n)\n
    '''
def prefixMapping():
    '''returns int\n\n
    prefixMapping(final int n)\n
    prefixMapping(final int n)\n
    prefixMapping(final int n)\n
    prefixMapping(final int n)\n
    '''
def attributeCount():
    '''returns int\n\n
    attributeCount()\n
    attributeCount()\n
    '''
def attributeName():
    '''returns QName\n\n
    attributeName(final int n)\n
    attributeName(final int n)\n
    '''
def attributeType():
    '''returns int\n\n
    attributeType(final int n)\n
    attributeType(final int n)\n
    '''
def unnormalizedAttributeValue():
    '''returns XMLString\n\n
    unnormalizedAttributeValue(final int n)\n
    unnormalizedAttributeValue(final int n)\n
    '''
def attributeValue():
    '''returns XMLString\n\n
    attributeValue(final int n)\n
    attributeValue(final int n)\n
    '''
def attributeValueNormalized():
    '''returns boolean\n\n
    attributeValueNormalized(final int n)\n
    attributeValueNormalized(final int n)\n
    '''
def attributeSpecified():
    '''returns boolean\n\n
    attributeSpecified(final int n)\n
    attributeSpecified(final int n)\n
    '''
def normalizeAttributeValue():
    '''returns None\n\n
    normalizeAttributeValue(final int n)\n
    normalizeAttributeValue(final int n)\n
    '''
def setAttributeValueNormalized():
    '''returns None\n\n
    setAttributeValueNormalized(final int n, final boolean b)\n
    setAttributeValueNormalized(final int n, final boolean b)\n
    '''
def content():
    '''returns XMLString\n\n
    content()\n
    content()\n
    content()\n
    content()\n
    content()\n
    content()\n
    '''
def singleCh():
    '''returns int\n\n
    singleCh()\n
    singleCh()\n
    '''
def target():
    '''returns XMLString\n\n
    target()\n
    target()\n
    '''
def errorURI():
    '''returns String\n\n
    errorURI()\n
    errorURI()\n
    '''
def errorCode():
    '''returns int\n\n
    errorCode()\n
    errorCode()\n
    '''
def errorParamsCount():
    '''returns int\n\n
    errorParamsCount()\n
    errorParamsCount()\n
    '''
def errorParam():
    '''returns XMLString\n\n
    errorParam(final int n)\n
    errorParam(final int n)\n
    '''
def errorOffset():
    '''returns long\n\n
    errorOffset()\n
    errorOffset()\n
    '''
def extensionState():
    '''returns Object\n\n
    extensionState()\n
    '''
