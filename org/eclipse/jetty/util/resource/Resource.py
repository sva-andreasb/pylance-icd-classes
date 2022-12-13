def setDefaultUseCaches():
    '''public static void setDefaultUseCaches(final boolean useCaches)
    '''
def getDefaultUseCaches():
    '''public static boolean getDefaultUseCaches()
    '''
def newResource():
    '''public static Resource newResource(final URI uri)
    public static Resource newResource(final URL url)
    public static Resource newResource(final String resource)
    public static Resource newResource(String resource, final boolean useCaches)
    public static Resource newResource(File file)
    '''
def newSystemResource():
    '''public static Resource newSystemResource(final String resource)
    '''
def newClassPathResource():
    '''public static Resource newClassPathResource(final String resource)
    public static Resource newClassPathResource(final String name, final boolean useCaches, final boolean checkParents)
    '''
def isContainedIn():
    '''public static boolean isContainedIn(final Resource r, final Resource containingResource)
    '''
def getURI():
    '''public URI getURI()
    '''
def getResource():
    '''public Resource getResource(final String path)
    '''
def encode():
    '''public String encode(final String uri)
    '''
def getAssociate():
    '''public Object getAssociate()
    '''
def setAssociate():
    '''public void setAssociate(final Object o)
    '''
def getAlias():
    '''public URL getAlias()
    '''
def getListHTML():
    '''public String getListHTML(String base, final boolean parent)
    '''
def writeTo():
    '''public void writeTo(final OutputStream out, final long start, final long count)
    '''
def copyTo():
    '''public void copyTo(final File destination)
    '''
def toURL():
    '''public static URL toURL(final File file)
    '''
