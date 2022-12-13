def get():
    '''public static SchemaTypeSystem get()
    '''
def getName():
    '''public String getName()
    '''
def isNamespaceDefined():
    '''public boolean isNamespaceDefined(final String namespace)
    '''
def findType():
    '''public SchemaType findType(final QName name)
    '''
def findDocumentType():
    '''public SchemaType findDocumentType(final QName name)
    '''
def findAttributeType():
    '''public SchemaType findAttributeType(final QName name)
    '''
def findElement():
    '''public SchemaGlobalElement findElement(final QName name)
    '''
def findAttribute():
    '''public SchemaGlobalAttribute findAttribute(final QName name)
    '''
def typeForClassname():
    '''public SchemaType typeForClassname(final String classname)
    '''
def getSourceAsStream():
    '''public InputStream getSourceAsStream(final String sourceName)
    '''
def globalTypes():
    '''public SchemaType[] globalTypes()
    '''
def documentTypes():
    '''public SchemaType[] documentTypes()
    '''
def attributeTypes():
    '''public SchemaType[] attributeTypes()
    '''
def globalElements():
    '''public SchemaGlobalElement[] globalElements()
    '''
def globalAttributes():
    '''public SchemaGlobalAttribute[] globalAttributes()
    '''
def modelGroups():
    '''public SchemaModelGroup[] modelGroups()
    '''
def attributeGroups():
    '''public SchemaAttributeGroup[] attributeGroups()
    '''
def annotations():
    '''public SchemaAnnotation[] annotations()
    '''
def handleForType():
    '''public String handleForType(final SchemaType type)
    '''
def getClassLoader():
    '''public ClassLoader getClassLoader()
    '''
def saveToDirectory():
    '''public void saveToDirectory(final File classDir)
    '''
def save():
    '''public void save(final Filer filer)
    '''
def resolve():
    '''public void resolve()
    '''
def typeForHandle():
    '''public SchemaType typeForHandle(final String handle)
    '''
def resolveHandle():
    '''public SchemaComponent resolveHandle(final String handle)
    '''
def fillInType():
    '''public void fillInType(final int btc)
    '''
def getNoType():
    '''public static SchemaType getNoType()
    '''
