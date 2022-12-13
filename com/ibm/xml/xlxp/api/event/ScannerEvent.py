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
'''public ScannerEvent(final int eventType)
'''
pass
def nsContext():
'''public int nsContext()
'''
pass
def asDocument():
'''public final Document asDocument()
'''
pass
def asXMLDecl():
'''public final XMLDecl asXMLDecl()
'''
pass
def asTextDecl():
'''public final TextDecl asTextDecl()
'''
pass
def asStartElement():
'''public final StartElement asStartElement()
'''
pass
def asEndElement():
'''public final EndElement asEndElement()
'''
pass
def asCharacters():
'''public final Characters asCharacters()
'''
pass
def asCharacter():
'''public final Character asCharacter()
'''
pass
def asProcessingInstruction():
'''public final ProcessingInstruction asProcessingInstruction()
'''
pass
def asComment():
'''public final Comment asComment()
'''
pass
def asCDATASection():
'''public final CDATASection asCDATASection()
'''
pass
def asDoctype():
'''public final Doctype asDoctype()
'''
pass
def asEntity():
'''public final Entity asEntity()
'''
pass
def asError():
'''public final Error asError()
'''
pass
def asExtension():
'''public final Extension asExtension()
'''
pass
def Document():
'''public Document(final int n)
'''
pass
def XMLDecl():
'''public XMLDecl()
'''
pass
def TextDecl():
'''public TextDecl()
'''
pass
def StartElement():
'''public StartElement(final int n)
'''
pass
def EndElement():
'''public EndElement()
'''
pass
def Characters():
'''public Characters(final int n)
'''
pass
def Character():
'''public Character(final int n)
'''
pass
def ProcessingInstruction():
'''public ProcessingInstruction()
'''
pass
def Comment():
'''public Comment()
'''
pass
def CDATASection():
'''public CDATASection(final int n)
'''
pass
def Doctype():
'''public Doctype()
'''
pass
def Entity():
'''public Entity(final int n)
'''
pass
def Error():
'''public Error(final int n)
'''
pass
def Extension():
'''public Extension()
'''
pass
