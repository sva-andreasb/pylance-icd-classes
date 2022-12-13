XSD = "String  \"http://www.w3.org/2001/XMLSchema\""
def XSDDatatype():
    '''public XSDDatatype(final String typeName)
    public XSDDatatype(final String typeName, final Class<?> javaClass)
    public XSDDatatype(final XSSimpleType xstype, final String namespace)
    '''
def parse():
    '''public Object parse(final String lexicalForm)
    '''
def unparse():
    '''public String unparse(final Object value)
    '''
def isEqual():
    '''public boolean isEqual(final LiteralLabel value1, final LiteralLabel value2)
    '''
def extendedTypeDefinition():
    '''public Object extendedTypeDefinition()
    '''
def loadUserDefined():
    '''public static List<String> loadUserDefined(final String uri, final Reader reader, final String encoding, final TypeMapper tm)
    public static List<String> loadUserDefined(final String uri, final String encoding, final TypeMapper tm)
    '''
def convertValidatedDataValue():
    '''public Object convertValidatedDataValue(final ValidatedInfo validatedInfo)
    '''
def parseValidated():
    '''public Object parseValidated(final String lexical)
    '''
def isValidLiteral():
    '''public boolean isValidLiteral(final LiteralLabel lit)
    '''
def isBaseTypeCompatible():
    '''public boolean isBaseTypeCompatible(final LiteralLabel lit)
    '''
def trimPlus():
    '''public static String trimPlus(final String str)
    '''
def loadXSDSimpleTypes():
    '''public static void loadXSDSimpleTypes(final TypeMapper tm)
    '''
def main():
    '''public static void main(final String[] args)
    '''
def getHashCode():
    '''public int getHashCode(final byte[] bytes)
    '''
