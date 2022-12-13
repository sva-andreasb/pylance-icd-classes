def SimpleScannerEventQueue():
    '''public SimpleScannerEventQueue()
    public SimpleScannerEventQueue(final DocumentEntityScanner documentEntityScanner, final DataBufferFactory dataBufferFactory)
    public SimpleScannerEventQueue(final DocumentEntityScanner fDocumentEntityScanner, final DataBufferFactory fBufferFactory, final SymbolTable fSymbolTable)
    '''
def reset():
    '''public void reset(final boolean b)
    '''
def setEventConsumer():
    '''public void setEventConsumer(final ScannerEventConsumer fEventConsumer)
    '''
def setNamespaceAwareness():
    '''public void setNamespaceAwareness(final boolean fIsNamespaceAware)
    '''
def symbolTable():
    '''public SymbolTable symbolTable()
    '''
def namespaceContext():
    '''public NamespaceContext namespaceContext()
    '''
def parseDocumentEntity():
    '''public void parseDocumentEntity(final ParsedEntity documentEntity)
    '''
def initialize():
    '''public void initialize()
    '''
def runConsumers():
    '''public boolean runConsumers()
    '''
def run():
    '''public void run()
    '''
def nextEvent():
    '''public final ScannerEvent nextEvent(final int n)
    '''
def reportWarning():
    '''public boolean reportWarning(final String s, final int n)
    '''
def reportRecoverableError():
    '''public boolean reportRecoverableError(final String s, final int n)
    '''
def reportFatalError():
    '''public boolean reportFatalError(final String s, final int n)
    '''
def setParameter():
    '''public void setParameter(final int n, final String s)
    public void setParameter(final int n, final int n2)
    public void setParameter(final int n, final QName qName)
    public void setParameter(final int n, final XMLString values)
    '''
def setInvalidCharParameter():
    '''public void setInvalidCharParameter(final int n, final int i)
    '''
def produceStartDocumentEvent():
    '''public final boolean produceStartDocumentEvent()
    '''
def produceEndDocumentEvent():
    '''public final boolean produceEndDocumentEvent()
    '''
def versionToProduce():
    '''public final XMLString versionToProduce()
    '''
def encNameToProduce():
    '''public final XMLString encNameToProduce()
    '''
def standaloneToProduce():
    '''public final XMLString standaloneToProduce()
    '''
def produceXMLDeclEvent():
    '''public final boolean produceXMLDeclEvent()
    '''
def produceTextDeclEvent():
    '''public final boolean produceTextDeclEvent()
    '''
def produceEmptyElementEvent():
    '''public final boolean produceEmptyElementEvent()
    '''
def produceStartElementEvent():
    '''public final boolean produceStartElementEvent()
    '''
def produceEndElementEvent():
    '''public final boolean produceEndElementEvent(final QName values)
    '''
def contentToProduce():
    '''public final XMLString contentToProduce()
    '''
def produceCharactersEvent():
    '''public final boolean produceCharactersEvent()
    '''
def produceWhitespaceEvent():
    '''public final boolean produceWhitespaceEvent()
    '''
def entityNameToProduce():
    '''public final XMLString entityNameToProduce()
    '''
def produceCharacterEvent():
    '''public final boolean produceCharacterEvent(final int n)
    '''
def producePredefinedEntityEvent():
    '''public final boolean producePredefinedEntityEvent(final int n)
    '''
def targetToProduce():
    '''public final XMLString targetToProduce()
    '''
def produceProcessingInstructionEvent():
    '''public final boolean produceProcessingInstructionEvent()
    '''
def produceCommentEvent():
    '''public final boolean produceCommentEvent()
    '''
def produceStartCDATASectionEvent():
    '''public final boolean produceStartCDATASectionEvent()
    '''
def produceEndCDATASectionEvent():
    '''public final boolean produceEndCDATASectionEvent()
    '''
def produceWarningEvent():
    '''public final boolean produceWarningEvent(final String s, final int n)
    '''
def produceRecoverableErrorEvent():
    '''public final boolean produceRecoverableErrorEvent(final String s, final int n)
    '''
def produceFatalErrorEvent():
    '''public final boolean produceFatalErrorEvent(final String s, final int n)
    '''
def produceExtensionEvent():
    '''public boolean produceExtensionEvent(final Object o)
    '''
def scanQName():
    '''public int scanQName(final ParsedEntity parsedEntity, final QName qName)
    '''
