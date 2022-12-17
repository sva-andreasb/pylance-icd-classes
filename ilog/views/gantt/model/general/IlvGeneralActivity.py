ID_PROPERTY = "String  \"id\""
NAME_PROPERTY = "String  \"name\""
DURATION_PROPERTY = "String  \"duration\""
TIME_INTERVAL_PROPERTY = "String  \"timeInterval\""
def ():
    '''returns Factory\n\n
    (final String s, final String s2, final IlvTimeInterval ilvTimeInterval)\n
    (final String s, final String s2, final Date date, final Date date2)\n
    (final String s, final String s2, final Date date, final IlvDuration ilvDuration)\n
    ()\n
    '''
def setTimeProperties():
    '''returns None\n\n
    setTimeProperties(final String[] a)\n
    '''
def setTimeInterval():
    '''returns None\n\n
    setTimeInterval(final IlvTimeInterval timeInterval)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String anObject)\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String s, final Object o)\n
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
def createActivity():
    '''returns IlvActivity\n\n
    createActivity(final IlvTimeInterval ilvTimeInterval)\n
    '''
