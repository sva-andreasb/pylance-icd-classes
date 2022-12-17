def reset():
    '''returns None\n\n
    reset(final boolean b)\n
    '''
def dropBufferReferences():
    '''returns None\n\n
    dropBufferReferences()\n
    '''
def setNamespaceAwareness():
    '''returns None\n\n
    setNamespaceAwareness(final boolean fIsNamespaceAware)\n
    '''
def namespaceContext():
    '''returns NamespaceContext\n\n
    namespaceContext()\n
    '''
def setDocumentEntity():
    '''returns None\n\n
    setDocumentEntity(final ParsedEntity parsedEntity)\n
    '''
def setEntityContent():
    '''returns None\n\n
    setEntityContent(final ParsedEntity parsedEntity)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def parseDocumentEntity():
    '''returns None\n\n
    parseDocumentEntity(final ParsedEntity parsedEntity)\n
    '''
def produceEvents():
    '''returns boolean\n\n
    produceEvents()\n
    '''
def produceStartDocumentEvent():
    '''returns boolean\n\n
    produceStartDocumentEvent()\n
    '''
def produceEndDocumentEvent():
    '''returns boolean\n\n
    produceEndDocumentEvent()\n
    '''
def produceXMLDeclEvent():
    '''returns boolean\n\n
    produceXMLDeclEvent()\n
    '''
def produceTextDeclEvent():
    '''returns boolean\n\n
    produceTextDeclEvent()\n
    '''
def produceEmptyElementEvent():
    '''returns boolean\n\n
    produceEmptyElementEvent()\n
    '''
def produceStartElementEvent():
    '''returns boolean\n\n
    produceStartElementEvent()\n
    '''
def produceEndElementEvent():
    '''returns boolean\n\n
    produceEndElementEvent(final QName values)\n
    '''
def produceCharactersEvent():
    '''returns boolean\n\n
    produceCharactersEvent()\n
    '''
def produceWhitespaceEvent():
    '''returns boolean\n\n
    produceWhitespaceEvent()\n
    '''
def produceCharacterEvent():
    '''returns boolean\n\n
    produceCharacterEvent(final int singleCh)\n
    '''
def producePredefinedEntityEvent():
    '''returns boolean\n\n
    producePredefinedEntityEvent(final int singleCh)\n
    '''
def produceProcessingInstructionEvent():
    '''returns boolean\n\n
    produceProcessingInstructionEvent()\n
    '''
def produceCommentEvent():
    '''returns boolean\n\n
    produceCommentEvent()\n
    '''
def produceStartCDATASectionEvent():
    '''returns boolean\n\n
    produceStartCDATASectionEvent()\n
    '''
def produceEndCDATASectionEvent():
    '''returns boolean\n\n
    produceEndCDATASectionEvent()\n
    '''
def produceStartEntityEvent():
    '''returns boolean\n\n
    produceStartEntityEvent()\n
    '''
def produceEndEntityEvent():
    '''returns boolean\n\n
    produceEndEntityEvent()\n
    '''
def produceWarningEvent():
    '''returns boolean\n\n
    produceWarningEvent(final String s, final int n)\n
    '''
def produceRecoverableErrorEvent():
    '''returns boolean\n\n
    produceRecoverableErrorEvent(final String s, final int n)\n
    '''
def produceFatalErrorEvent():
    '''returns boolean\n\n
    produceFatalErrorEvent(final String s, final int n)\n
    '''
def produceExtensionEvent():
    '''returns boolean\n\n
    produceExtensionEvent(final Object fExtensionState)\n
    '''
def setupStartElement():
    '''returns QName\n\n
    setupStartElement()\n
    '''
def finishEmptyElement():
    '''returns boolean\n\n
    finishEmptyElement()\n
    '''
def finishStartElement():
    '''returns boolean\n\n
    finishStartElement()\n
    '''
def setNSDeclURI():
    '''returns None\n\n
    setNSDeclURI(final int n, final int n2)\n
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
def scanQName():
    '''returns int\n\n
    scanQName(final ParsedEntity parsedEntity, final QName qName)\n
    '''
