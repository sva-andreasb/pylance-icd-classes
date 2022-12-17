ID_PROPERTY = "String  \"id\""
NAME_PROPERTY = "String  \"name\""
DURATION_PROPERTY = "String  \"duration\""
TIME_INTERVAL_PROPERTY = "String  \"timeInterval\""
PARENT_ID_PROPERTY = "String  \"parentID\""
def ():
    '''returns IlvTableActivity\n\n
    (final String s, final String s2, final IlvTimeInterval ilvTimeInterval)\n
    (final String s, final String s2, final Date date, final Date date2)\n
    (final String s, final String s2, final Date date, final IlvDuration ilvDuration)\n
    '''
def getID():
    '''returns String\n\n
    getID()\n
    '''
def setID():
    '''returns None\n\n
    setID(final String id)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def setTimeProperties():
    '''returns None\n\n
    setTimeProperties(final String[] array)\n
    '''
def getTimeInterval():
    '''returns IlvTimeInterval\n\n
    getTimeInterval()\n
    '''
def setTimeInterval():
    '''returns None\n\n
    setTimeInterval(final IlvTimeInterval timeInterval)\n
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
