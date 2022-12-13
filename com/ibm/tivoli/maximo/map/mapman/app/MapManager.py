def MapManager():
    '''    public MapManager(final MboSet ms)
    '''
def appValidate():
    '''    public void appValidate()
    '''
def delete():
    '''    public void delete(final long accessModifier)
    '''
def undelete():
    '''    public void undelete()
    '''
def duplicate():
    '''    public MboRemote duplicate()
    '''
def isAttributeModified():
    '''    public boolean isAttributeModified(final String attributeName)
    '''
def getOrgSiteForMaxvar():
    '''    public String getOrgSiteForMaxvar(final String maxvarName)
    '''
def add():
    '''    public void add()
    '''
def setAppDefaultValue():
    '''    public void setAppDefaultValue()
    '''
def copyOpLayers():
    '''    public void copyOpLayers(final MboSetRemote opLayers)
    '''
def isSpatialInstalled():
    '''    public static Boolean isSpatialInstalled()
    '''
def isAnywhereInstalled():
    '''    public static Boolean isAnywhereInstalled()
    '''
def getGMapsLicense():
    '''    public String getGMapsLicense()
    '''
def getGMapsSignature():
    '''    public String getGMapsSignature()
    '''
def getGMapsAuthenticationMethod():
    '''    public String getGMapsAuthenticationMethod()
    '''
def getDistanceMatrixURL():
    '''    public String getDistanceMatrixURL()
    '''
def getGMapsApiKey():
    '''    public String getGMapsApiKey()
    '''
def getMapProvider():
    '''    public String getMapProvider()
    '''
def isCarbonMap():
    '''    public Boolean isCarbonMap()
    '''
def getMapTipMboSet():
    '''    public MapTipSetRemote getMapTipMboSet()
    '''
def getMapManager():
    '''    public static MapManagerRemote getMapManager(final UserInfo user)
    public static MapManagerRemote getMapManager(final UserInfo user, final boolean isMobileMapManager)
    '''
def getMapManagerByNameAndSite():
    '''    public static MapManagerRemote getMapManagerByNameAndSite(final UserInfo userInfo, final String mapName, final String siteId)
    '''
def getMapManagerByName():
    '''    public static MapManagerRemote getMapManagerByName(final String mapName, final UserInfo userInfo)
    '''
def getCarbonMapManager():
    '''    public static MapManagerRemote getCarbonMapManager(final UserInfo user)
    public static MapManagerRemote getCarbonMapManager(final UserInfo user, final boolean isMobileMapManager)
    '''
def getCarbonMapManagerByNameAndSite():
    '''    public static MapManagerRemote getCarbonMapManagerByNameAndSite(final UserInfo userInfo, final String mapName, final String siteId)
    '''
def retrieveCommonSymbologyConfig():
    '''    public Map<String, String> retrieveCommonSymbologyConfig()
    '''
def retrieveParsedSymbologyConfig():
    '''    public Map<String, String> retrieveParsedSymbologyConfig()
    '''
def retrieveSymbologyForMaximoObject():
    '''    public Map<String, String> retrieveSymbologyForMaximoObject(final String mboName)
    public Map<String, String> retrieveSymbologyForMaximoObject(final MboRemote maximoObjectMbo)
    '''
def retrieveMboVisibilityConfiguration():
    '''    public JSONObject retrieveMboVisibilityConfiguration()
    '''
def retrieveMboClusterConfiguration():
    '''    public JSONObject retrieveMboClusterConfiguration()
    '''
def retrieveMboConfiguration():
    '''    public JSONObject retrieveMboConfiguration(final String attribute)
    '''
def retrieveMapConfigurationObject():
    '''    public MapConfiguration retrieveMapConfigurationObject(final UserInfo userInfo)
    '''
def generateAndUpdateMapConfigurationObject():
    '''    public MapConfiguration generateAndUpdateMapConfigurationObject()
    '''
def getOpenMapProvider():
    '''    public String getOpenMapProvider()
    '''
def getOpenMapURL():
    '''    public String getOpenMapURL()
    '''
def getPreloadBboxList():
    '''    public List<PreloadBbox> getPreloadBboxList(final MboSetRemote preloadMboSet)
    '''
