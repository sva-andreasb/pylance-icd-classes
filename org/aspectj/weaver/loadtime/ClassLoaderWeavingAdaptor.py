def ():
    '''returns ClassLoaderWeavingAdaptor\n\n
    ()\n
    (final ClassLoader deprecatedLoader, final IWeavingContext deprecatedContext)\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final ClassLoader classLoader, final IWeavingContext context)\n
    '''
def getContextId():
    '''returns String\n\n
    getContextId()\n
    '''
def getNamespace():
    '''returns String\n\n
    getNamespace()\n
    '''
def generatedClassesExistFor():
    '''returns boolean\n\n
    generatedClassesExistFor(final String className)\n
    '''
def flushGeneratedClasses():
    '''returns None\n\n
    flushGeneratedClasses()\n
    '''
def acceptClass():
    '''returns None\n\n
    acceptClass(final String name, final byte[] originalBytes, final byte[] wovenBytes)\n
    '''
