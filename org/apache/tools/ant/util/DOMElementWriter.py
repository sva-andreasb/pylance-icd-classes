def ():
    '''returns XmlNamespacePolicy\n\n
    ()\n
    (final boolean xmlDeclaration)\n
    (final boolean xmlDeclaration, final XmlNamespacePolicy namespacePolicy)\n
    (final boolean qualifyElements, final boolean qualifyAttributes)\n
    '''
def write():
    '''returns None\n\n
    write(final Element root, final OutputStream out)\n
    write(final Element element, final Writer out, final int indent, final String indentWith)\n
    '''
def writeXMLDeclaration():
    '''returns None\n\n
    writeXMLDeclaration(final Writer wri)\n
    '''
def openElement():
    '''returns None\n\n
    openElement(final Element element, final Writer out, final int indent, final String indentWith)\n
    openElement(final Element element, final Writer out, final int indent, final String indentWith, final boolean hasChildren)\n
    '''
def closeElement():
    '''returns None\n\n
    closeElement(final Element element, final Writer out, final int indent, final String indentWith, final boolean hasChildren)\n
    '''
def encode():
    '''returns String\n\n
    encode(final String value)\n
    '''
def encodedata():
    '''returns String\n\n
    encodedata(final String value)\n
    '''
def isReference():
    '''returns boolean\n\n
    isReference(final String ent)\n
    '''
def isLegalCharacter():
    '''returns boolean\n\n
    isLegalCharacter(final char c)\n
    '''
