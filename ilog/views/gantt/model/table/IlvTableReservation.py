ACTIVITY_PROPERTY = "String  \"activity\""
RESOURCE_PROPERTY = "String  \"resource\""
ACTIVITY_ID_PROPERTY = "String  \"activityID\""
RESOURCE_ID_PROPERTY = "String  \"resourceID\""
def ():
    '''returns IlvTableReservation\n\n
    (final IlvResource ilvResource, final IlvActivity ilvActivity)\n
    '''
def getActivity():
    '''returns IlvActivity\n\n
    getActivity()\n
    '''
def getResource():
    '''returns IlvResource\n\n
    getResource()\n
    '''
def setResource():
    '''returns None\n\n
    setResource(final IlvResource resource)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String s, final Object o)\n
    '''
def propertyNameIterator():
    '''returns Iterator<String>\n\n
    propertyNameIterator()\n
    '''
def isUserProperty():
    '''returns boolean\n\n
    isUserProperty(final String anObject)\n
    '''
