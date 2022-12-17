PROPERTY_CONTEXTFILTER = "String  \"context-filter\""
PROPERTY_NAMINGATTR = "String  \"naming-attribute\""
PROPERTY_SUBVAR = "String  \"substitution-variable\""
PROPERTY_CMSERVICE = "String  \"ContextMenuService\""
PROPERTY_LAUNCHINGAPP = "String  \"launchingApp\""
def ():
    '''returns CmsMenuDescriptor\n\n
    ()\n
    (final Element el)\n
    '''
def addContextFilter():
    '''returns None\n\n
    addContextFilter(final String name, final String value)\n
    '''
def addNamingAttribute():
    '''returns None\n\n
    addNamingAttribute(final String name, final String value)\n
    '''
def addSubstitutionVariable():
    '''returns None\n\n
    addSubstitutionVariable(final String name, final String value)\n
    addSubstitutionVariable(final String ic)\n
    '''
def getInstanceClass():
    '''returns String\n\n
    getInstanceClass()\n
    '''
def loadDynamicValues():
    '''returns None\n\n
    loadDynamicValues(final String menuId, final DataBean bean)\n
    '''
def loadXMLValues():
    '''returns None\n\n
    loadXMLValues(final Element el)\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final Element el)\n
    '''
def getValuesAsObject():
    '''returns JSONObject\n\n
    getValuesAsObject(final DataBean bean)\n
    '''
