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
def Configurable():
    '''    public Configurable()
    public Configurable(final Configurable parent)
    '''
def getParent():
    '''    public final Configurable getParent()
    '''
def setClassicCompatible():
    '''    public void setClassicCompatible(final boolean classicCompatibility)
    '''
def setClassicCompatibleAsInt():
    '''    public void setClassicCompatibleAsInt(final int classicCompatibility)
    '''
def isClassicCompatible():
    '''    public boolean isClassicCompatible()
    '''
def getClassicCompatibleAsInt():
    '''    public int getClassicCompatibleAsInt()
    '''
def setLocale():
    '''    public void setLocale(final Locale locale)
    '''
def getTimeZone():
    '''    public TimeZone getTimeZone()
    '''
def setTimeZone():
    '''    public void setTimeZone(final TimeZone timeZone)
    '''
def setSQLDateAndTimeTimeZone():
    '''    public void setSQLDateAndTimeTimeZone(final TimeZone tz)
    '''
def getSQLDateAndTimeTimeZone():
    '''    public TimeZone getSQLDateAndTimeTimeZone()
    '''
def getLocale():
    '''    public Locale getLocale()
    '''
def setNumberFormat():
    '''    public void setNumberFormat(final String numberFormat)
    '''
def getNumberFormat():
    '''    public String getNumberFormat()
    '''
def setBooleanFormat():
    '''    public void setBooleanFormat(final String booleanFormat)
    '''
def getBooleanFormat():
    '''    public String getBooleanFormat()
    '''
def setTimeFormat():
    '''    public void setTimeFormat(final String timeFormat)
    '''
def getTimeFormat():
    '''    public String getTimeFormat()
    '''
def setDateFormat():
    '''    public void setDateFormat(final String dateFormat)
    '''
def getDateFormat():
    '''    public String getDateFormat()
    '''
def setDateTimeFormat():
    '''    public void setDateTimeFormat(final String dateTimeFormat)
    '''
def getDateTimeFormat():
    '''    public String getDateTimeFormat()
    '''
def setTemplateExceptionHandler():
    '''    public void setTemplateExceptionHandler(final TemplateExceptionHandler templateExceptionHandler)
    '''
def getTemplateExceptionHandler():
    '''    public TemplateExceptionHandler getTemplateExceptionHandler()
    '''
def setArithmeticEngine():
    '''    public void setArithmeticEngine(final ArithmeticEngine arithmeticEngine)
    '''
def getArithmeticEngine():
    '''    public ArithmeticEngine getArithmeticEngine()
    '''
def setObjectWrapper():
    '''    public void setObjectWrapper(final ObjectWrapper objectWrapper)
    '''
def getObjectWrapper():
    '''    public ObjectWrapper getObjectWrapper()
    '''
def setOutputEncoding():
    '''    public void setOutputEncoding(final String outputEncoding)
    '''
def getOutputEncoding():
    '''    public String getOutputEncoding()
    '''
def setURLEscapingCharset():
    '''    public void setURLEscapingCharset(final String urlEscapingCharset)
    '''
def getURLEscapingCharset():
    '''    public String getURLEscapingCharset()
    '''
def setNewBuiltinClassResolver():
    '''    public void setNewBuiltinClassResolver(final TemplateClassResolver newBuiltinClassResolver)
    '''
def getNewBuiltinClassResolver():
    '''    public TemplateClassResolver getNewBuiltinClassResolver()
    '''
def setAutoFlush():
    '''    public void setAutoFlush(final boolean autoFlush)
    '''
def getAutoFlush():
    '''    public boolean getAutoFlush()
    '''
def setShowErrorTips():
    '''    public void setShowErrorTips(final boolean showTips)
    '''
def getShowErrorTips():
    '''    public boolean getShowErrorTips()
    '''
def setAPIBuiltinEnabled():
    '''    public void setAPIBuiltinEnabled(final boolean value)
    '''
def isAPIBuiltinEnabled():
    '''    public boolean isAPIBuiltinEnabled()
    '''
def setLogTemplateExceptions():
    '''    public void setLogTemplateExceptions(final boolean value)
    '''
def getLogTemplateExceptions():
    '''    public boolean getLogTemplateExceptions()
    '''
def setSetting():
    '''    public void setSetting(final String name, final String value)
    '''
def setStrictBeanModels():
    '''    public void setStrictBeanModels(final boolean strict)
    '''
def getSetting():
    '''    public String getSetting(final String key)
    '''
def getSettings():
    '''    public Map getSettings()
    '''
def setSettings():
    '''    public void setSettings(final Properties props)
    public void setSettings(final InputStream propsIn)
    '''
def setCustomAttribute():
    '''    public void setCustomAttribute(final String name, final Object value)
    '''
def getCustomAttributeNames():
    '''    public String[] getCustomAttributeNames()
    '''
def removeCustomAttribute():
    '''    public void removeCustomAttribute(final String name)
    '''
def getCustomAttribute():
    '''    public Object getCustomAttribute(final String name)
    '''
