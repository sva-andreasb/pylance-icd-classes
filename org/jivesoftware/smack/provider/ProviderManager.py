def getInstance():
    '''    public static synchronized ProviderManager getInstance()
    '''
def setInstance():
    '''    public static synchronized void setInstance(final ProviderManager providerManager)
    '''
def getIQProvider():
    '''    public Object getIQProvider(final String elementName, final String namespace)
    '''
def getIQProviders():
    '''    public Collection<Object> getIQProviders()
    '''
def addIQProvider():
    '''    public void addIQProvider(final String elementName, final String namespace, final Object provider)
    '''
def removeIQProvider():
    '''    public void removeIQProvider(final String elementName, final String namespace)
    '''
def getExtensionProvider():
    '''    public Object getExtensionProvider(final String elementName, final String namespace)
    '''
def addExtensionProvider():
    '''    public void addExtensionProvider(final String elementName, final String namespace, final Object provider)
    '''
def removeExtensionProvider():
    '''    public void removeExtensionProvider(final String elementName, final String namespace)
    '''
def getExtensionProviders():
    '''    public Collection<Object> getExtensionProviders()
    '''
