REST_LOGGER = "String  \"maximo.rest\""
def ():
    '''returns RestService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def getDomainInfo():
    '''returns DomainInfo\n\n
    getDomainInfo(final String objectName, final String domainName, final String siteid, final String orgid)\n
    '''
def isKey():
    '''returns boolean\n\n
    isKey(final MboRemote mbo, final String mboAttrName)\n
    '''
def xmlToMboSet():
    '''returns MboSetRemote\n\n
    xmlToMboSet(final UserInfo info, final List<Element> data, final Map<String, String> params, final MXTransaction trans, final String appName)\n
    '''
def xmlToMbo():
    '''returns None\n\n
    xmlToMbo(final MboRemote mbo, final Element data)\n
    '''
def serializeMbo():
    '''returns byte[]\n\n
    serializeMbo(final MboRemote mbo, final boolean dropnulls, final boolean retainmbos, final Set<String> colsSet, final boolean exclude, final boolean locale, final boolean generic, final boolean verbose, final String format, final boolean metaData, final boolean compact)\n
    '''
def serializeMboSet():
    '''returns byte[]\n\n
    serializeMboSet(final MboSetRemote mboSet, final boolean dropnulls, final boolean retainmbos, final Set<String> colsSet, final boolean exclude, final int rsStart, final int maxItems, final boolean locale, final boolean generic, final boolean verbose, final String format, final boolean metaData, final boolean compact)\n
    '''
def serializeOSMboSet():
    '''returns byte[]\n\n
    serializeOSMboSet(final MboSetRemote mboSet, final String mosName, final boolean dropnulls, final boolean retainmbos, final int rsStart, final int maxItems, final String operation, final boolean locale, final boolean generic, final boolean verbose, final boolean rootOnly, final boolean keys, final String format, final boolean metaData, final boolean compact)\n
    '''
def serializeOSMbo():
    '''returns byte[]\n\n
    serializeOSMbo(final MboRemote mbo, final String mosName, final boolean dropnulls, final String operation, final boolean locale, final boolean generic, final boolean verbose, final boolean rootOnly, final boolean keys, final String format, final boolean metaData, final boolean compact)\n
    '''