def scanNCName():
    '''public int scanNCName(final ParsedEntity parsedEntity, final XMLString xmlString)
    '''
def scanAttrValueBuffered():
    '''public boolean scanAttrValueBuffered(final ParsedEntity parsedEntity, final XMLString xmlString, final int n)
    '''
def scanAttrValueUnbuffered():
    '''public boolean scanAttrValueUnbuffered(final ParsedEntity parsedEntity, final XMLString xmlString, final int n)
    '''
def scanNamespaceURIBuffered():
    '''public boolean scanNamespaceURIBuffered(final ParsedEntity parsedEntity, final XMLString xmlString, final int n)
    '''
def scanNamespaceURIUnbuffered():
    '''public boolean scanNamespaceURIUnbuffered(final ParsedEntity parsedEntity, final XMLString xmlString, final int n)
    '''
def setupStartElement():
    '''public QName setupStartElement()
    '''
def currentElementType():
    '''public QName currentElementType()
    '''
def currentAttributeName():
    '''public QName currentAttributeName()
    '''
def setupSpecifiedAttribute():
    '''public XMLString setupSpecifiedAttribute()
    '''
def addSpecifiedAttribute():
    '''public boolean addSpecifiedAttribute()
    '''
def setAttributeType():
    '''public void setAttributeType(final int n, final int n2)
    '''
def attributeValueCharacters():
    '''public final void attributeValueCharacters(final XMLString xmlString, final boolean b)
    '''
def attributeValueCharacter():
    '''public void attributeValueCharacter(final int n, final boolean b)
    '''
def saveSpecifiedAttValue():
    '''public boolean saveSpecifiedAttValue()
    '''
def saveSpecifiedNamespaceURI():
    '''public boolean saveSpecifiedNamespaceURI()
    '''
def finishElement():
    '''public boolean finishElement()
    '''
def finishEmptyElement():
    '''public boolean finishEmptyElement()
    '''
def finishStartElement():
    '''public boolean finishStartElement()
    '''
def setNamespaceURI():
    '''public boolean setNamespaceURI(final QName qName)
    '''
def elementDepth():
    '''public int elementDepth()
    '''
def popElement():
    '''public QName popElement()
    '''
def topElement():
    '''public QName topElement()
    '''
def continueAfterEndOfEntity():
    '''public boolean continueAfterEndOfEntity()
    '''
def scanStartElementBuffered():
    '''public boolean scanStartElementBuffered(final ParsedEntity parsedEntity)
    '''
def scanStartElementUnbuffered():
    '''public boolean scanStartElementUnbuffered(final ParsedEntity parsedEntity)
    '''
def scanEndElementBuffered():
    '''public boolean scanEndElementBuffered(final ParsedEntity parsedEntity)
    '''
def scanEndElementUnbuffered():
    '''public boolean scanEndElementUnbuffered(final ParsedEntity parsedEntity)
    '''
def setInElementContent():
    '''public void setInElementContent(final boolean fInElementContent)
    '''
def scanContentBuffered():
    '''public boolean scanContentBuffered(final ParsedEntity parsedEntity)
    '''
def scanContentUnbuffered():
    '''public boolean scanContentUnbuffered(final ParsedEntity parsedEntity)
    '''
def DocumentEvent():
    '''public DocumentEvent(final int n)
    '''
def DocumentProducer():
    '''public DocumentProducer(final int n)
    '''
def XMLDeclEvent():
    '''public XMLDeclEvent()
    '''
def version():
    '''public XMLString version()
    public XMLString version()
    public XMLString version()
    public XMLString version()
    '''
def encName():
    '''public XMLString encName()
    public XMLString encName()
    public XMLString encName()
    public XMLString encName()
    '''
def standalone():
    '''public XMLString standalone()
    public XMLString standalone()
    '''
def XMLDeclProducer():
    '''public XMLDeclProducer()
    '''
def TextDeclEvent():
    '''public TextDeclEvent()
    '''
def TextDeclProducer():
    '''public TextDeclProducer()
    '''
def StartElementEvent():
    '''public StartElementEvent(final int n)
    '''
def nsContext():
    '''public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    public int nsContext()
    '''
def elementType():
    '''public QName elementType()
    public QName elementType()
    public QName elementType()
    public QName elementType()
    '''
def nsDecls():
    '''public NSDeclList nsDecls()
    public NSDeclList nsDecls()
    public NSDeclList nsDecls()
    public NSDeclList nsDecls()
    '''
