def setDefaultUseCaches():
'''public static void setDefaultUseCaches(final boolean useCaches)
'''
pass
def getDefaultUseCaches():
'''public static boolean getDefaultUseCaches()
'''
pass
def newResource():
'''public static Resource newResource(final URI uri)
public static Resource newResource(final URL url)
public static Resource newResource(final String resource)
public static Resource newResource(String resource, final boolean useCaches)
public static Resource newResource(File file)
'''
pass
def newSystemResource():
'''public static Resource newSystemResource(final String resource)
'''
pass
def newClassPathResource():
'''public static Resource newClassPathResource(final String resource)
public static Resource newClassPathResource(final String name, final boolean useCaches, final boolean checkParents)
'''
pass
def isContainedIn():
'''public static boolean isContainedIn(final Resource r, final Resource containingResource)
'''
pass
def getURI():
'''public URI getURI()
'''
pass
def getResource():
'''public Resource getResource(final String path)
'''
pass
def encode():
'''public String encode(final String uri)
'''
pass
def getAssociate():
'''public Object getAssociate()
'''
pass
def setAssociate():
'''public void setAssociate(final Object o)
'''
pass
def getAlias():
'''public URL getAlias()
'''
pass
def getListHTML():
'''public String getListHTML(String base, final boolean parent)
'''
pass
def writeTo():
'''public void writeTo(final OutputStream out, final long start, final long count)
'''
pass
def copyTo():
'''public void copyTo(final File destination)
'''
pass
def toURL():
'''public static URL toURL(final File file)
'''
pass
