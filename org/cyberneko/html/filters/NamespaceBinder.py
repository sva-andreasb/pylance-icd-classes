XHTML_1_0_URI = "String  \"http://www.w3.org/1999/xhtml\""
XML_URI = "String  \"http://www.w3.org/XML/1998/namespace\""
XMLNS_URI = "String  \"http://www.w3.org/2000/xmlns/\""
def NamespaceBinder():
    '''    public NamespaceBinder()
    '''
def getRecognizedFeatures():
    '''    public String[] getRecognizedFeatures()
    '''
def getFeatureDefault():
    '''    public Boolean getFeatureDefault(final String featureId)
    '''
def getRecognizedProperties():
    '''    public String[] getRecognizedProperties()
    '''
def getPropertyDefault():
    '''    public Object getPropertyDefault(final String propertyId)
    '''
def reset():
    '''    public void reset(final XMLComponentManager manager)
    public void reset()
    '''
def startDocument():
    '''    public void startDocument(final XMLLocator locator, final String encoding, final NamespaceContext nscontext, final Augmentations augs)
    '''
def startElement():
    '''    public void startElement(final QName element, final XMLAttributes attrs, final Augmentations augs)
    '''
def emptyElement():
    '''    public void emptyElement(final QName element, final XMLAttributes attrs, final Augmentations augs)
    '''
def endElement():
    '''    public void endElement(final QName element, final Augmentations augs)
    '''
def NamespaceSupport():
    '''    public NamespaceSupport()
    '''
def getURI():
    '''    public String getURI(final String prefix)
    '''
def getDeclaredPrefixCount():
    '''    public int getDeclaredPrefixCount()
    '''
def getDeclaredPrefixAt():
    '''    public String getDeclaredPrefixAt(final int index)
    '''
def getParentContext():
    '''    public NamespaceContext getParentContext()
    '''
def pushContext():
    '''    public void pushContext()
    '''
def popContext():
    '''    public void popContext()
    '''
def declarePrefix():
    '''    public boolean declarePrefix(final String prefix, final String uri)
    '''
def getPrefix():
    '''    public String getPrefix(final String uri)
    '''
def getAllPrefixes():
    '''    public Enumeration getAllPrefixes()
    '''
def Entry():
    '''    public Entry(final String prefix, final String uri)
    '''
