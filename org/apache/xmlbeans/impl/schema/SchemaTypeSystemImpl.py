DATA_BABE = "int  -629491010"
MAJOR_VERSION = "int  2"
MINOR_VERSION = "int  24"
RELEASE_NUMBER = "int  0"
FILETYPE_SCHEMAINDEX = "int  1"
FILETYPE_SCHEMATYPE = "int  2"
FILETYPE_SCHEMAELEMENT = "int  3"
FILETYPE_SCHEMAATTRIBUTE = "int  4"
FILETYPE_SCHEMAPOINTER = "int  5"
FILETYPE_SCHEMAMODELGROUP = "int  6"
FILETYPE_SCHEMAATTRIBUTEGROUP = "int  7"
FILETYPE_SCHEMAIDENTITYCONSTRAINT = "int  8"
FLAG_PART_SKIPPABLE = "int  1"
FLAG_PART_FIXED = "int  4"
FLAG_PART_NILLABLE = "int  8"
FLAG_PART_BLOCKEXT = "int  16"
FLAG_PART_BLOCKREST = "int  32"
FLAG_PART_BLOCKSUBST = "int  64"
FLAG_PART_ABSTRACT = "int  128"
FLAG_PART_FINALEXT = "int  256"
FLAG_PART_FINALREST = "int  512"
FLAG_PROP_ISATTR = "int  1"
FLAG_PROP_JAVASINGLETON = "int  2"
FLAG_PROP_JAVAOPTIONAL = "int  4"
FLAG_PROP_JAVAARRAY = "int  8"
FIELD_NONE = "int  0"
FIELD_GLOBAL = "int  1"
FIELD_LOCALATTR = "int  2"
FIELD_LOCALELT = "int  3"
def ():
    '''returns XsbReader\n\n
    (final Class indexclass)\n
    (final ResourceLoader resourceLoader, final String name, final SchemaTypeLoader linker)\n
    (String nameForSystem)\n
    (final String handle, final int filetype)\n
    '''
def loadFromBuilder():
    '''returns None\n\n
    loadFromBuilder(final SchemaGlobalElement[] globalElements, final SchemaGlobalAttribute[] globalAttributes, final SchemaType[] globalTypes, final SchemaType[] documentTypes, final SchemaType[] attributeTypes)\n
    '''
def loadFromStscState():
    '''returns None\n\n
    loadFromStscState(final StscState state)\n
    '''
def isIncomplete():
    '''returns boolean\n\n
    isIncomplete()\n
    '''
def saveToDirectory():
    '''returns None\n\n
    saveToDirectory(final File classDir)\n
    '''
def save():
    '''returns None\n\n
    save(final Filer filer)\n
    '''
def saveGlobalElements():
    '''returns None\n\n
    saveGlobalElements(final SchemaGlobalElement[] elts)\n
    '''
def saveGlobalAttributes():
    '''returns None\n\n
    saveGlobalAttributes(final SchemaGlobalAttribute[] attrs)\n
    '''
def saveModelGroups():
    '''returns None\n\n
    saveModelGroups(final SchemaModelGroup[] groups)\n
    '''
def saveAttributeGroups():
    '''returns None\n\n
    saveAttributeGroups(final SchemaAttributeGroup[] groups)\n
    '''
def saveIdentityConstraints():
    '''returns None\n\n
    saveIdentityConstraints(final SchemaIdentityConstraint[] idcs)\n
    '''
def saveGlobalElement():
    '''returns None\n\n
    saveGlobalElement(final SchemaGlobalElement elt)\n
    '''
def saveGlobalAttribute():
    '''returns None\n\n
    saveGlobalAttribute(final SchemaGlobalAttribute attr)\n
    '''
def saveModelGroup():
    '''returns None\n\n
    saveModelGroup(final SchemaModelGroup grp)\n
    '''
def saveAttributeGroup():
    '''returns None\n\n
    saveAttributeGroup(final SchemaAttributeGroup grp)\n
    '''
def saveIdentityConstraint():
    '''returns None\n\n
    saveIdentityConstraint(final SchemaIdentityConstraint idc)\n
    '''
def typeForHandle():
    '''returns SchemaType\n\n
    typeForHandle(final String handle)\n
    '''
def typeForClassname():
    '''returns SchemaType\n\n
    typeForClassname(final String classname)\n
    '''
def resolveHandle():
    '''returns SchemaComponent\n\n
    resolveHandle(final String handle)\n
    '''
def resolve():
    '''returns None\n\n
    resolve()\n
    '''
def isNamespaceDefined():
    '''returns boolean\n\n
    isNamespaceDefined(final String namespace)\n
    '''
def globalTypes():
    '''returns SchemaType[]\n\n
    globalTypes()\n
    '''
def redefinedGlobalTypes():
    '''returns SchemaType[]\n\n
    redefinedGlobalTypes()\n
    '''
def getSourceAsStream():
    '''returns InputStream\n\n
    getSourceAsStream(String sourceName)\n
    '''
def documentTypes():
    '''returns SchemaType[]\n\n
    documentTypes()\n
    '''
def attributeTypes():
    '''returns SchemaType[]\n\n
    attributeTypes()\n
    '''
def globalElements():
    '''returns SchemaGlobalElement[]\n\n
    globalElements()\n
    '''
def globalAttributes():
    '''returns SchemaGlobalAttribute[]\n\n
    globalAttributes()\n
    '''
def modelGroups():
    '''returns SchemaModelGroup[]\n\n
    modelGroups()\n
    '''
def redefinedModelGroups():
    '''returns SchemaModelGroup[]\n\n
    redefinedModelGroups()\n
    '''
def attributeGroups():
    '''returns SchemaAttributeGroup[]\n\n
    attributeGroups()\n
    '''
def redefinedAttributeGroups():
    '''returns SchemaAttributeGroup[]\n\n
    redefinedAttributeGroups()\n
    '''
def annotations():
    '''returns SchemaAnnotation[]\n\n
    annotations()\n
    '''
def identityConstraints():
    '''returns SchemaIdentityConstraint[]\n\n
    identityConstraints()\n
    '''
def getClassLoader():
    '''returns ClassLoader\n\n
    getClassLoader()\n
    '''
def handleForType():
    '''returns String\n\n
    handleForType(final SchemaType type)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def typeSystemForName():
    '''returns SchemaTypeSystem\n\n
    typeSystemForName(final String name)\n
    '''
def finishLoadingElement():
    '''returns SchemaGlobalElement\n\n
    finishLoadingElement()\n
    '''
def finishLoadingAttribute():
    '''returns SchemaGlobalAttribute\n\n
    finishLoadingAttribute()\n
    '''
def finishLoadingType():
    '''returns SchemaType\n\n
    finishLoadingType()\n
    '''
