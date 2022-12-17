LOCALE_KEY = "String  \"locale\""
NUMBER_FORMAT_KEY = "String  \"number_format\""
TIME_FORMAT_KEY = "String  \"time_format\""
DATE_FORMAT_KEY = "String  \"date_format\""
DATETIME_FORMAT_KEY = "String  \"datetime_format\""
TIME_ZONE_KEY = "String  \"time_zone\""
SQL_DATE_AND_TIME_TIME_ZONE_KEY = "String  \"sql_date_and_time_time_zone\""
CLASSIC_COMPATIBLE_KEY = "String  \"classic_compatible\""
TEMPLATE_EXCEPTION_HANDLER_KEY = "String  \"template_exception_handler\""
ARITHMETIC_ENGINE_KEY = "String  \"arithmetic_engine\""
OBJECT_WRAPPER_KEY = "String  \"object_wrapper\""
BOOLEAN_FORMAT_KEY = "String  \"boolean_format\""
OUTPUT_ENCODING_KEY = "String  \"output_encoding\""
URL_ESCAPING_CHARSET_KEY = "String  \"url_escaping_charset\""
STRICT_BEAN_MODELS = "String  \"strict_bean_models\""
STRICT_BEAN_MODELS_KEY = "String  \"strict_bean_models\""
AUTO_FLUSH_KEY = "String  \"auto_flush\""
NEW_BUILTIN_CLASS_RESOLVER_KEY = "String  \"new_builtin_class_resolver\""
SHOW_ERROR_TIPS_KEY = "String  \"show_error_tips\""
API_BUILTIN_ENABLED_KEY = "String  \"api_builtin_enabled\""
LOG_TEMPLATE_EXCEPTIONS_KEY = "String  \"log_template_exceptions\""
def ():
    '''returns Configurable\n\n
    ()\n
    (final Configurable parent)\n
    '''
def setClassicCompatible():
    '''returns None\n\n
    setClassicCompatible(final boolean classicCompatibility)\n
    '''
def setClassicCompatibleAsInt():
    '''returns None\n\n
    setClassicCompatibleAsInt(final int classicCompatibility)\n
    '''
def isClassicCompatible():
    '''returns boolean\n\n
    isClassicCompatible()\n
    '''
def getClassicCompatibleAsInt():
    '''returns int\n\n
    getClassicCompatibleAsInt()\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def getTimeZone():
    '''returns TimeZone\n\n
    getTimeZone()\n
    '''
def setTimeZone():
    '''returns None\n\n
    setTimeZone(final TimeZone timeZone)\n
    '''
def setSQLDateAndTimeTimeZone():
    '''returns None\n\n
    setSQLDateAndTimeTimeZone(final TimeZone tz)\n
    '''
def getSQLDateAndTimeTimeZone():
    '''returns TimeZone\n\n
    getSQLDateAndTimeTimeZone()\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def setNumberFormat():
    '''returns None\n\n
    setNumberFormat(final String numberFormat)\n
    '''
def getNumberFormat():
    '''returns String\n\n
    getNumberFormat()\n
    '''
def setBooleanFormat():
    '''returns None\n\n
    setBooleanFormat(final String booleanFormat)\n
    '''
def getBooleanFormat():
    '''returns String\n\n
    getBooleanFormat()\n
    '''
def setTimeFormat():
    '''returns None\n\n
    setTimeFormat(final String timeFormat)\n
    '''
def getTimeFormat():
    '''returns String\n\n
    getTimeFormat()\n
    '''
def setDateFormat():
    '''returns None\n\n
    setDateFormat(final String dateFormat)\n
    '''
def getDateFormat():
    '''returns String\n\n
    getDateFormat()\n
    '''
def setDateTimeFormat():
    '''returns None\n\n
    setDateTimeFormat(final String dateTimeFormat)\n
    '''
def getDateTimeFormat():
    '''returns String\n\n
    getDateTimeFormat()\n
    '''
def setTemplateExceptionHandler():
    '''returns None\n\n
    setTemplateExceptionHandler(final TemplateExceptionHandler templateExceptionHandler)\n
    '''
def getTemplateExceptionHandler():
    '''returns TemplateExceptionHandler\n\n
    getTemplateExceptionHandler()\n
    '''
def setArithmeticEngine():
    '''returns None\n\n
    setArithmeticEngine(final ArithmeticEngine arithmeticEngine)\n
    '''
def getArithmeticEngine():
    '''returns ArithmeticEngine\n\n
    getArithmeticEngine()\n
    '''
def setObjectWrapper():
    '''returns None\n\n
    setObjectWrapper(final ObjectWrapper objectWrapper)\n
    '''
def getObjectWrapper():
    '''returns ObjectWrapper\n\n
    getObjectWrapper()\n
    '''
def setOutputEncoding():
    '''returns None\n\n
    setOutputEncoding(final String outputEncoding)\n
    '''
def getOutputEncoding():
    '''returns String\n\n
    getOutputEncoding()\n
    '''
def setURLEscapingCharset():
    '''returns None\n\n
    setURLEscapingCharset(final String urlEscapingCharset)\n
    '''
def getURLEscapingCharset():
    '''returns String\n\n
    getURLEscapingCharset()\n
    '''
def setNewBuiltinClassResolver():
    '''returns None\n\n
    setNewBuiltinClassResolver(final TemplateClassResolver newBuiltinClassResolver)\n
    '''
def getNewBuiltinClassResolver():
    '''returns TemplateClassResolver\n\n
    getNewBuiltinClassResolver()\n
    '''
def setAutoFlush():
    '''returns None\n\n
    setAutoFlush(final boolean autoFlush)\n
    '''
def getAutoFlush():
    '''returns boolean\n\n
    getAutoFlush()\n
    '''
def setShowErrorTips():
    '''returns None\n\n
    setShowErrorTips(final boolean showTips)\n
    '''
def getShowErrorTips():
    '''returns boolean\n\n
    getShowErrorTips()\n
    '''
def setAPIBuiltinEnabled():
    '''returns None\n\n
    setAPIBuiltinEnabled(final boolean value)\n
    '''
def isAPIBuiltinEnabled():
    '''returns boolean\n\n
    isAPIBuiltinEnabled()\n
    '''
def setLogTemplateExceptions():
    '''returns None\n\n
    setLogTemplateExceptions(final boolean value)\n
    '''
def getLogTemplateExceptions():
    '''returns boolean\n\n
    getLogTemplateExceptions()\n
    '''
def setSetting():
    '''returns None\n\n
    setSetting(final String name, final String value)\n
    '''
def setStrictBeanModels():
    '''returns None\n\n
    setStrictBeanModels(final boolean strict)\n
    '''
def getSetting():
    '''returns String\n\n
    getSetting(final String key)\n
    '''
def getSettings():
    '''returns Map\n\n
    getSettings()\n
    '''
def setSettings():
    '''returns None\n\n
    setSettings(final Properties props)\n
    setSettings(final InputStream propsIn)\n
    '''
def setCustomAttribute():
    '''returns None\n\n
    setCustomAttribute(final String name, final Object value)\n
    '''
def getCustomAttributeNames():
    '''returns String[]\n\n
    getCustomAttributeNames()\n
    '''
def removeCustomAttribute():
    '''returns None\n\n
    removeCustomAttribute(final String name)\n
    '''
def getCustomAttribute():
    '''returns Object\n\n
    getCustomAttribute(final String name)\n
    '''
