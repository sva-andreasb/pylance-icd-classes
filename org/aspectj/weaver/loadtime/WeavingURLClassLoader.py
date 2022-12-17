WEAVING_CLASS_PATH = "String  \"aj.class.path\""
WEAVING_ASPECT_PATH = "String  \"aj.aspect.path\""
def ():
    '''returns WeavingURLClassLoader\n\n
    (final ClassLoader parent)\n
    (final URL[] urls, final ClassLoader parent)\n
    (final URL[] classURLs, final URL[] aspectURLs, final ClassLoader parent)\n
    '''
def getClassLoaderName():
    '''returns String\n\n
    getClassLoaderName()\n
    '''
def getAspectURLs():
    '''returns URL[]\n\n
    getAspectURLs()\n
    '''
def acceptClass():
    '''returns None\n\n
    acceptClass(final String name, final byte[] classBytes, final byte[] weavedBytes)\n
    '''
