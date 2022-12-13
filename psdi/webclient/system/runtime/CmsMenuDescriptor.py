PROPERTY_CONTEXTFILTER = "String  context-filter""
PROPERTY_NAMINGATTR = "String  naming-attribute""
PROPERTY_SUBVAR = "String  substitution-variable""
PROPERTY_CMSERVICE = "String  ContextMenuService""
PROPERTY_LAUNCHINGAPP = "String  launchingApp""
def CmsMenuDescriptor():
'''public CmsMenuDescriptor()
public CmsMenuDescriptor(final Element el)
'''
pass
def addContextFilter():
'''public void addContextFilter(final String name, final String value)
'''
pass
def getContextFilters():
'''public Map<String, String> getContextFilters()
'''
pass
def addNamingAttribute():
'''public void addNamingAttribute(final String name, final String value)
'''
pass
def getNamingAttributes():
'''public Map<String, String> getNamingAttributes()
'''
pass
def addSubstitutionVariable():
'''public void addSubstitutionVariable(final String name, final String value)
public void addSubstitutionVariable(final String ic)
'''
pass
def getSubstitutionVariables():
'''public Map<String, String> getSubstitutionVariables()
'''
pass
def getInstanceClass():
'''public String getInstanceClass()
'''
pass
def loadDynamicValues():
'''public void loadDynamicValues(final String menuId, final DataBean bean)
'''
pass
def loadXMLValues():
'''public void loadXMLValues(final Element el)
'''
pass
def initialize():
'''public void initialize(final Element el)
'''
pass
def getValuesAsObject():
'''public JSONObject getValuesAsObject(final DataBean bean)
'''
pass
