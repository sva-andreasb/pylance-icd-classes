IS_THE_SAME_CLASS = "int  0"
ON_DIFFERENT_INHERITANCE_PATH = "int  1"
ON_LOWER_INHERITANCE_HIERARCHY = "int  2"
ON_HIGHER_INHERITANCE_HIERARCHY = "int  3"
def getInstance():
'''public static synchronized MetadataCache getInstance(final Connection conn)
public static synchronized MetadataCache getInstance(final Connection conn, final boolean forceRefresh)
'''
pass
def writeLock():
'''public void writeLock()
'''
pass
def writeUnlock():
'''public void writeUnlock()
'''
pass
def isRelated():
'''public int isRelated(final byte[] class1, final byte[] class2)
'''
pass
def getDerivedClasses():
'''public Guid[] getDerivedClasses(final byte[] classGUID)
public ArrayList getDerivedClasses(final Guid classGUID)
'''
pass
def getAllClassTypes():
'''public HashMap[] getAllClassTypes()
'''
pass
def getClassType():
'''public HashMap[] getClassType(final Guid clazz)
'''
pass
def buildShortName():
'''public static String buildShortName(final String className)
'''
pass
def isDuplicateClass():
'''public static boolean isDuplicateClass(final String className)
'''
pass
def isValidClassType():
'''public boolean isValidClassType(final Guid classType)
'''
pass
def isDesiredClassType():
'''public boolean isDesiredClassType(final String classType)
'''
pass
def isDesiredRelationshipType():
'''public boolean isDesiredRelationshipType(final String relationship)
'''
pass
def isDesiredAttribute():
'''public boolean isDesiredAttribute(final String className, final String attName)
'''
pass
def isValidDesiredAttributeType():
'''public boolean isValidDesiredAttributeType(final String attributeType)
'''
pass
def getParentsOfClass():
'''public ArrayList getParentsOfClass(final Guid classGUID)
'''
pass
def getParentsOfInterface():
'''public ArrayList getParentsOfInterface(final byte[] interfaceGUID)
'''
pass
def isDerivedClass():
'''public boolean isDerivedClass(final Guid class1, final Guid class2)
'''
pass
def isValidInterfaceType():
'''public boolean isValidInterfaceType(final Guid interfaceGUID)
'''
pass
def getDesiredClasses():
'''public HashMap getDesiredClasses()
'''
pass
def getDesiredAttributes():
'''public HashMap getDesiredAttributes(final String className)
'''
pass
