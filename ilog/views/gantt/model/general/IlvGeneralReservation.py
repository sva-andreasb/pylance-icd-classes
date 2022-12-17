ACTIVITY_PROPERTY = "String  \"activity\""
RESOURCE_PROPERTY = "String  \"resource\""
def ():
    '''returns IlvGeneralReservation\n\n
    (final IlvResource ilvResource, final IlvActivity ilvActivity)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String key)\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String key, final Object obj)\n
    '''
def propertyNameIterator():
    '''returns Iterator<String>\n\n
    propertyNameIterator()\n
    '''
def getPropertyNames():
    '''returns Collection<String>\n\n
    getPropertyNames()\n
    '''
def isUserProperty():
    '''returns boolean\n\n
    isUserProperty(final String anObject)\n
    '''
def createReservation():
    '''returns IlvReservation\n\n
    createReservation(final IlvResource ilvResource, final IlvActivity ilvActivity)\n
    '''
