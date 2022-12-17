def ():
    '''returns XMLWriter\n\n
    ()\n
    (final Writer writer, final Model model, final int indent, final int tab)\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String propName, final Object propValue)\n
    '''
def setErrorHandler():
    '''returns RDFErrorHandler\n\n
    setErrorHandler(final RDFErrorHandler errorHandler)\n
    '''
def write():
    '''returns None\n\n
    write(final Model model, final OutputStream out, final String base)\n
    write(final Model model, final Writer writer, final String base)\n
    '''
def accept():
    '''returns boolean\n\n
    accept(final Statement statement)\n
    '''
def xmlDeclaration():
    '''returns None\n\n
    xmlDeclaration(final String encoding)\n
    '''
def rootStartTag():
    '''returns None\n\n
    rootStartTag(final String namespaceUri, final String localName)\n
    '''
def startTag():
    '''returns None\n\n
    startTag(final String namespaceUri, final String localName, final boolean isChildStartTag)\n
    '''
def attribute():
    '''returns None\n\n
    attribute(final String namespaceUri, final String localName, final String value)\n
    '''
def closeEmptyStartTag():
    '''returns None\n\n
    closeEmptyStartTag()\n
    '''
def closeStartTag():
    '''returns None\n\n
    closeStartTag(final boolean isParent)\n
    '''
def literal():
    '''returns None\n\n
    literal(final String literal)\n
    '''
def endTag():
    '''returns None\n\n
    endTag(final String namespaceUri, final String localName, final boolean isParent)\n
    '''
def rootEndTag():
    '''returns None\n\n
    rootEndTag(final String namespaceUri, final String localName, final boolean isParent)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
