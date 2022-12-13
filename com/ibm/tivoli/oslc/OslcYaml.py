def OslcYaml():
    '''public OslcYaml()
    '''
def setSwaggerVersion():
    '''public OslcYaml setSwaggerVersion(final String swaggerVersion)
    '''
def setOpenAPIVersion():
    '''public OslcYaml setOpenAPIVersion(final String openAPIVersion)
    '''
def setInfo():
    '''public OslcYaml setInfo(final String title, final String description, final String version)
    '''
def setInfoTermsOfService():
    '''public OslcYaml setInfoTermsOfService(final String tos)
    '''
def setInfoContact():
    '''public OslcYaml setInfoContact(final Object contactInfo)
    '''
def setInfoLicense():
    '''public OslcYaml setInfoLicense(final Object licenseIfo)
    '''
def setPatternedObject():
    '''public OslcYaml setPatternedObject(final String patternName, final Object content)
    '''
def setHost():
    '''public OslcYaml setHost(final String host)
    public OslcYaml setHost(final String host, final int port)
    '''
def setSchemes():
    '''public OslcYaml setSchemes(final String... strs)
    '''
def addSecuritySchemes():
    '''public OslcYaml addSecuritySchemes(final String key, final Object schemes)
    '''
def addSecurity():
    '''public OslcYaml addSecurity(final String key, final Object scope)
    '''
def setBasePath():
    '''public OslcYaml setBasePath(final String basePath)
    '''
def setServer():
    '''public OslcYaml setServer(final JSONObject server)
    '''
def setConsumes():
    '''public OslcYaml setConsumes(final String... consumes)
    '''
def addActionSchemaToComponent():
    '''public boolean addActionSchemaToComponent(final String actionName, final JSONObject actionSchema)
    '''
def addOSSchemaToComponent():
    '''public boolean addOSSchemaToComponent(final String osName, final UserInfo userInfo)
    '''
def addMethodBasicInfo():
    '''public OslcYaml addMethodBasicInfo(final String pathName, final String methodName, final String summary, final String description)
    '''
def addMethodOperationId():
    '''public OslcYaml addMethodOperationId(final String pathName, final String methodName, final String id)
    public OslcYaml addMethodOperationId()
    '''
def addMethodProduces():
    '''public OslcYaml addMethodProduces(final String pathName, final String methodName, final String... produces)
    '''
def addMethodTags():
    '''public OslcYaml addMethodTags(final String pathName, final String methodName, final String... tags)
    '''
def addMethodParams():
    '''public OslcYaml addMethodParams(final String pathName, final String methodName, final JSONObject params)
    '''
def addMethodRequestBody():
    '''public OslcYaml addMethodRequestBody(final String pathName, final String methodName, final JSONObject body)
    '''
def addMethodRequestBodyContent():
    '''public OslcYaml addMethodRequestBodyContent(final String pathName, final String methodName, final String contentType, final JSONObject params)
    '''
def addMethodResponse():
    '''public OslcYaml addMethodResponse(final String pathName, final String methodName, final String status, final JSONObject statusContent)
    '''
def addMethodResponseForOS():
    '''public OslcYaml addMethodResponseForOS(final String pathName, final String methodName, final String status, final JSONObject statusContent, final boolean osSchemaAdded, final String osName, final boolean isResource)
    '''
def addMethodExternalDocs():
    '''public OslcYaml addMethodExternalDocs()
    '''
def addMethodConsumes():
    '''public OslcYaml addMethodConsumes(final String pathName, final String methodName, final String... consumes)
    '''
def addMethodSchemes():
    '''public OslcYaml addMethodSchemes(final String pathName, final String methodName, final String... schemes)
    '''
def addMethodDeprecated():
    '''public OslcYaml addMethodDeprecated()
    '''
def addMethodPatternedObject():
    '''public OslcYaml addMethodPatternedObject()
    '''
def addDefinitionsProperties():
    '''public OslcYaml addDefinitionsProperties(final String defName, final String propertyName, final JSONObject definitions)
    '''
def addDefinitionsRequired():
    '''public OslcYaml addDefinitionsRequired(final String defName, final JSONArray requiredArr)
    '''
def addDefinitionsDescription():
    '''public OslcYaml addDefinitionsDescription(final String defName, final String description)
    '''
def addParameters():
    '''public OslcYaml addParameters(final String paramName, final JSONObject parameters)
    '''
def addResponses():
    '''public OslcYaml addResponses(final String paramName, final JSONObject parameters)
    '''
def addSecurityDefinitions():
    '''public OslcYaml addSecurityDefinitions()
    '''
def addTags():
    '''public OslcYaml addTags()
    '''
def addExternalDocs():
    '''public OslcYaml addExternalDocs()
    '''
def getJSON():
    '''public JSONObject getJSON()
    '''
def getYaml():
    '''public String getYaml()
    '''
def setParamBasicInfo():
    '''public void setParamBasicInfo(final JSONObject param, final String in, final String name, final String description, final String required, final String type)
    '''
def main():
    '''public static void main(final String... args)
    '''
def getYamlfromJSON():
    '''public static String getYamlfromJSON(final JSONObject object)
    '''
def jsonPrettyPrinter():
    '''public static void jsonPrettyPrinter(final Object object)
    '''
def setIsJson():
    '''public void setIsJson(final boolean isJson)
    '''
