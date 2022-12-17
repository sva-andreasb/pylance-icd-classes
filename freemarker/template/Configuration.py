DEFAULT_ENCODING_KEY = "String  \"default_encoding\""
LOCALIZED_LOOKUP_KEY = "String  \"localized_lookup\""
STRICT_SYNTAX_KEY = "String  \"strict_syntax\""
WHITESPACE_STRIPPING_KEY = "String  \"whitespace_stripping\""
CACHE_STORAGE_KEY = "String  \"cache_storage\""
TEMPLATE_UPDATE_DELAY_KEY = "String  \"template_update_delay\""
AUTO_IMPORT_KEY = "String  \"auto_import\""
AUTO_INCLUDE_KEY = "String  \"auto_include\""
TAG_SYNTAX_KEY = "String  \"tag_syntax\""
TEMPLATE_LOADER_KEY = "String  \"template_loader\""
TEMPLATE_LOOKUP_STRATEGY_KEY = "String  \"template_lookup_strategy\""
TEMPLATE_NAME_FORMAT_KEY = "String  \"template_name_format\""
INCOMPATIBLE_IMPROVEMENTS_KEY = "String  \"incompatible_improvements\""
INCOMPATIBLE_IMPROVEMENTS = "String  \"incompatible_improvements\""
INCOMPATIBLE_ENHANCEMENTS = "String  \"incompatible_enhancements\""
AUTO_DETECT_TAG_SYNTAX = "int  0"
ANGLE_BRACKET_TAG_SYNTAX = "int  1"
SQUARE_BRACKET_TAG_SYNTAX = "int  2"
def ():
    '''returns LegacyDefaultFileTemplateLoader\n\n
    ()\n
    (final Version incompatibleImprovements)\n
    ()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def loadBuiltInEncodingMap():
    '''returns None\n\n
    loadBuiltInEncodingMap()\n
    '''
def clearEncodingMap():
    '''returns None\n\n
    clearEncodingMap()\n
    '''
def setTemplateLoader():
    '''returns None\n\n
    setTemplateLoader(final TemplateLoader templateLoader)\n
    '''
def unsetTemplateLoader():
    '''returns None\n\n
    unsetTemplateLoader()\n
    '''
def isTemplateLoaderExplicitlySet():
    '''returns boolean\n\n
    isTemplateLoaderExplicitlySet()\n
    '''
def getTemplateLoader():
    '''returns TemplateLoader\n\n
    getTemplateLoader()\n
    '''
def setTemplateLookupStrategy():
    '''returns None\n\n
    setTemplateLookupStrategy(final TemplateLookupStrategy templateLookupStrategy)\n
    '''
def unsetTemplateLookupStrategy():
    '''returns None\n\n
    unsetTemplateLookupStrategy()\n
    '''
def isTemplateLookupStrategyExplicitlySet():
    '''returns boolean\n\n
    isTemplateLookupStrategyExplicitlySet()\n
    '''
def getTemplateLookupStrategy():
    '''returns TemplateLookupStrategy\n\n
    getTemplateLookupStrategy()\n
    '''
def setTemplateNameFormat():
    '''returns None\n\n
    setTemplateNameFormat(final TemplateNameFormat templateNameFormat)\n
    '''
def unsetTemplateNameFormat():
    '''returns None\n\n
    unsetTemplateNameFormat()\n
    '''
def isTemplateNameFormatExplicitlySet():
    '''returns boolean\n\n
    isTemplateNameFormatExplicitlySet()\n
    '''
def getTemplateNameFormat():
    '''returns TemplateNameFormat\n\n
    getTemplateNameFormat()\n
    '''
def setCacheStorage():
    '''returns None\n\n
    setCacheStorage(final CacheStorage cacheStorage)\n
    '''
def unsetCacheStorage():
    '''returns None\n\n
    unsetCacheStorage()\n
    '''
def isCacheStorageExplicitlySet():
    '''returns boolean\n\n
    isCacheStorageExplicitlySet()\n
    '''
def getCacheStorage():
    '''returns CacheStorage\n\n
    getCacheStorage()\n
    '''
def setDirectoryForTemplateLoading():
    '''returns None\n\n
    setDirectoryForTemplateLoading(final File dir)\n
    '''
def setServletContextForTemplateLoading():
    '''returns None\n\n
    setServletContextForTemplateLoading(final Object servletContext, final String path)\n
    '''
def setClassForTemplateLoading():
    '''returns None\n\n
    setClassForTemplateLoading(final Class resourceLoaderClass, final String basePackagePath)\n
    '''
def setClassLoaderForTemplateLoading():
    '''returns None\n\n
    setClassLoaderForTemplateLoading(final ClassLoader classLoader, final String basePackagePath)\n
    '''
def setTemplateUpdateDelay():
    '''returns None\n\n
    setTemplateUpdateDelay(final int seconds)\n
    '''
def setStrictSyntaxMode():
    '''returns None\n\n
    setStrictSyntaxMode(final boolean b)\n
    '''
def setObjectWrapper():
    '''returns None\n\n
    setObjectWrapper(final ObjectWrapper objectWrapper)\n
    '''
def unsetObjectWrapper():
    '''returns None\n\n
    unsetObjectWrapper()\n
    '''
def isObjectWrapperExplicitlySet():
    '''returns boolean\n\n
    isObjectWrapperExplicitlySet()\n
    '''
def setTemplateExceptionHandler():
    '''returns None\n\n
    setTemplateExceptionHandler(final TemplateExceptionHandler templateExceptionHandler)\n
    '''
def unsetTemplateExceptionHandler():
    '''returns None\n\n
    unsetTemplateExceptionHandler()\n
    '''
def isTemplateExceptionHandlerExplicitlySet():
    '''returns boolean\n\n
    isTemplateExceptionHandlerExplicitlySet()\n
    '''
def setLogTemplateExceptions():
    '''returns None\n\n
    setLogTemplateExceptions(final boolean value)\n
    '''
def unsetLogTemplateExceptions():
    '''returns None\n\n
    unsetLogTemplateExceptions()\n
    '''
def isLogTemplateExceptionsExplicitlySet():
    '''returns boolean\n\n
    isLogTemplateExceptionsExplicitlySet()\n
    '''
def getStrictSyntaxMode():
    '''returns boolean\n\n
    getStrictSyntaxMode()\n
    '''
def setIncompatibleImprovements():
    '''returns None\n\n
    setIncompatibleImprovements(final Version incompatibleImprovements)\n
    '''
def getIncompatibleImprovements():
    '''returns Version\n\n
    getIncompatibleImprovements()\n
    '''
def setIncompatibleEnhancements():
    '''returns None\n\n
    setIncompatibleEnhancements(final String version)\n
    '''
def getIncompatibleEnhancements():
    '''returns String\n\n
    getIncompatibleEnhancements()\n
    '''
def getParsedIncompatibleEnhancements():
    '''returns int\n\n
    getParsedIncompatibleEnhancements()\n
    '''
def setWhitespaceStripping():
    '''returns None\n\n
    setWhitespaceStripping(final boolean b)\n
    '''
def getWhitespaceStripping():
    '''returns boolean\n\n
    getWhitespaceStripping()\n
    '''
def setTagSyntax():
    '''returns None\n\n
    setTagSyntax(final int tagSyntax)\n
    '''
def getTagSyntax():
    '''returns int\n\n
    getTagSyntax()\n
    '''
def getTemplate():
    '''returns Template\n\n
    getTemplate(final String name)\n
    getTemplate(final String name, final Locale locale)\n
    getTemplate(final String name, final String encoding)\n
    getTemplate(final String name, final Locale locale, final String encoding)\n
    getTemplate(final String name, final Locale locale, final String encoding, final boolean parseAsFTL)\n
    getTemplate(final String name, final Locale locale, final String encoding, final boolean parseAsFTL, final boolean ignoreMissing)\n
    getTemplate(final String name, Locale locale, final Object customLookupCondition, String encoding, final boolean parseAsFTL, final boolean ignoreMissing)\n
    '''
def setDefaultEncoding():
    '''returns None\n\n
    setDefaultEncoding(final String encoding)\n
    '''
def getDefaultEncoding():
    '''returns String\n\n
    getDefaultEncoding()\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding(final Locale locale)\n
    '''
def setEncoding():
    '''returns None\n\n
    setEncoding(final Locale locale, final String encoding)\n
    '''
def setSharedVariable():
    '''returns None\n\n
    setSharedVariable(final String name, final TemplateModel tm)\n
    setSharedVariable(final String name, final Object value)\n
    '''
def getSharedVariableNames():
    '''returns Set\n\n
    getSharedVariableNames()\n
    '''
def setSharedVaribles():
    '''returns None\n\n
    setSharedVaribles(final Map map)\n
    '''
def setAllSharedVariables():
    '''returns None\n\n
    setAllSharedVariables(final TemplateHashModelEx hash)\n
    '''
def getSharedVariable():
    '''returns TemplateModel\n\n
    getSharedVariable(final String name)\n
    '''
def clearSharedVariables():
    '''returns None\n\n
    clearSharedVariables()\n
    '''
def clearTemplateCache():
    '''returns None\n\n
    clearTemplateCache()\n
    '''
def removeTemplateFromCache():
    '''returns None\n\n
    removeTemplateFromCache(final String name)\n
    removeTemplateFromCache(final String name, final Locale locale)\n
    removeTemplateFromCache(final String name, final String encoding)\n
    removeTemplateFromCache(final String name, final Locale locale, final String encoding)\n
    removeTemplateFromCache(final String name, final Locale locale, final String encoding, final boolean parse)\n
    '''
def getLocalizedLookup():
    '''returns boolean\n\n
    getLocalizedLookup()\n
    '''
def setLocalizedLookup():
    '''returns None\n\n
    setLocalizedLookup(final boolean localizedLookup)\n
    '''
def setSetting():
    '''returns None\n\n
    setSetting(String name, final String value)\n
    '''
def addAutoImport():
    '''returns None\n\n
    addAutoImport(final String namespaceVarName, final String templateName)\n
    '''
def removeAutoImport():
    '''returns None\n\n
    removeAutoImport(final String namespaceVarName)\n
    '''
def setAutoImports():
    '''returns None\n\n
    setAutoImports(final Map map)\n
    '''
def addAutoInclude():
    '''returns None\n\n
    addAutoInclude(final String templateName)\n
    '''
def setAutoIncludes():
    '''returns None\n\n
    setAutoIncludes(final List templateNames)\n
    '''
def removeAutoInclude():
    '''returns None\n\n
    removeAutoInclude(final String templateName)\n
    '''
def getSupportedBuiltInNames():
    '''returns Set\n\n
    getSupportedBuiltInNames()\n
    '''
def getSupportedBuiltInDirectiveNames():
    '''returns Set\n\n
    getSupportedBuiltInDirectiveNames()\n
    '''
