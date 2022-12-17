def ():
    '''returns SimpleFilterProvider\n\n
    ()\n
    (final Map<String, ?> mapping)\n
    '''
def setDefaultFilter():
    '''returns SimpleFilterProvider\n\n
    setDefaultFilter(final BeanPropertyFilter f)\n
    setDefaultFilter(final PropertyFilter f)\n
    setDefaultFilter(final SimpleBeanPropertyFilter f)\n
    '''
def getDefaultFilter():
    '''returns PropertyFilter\n\n
    getDefaultFilter()\n
    '''
def setFailOnUnknownId():
    '''returns SimpleFilterProvider\n\n
    setFailOnUnknownId(final boolean state)\n
    '''
def willFailOnUnknownId():
    '''returns boolean\n\n
    willFailOnUnknownId()\n
    '''
def addFilter():
    '''returns SimpleFilterProvider\n\n
    addFilter(final String id, final BeanPropertyFilter filter)\n
    addFilter(final String id, final PropertyFilter filter)\n
    addFilter(final String id, final SimpleBeanPropertyFilter filter)\n
    '''
def removeFilter():
    '''returns PropertyFilter\n\n
    removeFilter(final String id)\n
    '''
def findFilter():
    '''returns BeanPropertyFilter\n\n
    findFilter(final Object filterId)\n
    '''
def findPropertyFilter():
    '''returns PropertyFilter\n\n
    findPropertyFilter(final Object filterId, final Object valueToFilter)\n
    '''