def scanNCName():
    '''returns int\n\n
    scanNCName(final ParsedEntity parsedEntity, final XMLString xmlString)\n
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
def currentElementType():
    '''returns QName\n\n
    currentElementType()\n
    '''
def currentAttributeName():
    '''returns QName\n\n
    currentAttributeName()\n
    '''
def currentAttributeValue():
    '''returns XMLString\n\n
    currentAttributeValue()\n
    '''
def setupSpecifiedAttribute():
    '''returns XMLString\n\n
    setupSpecifiedAttribute()\n
    '''
def addSpecifiedAttribute():
    '''returns boolean\n\n
    addSpecifiedAttribute()\n
    '''
def attributeValueCharacters():
    '''returns None\n\n
    attributeValueCharacters(final XMLString xmlString, final boolean b)\n
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
def setAttributeType():
    '''returns None\n\n
    setAttributeType(final int n, final int n2)\n
    '''
def addDefaultAttribute():
    '''returns boolean\n\n
    addDefaultAttribute(final QName values, final int currentAttributeType, final XMLString values2)\n
    '''
def addDefaultNSDecl():
    '''returns boolean\n\n
    addDefaultNSDecl(final QName qName, final XMLString xmlString)\n
    '''
def contentToProduce():
    '''returns XMLString\n\n
    contentToProduce()\n
    '''
def versionToProduce():
    '''returns XMLString\n\n
    versionToProduce()\n
    '''
def encNameToProduce():
    '''returns XMLString\n\n
    encNameToProduce()\n
    '''
def standaloneToProduce():
    '''returns XMLString\n\n
    standaloneToProduce()\n
    '''
def targetToProduce():
    '''returns XMLString\n\n
    targetToProduce()\n
    '''
def entityNameToProduce():
    '''returns XMLString\n\n
    entityNameToProduce()\n
    '''
def setParameter():
    '''returns None\n\n
    setParameter(final int n, final XMLString values)\n
    setParameter(final int n, final String s)\n
    setParameter(final int n, final int n2)\n
    setParameter(final int n, final QName qName)\n
    '''
def setInvalidCharParameter():
    '''returns None\n\n
    setInvalidCharParameter(final int n, final int i)\n
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
def nsDeclCount():
    '''returns int\n\n
    nsDeclCount()\n
    '''
def nsDeclPrefix():
    '''returns int\n\n
    nsDeclPrefix(final int n)\n
    '''
def nsDeclURI():
    '''returns int\n\n
    nsDeclURI(final int n)\n
    '''
def nsDeclQName():
    '''returns int\n\n
    nsDeclQName(final int n)\n
    '''
def prefixMapping():
    '''returns int\n\n
    prefixMapping(final int n)\n
    '''
def attributeCount():
    '''returns int\n\n
    attributeCount()\n
    '''
def attributeName():
    '''returns QName\n\n
    attributeName(final int n)\n
    '''
def attributeType():
    '''returns int\n\n
    attributeType(final int n)\n
    '''
def unnormalizedAttributeValue():
    '''returns XMLString\n\n
    unnormalizedAttributeValue(final int n)\n
    '''
def attributeValue():
    '''returns XMLString\n\n
    attributeValue(final int n)\n
    '''
def attributeValueNormalized():
    '''returns boolean\n\n
    attributeValueNormalized(final int n)\n
    '''
def attributeSpecified():
    '''returns boolean\n\n
    attributeSpecified(final int n)\n
    '''
def normalizeAttributeValue():
    '''returns None\n\n
    normalizeAttributeValue(final int n)\n
    '''
def setAttributeValueNormalized():
    '''returns None\n\n
    setAttributeValueNormalized(final int n, final boolean b)\n
    '''
