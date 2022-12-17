def ():
    '''returns MagicSAXFilter\n\n
    (final ResourceBundle messages)\n
    '''
def reset():
    '''returns None\n\n
    reset(final InternalPolicy instance)\n
    '''
def characters():
    '''returns None\n\n
    characters(final XMLString text, final Augmentations augs)\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString text, final Augmentations augs)\n
    '''
def doctypeDecl():
    '''returns None\n\n
    doctypeDecl(final String root, final String publicId, final String systemId, final Augmentations augs)\n
    '''
def emptyElement():
    '''returns None\n\n
    emptyElement(final QName element, final XMLAttributes attributes, final Augmentations augs)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final QName element, final Augmentations augs)\n
    '''
def processingInstruction():
    '''returns None\n\n
    processingInstruction(final String target, final XMLString data, final Augmentations augs)\n
    '''
def startCDATA():
    '''returns None\n\n
    startCDATA(final Augmentations augs)\n
    '''
def endCDATA():
    '''returns None\n\n
    endCDATA(final Augmentations augs)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName element, XMLAttributes attributes, final Augmentations augs)\n
    '''
def getErrorMessages():
    '''returns List<String>\n\n
    getErrorMessages()\n
    '''
