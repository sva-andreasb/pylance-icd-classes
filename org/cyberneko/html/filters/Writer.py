NOTIFY_CHAR_REFS = "String  \"http://apache.org/xml/features/scanner/notify-char-refs\""
NOTIFY_HTML_BUILTIN_REFS = "String  \"http://cyberneko.org/html/features/scanner/notify-builtin-refs\""
def ():
    '''returns Writer\n\n
    ()\n
    (final OutputStream outputStream, final String encoding)\n
    (final java.io.Writer writer, final String encoding)\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument(final XMLLocator locator, final String encoding, final NamespaceContext nscontext, final Augmentations augs)\n
    startDocument(final XMLLocator locator, final String encoding, final Augmentations augs)\n
    '''
def comment():
    '''returns None\n\n
    comment(final XMLString text, final Augmentations augs)\n
    '''
def startElement():
    '''returns None\n\n
    startElement(final QName element, final XMLAttributes attributes, final Augmentations augs)\n
    '''
def emptyElement():
    '''returns None\n\n
    emptyElement(final QName element, final XMLAttributes attributes, final Augmentations augs)\n
    '''
def characters():
    '''returns None\n\n
    characters(final XMLString text, final Augmentations augs)\n
    '''
def endElement():
    '''returns None\n\n
    endElement(final QName element, final Augmentations augs)\n
    '''
def startGeneralEntity():
    '''returns None\n\n
    startGeneralEntity(String name, final XMLResourceIdentifier id, final String encoding, final Augmentations augs)\n
    '''
def endGeneralEntity():
    '''returns None\n\n
    endGeneralEntity(final String name, final Augmentations augs)\n
    '''
