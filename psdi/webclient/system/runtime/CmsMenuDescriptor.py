PROPERTY_CONTEXTFILTER = "String  \"context-filter\""
PROPERTY_NAMINGATTR = "String  \"naming-attribute\""
PROPERTY_SUBVAR = "String  \"substitution-variable\""
PROPERTY_CMSERVICE = "String  \"ContextMenuService\""
PROPERTY_LAUNCHINGAPP = "String  \"launchingApp\""
def CmsMenuDescriptor():
    '''public CmsMenuDescriptor()
    public CmsMenuDescriptor(final Element el)
    '''
def addContextFilter():
    '''public void addContextFilter(final String name, final String value)
    '''
def getContextFilters():
    '''public Map<String, String> getContextFilters()
    '''
def addNamingAttribute():
    '''public void addNamingAttribute(final String name, final String value)
    '''
def getNamingAttributes():
    '''public Map<String, String> getNamingAttributes()
    '''
def addSubstitutionVariable():
    '''public void addSubstitutionVariable(final String name, final String value)
    public void addSubstitutionVariable(final String ic)
    '''
def getSubstitutionVariables():
    '''public Map<String, String> getSubstitutionVariables()
    '''
def getInstanceClass():
    '''public String getInstanceClass()
    '''
def loadDynamicValues():
    '''public void loadDynamicValues(final String menuId, final DataBean bean)
    '''
def loadXMLValues():
    '''public void loadXMLValues(final Element el)
    '''
def initialize():
    '''public void initialize(final Element el)
    '''
def getValuesAsObject():
    '''public JSONObject getValuesAsObject(final DataBean bean)
    '''
