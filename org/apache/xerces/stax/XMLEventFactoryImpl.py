def setLocation():
    '''returns None\n\n
    setLocation(final Location fLocation)\n
    '''
def createAttribute():
    '''returns Attribute\n\n
    createAttribute(final String prefix, final String namespaceURI, final String localPart, final String s)\n
    createAttribute(final String localPart, final String s)\n
    createAttribute(final QName qName, final String s)\n
    '''
def createNamespace():
    '''returns Namespace\n\n
    createNamespace(final String s)\n
    createNamespace(final String s, final String s2)\n
    '''
def createStartElement():
    '''returns StartElement\n\n
    createStartElement(final QName qName, final Iterator iterator, final Iterator iterator2)\n
    createStartElement(final String prefix, final String namespaceURI, final String localPart)\n
    createStartElement(final String prefix, final String namespaceURI, final String localPart, final Iterator iterator, final Iterator iterator2)\n
    createStartElement(final String prefix, final String namespaceURI, final String localPart, final Iterator iterator, final Iterator iterator2, final NamespaceContext namespaceContext)\n
    '''
def createEndElement():
    '''returns EndElement\n\n
    createEndElement(final QName qName, final Iterator iterator)\n
    createEndElement(final String prefix, final String namespaceURI, final String localPart)\n
    createEndElement(final String prefix, final String namespaceURI, final String localPart, final Iterator iterator)\n
    '''
def createCharacters():
    '''returns Characters\n\n
    createCharacters(final String s)\n
    '''
def createCData():
    '''returns Characters\n\n
    createCData(final String s)\n
    '''
def createSpace():
    '''returns Characters\n\n
    createSpace(final String s)\n
    '''
def createIgnorableSpace():
    '''returns Characters\n\n
    createIgnorableSpace(final String s)\n
    '''
def createStartDocument():
    '''returns StartDocument\n\n
    createStartDocument()\n
    createStartDocument(final String s, final String s2, final boolean b)\n
    createStartDocument(final String s, final String s2)\n
    createStartDocument(final String s)\n
    '''
def createEndDocument():
    '''returns EndDocument\n\n
    createEndDocument()\n
    '''
def createEntityReference():
    '''returns EntityReference\n\n
    createEntityReference(final String s, final EntityDeclaration entityDeclaration)\n
    '''
def createComment():
    '''returns Comment\n\n
    createComment(final String s)\n
    '''
def createProcessingInstruction():
    '''returns ProcessingInstruction\n\n
    createProcessingInstruction(final String s, final String s2)\n
    '''
def createDTD():
    '''returns DTD\n\n
    createDTD(final String s)\n
    '''
