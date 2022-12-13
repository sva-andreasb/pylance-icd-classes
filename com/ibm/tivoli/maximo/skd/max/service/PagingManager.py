def PagingManager():
    '''    public PagingManager()
    public PagingManager(final Schedule schedule, final ActivityMaxDataManager manager, final ConstraintMaxDataManager constraintDataManager, final DataSpec dataSpec)
    '''
def dataSpecChanged():
    '''    public void dataSpecChanged(final DataSpec spec)
    '''
def invalidate():
    '''    public void invalidate()
    '''
def clearCachedData():
    '''    public void clearCachedData()
    '''
def getPageCount():
    '''    public int getPageCount()
    '''
def getComparePageCount():
    '''    public int getComparePageCount(final Schedule leftModel, final long rightModelId)
    '''
def getCompareRowCount():
    '''    public int getCompareRowCount(final Schedule leftModel, final long rightModelId)
    '''
def setCompareRowCount():
    '''    public void setCompareRowCount(final int compareRowCount)
    '''
def setComparePageCount():
    '''    public void setComparePageCount(final int comparePageCount)
    '''
def getRowCount():
    '''    public int getRowCount()
    '''
def getChildrenRowCount():
    '''    public int getChildrenRowCount()
    '''
def setPage():
    '''    public void setPage(final int page)
    '''
def getPage():
    '''    public Page getPage()
    public Page getPage(final int page)
    public Page getPage(final List<String> activityIDs)
    '''
def getNextPage():
    '''    public Page getNextPage()
    '''
def getPreviousPage():
    '''    public Page getPreviousPage()
    '''
def getFlatPage():
    '''    public Page getFlatPage(final int page, final long otherProjectID)
    '''
def loadDataObjects():
    '''    public JSONArray loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final long offsetRecord)
    public JSONArray loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final List<String> activityIDs)
    '''
def bulkLoadDataObjects():
    '''    public JSONArray bulkLoadDataObjects(final Schedule schedule, final DataSpec dataSpec, final long offsetRecord)
    '''
def loadMissingDataObjects():
    '''    public JSONArray loadMissingDataObjects(final Schedule leftModel, final long rightModelId)
    '''
def initializeDataObjects():
    '''    public JSONArray initializeDataObjects(final long offsetRecord)
    '''
def getItemById():
    '''    public JSONObject getItemById(final String id)
    '''
def getChildren():
    '''    public JSONArray getChildren(final Activity parentActivity, final boolean applyFilters)
    public JSONArray getChildren(final Activity parentActivity, final boolean applyFilters, final Integer level)
    '''
def fetchChildren():
    '''    public JSONArray fetchChildren(final Schedule schedule2, final DataSpec dataSpec2, final String internalID, final Long offset, final Integer level)
    '''
def addToCache():
    '''    public void addToCache(final Activity activity)
    '''
def applyConfigurationChanges():
    '''    public void applyConfigurationChanges(final JSONObject changes)
    '''
def getDataManager():
    '''    public ActivityMaxDataManager getDataManager()
    '''
def setDataManager():
    '''    public void setDataManager(final ActivityMaxDataManager dataManager)
    '''
def getConstraintDataManager():
    '''    public ConstraintMaxDataManager getConstraintDataManager()
    '''
def setConstraintDataManager():
    '''    public void setConstraintDataManager(final ConstraintMaxDataManager constraintDataManager)
    '''
def getDataSpec():
    '''    public DataSpec getDataSpec()
    '''
def setDataSpec():
    '''    public void setDataSpec(final DataSpec dataSpec)
    '''
def getCurrentPage():
    '''    public int getCurrentPage()
    '''
def setCurrentPage():
    '''    public void setCurrentPage(final int currentPage)
    '''
def rootChildenActivityIterator():
    '''    public Iterator<IMXActivity> rootChildenActivityIterator()
    '''
def isContraintsEnabled():
    '''    public boolean isContraintsEnabled()
    '''
def setContraintsEnabled():
    '''    public void setContraintsEnabled(final boolean contraintsEnabled)
    '''
