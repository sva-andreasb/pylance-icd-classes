IS_THE_SAME_CLASS = "int  0"
ON_DIFFERENT_INHERITANCE_PATH = "int  1"
ON_LOWER_INHERITANCE_HIERARCHY = "int  2"
ON_HIGHER_INHERITANCE_HIERARCHY = "int  3"
def writeLock():
    '''returns None\n\n
    writeLock()\n
    '''
def writeUnlock():
    '''returns None\n\n
    writeUnlock()\n
    '''
def isRelated():
    '''returns int\n\n
    isRelated(final byte[] class1, final byte[] class2)\n
    '''
def getDerivedClasses():
    '''returns ArrayList\n\n
    getDerivedClasses(final byte[] classGUID)\n
    getDerivedClasses(final Guid classGUID)\n
    '''
def getAllClassTypes():
    '''returns HashMap[]\n\n
    getAllClassTypes()\n
    '''
def getClassType():
    '''returns HashMap[]\n\n
    getClassType(final Guid clazz)\n
    '''
def isValidClassType():
    '''returns boolean\n\n
    isValidClassType(final Guid classType)\n
    '''
def isDesiredClassType():
    '''returns boolean\n\n
    isDesiredClassType(final String classType)\n
    '''
def isDesiredRelationshipType():
    '''returns boolean\n\n
    isDesiredRelationshipType(final String relationship)\n
    '''
def isDesiredAttribute():
    '''returns boolean\n\n
    isDesiredAttribute(final String className, final String attName)\n
    '''
def isValidDesiredAttributeType():
    '''returns boolean\n\n
    isValidDesiredAttributeType(final String attributeType)\n
    '''
def getParentsOfClass():
    '''returns ArrayList\n\n
    getParentsOfClass(final Guid classGUID)\n
    '''
def getParentsOfInterface():
    '''returns ArrayList\n\n
    getParentsOfInterface(final byte[] interfaceGUID)\n
    '''
def isDerivedClass():
    '''returns boolean\n\n
    isDerivedClass(final Guid class1, final Guid class2)\n
    '''
def isValidInterfaceType():
    '''returns boolean\n\n
    isValidInterfaceType(final Guid interfaceGUID)\n
    '''
def getDesiredClasses():
    '''returns HashMap\n\n
    getDesiredClasses()\n
    '''
def getDesiredAttributes():
    '''returns HashMap\n\n
    getDesiredAttributes(final String className)\n
    '''
