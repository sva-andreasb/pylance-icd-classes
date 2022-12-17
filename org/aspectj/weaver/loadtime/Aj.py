def ():
    '''returns ExplicitlyInitializedClassLoaderWeavingAdaptor\n\n
    ()\n
    (final IWeavingContext context)\n
    (final ClassLoader loader)\n
    (final ClassLoaderWeavingAdaptor weavingAdaptor)\n
    '''
def initialize():
    '''returns None\n\n
    initialize()\n
    '''
def preProcess():
    '''returns byte[]\n\n
    preProcess(final String className, final byte[] bytes, final ClassLoader loader, final ProtectionDomain protectionDomain)\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace(final ClassLoader loader)\n
    '''
def generatedClassesExist():
    '''returns boolean\n\n
    generatedClassesExist(final ClassLoader loader)\n
    '''
def flushGeneratedClasses():
    '''returns None\n\n
    flushGeneratedClasses(final ClassLoader loader)\n
    '''
def getClassLoader():
    '''returns ClassLoader\n\n
    getClassLoader()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getWeavingAdaptor():
    '''returns ClassLoaderWeavingAdaptor\n\n
    getWeavingAdaptor(final ClassLoader loader, final IWeavingContext weavingContext)\n
    '''
