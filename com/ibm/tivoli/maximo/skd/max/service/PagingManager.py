def ():
    '''returns PagingManager\n\n
    ()\n
    (final Schedule schedule, final ActivityMaxDataManager manager, final ConstraintMaxDataManager constraintDataManager, final DataSpec dataSpec)\n
    '''
def dataSpecChanged():
    '''returns None\n\n
    dataSpecChanged(final DataSpec spec)\n
    '''
def invalidate():
    '''returns None\n\n
    invalidate()\n
    '''
def clearCachedData():
    '''returns None\n\n
    clearCachedData()\n
    '''
def getPageCount():
    '''returns int\n\n
    getPageCount()\n
    '''
def getComparePageCount():
    '''returns int\n\n
    getComparePageCount(final Schedule leftModel, final long rightModelId)\n
    '''
def getCompareRowCount():
    '''returns int\n\n
    getCompareRowCount(final Schedule leftModel, final long rightModelId)\n
    '''
def setCompareRowCount():
    '''returns None\n\n
    setCompareRowCount(final int compareRowCount)\n
    '''
def setComparePageCount():
    '''returns None\n\n
    setComparePageCount(final int comparePageCount)\n
    '''
def getRowCount():
    '''returns int\n\n
    getRowCount()\n
    '''
def getChildrenRowCount():
    '''returns int\n\n
    getChildrenRowCount()\n
    '''
def setPage():
    '''returns None\n\n
    setPage(final int page)\n
    '''
def getPage():
    '''returns Page\n\n
    getPage()\n
    getPage(final int page)\n
    getPage(final List<String> activityIDs)\n
    '''
def getNextPage():
    '''returns Page\n\n
    getNextPage()\n
    '''
def getPreviousPage():
    '''returns Page\n\n
    getPreviousPage()\n
    '''
def getFlatPage():
    '''returns Page\n\n
    getFlatPage(final int page, final long otherProjectID)\n
    '''
def loadDataObjects():
    '''returns JSONArray\n\n
    loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final long offsetRecord)\n
    loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final List<String> activityIDs)\n
    '''
def bulkLoadDataObjects():
    '''returns JSONArray\n\n
    bulkLoadDataObjects(final Schedule schedule, final DataSpec dataSpec, final long offsetRecord)\n
    '''
def loadMissingDataObjects():
    '''returns JSONArray\n\n
    loadMissingDataObjects(final Schedule leftModel, final long rightModelId)\n
    '''
def initializeDataObjects():
    '''returns JSONArray\n\n
    initializeDataObjects(final long offsetRecord)\n
    '''
def getItemById():
    '''returns JSONObject\n\n
    getItemById(final String id)\n
    '''
def getChildren():
    '''returns JSONArray\n\n
    getChildren(final Activity parentActivity, final boolean applyFilters)\n
    getChildren(final Activity parentActivity, final boolean applyFilters, final Integer level)\n
    '''
def fetchChildren():
    '''returns JSONArray\n\n
    fetchChildren(final Schedule schedule2, final DataSpec dataSpec2, final String internalID, final Long offset, final Integer level)\n
    '''
def addToCache():
    '''returns None\n\n
    addToCache(final Activity activity)\n
    '''
def applyConfigurationChanges():
    '''returns None\n\n
    applyConfigurationChanges(final JSONObject changes)\n
    '''
def getDataManager():
    '''returns ActivityMaxDataManager\n\n
    getDataManager()\n
    '''
def setDataManager():
    '''returns None\n\n
    setDataManager(final ActivityMaxDataManager dataManager)\n
    '''
def getConstraintDataManager():
    '''returns ConstraintMaxDataManager\n\n
    getConstraintDataManager()\n
    '''
def setConstraintDataManager():
    '''returns None\n\n
    setConstraintDataManager(final ConstraintMaxDataManager constraintDataManager)\n
    '''
def getDataSpec():
    '''returns DataSpec\n\n
    getDataSpec()\n
    '''
def setDataSpec():
    '''returns None\n\n
    setDataSpec(final DataSpec dataSpec)\n
    '''
def getCurrentPage():
    '''returns int\n\n
    getCurrentPage()\n
    '''
def setCurrentPage():
    '''returns None\n\n
    setCurrentPage(final int currentPage)\n
    '''
def rootChildenActivityIterator():
    '''returns Iterator<IMXActivity>\n\n
    rootChildenActivityIterator()\n
    '''
def isContraintsEnabled():
    '''returns boolean\n\n
    isContraintsEnabled()\n
    '''
def setContraintsEnabled():
    '''returns None\n\n
    setContraintsEnabled(final boolean contraintsEnabled)\n
    '''
