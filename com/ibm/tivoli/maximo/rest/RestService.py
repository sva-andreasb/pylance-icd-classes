REST_LOGGER = "String  \"maximo.rest\""
def RestService():
    '''    public RestService()
    public RestService(final MXServer mxServer)
    '''
def getDomainInfo():
    '''    public DomainInfo getDomainInfo(final String objectName, final String domainName, final String siteid, final String orgid)
    '''
def isKey():
    '''    public boolean isKey(final MboRemote mbo, final String mboAttrName)
    '''
def xmlToMboSet():
    '''    public MboSetRemote xmlToMboSet(final UserInfo info, final List<Element> data, final Map<String, String> params, final MXTransaction trans, final String appName)
    '''
def xmlToMbo():
    '''    public void xmlToMbo(final MboRemote mbo, final Element data)
    '''
def serializeMbo():
    '''    public byte[] serializeMbo(final MboRemote mbo, final boolean dropnulls, final boolean retainmbos, final Set<String> colsSet, final boolean exclude, final boolean locale, final boolean generic, final boolean verbose, final String format, final boolean metaData, final boolean compact)
    '''
def serializeMboSet():
    '''    public byte[] serializeMboSet(final MboSetRemote mboSet, final boolean dropnulls, final boolean retainmbos, final Set<String> colsSet, final boolean exclude, final int rsStart, final int maxItems, final boolean locale, final boolean generic, final boolean verbose, final String format, final boolean metaData, final boolean compact)
    '''
def serializeOSMboSet():
    '''    public byte[] serializeOSMboSet(final MboSetRemote mboSet, final String mosName, final boolean dropnulls, final boolean retainmbos, final int rsStart, final int maxItems, final String operation, final boolean locale, final boolean generic, final boolean verbose, final boolean rootOnly, final boolean keys, final String format, final boolean metaData, final boolean compact)
    '''
def serializeOSMbo():
    '''    public byte[] serializeOSMbo(final MboRemote mbo, final String mosName, final boolean dropnulls, final String operation, final boolean locale, final boolean generic, final boolean verbose, final boolean rootOnly, final boolean keys, final String format, final boolean metaData, final boolean compact)
    '''
