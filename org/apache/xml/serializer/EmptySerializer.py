def asContentHandler():
    '''returns ContentHandler\n\n
    asContentHandler()\n
    '''
def setContentHandler():
    '''returns None\n\n
    setContentHandler(final ContentHandler ch)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def getOutputFormat():
    '''returns Properties\n\n
    getOutputFormat()\n
    '''
def getOutputStream():
    '''returns OutputStream\n\n
    getOutputStream()\n
    '''
def getWriter():
    '''returns Writer\n\n
    getWriter()\n
    '''
def reset():
    '''returns boolean\n\n
    reset()\n
    '''
def serialize():
    '''returns None\n\n
    serialize(final Node node)\n
    '''
def setCdataSectionElements():
    '''returns None\n\n
    setCdataSectionElements(final Vector URI_and_localNames)\n
    setCdataSectionElements(final Hashtable h)\n
    '''
def setEscaping():
    '''returns boolean\n\n
    setEscaping(final boolean escape)\n
    '''
def setIndent():
    '''returns None\n\n
    setIndent(final boolean indent)\n
    '''
def setIndentAmount():
    '''returns None\n\n
    setIndentAmount(final int spaces)\n
    '''
def setOutputFormat():
    '''returns None\n\n
    setOutputFormat(final Properties format)\n
    '''
def setOutputStream():
    '''returns None\n\n
    setOutputStream(final OutputStream output)\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final String version)\n
    '''
def setWriter():
    '''returns None\n\n
    setWriter(final Writer writer)\n
    '''
def setTransformer():
    '''returns None\n\n
    setTransformer(final Transformer transformer)\n
    '''
def getTransformer():
    '''returns Transformer\n\n
    getTransformer()\n
    '''
def flushPending():
    '''returns None\n\n
    flushPending()\n
    '''
def addAttribute():
    '''returns None\n\n
    addAttribute(final String uri, final String localName, final String rawName, final String type, final String value, final boolean XSLAttribute)\n
    addAttribute(final String name, final String value)\n
    addAttribute(final String uri, final String localName, final String rawName, final String type, final String value)\n
    '''
def addAttributes():
    '''returns None\n\n
    addAttributes(final Attributes atts)\n
    '''
def characters():
    '''returns None\n\n
    characters(final String chars)\n
    characters(final char[] arg0, final int arg1, final int arg2)\n
    characters(final Node node)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final String elemName)\n
    endElement(final String arg0, final String arg1, final String arg2)\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final String uri, final String localName, final String qName)\n
    startElement(final String qName)\n
    startElement(final String arg0, final String arg1, final String arg2, final Attributes arg3)\n
    '''
def namespaceAfterStartElement():
    '''returns None\n\n
    namespaceAfterStartElement(final String uri, final String prefix)\n
    '''
def startPrefixMapping():
    '''returns None\n\n
    startPrefixMapping(final String prefix, final String uri, final boolean shouldFlush)\n
    startPrefixMapping(final String arg0, final String arg1)\n
    '''
def entityReference():
    '''returns None\n\n
    entityReference(final String entityName)\n
    '''
def getNamespaceMappings():
    '''returns NamespaceMappings\n\n
    getNamespaceMappings()\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix(final String uri)\n
    '''
def getNamespaceURI():
    '''returns String\n\n
    getNamespaceURI(final String name, final boolean isElement)\n
    '''
def getNamespaceURIFromPrefix():
    '''returns String\n\n
    getNamespaceURIFromPrefix(final String prefix)\n
    '''
def setDocumentLocator():
    '''returns None\n\n
    setDocumentLocator(final Locator arg0)\n
    '''
def endDocument():
    '''returns None\n\n
    endDocument()\n
    '''
def endPrefixMapping():
    '''returns None\n\n
    endPrefixMapping(final String arg0)\n
    '''
def ignorableWhitespace():
    '''returns None\n\n
    ignorableWhitespace(final char[] arg0, final int arg1, final int arg2)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String arg0, final String arg1)\n
    '''
def skippedEntity():
    '''returns None\n\n
    skippedEntity(final String arg0)\n
    '''
def comment():
    '''returns None\n\n
    comment(final String comment)\n
    comment(final char[] arg0, final int arg1, final int arg2)\n
    '''
def startDTD():
    '''returns None\n\n
    startDTD(final String arg0, final String arg1, final String arg2)\n
    '''
def endDTD():
    '''returns None\n\n
    endDTD()\n
    '''
def startEntity():
    '''returns None\n\n
    startEntity(final String arg0)\n
    '''
def endEntity():
    '''returns None\n\n
    endEntity(final String arg0)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA()\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA()\n
    '''
def getDoctypePublic():
    '''returns String\n\n
    getDoctypePublic()\n
    '''
def getDoctypeSystem():
    '''returns String\n\n
    getDoctypeSystem()\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def getIndent():
    '''returns boolean\n\n
    getIndent()\n
    '''
def getIndentAmount():
    '''returns int\n\n
    getIndentAmount()\n
    '''
def getMediaType():
    '''returns String\n\n
    getMediaType()\n
    '''
def getOmitXMLDeclaration():
    '''returns boolean\n\n
    getOmitXMLDeclaration()\n
    '''
def getStandalone():
    '''returns String\n\n
    getStandalone()\n
    '''
def getVersion():
    '''returns String\n\n
    getVersion()\n
    '''
def setDoctype():
    '''returns None\n\n
    setDoctype(final String system, final String pub)\n
    '''
def setDoctypePublic():
    '''returns None\n\n
    setDoctypePublic(final String doctype)\n
    '''
def setDoctypeSystem():
    '''returns None\n\n
    setDoctypeSystem(final String doctype)\n
    '''
def setEncoding():
    '''returns None\n\n
    setEncoding(final String encoding)\n
    '''
def setMediaType():
    '''returns None\n\n
    setMediaType(final String mediatype)\n
    '''
def setOmitXMLDeclaration():
    '''returns None\n\n
    setOmitXMLDeclaration(final boolean b)\n
    '''
def setStandalone():
    '''returns None\n\n
    setStandalone(final String standalone)\n
    '''
def elementDecl():
    '''returns None\n\n
    elementDecl(final String arg0, final String arg1)\n
    '''
def attributeDecl():
    '''returns None\n\n
    attributeDecl(final String arg0, final String arg1, final String arg2, final String arg3, final String arg4)\n
    '''
def internalEntityDecl():
    '''returns None\n\n
    internalEntityDecl(final String arg0, final String arg1)\n
    '''
def externalEntityDecl():
    '''returns None\n\n
    externalEntityDecl(final String arg0, final String arg1, final String arg2)\n
    '''
def warning():
    '''returns None\n\n
    warning(final SAXParseException arg0)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException arg0)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException arg0)\n
    '''
def asDOMSerializer():
    '''returns DOMSerializer\n\n
    asDOMSerializer()\n
    '''
def setNamespaceMappings():
    '''returns None\n\n
    setNamespaceMappings(final NamespaceMappings mappings)\n
    '''
def setSourceLocator():
    '''returns None\n\n
    setSourceLocator(final SourceLocator locator)\n
    '''
def addUniqueAttribute():
    '''returns None\n\n
    addUniqueAttribute(final String name, final String value, final int flags)\n
    '''
def addXSLAttribute():
    '''returns None\n\n
    addXSLAttribute(final String qName, final String value, final String uri)\n
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
def getOutputProperty():
    '''returns String\n\n
    getOutputProperty(final String name)\n
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
def asDOM3Serializer():
    '''returns Object\n\n
    asDOM3Serializer()\n
    '''
