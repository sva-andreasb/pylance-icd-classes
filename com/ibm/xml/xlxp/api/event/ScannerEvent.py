EVENT_START_DOCUMENT = "int  0"
EVENT_END_DOCUMENT = "int  1"
EVENT_XML_DECL = "int  2"
EVENT_TEXT_DECL = "int  3"
EVENT_EMPTY_ELEMENT = "int  4"
EVENT_START_ELEMENT = "int  5"
EVENT_LEAF_ELEMENT = "int  6"
EVENT_END_ELEMENT = "int  7"
EVENT_CHARACTERS = "int  8"
EVENT_WHITESPACE = "int  9"
EVENT_CHARACTER = "int  10"
EVENT_PREDEFINED_ENTITY = "int  11"
EVENT_PROCESSING_INSTRUCTION = "int  12"
EVENT_COMMENT = "int  13"
EVENT_START_CDATA_SECTION = "int  14"
EVENT_END_CDATA_SECTION = "int  15"
EVENT_DOCTYPE = "int  16"
EVENT_START_ENTITY = "int  17"
EVENT_END_ENTITY = "int  18"
EVENT_ENTITY_REFERENCE = "int  19"
EVENT_WARNING = "int  20"
EVENT_RECOVERABLE_ERROR = "int  21"
EVENT_FATAL_ERROR = "int  22"
EVENT_EXTENSION = "int  23"
def ScannerEvent():
    '''    public ScannerEvent(final int eventType)
    '''
def nsContext():
    '''    public int nsContext()
    '''
def asDocument():
    '''    public final Document asDocument()
    '''
def asXMLDecl():
    '''    public final XMLDecl asXMLDecl()
    '''
def asTextDecl():
    '''    public final TextDecl asTextDecl()
    '''
def asStartElement():
    '''    public final StartElement asStartElement()
    '''
def asEndElement():
    '''    public final EndElement asEndElement()
    '''
def asCharacters():
    '''    public final Characters asCharacters()
    '''
def asCharacter():
    '''    public final Character asCharacter()
    '''
def asProcessingInstruction():
    '''    public final ProcessingInstruction asProcessingInstruction()
    '''
def asComment():
    '''    public final Comment asComment()
    '''
def asCDATASection():
    '''    public final CDATASection asCDATASection()
    '''
def asDoctype():
    '''    public final Doctype asDoctype()
    '''
def asEntity():
    '''    public final Entity asEntity()
    '''
def asError():
    '''    public final Error asError()
    '''
def asExtension():
    '''    public final Extension asExtension()
    '''
def Document():
    '''    public Document(final int n)
    '''
def XMLDecl():
    '''    public XMLDecl()
    '''
def TextDecl():
    '''    public TextDecl()
    '''
def StartElement():
    '''    public StartElement(final int n)
    '''
def EndElement():
    '''    public EndElement()
    '''
def Characters():
    '''    public Characters(final int n)
    '''
def Character():
    '''    public Character(final int n)
    '''
def ProcessingInstruction():
    '''    public ProcessingInstruction()
    '''
def Comment():
    '''    public Comment()
    '''
def CDATASection():
    '''    public CDATASection(final int n)
    '''
def Doctype():
    '''    public Doctype()
    '''
def Entity():
    '''    public Entity(final int n)
    '''
def Error():
    '''    public Error(final int n)
    '''
def Extension():
    '''    public Extension()
    '''
