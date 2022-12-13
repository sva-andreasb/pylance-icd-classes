def serializeEndpart():
    '''    public static void serializeEndpart(final XMLStreamWriter writer)
    '''
def serializeAttribute():
    '''    public static void serializeAttribute(final OMAttribute attr, final XMLStreamWriter writer)
    '''
def serializeNamespace():
    '''    public static void serializeNamespace(final OMNamespace namespace, final XMLStreamWriter writer)
    '''
def isSetPrefixBeforeStartElement():
    '''    public static boolean isSetPrefixBeforeStartElement(final XMLStreamWriter writer)
    '''
def serializeStartpart():
    '''    public static void serializeStartpart(final OMElement element, final XMLStreamWriter writer)
    public static void serializeStartpart(final OMElement element, final String localName, final XMLStreamWriter writer)
    '''
def serializeNamespaces():
    '''    public static void serializeNamespaces(final OMElement element, final XMLStreamWriter writer)
    '''
def serializeAttributes():
    '''    public static void serializeAttributes(final OMElement element, final XMLStreamWriter writer)
    '''
def serializeNormal():
    '''    public static void serializeNormal(final OMElement element, final XMLStreamWriter writer, final boolean cache)
    '''
def serializeByPullStream():
    '''    public static void serializeByPullStream(final OMElement element, final XMLStreamWriter writer)
    public static void serializeByPullStream(final OMElement element, final XMLStreamWriter writer, final boolean cache)
    '''
def getNextNSPrefix():
    '''    public static String getNextNSPrefix()
    public static String getNextNSPrefix(final XMLStreamWriter writer)
    '''
def generateSetPrefix():
    '''    public static String generateSetPrefix(String prefix, final String namespace, final XMLStreamWriter writer, final boolean attr)
    '''
def isAssociated():
    '''    public static boolean isAssociated(String prefix, String namespace, final XMLStreamWriter writer)
    '''
