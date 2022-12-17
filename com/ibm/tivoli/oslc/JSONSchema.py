def ():
    '''returns JSONSchema\n\n
    ()\n
    (final boolean orderNeeded, final boolean sortAsc, final boolean oasSchemaCompliance)\n
    (final String id, final boolean oasSchemaCompliance)\n
    (final String schemaURIVer, final boolean orderNeeded, final boolean sortAsc, final boolean oasSchemaCompliance)\n
    (final JSONObject obj, final boolean oasSchemaCompliance)\n
    (final String schemaURI, final String title, final String description, final String type, final boolean oasSchemaCompliance)\n
    (final String schemaURI, final String title, final String description, final String type, final boolean orderNeeded, final boolean sortAsc, final boolean oasSchemaCompliance)\n
    '''
def addExtendedSchema():
    '''returns JSONSchema\n\n
    addExtendedSchema(final String key, final JSONObject jo)\n
    '''
def isItem():
    '''returns JSONSchema\n\n
    isItem(final boolean isItem)\n
    '''
def isOrderNeeded():
    '''returns boolean\n\n
    isOrderNeeded()\n
    '''
def getTermSchemaURI():
    '''returns String\n\n
    getTermSchemaURI()\n
    '''
def schemaURI():
    '''returns JSONSchema\n\n
    schemaURI(final String schemaURI)\n
    '''
def getTermTitle():
    '''returns String\n\n
    getTermTitle()\n
    '''
def title():
    '''returns JSONSchema\n\n
    title(final String title)\n
    '''
def getTermDescription():
    '''returns String\n\n
    getTermDescription()\n
    '''
def descripton():
    '''returns JSONSchema\n\n
    descripton(final String description)\n
    '''
def resource():
    '''returns JSONSchema\n\n
    resource(final String resource)\n
    '''
def getTermType():
    '''returns String\n\n
    getTermType()\n
    '''
def type():
    '''returns JSONSchema\n\n
    type(final String type)\n
    '''
def getTermRef():
    '''returns String\n\n
    getTermRef()\n
    '''
def ref():
    '''returns JSONSchema\n\n
    ref(final String ref)\n
    '''
def getTermSubType():
    '''returns String\n\n
    getTermSubType()\n
    '''
def setTermSubType():
    '''returns JSONSchema\n\n
    setTermSubType(final String termSubType)\n
    '''
def getTermDefinition():
    '''returns JSONObject\n\n
    getTermDefinition()\n
    '''
def addTermDefinition():
    '''returns JSONSchema\n\n
    addTermDefinition(final JSONObject termDefinition)\n
    '''
def addTermSubDefinition():
    '''returns JSONSchema\n\n
    addTermSubDefinition(final String subSchemaName, final Object subSchema)\n
    '''
def getRequired():
    '''returns JSONArray\n\n
    getRequired()\n
    '''
def addSubRequired():
    '''returns JSONSchema\n\n
    addSubRequired(final String requiredItem)\n
    '''
def addRequired():
    '''returns JSONSchema\n\n
    addRequired(final JSONArray required)\n
    '''
def getPK():
    '''returns JSONArray\n\n
    getPK()\n
    '''
def addPrimaryKey():
    '''returns JSONSchema\n\n
    addPrimaryKey(final String pkName)\n
    '''
def addPrimaryKeys():
    '''returns JSONSchema\n\n
    addPrimaryKeys(final JSONArray pk)\n
    '''
def addProperty():
    '''returns JSONSchema\n\n
    addProperty(final JSONProperty jp)\n
    '''
def removeProperty():
    '''returns None\n\n
    removeProperty(final String propName)\n
    '''
def getProperty():
    '''returns JSONSchema\n\n
    getProperty(final String propName)\n
    '''
def addItem():
    '''returns JSONSchema\n\n
    addItem(final JSONSchema js)\n
    '''
def build():
    '''returns JSONObject\n\n
    build()\n
    '''
def schemaPrinter():
    '''returns None\n\n
    schemaPrinter()\n
    '''
def toJSONByte():
    '''returns byte[]\n\n
    toJSONByte()\n
    '''
def toJSON():
    '''returns JSONObject\n\n
    toJSON()\n
    '''
def isOasSchemaCompliance():
    '''returns boolean\n\n
    isOasSchemaCompliance()\n
    '''
