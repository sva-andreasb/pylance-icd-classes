TYPE_PROPERTY = "String  \"constraintType\""
FROM_ACTIVITY_PROPERTY = "String  \"fromActivity\""
TO_ACTIVITY_PROPERTY = "String  \"toActivity\""
def ():
    '''returns IlvGeneralConstraint\n\n
    (final IlvActivity ilvActivity, final IlvActivity ilvActivity2, final IlvConstraintType ilvConstraintType)\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String s)\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String s, final Object obj)\n
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
def createConstraint():
    '''returns IlvConstraint\n\n
    createConstraint(final IlvActivity ilvActivity, final IlvActivity ilvActivity2, final IlvConstraintType ilvConstraintType)\n
    '''
