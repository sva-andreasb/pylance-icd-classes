def ():
    '''returns SchemaTypeVisitorImpl\n\n
    (final SchemaParticle part)\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init(final SchemaParticle part)\n
    init(final SchemaParticle part)\n
    '''
def expand():
    '''returns VisitorState[]\n\n
    expand(final VisitorState[] orig)\n
    '''
def visit():
    '''returns boolean\n\n
    visit(final QName eltName)\n
    visit(final QName eltName, final boolean testValidity)\n
    '''
def testValid():
    '''returns boolean\n\n
    testValid(final QName eltName)\n
    '''
def get_elementflags():
    '''returns int\n\n
    get_elementflags()\n
    '''
def get_default_text():
    '''returns String\n\n
    get_default_text()\n
    '''
def get_schema_field():
    '''returns SchemaField\n\n
    get_schema_field()\n
    '''
def currentParticle():
    '''returns SchemaParticle\n\n
    currentParticle()\n
    '''
def isAllValid():
    '''returns boolean\n\n
    isAllValid()\n
    '''
def copy():
    '''returns None\n\n
    copy(final VisitorState orig)\n
    '''
