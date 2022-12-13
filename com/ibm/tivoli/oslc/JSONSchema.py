def JSONSchema():
    '''public JSONSchema()
    public JSONSchema(final boolean orderNeeded, final boolean sortAsc, final boolean oasSchemaCompliance)
    public JSONSchema(final String id, final boolean oasSchemaCompliance)
    public JSONSchema(final String schemaURIVer, final boolean orderNeeded, final boolean sortAsc, final boolean oasSchemaCompliance)
    public JSONSchema(final JSONObject obj, final boolean oasSchemaCompliance)
    public JSONSchema(final String schemaURI, final String title, final String description, final String type, final boolean oasSchemaCompliance)
    public JSONSchema(final String schemaURI, final String title, final String description, final String type, final boolean orderNeeded, final boolean sortAsc, final boolean oasSchemaCompliance)
    '''
def addExtendedSchema():
    '''public JSONSchema addExtendedSchema(final String key, final JSONObject jo)
    '''
def isItem():
    '''public JSONSchema isItem(final boolean isItem)
    '''
def isOrderNeeded():
    '''public boolean isOrderNeeded()
    '''
def getTermSchemaURI():
    '''public String getTermSchemaURI()
    '''
def schemaURI():
    '''public JSONSchema schemaURI(final String schemaURI)
    '''
def getTermTitle():
    '''public String getTermTitle()
    '''
def title():
    '''public JSONSchema title(final String title)
    '''
def getTermDescription():
    '''public String getTermDescription()
    '''
def descripton():
    '''public JSONSchema descripton(final String description)
    '''
def resource():
    '''public JSONSchema resource(final String resource)
    '''
def getTermType():
    '''public String getTermType()
    '''
def type():
    '''public JSONSchema type(final String type)
    '''
def getTermRef():
    '''public String getTermRef()
    '''
def ref():
    '''public JSONSchema ref(final String ref)
    '''
def getTermSubType():
    '''public String getTermSubType()
    '''
def setTermSubType():
    '''public JSONSchema setTermSubType(final String termSubType)
    '''
def getTermDefinition():
    '''public JSONObject getTermDefinition()
    '''
def addTermDefinition():
    '''public JSONSchema addTermDefinition(final JSONObject termDefinition)
    '''
def addTermSubDefinition():
    '''public JSONSchema addTermSubDefinition(final String subSchemaName, final Object subSchema)
    '''
def getRequired():
    '''public JSONArray getRequired()
    '''
def addSubRequired():
    '''public JSONSchema addSubRequired(final String requiredItem)
    '''
def addRequired():
    '''public JSONSchema addRequired(final JSONArray required)
    '''
def getPK():
    '''public JSONArray getPK()
    '''
def addPrimaryKey():
    '''public JSONSchema addPrimaryKey(final String pkName)
    '''
def addPrimaryKeys():
    '''public JSONSchema addPrimaryKeys(final JSONArray pk)
    '''
def addProperty():
    '''public JSONSchema addProperty(final JSONProperty jp)
    '''
def removeProperty():
    '''public void removeProperty(final String propName)
    '''
def getProperty():
    '''public JSONSchema getProperty(final String propName)
    '''
def addItem():
    '''public JSONSchema addItem(final JSONSchema js)
    '''
def build():
    '''public JSONObject build()
    '''
def schemaPrinter():
    '''public void schemaPrinter()
    '''
def toJSONByte():
    '''public byte[] toJSONByte()
    '''
def toJSON():
    '''public JSONObject toJSON()
    '''
def main():
    '''public static void main(final String[] args)
    '''
def isOasSchemaCompliance():
    '''public boolean isOasSchemaCompliance()
    '''
