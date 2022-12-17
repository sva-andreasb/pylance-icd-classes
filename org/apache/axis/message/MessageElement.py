def ():
    '''returns MessageElement\n\n
    ()\n
    (final String namespace, final String localPart)\n
    (final String localPart, final String prefix, final String namespace)\n
    (final Name eltName)\n
    (final String namespace, final String localPart, final Object value)\n
    (final QName name)\n
    (final QName name, final Object value)\n
    (final Element elem)\n
    (final CharacterData text)\n
    (final String namespace, final String localPart, final String prefix, final Attributes attributes, final DeserializationContext context)\n
    '''
def getDeserializationContext():
    '''returns DeserializationContext\n\n
    getDeserializationContext()\n
    '''
def setFixupDeserializer():
    '''returns None\n\n
    setFixupDeserializer(final Deserializer dser)\n
    '''
def getFixupDeserializer():
    '''returns Deserializer\n\n
    getFixupDeserializer()\n
    '''
def setEndIndex():
    '''returns None\n\n
    setEndIndex(final int endIndex)\n
    '''
def isRoot():
    '''returns boolean\n\n
    isRoot()\n
    '''
def getID():
    '''returns String\n\n
    getID()\n
    '''
def getHref():
    '''returns String\n\n
    getHref()\n
    '''
def getAttributesEx():
    '''returns Attributes\n\n
    getAttributesEx()\n
    '''
def cloneNode():
    '''returns Node\n\n
    cloneNode(final boolean deep)\n
    '''
def setAllAttributes():
    '''returns None\n\n
    setAllAttributes(final Attributes attrs)\n
    '''
def detachAllChildren():
    '''returns None\n\n
    detachAllChildren()\n
    '''
def getCompleteAttributes():
    '''returns Attributes\n\n
    getCompleteAttributes()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getQName():
    '''returns QName\n\n
    getQName()\n
    '''
def setQName():
    '''returns None\n\n
    setQName(final QName qName)\n
    '''
def setNamespaceURI():
    '''returns None\n\n
    setNamespaceURI(final String nsURI)\n
    '''
def getType():
    '''returns QName\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final QName qname)\n
    '''
def getRecorder():
    '''returns SAX2EventRecorder\n\n
    getRecorder()\n
    '''
def setRecorder():
    '''returns None\n\n
    setRecorder(final SAX2EventRecorder rec)\n
    '''
def getEncodingStyle():
    '''returns String\n\n
    getEncodingStyle()\n
    '''
def removeContents():
    '''returns None\n\n
    removeContents()\n
    '''
def getVisibleNamespacePrefixes():
    '''returns Iterator\n\n
    getVisibleNamespacePrefixes()\n
    '''
def setEncodingStyle():
    '''returns None\n\n
    setEncodingStyle(String encodingStyle)\n
    '''
def addChild():
    '''returns None\n\n
    addChild(final MessageElement el)\n
    '''
def getChildren():
    '''returns List\n\n
    getChildren()\n
    '''
def setContentsIndex():
    '''returns None\n\n
    setContentsIndex(final int index)\n
    '''
def setNSMappings():
    '''returns None\n\n
    setNSMappings(final ArrayList namespaces)\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix(final String searchNamespaceURI)\n
    '''
def getNamespaceURI():
    '''returns String\n\n
    getNamespaceURI(String searchPrefix)\n
    '''
def getObjectValue():
    '''returns Object\n\n
    getObjectValue()\n
    getObjectValue(final Class cls)\n
    '''
def setObjectValue():
    '''returns None\n\n
    setObjectValue(final Object newValue)\n
    '''
def getValueAsType():
    '''returns Object\n\n
    getValueAsType(final QName type)\n
    getValueAsType(final QName type, final Class cls)\n
    '''
def addAttribute():
    '''returns SOAPElement\n\n
    addAttribute(final String namespace, final String localName, final QName value)\n
    addAttribute(final String namespace, final String localName, final String value)\n
    addAttribute(final String attrPrefix, final String namespace, final String localName, final String value)\n
    addAttribute(final Name attrName, final String value)\n
    '''
def setAttribute():
    '''returns None\n\n
    setAttribute(final String namespace, final String localName, final String value)\n
    setAttribute(final String name, final String value)\n
    '''
def getAttributeValue():
    '''returns String\n\n
    getAttributeValue(final String localName)\n
    getAttributeValue(final Name attrName)\n
    '''
def setEnvelope():
    '''returns None\n\n
    setEnvelope(final SOAPEnvelope env)\n
    '''
def getEnvelope():
    '''returns SOAPEnvelope\n\n
    getEnvelope()\n
    '''
def getRealElement():
    '''returns MessageElement\n\n
    getRealElement()\n
    '''
def getAsDocument():
    '''returns Document\n\n
    getAsDocument()\n
    '''
def getAsString():
    '''returns String\n\n
    getAsString()\n
    '''
def getAsDOM():
    '''returns Element\n\n
    getAsDOM()\n
    '''
def publishToHandler():
    '''returns None\n\n
    publishToHandler(final ContentHandler handler)\n
    '''
def publishContents():
    '''returns None\n\n
    publishContents(final ContentHandler handler)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def addMapping():
    '''returns None\n\n
    addMapping(final Mapping map)\n
    '''
