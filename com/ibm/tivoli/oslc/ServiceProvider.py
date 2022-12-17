def ():
    '''returns Publisher\n\n
    (final String uri)\n
    (final String uri, final boolean member)\n
    (final String domURI)\n
    (final String uri, final Set<String> resourceTypes, final Set<String> usage, final String title, final Set<String> resourceShapes)\n
    (final String name, final String title, final String uri)\n
    '''
def addPrefixDefinition():
    '''returns None\n\n
    addPrefixDefinition(final String prefix, final String uri)\n
    '''
def setPrefixDefinitions():
    '''returns None\n\n
    setPrefixDefinitions(final Map<String, String> prefixNsMap)\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String title)\n
    '''
def setPublisher():
    '''returns None\n\n
    setPublisher(final Publisher publisher)\n
    '''
def setDescription():
    '''returns None\n\n
    setDescription(final String description)\n
    '''
def addService():
    '''returns None\n\n
    addService(final Service service)\n
    '''
def setServices():
    '''returns None\n\n
    setServices(final List<Service> serviceList)\n
    '''
def asRDFModel():
    '''returns Model\n\n
    asRDFModel()\n
    '''
def addAsCollectionMember():
    '''returns None\n\n
    addAsCollectionMember(final Resource collection)\n
    '''
def addCreationDialog():
    '''returns None\n\n
    addCreationDialog(final String uri, final Set<String> resourceTypes, final Set<String> usage, final Set<String> shapes, final String title)\n
    '''
def addSelectionDialog():
    '''returns None\n\n
    addSelectionDialog(final String uri, final Set<String> resourceTypes, final Set<String> usage, final Set<String> shapes, final String title)\n
    '''
def addCreationFactory():
    '''returns None\n\n
    addCreationFactory(final String uri, final Set<String> resourceTypes, final Set<String> usage, final Set<String> shapes, final String title)\n
    '''
def addQueryCapability():
    '''returns None\n\n
    addQueryCapability(final String uri, final Set<String> resourceTypes, final Set<String> usage, final Set<String> shapes, final String title)\n
    '''
