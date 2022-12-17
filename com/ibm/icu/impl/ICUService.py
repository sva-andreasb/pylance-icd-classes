def ():
    '''returns SimpleFactory\n\n
    ()\n
    (final String name)\n
    (final String id)\n
    (final Object instance, final String id)\n
    (final Object instance, final String id, final boolean visible)\n
    '''
def get():
    '''returns Object\n\n
    get(final String descriptor)\n
    get(final String descriptor, final String[] actualReturn)\n
    '''
def getKey():
    '''returns Object\n\n
    getKey(final Key key)\n
    getKey(final Key key, final String[] actualReturn)\n
    getKey(final Key key, final String[] actualReturn, final Factory factory)\n
    '''
def getVisibleIDs():
    '''returns Set<String>\n\n
    getVisibleIDs()\n
    getVisibleIDs(final String matchID)\n
    '''
def getDisplayName():
    '''returns String\n\n
    getDisplayName(final String id)\n
    getDisplayName(final String id, final ULocale locale)\n
    getDisplayName(final String identifier, final ULocale locale)\n
    '''
def registerObject():
    '''returns Factory\n\n
    registerObject(final Object obj, final String id)\n
    registerObject(final Object obj, final String id, final boolean visible)\n
    '''
def isDefault():
    '''returns boolean\n\n
    isDefault()\n
    '''
def createKey():
    '''returns Key\n\n
    createKey(final String id)\n
    '''
def stats():
    '''returns String\n\n
    stats()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def canonicalID():
    '''returns String\n\n
    canonicalID()\n
    '''
def currentID():
    '''returns String\n\n
    currentID()\n
    '''
def currentDescriptor():
    '''returns String\n\n
    currentDescriptor()\n
    '''
def fallback():
    '''returns boolean\n\n
    fallback()\n
    '''
def isFallbackOf():
    '''returns boolean\n\n
    isFallbackOf(final String idToCheck)\n
    '''
def create():
    '''returns Object\n\n
    create(final Key key, final ICUService service)\n
    '''
def updateVisibleIDs():
    '''returns None\n\n
    updateVisibleIDs(final Map<String, Factory> result)\n
    '''
