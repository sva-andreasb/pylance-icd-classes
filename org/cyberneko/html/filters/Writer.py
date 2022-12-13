NOTIFY_CHAR_REFS = "String  \"http://apache.org/xml/features/scanner/notify-char-refs\""
NOTIFY_HTML_BUILTIN_REFS = "String  \"http://cyberneko.org/html/features/scanner/notify-builtin-refs\""
def Writer():
    '''public Writer()
    public Writer(final OutputStream outputStream, final String encoding)
    public Writer(final java.io.Writer writer, final String encoding)
    '''
def startDocument():
    '''public void startDocument(final XMLLocator locator, final String encoding, final NamespaceContext nscontext, final Augmentations augs)
    public void startDocument(final XMLLocator locator, final String encoding, final Augmentations augs)
    '''
def comment():
    '''public void comment(final XMLString text, final Augmentations augs)
    '''
def startElement():
    '''public void startElement(final QName element, final XMLAttributes attributes, final Augmentations augs)
    '''
def emptyElement():
    '''public void emptyElement(final QName element, final XMLAttributes attributes, final Augmentations augs)
    '''
def characters():
    '''public void characters(final XMLString text, final Augmentations augs)
    '''
def endElement():
    '''public void endElement(final QName element, final Augmentations augs)
    '''
def startGeneralEntity():
    '''public void startGeneralEntity(String name, final XMLResourceIdentifier id, final String encoding, final Augmentations augs)
    '''
def endGeneralEntity():
    '''public void endGeneralEntity(final String name, final Augmentations augs)
    '''
def main():
    '''public static void main(final String[] argv)
    '''
