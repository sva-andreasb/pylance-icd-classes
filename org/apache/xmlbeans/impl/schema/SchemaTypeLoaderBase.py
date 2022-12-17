def findType():
    '''returns SchemaType\n\n
    findType(final QName name)\n
    '''
def findDocumentType():
    '''returns SchemaType\n\n
    findDocumentType(final QName name)\n
    '''
def findAttributeType():
    '''returns SchemaType\n\n
    findAttributeType(final QName name)\n
    '''
def findModelGroup():
    '''returns SchemaModelGroup\n\n
    findModelGroup(final QName name)\n
    '''
def findAttributeGroup():
    '''returns SchemaAttributeGroup\n\n
    findAttributeGroup(final QName name)\n
    '''
def findElement():
    '''returns SchemaGlobalElement\n\n
    findElement(final QName name)\n
    '''
def findAttribute():
    '''returns SchemaGlobalAttribute\n\n
    findAttribute(final QName name)\n
    '''
def newInstance():
    '''returns XmlObject\n\n
    newInstance(final SchemaType type, final XmlOptions options)\n
    '''
def parse():
    '''returns XmlObject\n\n
    parse(final String xmlText, final SchemaType type, final XmlOptions options)\n
    parse(final XMLInputStream xis, final SchemaType type, final XmlOptions options)\n
    parse(final XMLStreamReader xsr, final SchemaType type, final XmlOptions options)\n
    parse(final File file, final SchemaType type, XmlOptions options)\n
    parse(URL url, final SchemaType type, XmlOptions options)\n
    parse(InputStream jiois, final SchemaType type, final XmlOptions options)\n
    parse(final Reader jior, final SchemaType type, final XmlOptions options)\n
    parse(final Node node, final SchemaType type, final XmlOptions options)\n
    '''
def newXmlSaxHandler():
    '''returns XmlSaxHandler\n\n
    newXmlSaxHandler(final SchemaType type, final XmlOptions options)\n
    '''
def newDomImplementation():
    '''returns DOMImplementation\n\n
    newDomImplementation(final XmlOptions options)\n
    '''
def newValidatingXMLInputStream():
    '''returns XMLInputStream\n\n
    newValidatingXMLInputStream(final XMLInputStream xis, final SchemaType type, final XmlOptions options)\n
    '''
def compilePath():
    '''returns String\n\n
    compilePath(final String pathExpr)\n
    compilePath(final String pathExpr, final XmlOptions options)\n
    '''
def compileQuery():
    '''returns String\n\n
    compileQuery(final String queryExpr)\n
    compileQuery(final String queryExpr, final XmlOptions options)\n
    '''
def typeForSignature():
    '''returns SchemaType\n\n
    typeForSignature(final String signature)\n
    '''
