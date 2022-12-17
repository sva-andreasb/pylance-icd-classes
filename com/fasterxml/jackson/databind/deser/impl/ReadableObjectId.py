def ():
    '''returns Referring\n\n
    (final ObjectIdGenerator.IdKey key)\n
    (final UnresolvedForwardReference ref, final Class<?> beanType)\n
    (final UnresolvedForwardReference ref, final JavaType beanType)\n
    '''
def setResolver():
    '''returns None\n\n
    setResolver(final ObjectIdResolver resolver)\n
    '''
def appendReferring():
    '''returns None\n\n
    appendReferring(final Referring currentReferring)\n
    '''
def bindItem():
    '''returns None\n\n
    bindItem(final Object ob)\n
    '''
def resolve():
    '''returns Object\n\n
    resolve()\n
    '''
def hasReferringProperties():
    '''returns boolean\n\n
    hasReferringProperties()\n
    '''
def referringProperties():
    '''returns Iterator<Referring>\n\n
    referringProperties()\n
    '''
def tryToResolveUnresolved():
    '''returns boolean\n\n
    tryToResolveUnresolved(final DeserializationContext ctxt)\n
    '''
def getResolver():
    '''returns ObjectIdResolver\n\n
    getResolver()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getLocation():
    '''returns JsonLocation\n\n
    getLocation()\n
    '''
def hasId():
    '''returns boolean\n\n
    hasId(final Object id)\n
    '''
