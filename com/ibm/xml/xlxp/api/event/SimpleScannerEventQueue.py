def SimpleScannerEventQueue():
'''public SimpleScannerEventQueue()
public SimpleScannerEventQueue(final DocumentEntityScanner documentEntityScanner, final DataBufferFactory dataBufferFactory)
public SimpleScannerEventQueue(final DocumentEntityScanner fDocumentEntityScanner, final DataBufferFactory fBufferFactory, final SymbolTable fSymbolTable)
'''
pass
def reset():
'''public void reset(final boolean b)
'''
pass
def setEventConsumer():
'''public void setEventConsumer(final ScannerEventConsumer fEventConsumer)
'''
pass
def setNamespaceAwareness():
'''public void setNamespaceAwareness(final boolean fIsNamespaceAware)
'''
pass
def symbolTable():
'''public SymbolTable symbolTable()
'''
pass
def namespaceContext():
'''public NamespaceContext namespaceContext()
'''
pass
def parseDocumentEntity():
'''public void parseDocumentEntity(final ParsedEntity documentEntity)
'''
pass
def initialize():
'''public void initialize()
'''
pass
def runConsumers():
'''public boolean runConsumers()
'''
pass
def run():
'''public void run()
'''
pass
def nextEvent():
'''public final ScannerEvent nextEvent(final int n)
'''
pass
def reportWarning():
'''public boolean reportWarning(final String s, final int n)
'''
pass
def reportRecoverableError():
'''public boolean reportRecoverableError(final String s, final int n)
'''
pass
def reportFatalError():
'''public boolean reportFatalError(final String s, final int n)
'''
pass
def setParameter():
'''public void setParameter(final int n, final String s)
public void setParameter(final int n, final int n2)
public void setParameter(final int n, final QName qName)
public void setParameter(final int n, final XMLString values)
'''
pass
def setInvalidCharParameter():
'''public void setInvalidCharParameter(final int n, final int i)
'''
pass
def produceStartDocumentEvent():
'''public final boolean produceStartDocumentEvent()
'''
pass
def produceEndDocumentEvent():
'''public final boolean produceEndDocumentEvent()
'''
pass
def versionToProduce():
'''public final XMLString versionToProduce()
'''
pass
def encNameToProduce():
'''public final XMLString encNameToProduce()
'''
pass
def standaloneToProduce():
'''public final XMLString standaloneToProduce()
'''
pass
def produceXMLDeclEvent():
'''public final boolean produceXMLDeclEvent()
'''
pass
def produceTextDeclEvent():
'''public final boolean produceTextDeclEvent()
'''
pass
def produceEmptyElementEvent():
'''public final boolean produceEmptyElementEvent()
'''
pass
def produceStartElementEvent():
'''public final boolean produceStartElementEvent()
'''
pass
def produceEndElementEvent():
'''public final boolean produceEndElementEvent(final QName values)
'''
pass
def contentToProduce():
'''public final XMLString contentToProduce()
'''
pass
def produceCharactersEvent():
'''public final boolean produceCharactersEvent()
'''
pass
def produceWhitespaceEvent():
'''public final boolean produceWhitespaceEvent()
'''
pass
def entityNameToProduce():
'''public final XMLString entityNameToProduce()
'''
pass
def produceCharacterEvent():
'''public final boolean produceCharacterEvent(final int n)
'''
pass
def producePredefinedEntityEvent():
'''public final boolean producePredefinedEntityEvent(final int n)
'''
pass
def targetToProduce():
'''public final XMLString targetToProduce()
'''
pass
def produceProcessingInstructionEvent():
'''public final boolean produceProcessingInstructionEvent()
'''
pass
def produceCommentEvent():
'''public final boolean produceCommentEvent()
'''
pass
def produceStartCDATASectionEvent():
'''public final boolean produceStartCDATASectionEvent()
'''
pass
def produceEndCDATASectionEvent():
'''public final boolean produceEndCDATASectionEvent()
'''
pass
def produceWarningEvent():
'''public final boolean produceWarningEvent(final String s, final int n)
'''
pass
def produceRecoverableErrorEvent():
'''public final boolean produceRecoverableErrorEvent(final String s, final int n)
'''
pass
def produceFatalErrorEvent():
'''public final boolean produceFatalErrorEvent(final String s, final int n)
'''
pass
def produceExtensionEvent():
'''public boolean produceExtensionEvent(final Object o)
'''
pass
def scanQName():
'''public int scanQName(final ParsedEntity parsedEntity, final QName qName)
'''
pass
def scanNCName():
'''public int scanNCName(final ParsedEntity parsedEntity, final XMLString xmlString)
'''
pass
def scanAttrValueBuffered():
'''public boolean scanAttrValueBuffered(final ParsedEntity parsedEntity, final XMLString xmlString, final int n)
'''
pass
def scanAttrValueUnbuffered():
'''public boolean scanAttrValueUnbuffered(final ParsedEntity parsedEntity, final XMLString xmlString, final int n)
'''
pass
def scanNamespaceURIBuffered():
'''public boolean scanNamespaceURIBuffered(final ParsedEntity parsedEntity, final XMLString xmlString, final int n)
'''
pass
def scanNamespaceURIUnbuffered():
'''public boolean scanNamespaceURIUnbuffered(final ParsedEntity parsedEntity, final XMLString xmlString, final int n)
'''
pass
def setupStartElement():
'''public QName setupStartElement()
'''
pass
def currentElementType():
'''public QName currentElementType()
'''
pass
def currentAttributeName():
'''public QName currentAttributeName()
'''
pass
def setupSpecifiedAttribute():
'''public XMLString setupSpecifiedAttribute()
'''
pass
def addSpecifiedAttribute():
'''public boolean addSpecifiedAttribute()
'''
pass
def setAttributeType():
'''public void setAttributeType(final int n, final int n2)
'''
pass
def attributeValueCharacters():
'''public final void attributeValueCharacters(final XMLString xmlString, final boolean b)
'''
pass
def attributeValueCharacter():
'''public void attributeValueCharacter(final int n, final boolean b)
'''
pass
def saveSpecifiedAttValue():
'''public boolean saveSpecifiedAttValue()
'''
pass
def saveSpecifiedNamespaceURI():
'''public boolean saveSpecifiedNamespaceURI()
'''
pass
def finishElement():
'''public boolean finishElement()
'''
pass
def finishEmptyElement():
'''public boolean finishEmptyElement()
'''
pass
def finishStartElement():
'''public boolean finishStartElement()
'''
pass
def setNamespaceURI():
'''public boolean setNamespaceURI(final QName qName)
'''
pass
def elementDepth():
'''public int elementDepth()
'''
pass
def popElement():
'''public QName popElement()
'''
pass
def topElement():
'''public QName topElement()
'''
pass
def continueAfterEndOfEntity():
'''public boolean continueAfterEndOfEntity()
'''
pass
def scanStartElementBuffered():
'''public boolean scanStartElementBuffered(final ParsedEntity parsedEntity)
'''
pass
def scanStartElementUnbuffered():
'''public boolean scanStartElementUnbuffered(final ParsedEntity parsedEntity)
'''
pass
def scanEndElementBuffered():
'''public boolean scanEndElementBuffered(final ParsedEntity parsedEntity)
'''
pass
def scanEndElementUnbuffered():
'''public boolean scanEndElementUnbuffered(final ParsedEntity parsedEntity)
'''
pass
def setInElementContent():
'''public void setInElementContent(final boolean fInElementContent)
'''
pass
def scanContentBuffered():
'''public boolean scanContentBuffered(final ParsedEntity parsedEntity)
'''
pass
def scanContentUnbuffered():
'''public boolean scanContentUnbuffered(final ParsedEntity parsedEntity)
'''
pass
def DocumentEvent():
'''public DocumentEvent(final int n)
'''
pass
def DocumentProducer():
'''public DocumentProducer(final int n)
'''
pass
def XMLDeclEvent():
'''public XMLDeclEvent()
'''
pass
def version():
'''public XMLString version()
public XMLString version()
public XMLString version()
public XMLString version()
'''
pass
def encName():
'''public XMLString encName()
public XMLString encName()
public XMLString encName()
public XMLString encName()
'''
pass
def standalone():
'''public XMLString standalone()
public XMLString standalone()
'''
pass
def XMLDeclProducer():
'''public XMLDeclProducer()
'''
pass
def TextDeclEvent():
'''public TextDeclEvent()
'''
pass
def TextDeclProducer():
'''public TextDeclProducer()
'''
pass
def StartElementEvent():
'''public StartElementEvent(final int n)
'''
pass
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
pass
def elementType():
'''public QName elementType()
public QName elementType()
public QName elementType()
public QName elementType()
'''
pass
def nsDecls():
'''public NSDeclList nsDecls()
public NSDeclList nsDecls()
public NSDeclList nsDecls()
public NSDeclList nsDecls()
'''
pass
def attributes():
'''public AttrList attributes()
public AttrList attributes()
'''
pass
def elementValue():
'''public XMLString elementValue()
public XMLString elementValue()
'''
pass
def nsDeclCount():
'''public int nsDeclCount()
public int nsDeclCount()
public int nsDeclCount()
public int nsDeclCount()
'''
pass
def nsDeclPrefix():
'''public int nsDeclPrefix(final int n)
public int nsDeclPrefix(final int n)
public int nsDeclPrefix(final int n)
public int nsDeclPrefix(final int n)
'''
pass
def nsDeclURI():
'''public int nsDeclURI(final int n)
public int nsDeclURI(final int n)
public int nsDeclURI(final int n)
public int nsDeclURI(final int n)
'''
pass
def nsDeclQName():
'''public int nsDeclQName(final int n)
public int nsDeclQName(final int n)
public int nsDeclQName(final int n)
public int nsDeclQName(final int n)
'''
pass
def prefixMapping():
'''public int prefixMapping(final int n)
public int prefixMapping(final int n)
public int prefixMapping(final int n)
public int prefixMapping(final int n)
'''
pass
def attributeCount():
'''public int attributeCount()
public int attributeCount()
'''
pass
def attributeName():
'''public QName attributeName(final int n)
public QName attributeName(final int n)
'''
pass
def attributeType():
'''public int attributeType(final int n)
public int attributeType(final int n)
'''
pass
def unnormalizedAttributeValue():
'''public XMLString unnormalizedAttributeValue(final int n)
public XMLString unnormalizedAttributeValue(final int n)
'''
pass
def attributeValue():
'''public XMLString attributeValue(final int n)
public XMLString attributeValue(final int n)
'''
pass
def attributeValueNormalized():
'''public boolean attributeValueNormalized(final int n)
public boolean attributeValueNormalized(final int n)
'''
pass
def attributeSpecified():
'''public boolean attributeSpecified(final int n)
public boolean attributeSpecified(final int n)
'''
pass
def normalizeAttributeValue():
'''public void normalizeAttributeValue(final int n)
public void normalizeAttributeValue(final int n)
'''
pass
def setAttributeValueNormalized():
'''public void setAttributeValueNormalized(final int n, final boolean b)
public void setAttributeValueNormalized(final int n, final boolean b)
'''
pass
def StartElementProducer():
'''public StartElementProducer(final int n)
'''
pass
def EndElementEvent():
'''public EndElementEvent()
'''
pass
def EndElementProducer():
'''public EndElementProducer()
'''
pass
def CharactersEvent():
'''public CharactersEvent(final int n)
'''
pass
def content():
'''public XMLString content()
public XMLString content()
public XMLString content()
public XMLString content()
public XMLString content()
public XMLString content()
'''
pass
def CharactersProducer():
'''public CharactersProducer(final int n)
'''
pass
def CharacterEvent():
'''public CharacterEvent(final int n)
'''
pass
def singleCh():
'''public int singleCh()
public int singleCh()
'''
pass
def CharacterProducer():
'''public CharacterProducer(final int n)
'''
pass
def ProcessingInstructionEvent():
'''public ProcessingInstructionEvent()
'''
pass
def target():
'''public XMLString target()
public XMLString target()
'''
pass
def ProcessingInstructionProducer():
'''public ProcessingInstructionProducer()
'''
pass
def CommentEvent():
'''public CommentEvent()
'''
pass
def CommentProducer():
'''public CommentProducer()
'''
pass
def CDATASectionEvent():
'''public CDATASectionEvent(final int n)
'''
pass
def CDATASectionProducer():
'''public CDATASectionProducer(final int n)
'''
pass
def ErrorEvent():
'''public ErrorEvent(final int n)
'''
pass
def errorURI():
'''public String errorURI()
public String errorURI()
'''
pass
def errorCode():
'''public int errorCode()
public int errorCode()
'''
pass
def errorParamsCount():
'''public int errorParamsCount()
public int errorParamsCount()
'''
pass
def errorParam():
'''public XMLString errorParam(final int n)
public XMLString errorParam(final int n)
'''
pass
def errorOffset():
'''public long errorOffset()
public long errorOffset()
'''
pass
def ErrorProducer():
'''public ErrorProducer(final int n)
'''
pass
def ExtensionEvent():
'''public ExtensionEvent()
'''
pass
def extensionState():
'''public Object extensionState()
'''
pass
