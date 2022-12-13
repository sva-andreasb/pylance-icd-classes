INTERACTION_LOGGER = "String  \"maximo.interaction\""
INTERACTION_DIR = "String  \"interaction\""
INTERACTION = "String  \"INTERACTION\""
DIALOG = "String  \"dialog\""
OBP = "String  \"obp\""
MAXTYPE_YORN = "String  \"YORN\""
MAXTYPE_BLOB = "String  \"BLOB\""
MAXTYPE_DATETIME = "String  \"DATETIME\""
MAXTYPE_FLOAT = "String  \"FLOAT\""
MAXTYPE_DATE = "String  \"DATE\""
MAXTYPE_TIME = "String  \"TIME\""
MAXTYPE_ALN = "String  \"ALN\""
MAXTYPE_INTEGER = "String  \"INTEGER\""
MAXTYPE_DECIMAL = "String  \"DECIMAL\""
def getMaxType():
    '''    public static String getMaxType(final WSIOAttribute wsioAttr)
    '''
def getFileName():
    '''    public static String getFileName(final String inter, final String name)
    '''
def reloadCache():
    '''    public static void reloadCache(final WSIO optimizedRequest, final WSIO optimizedResponse)
    '''
def getMaxAttrDomainIds():
    '''    public static Set<String> getMaxAttrDomainIds(final StringBuffer whereclause, final UserInfo userInfo)
    '''
def getWsioRelationsWhere():
    '''    public static StringBuffer getWsioRelationsWhere(final WSIO wsio, final StringBuffer where)
    '''
def getObjectsWhere():
    '''    public static StringBuffer getObjectsWhere(final WSIO wsio, final StringBuffer where)
    '''
def getIntrRelationsWhere():
    '''    public static StringBuffer getIntrRelationsWhere(final WSIO wsio, final InteractionInfo interactionInfo, final boolean isReq)
    '''
def getDomainsWhere():
    '''    public static StringBuffer getDomainsWhere(final Set<String> domHashSet)
    '''
def getDomainListWhere():
    '''    public static StringBuffer getDomainListWhere(final Set<String> domHashSet, final StringBuffer buf)
    '''
