XSD = "String  \"http://www.w3.org/2001/XMLSchema\""
def ():
    '''returns XSDDatatype\n\n
    (final String typeName)\n
    (final String typeName, final Class<?> javaClass)\n
    (final XSSimpleType xstype, final String namespace)\n
    '''
def parse():
    '''returns Object\n\n
    parse(final String lexicalForm)\n
    '''
def unparse():
    '''returns String\n\n
    unparse(final Object value)\n
    '''
def isEqual():
    '''returns boolean\n\n
    isEqual(final LiteralLabel value1, final LiteralLabel value2)\n
    '''
def extendedTypeDefinition():
    '''returns Object\n\n
    extendedTypeDefinition()\n
    '''
def convertValidatedDataValue():
    '''returns Object\n\n
    convertValidatedDataValue(final ValidatedInfo validatedInfo)\n
    '''
def parseValidated():
    '''returns Object\n\n
    parseValidated(final String lexical)\n
    '''
def isValidLiteral():
    '''returns boolean\n\n
    isValidLiteral(final LiteralLabel lit)\n
    '''
def isBaseTypeCompatible():
    '''returns boolean\n\n
    isBaseTypeCompatible(final LiteralLabel lit)\n
    '''
def getHashCode():
    '''returns int\n\n
    getHashCode(final byte[] bytes)\n
    '''
