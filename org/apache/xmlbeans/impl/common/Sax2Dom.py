EMPTYSTRING = "String  \"\""
XML_PREFIX = "String  \"xml\""
XMLNS_PREFIX = "String  \"xmlns\""
XMLNS_STRING = "String  \"xmlns:\""
XMLNS_URI = "String  \"http://www.w3.org/2000/xmlns/\""
def Sax2Dom():
    '''    public Sax2Dom()
    public Sax2Dom(final Node root)
    '''
def getDOM():
    '''    public Node getDOM()
    '''
def characters():
    '''    public void characters(final char[] ch, final int start, final int length)
    '''
def startDocument():
    '''    public void startDocument()
    '''
def endDocument():
    '''    public void endDocument()
    '''
def startElement():
    '''    public void startElement(final String namespace, final String localName, final String qName, final Attributes attrs)
    '''
def endElement():
    '''    public void endElement(final String namespace, final String localName, final String qName)
    '''
def startPrefixMapping():
    '''    public void startPrefixMapping(final String prefix, final String uri)
    '''
def endPrefixMapping():
    '''    public void endPrefixMapping(final String prefix)
    '''
def ignorableWhitespace():
    '''    public void ignorableWhitespace(final char[] ch, final int start, final int length)
    '''
def processingInstruction():
    '''    public void processingInstruction(final String target, final String data)
    '''
def setDocumentLocator():
    '''    public void setDocumentLocator(final Locator locator)
    '''
def skippedEntity():
    '''    public void skippedEntity(final String name)
    '''
def comment():
    '''    public void comment(final char[] ch, final int start, final int length)
    '''
def startCDATA():
    '''    public void startCDATA()
    '''
def endCDATA():
    '''    public void endCDATA()
    '''
def startEntity():
    '''    public void startEntity(final String name)
    '''
def endEntity():
    '''    public void endEntity(final String name)
    '''
def startDTD():
    '''    public void startDTD(final String name, final String publicId, final String systemId)
    '''
def endDTD():
    '''    public void endDTD()
    '''
