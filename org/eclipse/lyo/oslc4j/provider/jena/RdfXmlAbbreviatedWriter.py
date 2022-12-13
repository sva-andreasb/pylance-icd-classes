def RdfXmlAbbreviatedWriter():
    '''public RdfXmlAbbreviatedWriter()
    '''
def setProperty():
    '''public Object setProperty(final String propName, final Object propValue)
    '''
def setErrorHandler():
    '''public RDFErrorHandler setErrorHandler(final RDFErrorHandler errorHandler)
    '''
def write():
    '''public void write(final Model model, final OutputStream out, final String base)
    public void write(final Model model, final Writer writer, final String base)
    '''
def accept():
    '''public boolean accept(final Statement statement)
    '''
def XMLWriter():
    '''public XMLWriter(final Writer writer, final Model model, final int indent, final int tab)
    '''
def xmlDeclaration():
    '''public void xmlDeclaration(final String encoding)
    '''
def rootStartTag():
    '''public void rootStartTag(final String namespaceUri, final String localName)
    '''
def startTag():
    '''public void startTag(final String namespaceUri, final String localName, final boolean isChildStartTag)
    '''
def attribute():
    '''public void attribute(final String namespaceUri, final String localName, final String value)
    '''
def closeEmptyStartTag():
    '''public void closeEmptyStartTag()
    '''
def closeStartTag():
    '''public void closeStartTag(final boolean isParent)
    '''
def literal():
    '''public void literal(final String literal)
    '''
def endTag():
    '''public void endTag(final String namespaceUri, final String localName, final boolean isParent)
    '''
def rootEndTag():
    '''public void rootEndTag(final String namespaceUri, final String localName, final boolean isParent)
    '''
def end():
    '''public void end()
    '''
