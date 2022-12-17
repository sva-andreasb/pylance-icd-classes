TYPE_PROPERTY = "String  \"constraintType\""
FROM_ACTIVITY_PROPERTY = "String  \"fromActivity\""
TO_ACTIVITY_PROPERTY = "String  \"toActivity\""
FROM_ACTIVITY_ID_PROPERTY = "String  \"fromActivityID\""
TO_ACTIVITY_ID_PROPERTY = "String  \"toActivityID\""
def ():
    '''returns IlvTableConstraint\n\n
    (final IlvActivity ilvActivity, final IlvActivity ilvActivity2, final IlvConstraintType ilvConstraintType)\n
    '''
def getFromActivity():
    '''returns IlvActivity\n\n
    getFromActivity()\n
    '''
def getToActivity():
    '''returns IlvActivity\n\n
    getToActivity()\n
    '''
def getType():
    '''returns IlvConstraintType\n\n
    getType()\n
    '''
def setType():
    '''returns None\n\n
    setType(final IlvConstraintType type)\n
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
