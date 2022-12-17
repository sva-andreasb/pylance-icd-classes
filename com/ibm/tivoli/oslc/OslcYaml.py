def ():
    '''returns OslcYaml\n\n
    ()\n
    '''
def setSwaggerVersion():
    '''returns OslcYaml\n\n
    setSwaggerVersion(final String swaggerVersion)\n
    '''
def setOpenAPIVersion():
    '''returns OslcYaml\n\n
    setOpenAPIVersion(final String openAPIVersion)\n
    '''
def setInfo():
    '''returns OslcYaml\n\n
    setInfo(final String title, final String description, final String version)\n
    '''
def setInfoTermsOfService():
    '''returns OslcYaml\n\n
    setInfoTermsOfService(final String tos)\n
    '''
def setInfoContact():
    '''returns OslcYaml\n\n
    setInfoContact(final Object contactInfo)\n
    '''
def setInfoLicense():
    '''returns OslcYaml\n\n
    setInfoLicense(final Object licenseIfo)\n
    '''
def setPatternedObject():
    '''returns OslcYaml\n\n
    setPatternedObject(final String patternName, final Object content)\n
    '''
def setHost():
    '''returns OslcYaml\n\n
    setHost(final String host)\n
    setHost(final String host, final int port)\n
    '''
def setSchemes():
    '''returns OslcYaml\n\n
    setSchemes(final String... strs)\n
    '''
def addSecuritySchemes():
    '''returns OslcYaml\n\n
    addSecuritySchemes(final String key, final Object schemes)\n
    '''
def addSecurity():
    '''returns OslcYaml\n\n
    addSecurity(final String key, final Object scope)\n
    '''
def setBasePath():
    '''returns OslcYaml\n\n
    setBasePath(final String basePath)\n
    '''
def setServer():
    '''returns OslcYaml\n\n
    setServer(final JSONObject server)\n
    '''
def setConsumes():
    '''returns OslcYaml\n\n
    setConsumes(final String... consumes)\n
    '''
def addActionSchemaToComponent():
    '''returns boolean\n\n
    addActionSchemaToComponent(final String actionName, final JSONObject actionSchema)\n
    '''
def addOSSchemaToComponent():
    '''returns boolean\n\n
    addOSSchemaToComponent(final String osName, final UserInfo userInfo)\n
    '''
def addMethodBasicInfo():
    '''returns OslcYaml\n\n
    addMethodBasicInfo(final String pathName, final String methodName, final String summary, final String description)\n
    '''
def addMethodOperationId():
    '''returns OslcYaml\n\n
    addMethodOperationId(final String pathName, final String methodName, final String id)\n
    addMethodOperationId()\n
    '''
def addMethodProduces():
    '''returns OslcYaml\n\n
    addMethodProduces(final String pathName, final String methodName, final String... produces)\n
    '''
def addMethodTags():
    '''returns OslcYaml\n\n
    addMethodTags(final String pathName, final String methodName, final String... tags)\n
    '''
def addMethodParams():
    '''returns OslcYaml\n\n
    addMethodParams(final String pathName, final String methodName, final JSONObject params)\n
    '''
def addMethodRequestBody():
    '''returns OslcYaml\n\n
    addMethodRequestBody(final String pathName, final String methodName, final JSONObject body)\n
    '''
def addMethodRequestBodyContent():
    '''returns OslcYaml\n\n
    addMethodRequestBodyContent(final String pathName, final String methodName, final String contentType, final JSONObject params)\n
    '''
def addMethodResponse():
    '''returns OslcYaml\n\n
    addMethodResponse(final String pathName, final String methodName, final String status, final JSONObject statusContent)\n
    '''
def addMethodResponseForOS():
    '''returns OslcYaml\n\n
    addMethodResponseForOS(final String pathName, final String methodName, final String status, final JSONObject statusContent, final boolean osSchemaAdded, final String osName, final boolean isResource)\n
    '''
def addMethodExternalDocs():
    '''returns OslcYaml\n\n
    addMethodExternalDocs()\n
    '''
def addMethodConsumes():
    '''returns OslcYaml\n\n
    addMethodConsumes(final String pathName, final String methodName, final String... consumes)\n
    '''
def addMethodSchemes():
    '''returns OslcYaml\n\n
    addMethodSchemes(final String pathName, final String methodName, final String... schemes)\n
    '''
def addMethodDeprecated():
    '''returns OslcYaml\n\n
    addMethodDeprecated()\n
    '''
def addMethodPatternedObject():
    '''returns OslcYaml\n\n
    addMethodPatternedObject()\n
    '''
def addDefinitionsProperties():
    '''returns OslcYaml\n\n
    addDefinitionsProperties(final String defName, final String propertyName, final JSONObject definitions)\n
    '''
def addDefinitionsRequired():
    '''returns OslcYaml\n\n
    addDefinitionsRequired(final String defName, final JSONArray requiredArr)\n
    '''
def addDefinitionsDescription():
    '''returns OslcYaml\n\n
    addDefinitionsDescription(final String defName, final String description)\n
    '''
def addParameters():
    '''returns OslcYaml\n\n
    addParameters(final String paramName, final JSONObject parameters)\n
    '''
def addResponses():
    '''returns OslcYaml\n\n
    addResponses(final String paramName, final JSONObject parameters)\n
    '''
def addSecurityDefinitions():
    '''returns OslcYaml\n\n
    addSecurityDefinitions()\n
    '''
def addTags():
    '''returns OslcYaml\n\n
    addTags()\n
    '''
def addExternalDocs():
    '''returns OslcYaml\n\n
    addExternalDocs()\n
    '''
def getJSON():
    '''returns JSONObject\n\n
    getJSON()\n
    '''
def getYaml():
    '''returns String\n\n
    getYaml()\n
    '''
def setParamBasicInfo():
    '''returns None\n\n
    setParamBasicInfo(final JSONObject param, final String in, final String name, final String description, final String required, final String type)\n
    '''
def setIsJson():
    '''returns None\n\n
    setIsJson(final boolean isJson)\n
    '''
