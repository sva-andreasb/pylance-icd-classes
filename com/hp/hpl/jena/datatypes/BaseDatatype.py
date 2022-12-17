def ():
    '''returns TypedValue\n\n
    (final String uri)\n
    (final String lexicalValue, final String datatypeURI)\n
    '''
def getURI():
    '''returns String\n\n
    getURI()\n
    '''
def unparse():
    '''returns String\n\n
    unparse(final Object value)\n
    '''
def parse():
    '''returns Object\n\n
    parse(final String lexicalForm)\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid(final String lexicalForm)\n
    '''
def isValidLiteral():
    '''returns boolean\n\n
    isValidLiteral(final LiteralLabel lit)\n
    '''
def isValidValue():
    '''returns boolean\n\n
    isValidValue(final Object valueForm)\n
    '''
def isEqual():
    '''returns boolean\n\n
    isEqual(final LiteralLabel value1, final LiteralLabel value2)\n
    '''
def getHashCode():
    '''returns int\n\n
    getHashCode(final LiteralLabel lit)\n
    '''
def langTagCompatible():
    '''returns boolean\n\n
    langTagCompatible(final LiteralLabel value1, final LiteralLabel value2)\n
    '''
def cannonicalise():
    '''returns Object\n\n
    cannonicalise(final Object value)\n
    '''
def extendedTypeDefinition():
    '''returns Object\n\n
    extendedTypeDefinition()\n
    '''
def normalizeSubType():
    '''returns RDFDatatype\n\n
    normalizeSubType(final Object value, final RDFDatatype dt)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