def attributes():
    '''public AttrList attributes()
    public AttrList attributes()
    '''
def elementValue():
    '''public XMLString elementValue()
    public XMLString elementValue()
    '''
def nsDeclCount():
    '''public int nsDeclCount()
    public int nsDeclCount()
    public int nsDeclCount()
    public int nsDeclCount()
    '''
def nsDeclPrefix():
    '''public int nsDeclPrefix(final int n)
    public int nsDeclPrefix(final int n)
    public int nsDeclPrefix(final int n)
    public int nsDeclPrefix(final int n)
    '''
def nsDeclURI():
    '''public int nsDeclURI(final int n)
    public int nsDeclURI(final int n)
    public int nsDeclURI(final int n)
    public int nsDeclURI(final int n)
    '''
def nsDeclQName():
    '''public int nsDeclQName(final int n)
    public int nsDeclQName(final int n)
    public int nsDeclQName(final int n)
    public int nsDeclQName(final int n)
    '''
def prefixMapping():
    '''public int prefixMapping(final int n)
    public int prefixMapping(final int n)
    public int prefixMapping(final int n)
    public int prefixMapping(final int n)
    '''
def attributeCount():
    '''public int attributeCount()
    public int attributeCount()
    '''
def attributeName():
    '''public QName attributeName(final int n)
    public QName attributeName(final int n)
    '''
def attributeType():
    '''public int attributeType(final int n)
    public int attributeType(final int n)
    '''
def unnormalizedAttributeValue():
    '''public XMLString unnormalizedAttributeValue(final int n)
    public XMLString unnormalizedAttributeValue(final int n)
    '''
def attributeValue():
    '''public XMLString attributeValue(final int n)
    public XMLString attributeValue(final int n)
    '''
def attributeValueNormalized():
    '''public boolean attributeValueNormalized(final int n)
    public boolean attributeValueNormalized(final int n)
    '''
def attributeSpecified():
    '''public boolean attributeSpecified(final int n)
    public boolean attributeSpecified(final int n)
    '''
def normalizeAttributeValue():
    '''public void normalizeAttributeValue(final int n)
    public void normalizeAttributeValue(final int n)
    '''
def setAttributeValueNormalized():
    '''public void setAttributeValueNormalized(final int n, final boolean b)
    public void setAttributeValueNormalized(final int n, final boolean b)
    '''
def StartElementProducer():
    '''public StartElementProducer(final int n)
    '''
def EndElementEvent():
    '''public EndElementEvent()
    '''
def EndElementProducer():
    '''public EndElementProducer()
    '''
def CharactersEvent():
    '''public CharactersEvent(final int n)
    '''
def content():
    '''public XMLString content()
    public XMLString content()
    public XMLString content()
    public XMLString content()
    public XMLString content()
    public XMLString content()
    '''
def CharactersProducer():
    '''public CharactersProducer(final int n)
    '''
def CharacterEvent():
    '''public CharacterEvent(final int n)
    '''
def singleCh():
    '''public int singleCh()
    public int singleCh()
    '''
def CharacterProducer():
    '''public CharacterProducer(final int n)
    '''
def ProcessingInstructionEvent():
    '''public ProcessingInstructionEvent()
    '''
def target():
    '''public XMLString target()
    public XMLString target()
    '''
def ProcessingInstructionProducer():
    '''public ProcessingInstructionProducer()
    '''
def CommentEvent():
    '''public CommentEvent()
    '''
def CommentProducer():
    '''public CommentProducer()
    '''
def CDATASectionEvent():
    '''public CDATASectionEvent(final int n)
    '''
def CDATASectionProducer():
    '''public CDATASectionProducer(final int n)
    '''
def ErrorEvent():
    '''public ErrorEvent(final int n)
    '''
def errorURI():
    '''public String errorURI()
    public String errorURI()
    '''
def errorCode():
    '''public int errorCode()
    public int errorCode()
    '''
def errorParamsCount():
    '''public int errorParamsCount()
    public int errorParamsCount()
    '''
def errorParam():
    '''public XMLString errorParam(final int n)
    public XMLString errorParam(final int n)
    '''
def errorOffset():
    '''public long errorOffset()
    public long errorOffset()
    '''
def ErrorProducer():
    '''public ErrorProducer(final int n)
    '''
def ExtensionEvent():
    '''public ExtensionEvent()
    '''
def extensionState():
    '''public Object extensionState()
    '''
