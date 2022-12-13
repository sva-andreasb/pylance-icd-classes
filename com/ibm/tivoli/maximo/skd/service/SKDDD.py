SKDACTIONINFOMAP_SEPARATOR = "String  \"\u00ef¿½\""
def SKDDD():
    '''    public SKDDD()
    '''
def getName():
    '''    public String getName()
    '''
def init():
    '''    public void init()
    public void init(final MXServer mxs)
    '''
def reload():
    '''    public void reload()
    public void reload(final String key)
    '''
def getAppFromMaxApps():
    '''    public List<String> getAppFromMaxApps(final String objectName, final UserInfo userInfo)
    '''
def getPropertyInfo():
    '''    public SKDPropertyInfo getPropertyInfo(final String skdObjectName, final String objectName, final String propertyName)
    '''
def getPropertyInfoMap():
    '''    public HashMap<String, SKDPropertyInfo> getPropertyInfoMap(final String skdObjectName, final String objectName)
    public LinkedHashMap<String, SKDPropertyInfo> getPropertyInfoMap(final String skdObjectName)
    '''
def getPropertyInfoMapByObjectName():
    '''    public HashMap<String, LinkedHashMap<String, SKDPropertyInfo>> getPropertyInfoMapByObjectName(final String objectName)
    '''
def getPropertyInfoMapBySKDObjectName():
    '''    public HashMap<String, LinkedHashMap<String, SKDPropertyInfo>> getPropertyInfoMapBySKDObjectName(final String skdObjectName)
    '''
def getObjectInfoListBySKDObjectName():
    '''    public ArrayList<SKDObjectInfo> getObjectInfoListBySKDObjectName(final String skdObjectName)
    '''
def getObjectInfoMapBySKDObjectName():
    '''    public HashMap<String, SKDObjectInfo> getObjectInfoMapBySKDObjectName(final String skdObjectName)
    '''
def getAllSameAsObjectNames():
    '''    public Set<String> getAllSameAsObjectNames(final String skdObjectName, final String objectName)
    '''
def getDataGroupInfoList():
    '''    public HashMap<String, SKDDataGroupInfo> getDataGroupInfoList(final String skdObjectName)
    '''
def getActionInfo():
    '''    public HashMap<String, HashMap<String, SKDActionInfo>> getActionInfo()
    public HashMap<String, HashMap<String, SKDActionInfo>> getActionInfo(final String useWith)
    '''
def getUidActionInfo():
    '''    public HashMap<Long, SKDActionInfo> getUidActionInfo()
    '''
