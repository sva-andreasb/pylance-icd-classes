SOAPENC = "String  \"http://schemas.xmlsoap.org/soap/encoding/\""
SOAP_ARRAY = "String  \"Array\""
ARRAY_TYPE = "String  \"arrayType\""
def getName():
    '''returns String\n\n
    getName()\n
    '''
def findType():
    '''returns SchemaType\n\n
    findType(final QName qName)\n
    '''
def findDocumentType():
    '''returns SchemaType\n\n
    findDocumentType(final QName qName)\n
    '''
def findAttributeType():
    '''returns SchemaType\n\n
    findAttributeType(final QName qName)\n
    '''
def findElement():
    '''returns SchemaGlobalElement\n\n
    findElement(final QName qName)\n
    '''
def findAttribute():
    '''returns SchemaGlobalAttribute\n\n
    findAttribute(final QName qName)\n
    '''
def findModelGroup():
    '''returns SchemaModelGroup\n\n
    findModelGroup(final QName qName)\n
    '''
def findAttributeGroup():
    '''returns SchemaAttributeGroup\n\n
    findAttributeGroup(final QName qName)\n
    '''
def isNamespaceDefined():
    '''returns boolean\n\n
    isNamespaceDefined(final String string)\n
    '''
def typeForClassname():
    '''returns SchemaType\n\n
    typeForClassname(final String string)\n
    '''
def getSourceAsStream():
    '''returns InputStream\n\n
    getSourceAsStream(final String string)\n
    '''
def getClassLoader():
    '''returns ClassLoader\n\n
    getClassLoader()\n
    '''
def resolve():
    '''returns None\n\n
    resolve()\n
    '''
def globalTypes():
    '''returns SchemaType[]\n\n
    globalTypes()\n
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
def attributeGroups():
    '''returns SchemaAttributeGroup[]\n\n
    attributeGroups()\n
    '''
def annotations():
    '''returns SchemaAnnotation[]\n\n
    annotations()\n
    '''
def handleForType():
    '''returns String\n\n
    handleForType(final SchemaType type)\n
    '''
def resolveHandle():
    '''returns SchemaComponent\n\n
    resolveHandle(final String string)\n
    '''
def typeForHandle():
    '''returns SchemaType\n\n
    typeForHandle(final String string)\n
    '''
def saveToDirectory():
    '''returns None\n\n
    saveToDirectory(final File file)\n
    '''
def save():
    '''returns None\n\n
    save(final Filer filer)\n
    '''
