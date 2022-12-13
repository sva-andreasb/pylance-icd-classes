DEFAULT_ENTERPRISE_NUMBER = "int  18060"
DEFAULT_ID = "String  \"Audit\""
DEFAULT_MDCID = "String  \"mdc\""
def getContentFormat():
    '''    public Map<String, String> getContentFormat()
    '''
def toSerializable():
    '''    public String toSerializable(final LogEvent event)
    '''
def toString():
    '''    public String toString()
    '''
def createLayout():
    '''    public static Rfc5424Layout createLayout(@PluginAttribute(value = "facility", defaultString = "LOCAL0") final Facility facility, @PluginAttribute("id") final String id, @PluginAttribute(value = "enterpriseNumber", defaultInt = 18060) final int enterpriseNumber, @PluginAttribute(value = "includeMDC", defaultBoolean = true) final boolean includeMDC, @PluginAttribute(value = "mdcId", defaultString = "mdc") final String mdcId, @PluginAttribute("mdcPrefix") final String mdcPrefix, @PluginAttribute("eventPrefix") final String eventPrefix, @PluginAttribute("newLine") final boolean newLine, @PluginAttribute("newLineEscape") final String escapeNL, @PluginAttribute("appName") final String appName, @PluginAttribute("messageId") final String msgId, @PluginAttribute("mdcExcludes") final String excludes, @PluginAttribute("mdcIncludes") String includes, @PluginAttribute("mdcRequired") final String required, @PluginAttribute("exceptionPattern") final String exceptionPattern, @PluginAttribute("useTlsMessageFormat") final boolean useTlsMessageFormat, @PluginElement("LoggerFields") final LoggerFields[] loggerFields, @PluginConfiguration final Configuration config)
    '''
def getFacility():
    '''    public Facility getFacility()
    '''
def FieldFormatter():
    '''    public FieldFormatter(final Map<String, List<PatternFormatter>> fieldMap, final boolean discardIfEmpty)
    '''
def format():
    '''    public StructuredDataElement format(final LogEvent event)
    '''
def StructuredDataElement():
    '''    public StructuredDataElement(final Map<String, String> fields, final String prefix, final boolean discardIfEmpty)
    '''
