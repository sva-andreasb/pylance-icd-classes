def resPathToURI():
    '''    public static String resPathToURI(final List<String> resPath)
    '''
def createResourceRef():
    '''    public static JSONObject createResourceRef(final String resourceURI, final boolean leanJson)
    '''
def createResource():
    '''    public static JSONObject createResource(final String resourceURI, final boolean leanJson)
    '''
def createResponseInfo():
    '''    public static void createResponseInfo(final OslcRequest oslcRequest, final JSONObject rootOjo, final int rsTotal, final boolean nextPage, final boolean leanJson, final boolean bcollectionTotalCount, final boolean hasBookmark, final int pageSize)
    '''
def getNextPageURI():
    '''    public static String getNextPageURI(final OslcRequest oslcRequest, final JSONObject jo, final int pageSize)
    '''
def getPrevPageURI():
    '''    public static String getPrevPageURI(final OslcRequest oslcRequest, final int pageSize)
    '''
def serializeAllMboAttributes():
    '''    public static void serializeAllMboAttributes(final JSONObject mboOjo, final MboRemote mbo, final String uri, final boolean dropNulls, final boolean showHidden, final OslcRequest oslcRequest, final boolean setLocalizedRep, final boolean addLocalizedRep)
    '''
def setMboColumnValue():
    '''    public static void setMboColumnValue(final JSONObject mboOjo, final MboValueInfo mbv, final MboRemote mbo, final String alias, final OslcRequest oslcRequest, final boolean setLocalizedRep, final boolean addLocalizedRep)
    '''