def addChildElement():
    '''returns SOAPElement\n\n
    addChildElement(final Name childName)\n
    addChildElement(final String localName)\n
    addChildElement(final String localName, final String prefixName)\n
    addChildElement(final String localName, final String childPrefix, final String uri)\n
    addChildElement(final SOAPElement element)\n
    '''
def addTextNode():
    '''returns SOAPElement\n\n
    addTextNode(final String s)\n
    '''
def addNamespaceDeclaration():
    '''returns SOAPElement\n\n
    addNamespaceDeclaration(final String prefix, final String uri)\n
    '''
def getAllAttributes():
    '''returns Iterator\n\n
    getAllAttributes()\n
    '''
def getNamespacePrefixes():
    '''returns Iterator\n\n
    getNamespacePrefixes()\n
    '''
def getElementName():
    '''returns Name\n\n
    getElementName()\n
    '''
def removeAttribute():
    '''returns None\n\n
    removeAttribute(final Name attrName)\n
    removeAttribute(final String attrName)\n
    '''
def removeNamespaceDeclaration():
    '''returns boolean\n\n
    removeNamespaceDeclaration(final String namespacePrefix)\n
    '''
def getChildElements():
    '''returns Iterator\n\n
    getChildElements()\n
    getChildElements(final QName qname)\n
    getChildElements(final Name childName)\n
    '''
def getChildElement():
    '''returns MessageElement\n\n
    getChildElement(final QName qname)\n
    '''
def getTagName():
    '''returns String\n\n
    getTagName()\n
    '''
def hasAttribute():
    '''returns boolean\n\n
    hasAttribute(String attrName)\n
    '''
def getAttribute():
    '''returns String\n\n
    getAttribute(final String attrName)\n
    '''
def removeAttributeNS():
    '''returns None\n\n
    removeAttributeNS(final String namespace, final String localName)\n
    '''
def hasAttributeNS():
    '''returns boolean\n\n
    hasAttributeNS(String namespace, String localName)\n
    '''
def getAttributeNode():
    '''returns Attr\n\n
    getAttributeNode(final String attrName)\n
    '''
def removeAttributeNode():
    '''returns Attr\n\n
    removeAttributeNode(final Attr oldAttr)\n
    '''
def setAttributeNode():
    '''returns Attr\n\n
    setAttributeNode(final Attr newAttr)\n
    '''
def setAttributeNodeNS():
    '''returns Attr\n\n
    setAttributeNodeNS(final Attr newAttr)\n
    '''
def getElementsByTagName():
    '''returns NodeList\n\n
    getElementsByTagName(final String tagName)\n
    '''
def getAttributeNS():
    '''returns String\n\n
    getAttributeNS(String namespaceURI, final String localName)\n
    '''
def setAttributeNS():
    '''returns None\n\n
    setAttributeNS(String namespaceURI, final String qualifiedName, final String value)\n
    '''
def getAttributeNodeNS():
    '''returns Attr\n\n
    getAttributeNodeNS(final String namespace, final String localName)\n
    '''
def getElementsByTagNameNS():
    '''returns NodeList\n\n
    getElementsByTagNameNS(final String namespace, final String localName)\n
    '''
def item():
    '''returns Node\n\n
    item(final int index)\n
    '''
def getLength():
    '''returns int\n\n
    getLength()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def getValue():
    '''returns String\n\n
    getValue()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String value)\n
    '''
def getOwnerDocument():
    '''returns Document\n\n
    getOwnerDocument()\n
    '''
