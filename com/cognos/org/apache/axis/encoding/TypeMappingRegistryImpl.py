def ():
    '''returns TypeMappingRegistryImpl\n\n
    (final TypeMappingImpl tm)\n
    ()\n
    (final boolean registerDefaults)\n
    '''
def delegate():
    '''returns None\n\n
    delegate(final TypeMappingRegistry secondaryTMR)\n
    '''
def register():
    '''returns TypeMapping\n\n
    register(final String namespaceURI, final TypeMapping mapping)\n
    '''
def registerDefault():
    '''returns None\n\n
    registerDefault(final TypeMapping mapping)\n
    '''
def doRegisterFromVersion():
    '''returns None\n\n
    doRegisterFromVersion(final String version)\n
    '''
def getTypeMapping():
    '''returns TypeMapping\n\n
    getTypeMapping(final String namespaceURI)\n
    '''
def unregisterTypeMapping():
    '''returns TypeMapping\n\n
    unregisterTypeMapping(final String namespaceURI)\n
    '''
def removeTypeMapping():
    '''returns boolean\n\n
    removeTypeMapping(final TypeMapping mapping)\n
    '''
def createTypeMapping():
    '''returns TypeMapping\n\n
    createTypeMapping()\n
    '''
def getRegisteredEncodingStyleURIs():
    '''returns String[]\n\n
    getRegisteredEncodingStyleURIs()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def getDefaultTypeMapping():
    '''returns TypeMapping\n\n
    getDefaultTypeMapping()\n
    '''
