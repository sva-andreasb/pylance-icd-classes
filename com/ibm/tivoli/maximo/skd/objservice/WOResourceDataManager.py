GRAPHASSIGN = "String  \"GRPASSIGN\""
CACHEKEY_RESOURCECRAFTDATA_LOADED = "String  \"WOResourceDataManager-CraftDataLoaded\""
CACHEKEY_RESOURCECRAFTDATA = "String  \"WOResourceDataManager-CraftData\""
CACHEKEY_RESOURCENONWORKDATA_LOADED = "String  \"WOResourceDataManager-NonWorkDataLoaded\""
CACHEKEY_RESOURCENONWORKDATA = "String  \"WOResourceDataManager-NonWorkData\""
CACHEKEY_RESOURCEWORKDATA_LOADED = "String  \"WOResourceDataManager-WorkDataLoaded\""
CACHEKEY_RESOURCEWORKDATA = "String  \"WOResourceDataManager-WorkData\""
def initializeResource():
    '''returns None\n\n
    initializeResource(final MXResource resource, final String objectName, final MboRemote mboObject)\n
    '''
def resourceRecordCount():
    '''returns int\n\n
    resourceRecordCount(final ArrayList<String> queries)\n
    '''
def populateResources():
    '''returns None\n\n
    populateResources(final ArrayList<String> queries)\n
    '''
def populateResourcePropertyDetails():
    '''returns None\n\n
    populateResourcePropertyDetails()\n
    '''
def applyResourceChange():
    '''returns None\n\n
    applyResourceChange(final MboRemote resourceMboRemote, final MXTransaction txn)\n
    '''
def loadResource():
    '''returns None\n\n
    loadResource(final MXResource resource, final String objectName, final MboRemote mboObject)\n
    loadResource(final MXResource resource, final String objectName, final MXGanttModel model)\n
    '''
def sortResourceChildren():
    '''returns List<IlvResource>\n\n
    sortResourceChildren(final IlvResource resource, final String objectName, final MXGanttModel model)\n
    '''
def getResourceShiftAvailableData():
    '''returns None\n\n
    getResourceShiftAvailableData(final String objectName, final String projectId)\n
    '''
def getResourceNonWorkData():
    '''returns None\n\n
    getResourceNonWorkData(final String objectName, final String projectId)\n
    '''
def getResourceWorkData():
    '''returns None\n\n
    getResourceWorkData(final String objectName, final String projectId)\n
    '''
def compare():
    '''returns int\n\n
    compare(final IlvResource a01, final IlvResource a02)\n
    '''
