def comment():
    '''returns None\n\n
    comment(final String data)\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator locator)\n
    '''
def addAttribute():
    '''returns None\n\n
    addAttribute(final String uri, final String localName, final String rawName, final String type, final String value, final boolean XSLAttribute)\n
    addAttribute(final String name, final String value)\n
    addAttribute(final String uri, final String localName, final String rawName, final String type, final String value)\n
    '''
def addAttributeAlways():
    '''returns boolean\n\n
    addAttributeAlways(final String uri, final String localName, final String rawName, final String type, final String value, final boolean XSLAttribute)\n
    '''
def addXSLAttribute():
    '''returns None\n\n
    addXSLAttribute(final String name, final String value, final String uri)\n
    '''
def addAttributes():
    '''returns None\n\n
    addAttributes(final Attributes atts)\n
    '''
def asContentHandler():
    '''returns ContentHandler\n\n
    asContentHandler()\n
    '''
def endEntity():
    '''returns None\n\n
    endEntity(final String name)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def setEncoding():
    '''returns None\n\n
    setEncoding(final String encoding)\n
    '''
def setOmitXMLDeclaration():
    '''returns None\n\n
    setOmitXMLDeclaration(final boolean b)\n
    '''
def getOmitXMLDeclaration():
    '''returns boolean\n\n
    getOmitXMLDeclaration()\n
    '''
def getDoctypePublic():
    '''returns String\n\n
    getDoctypePublic()\n
    '''
def setDoctypePublic():
    '''returns None\n\n
    setDoctypePublic(final String doctypePublic)\n
    '''
def getDoctypeSystem():
    '''returns String\n\n
    getDoctypeSystem()\n
    '''
def setDoctypeSystem():
    '''returns None\n\n
    setDoctypeSystem(final String doctypeSystem)\n
    '''
def setDoctype():
    '''returns None\n\n
    setDoctype(final String doctypeSystem, final String doctypePublic)\n
    '''
def setStandalone():
    '''returns None\n\n
    setStandalone(final String standalone)\n
    '''
def getStandalone():
    '''returns String\n\n
    getStandalone()\n
    '''
def getIndent():
    '''returns boolean\n\n
    getIndent()\n
    '''
def getMediaType():
    '''returns String\n\n
    getMediaType()\n
    '''
def getVersion():
    '''returns String\n\n
    getVersion()\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final String version)\n
    '''
def setMediaType():
    '''returns None\n\n
    setMediaType(final String mediaType)\n
    '''
def getIndentAmount():
    '''returns int\n\n
    getIndentAmount()\n
    '''
def setIndentAmount():
    '''returns None\n\n
    setIndentAmount(final int m_indentAmount)\n
    '''
def setIndent():
    '''returns None\n\n
    setIndent(final boolean doIndent)\n
    '''
def namespaceAfterStartElement():
    '''returns None\n\n
    namespaceAfterStartElement(final String uri, final String prefix)\n
    '''
def asDOMSerializer():
    '''returns DOMSerializer\n\n
    asDOMSerializer()\n
    '''
def getNamespaceMappings():
    '''returns NamespaceMappings\n\n
    getNamespaceMappings()\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix(final String namespaceURI)\n
    '''
def getNamespaceURI():
    '''returns String\n\n
    getNamespaceURI(final String qname, final boolean isElement)\n
    '''
def getNamespaceURIFromPrefix():
    '''returns String\n\n
    getNamespaceURIFromPrefix(final String prefix)\n
    '''
def entityReference():
    '''returns None\n\n
    entityReference(final String name)\n
    '''
def setTransformer():
    '''returns None\n\n
    setTransformer(final Transformer t)\n
    '''
def getTransformer():
    '''returns Transformer\n\n
    getTransformer()\n
    '''
def characters():
    '''returns None\n\n
    characters(final Node node)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException exc)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException exc)\n
    '''
def warning():
    '''returns None\n\n
    warning(final SAXParseException exc)\n
    '''
def fireEndEntity():
    '''returns None\n\n
    fireEndEntity(final String name)\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def setSourceLocator():
    '''returns None\n\n
    setSourceLocator(final SourceLocator locator)\n
    '''
def setNamespaceMappings():
    '''returns None\n\n
    setNamespaceMappings(final NamespaceMappings mappings)\n
    '''
def reset():
    '''returns boolean\n\n
    reset()\n
    '''
def notationDecl():
    '''returns None\n\n
    notationDecl(final String arg0, final String arg1, final String arg2)\n
    '''
def unparsedEntityDecl():
    '''returns None\n\n
    unparsedEntityDecl(final String arg0, final String arg1, final String arg2, final String arg3)\n
    '''
def setDTDEntityExpansion():
    '''returns None\n\n
    setDTDEntityExpansion(final boolean expand)\n
    '''
def documentIsEmpty():
    '''returns boolean\n\n
    documentIsEmpty()\n
    '''
def getOutputProperty():
    '''returns String\n\n
    getOutputProperty(final String name)\n
    '''
def getOutputPropertyNonDefault():
    '''returns String\n\n
    getOutputPropertyNonDefault(final String name)\n
    '''
def asDOM3Serializer():
    '''returns Object\n\n
    asDOM3Serializer()\n
    '''
def getOutputPropertyDefault():
    '''returns String\n\n
    getOutputPropertyDefault(final String name)\n
    '''
def setOutputProperty():
    '''returns None\n\n
    setOutputProperty(final String name, final String val)\n
    '''
def setOutputPropertyDefault():
    '''returns None\n\n
    setOutputPropertyDefault(final String name, final String val)\n
    '''
