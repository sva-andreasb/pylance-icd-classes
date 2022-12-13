IS_THE_SAME_CLASS = "int  0"
ON_DIFFERENT_INHERITANCE_PATH = "int  1"
ON_LOWER_INHERITANCE_HIERARCHY = "int  2"
ON_HIGHER_INHERITANCE_HIERARCHY = "int  3"
def getInstance():
    '''    public static synchronized MetadataCache getInstance(final Connection conn)
    public static synchronized MetadataCache getInstance(final Connection conn, final boolean forceRefresh)
    '''
def writeLock():
    '''    public void writeLock()
    '''
def writeUnlock():
    '''    public void writeUnlock()
    '''
def isRelated():
    '''    public int isRelated(final byte[] class1, final byte[] class2)
    '''
def getDerivedClasses():
    '''    public Guid[] getDerivedClasses(final byte[] classGUID)
    public ArrayList getDerivedClasses(final Guid classGUID)
    '''
def getAllClassTypes():
    '''    public HashMap[] getAllClassTypes()
    '''
def getClassType():
    '''    public HashMap[] getClassType(final Guid clazz)
    '''
def buildShortName():
    '''    public static String buildShortName(final String className)
    '''
def isDuplicateClass():
    '''    public static boolean isDuplicateClass(final String className)
    '''
def isValidClassType():
    '''    public boolean isValidClassType(final Guid classType)
    '''
def isDesiredClassType():
    '''    public boolean isDesiredClassType(final String classType)
    '''
def isDesiredRelationshipType():
    '''    public boolean isDesiredRelationshipType(final String relationship)
    '''
def isDesiredAttribute():
    '''    public boolean isDesiredAttribute(final String className, final String attName)
    '''
def isValidDesiredAttributeType():
    '''    public boolean isValidDesiredAttributeType(final String attributeType)
    '''
def getParentsOfClass():
    '''    public ArrayList getParentsOfClass(final Guid classGUID)
    '''
def getParentsOfInterface():
    '''    public ArrayList getParentsOfInterface(final byte[] interfaceGUID)
    '''
def isDerivedClass():
    '''    public boolean isDerivedClass(final Guid class1, final Guid class2)
    '''
def isValidInterfaceType():
    '''    public boolean isValidInterfaceType(final Guid interfaceGUID)
    '''
def getDesiredClasses():
    '''    public HashMap getDesiredClasses()
    '''
def getDesiredAttributes():
    '''    public HashMap getDesiredAttributes(final String className)
    '''
