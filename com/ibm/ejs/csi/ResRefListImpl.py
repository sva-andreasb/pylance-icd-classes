def ():
    '''returns ResRefListImpl\n\n
    (final List<ResRef> list)\n
    (final String beanName, final EnterpriseBean eb, final EnterpriseBeanBinding ebb, final EnterpriseBeanExtension ebx)\n
    (final WebApp webApp, final WebAppExtension webAppExt)\n
    (final WebApp webApp, final WebAppExtension webAppExt, final WebAppBinding web_bindings)\n
    '''
def findByName():
    '''returns ResRef\n\n
    findByName(final String s)\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
def get():
    '''returns ResRef\n\n
    get(final int i)\n
    '''
def setLookupString():
    '''returns None\n\n
    setLookupString(final String lookUp)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def completeInitialization():
    '''returns None\n\n
    completeInitialization()\n
    '''
def setToUnintialized():
    '''returns None\n\n
    setToUnintialized()\n
    '''
def isInitialized():
    '''returns boolean\n\n
    isInitialized()\n
    '''
def add():
    '''returns None\n\n
    add(final String name, final String jndiName, final String classType, final Resource.AuthenticationType resAuthType, final boolean sharable, final String description)\n
    '''
def addEjbResourceRefType():
    '''returns None\n\n
    addEjbResourceRefType(final List<ResourceRefType> rrtList)\n
    '''
def addWebModuleResRef():
    '''returns None\n\n
    addWebModuleResRef(final ResourceRefBinding binding)\n
    '''
