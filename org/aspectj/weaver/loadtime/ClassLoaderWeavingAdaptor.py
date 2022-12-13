def ClassLoaderWeavingAdaptor():
    '''    public ClassLoaderWeavingAdaptor()
    public ClassLoaderWeavingAdaptor(final ClassLoader deprecatedLoader, final IWeavingContext deprecatedContext)
    '''
def initialize():
    '''    public void initialize(final ClassLoader classLoader, final IWeavingContext context)
    '''
def getContextId():
    '''    public String getContextId()
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def generatedClassesExistFor():
    '''    public boolean generatedClassesExistFor(final String className)
    '''
def flushGeneratedClasses():
    '''    public void flushGeneratedClasses()
    '''
def acceptClass():
    '''    public void acceptClass(final String name, final byte[] originalBytes, final byte[] wovenBytes)
    '''
