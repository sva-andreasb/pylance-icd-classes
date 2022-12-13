SYNTHESIZED_NAMESPACE_PREFX = "String  \"http://cyberneko.org/html/ns/synthesized/\""
def Purifier():
    '''public Purifier()
    '''
def reset():
    '''public void reset(final XMLComponentManager manager)
    '''
def startDocument():
    '''public void startDocument(final XMLLocator locator, final String encoding, final Augmentations augs)
    public void startDocument(final XMLLocator locator, final String encoding, final NamespaceContext nscontext, final Augmentations augs)
    '''
def xmlDecl():
    '''public void xmlDecl(String version, String encoding, String standalone, final Augmentations augs)
    '''
def comment():
    '''public void comment(XMLString text, final Augmentations augs)
    '''
def processingInstruction():
    '''public void processingInstruction(String target, XMLString data, final Augmentations augs)
    '''
def doctypeDecl():
    '''public void doctypeDecl(final String root, final String pubid, final String sysid, final Augmentations augs)
    '''
def startElement():
    '''public void startElement(final QName element, final XMLAttributes attrs, final Augmentations augs)
    '''
def emptyElement():
    '''public void emptyElement(final QName element, final XMLAttributes attrs, final Augmentations augs)
    '''
def startCDATA():
    '''public void startCDATA(final Augmentations augs)
    '''
def endCDATA():
    '''public void endCDATA(final Augmentations augs)
    '''
def characters():
    '''public void characters(XMLString text, final Augmentations augs)
    '''
def endElement():
    '''public void endElement(QName element, final Augmentations augs)
    '''
