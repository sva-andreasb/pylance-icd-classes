SYNTHESIZED_NAMESPACE_PREFX = "String  \"http://cyberneko.org/html/ns/synthesized/\""
def ():
    '''returns Purifier\n\n
    ()\n
    '''
def reset():
    '''returns None\n\n
    reset(final XMLComponentManager manager)\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument(final XMLLocator locator, final String encoding, final Augmentations augs)\n
    startDocument(final XMLLocator locator, final String encoding, final NamespaceContext nscontext, final Augmentations augs)\n
    '''
def xmlDecl():
    '''returns None\n\n
    xmlDecl(String version, String encoding, String standalone, final Augmentations augs)\n
    '''
def comment():
    '''returns None\n\n
    comment(XMLString text, final Augmentations augs)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(String target, XMLString data, final Augmentations augs)\n
    '''
def doctypeDecl():
    '''returns None\n\n
    doctypeDecl(final String root, final String pubid, final String sysid, final Augmentations augs)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName element, final XMLAttributes attrs, final Augmentations augs)\n
    '''
def emptyElement():
    '''returns None\n\n
    emptyElement(final QName element, final XMLAttributes attrs, final Augmentations augs)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA(final Augmentations augs)\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA(final Augmentations augs)\n
    '''
def characters():
    '''returns None\n\n
    characters(XMLString text, final Augmentations augs)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(QName element, final Augmentations augs)\n
    '''
