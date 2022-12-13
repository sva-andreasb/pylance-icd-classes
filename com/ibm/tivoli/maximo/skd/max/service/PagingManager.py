def PagingManager():
'''public PagingManager()
public PagingManager(final Schedule schedule, final ActivityMaxDataManager manager, final ConstraintMaxDataManager constraintDataManager, final DataSpec dataSpec)
'''
pass
def dataSpecChanged():
'''public void dataSpecChanged(final DataSpec spec)
'''
pass
def invalidate():
'''public void invalidate()
'''
pass
def clearCachedData():
'''public void clearCachedData()
'''
pass
def getPageCount():
'''public int getPageCount()
'''
pass
def getComparePageCount():
'''public int getComparePageCount(final Schedule leftModel, final long rightModelId)
'''
pass
def getCompareRowCount():
'''public int getCompareRowCount(final Schedule leftModel, final long rightModelId)
'''
pass
def setCompareRowCount():
'''public void setCompareRowCount(final int compareRowCount)
'''
pass
def setComparePageCount():
'''public void setComparePageCount(final int comparePageCount)
'''
pass
def getRowCount():
'''public int getRowCount()
'''
pass
def getChildrenRowCount():
'''public int getChildrenRowCount()
'''
pass
def setPage():
'''public void setPage(final int page)
'''
pass
def getPage():
'''public Page getPage()
public Page getPage(final int page)
public Page getPage(final List<String> activityIDs)
'''
pass
def getNextPage():
'''public Page getNextPage()
'''
pass
def getPreviousPage():
'''public Page getPreviousPage()
'''
pass
def getFlatPage():
'''public Page getFlatPage(final int page, final long otherProjectID)
'''
pass
def loadDataObjects():
'''public JSONArray loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final long offsetRecord)
public JSONArray loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final List<String> activityIDs)
'''
pass
def bulkLoadDataObjects():
'''public JSONArray bulkLoadDataObjects(final Schedule schedule, final DataSpec dataSpec, final long offsetRecord)
'''
pass
def loadMissingDataObjects():
'''public JSONArray loadMissingDataObjects(final Schedule leftModel, final long rightModelId)
'''
pass
def initializeDataObjects():
'''public JSONArray initializeDataObjects(final long offsetRecord)
'''
pass
def getItemById():
'''public JSONObject getItemById(final String id)
'''
pass
def getChildren():
'''public JSONArray getChildren(final Activity parentActivity, final boolean applyFilters)
public JSONArray getChildren(final Activity parentActivity, final boolean applyFilters, final Integer level)
'''
pass
def fetchChildren():
'''public JSONArray fetchChildren(final Schedule schedule2, final DataSpec dataSpec2, final String internalID, final Long offset, final Integer level)
'''
pass
def addToCache():
'''public void addToCache(final Activity activity)
'''
pass
def applyConfigurationChanges():
'''public void applyConfigurationChanges(final JSONObject changes)
'''
pass
def getDataManager():
'''public ActivityMaxDataManager getDataManager()
'''
pass
def setDataManager():
'''public void setDataManager(final ActivityMaxDataManager dataManager)
'''
pass
def getConstraintDataManager():
'''public ConstraintMaxDataManager getConstraintDataManager()
'''
pass
def setConstraintDataManager():
'''public void setConstraintDataManager(final ConstraintMaxDataManager constraintDataManager)
'''
pass
def getDataSpec():
'''public DataSpec getDataSpec()
'''
pass
def setDataSpec():
'''public void setDataSpec(final DataSpec dataSpec)
'''
pass
def getCurrentPage():
'''public int getCurrentPage()
'''
pass
def setCurrentPage():
'''public void setCurrentPage(final int currentPage)
'''
pass
def rootChildenActivityIterator():
'''public Iterator<IMXActivity> rootChildenActivityIterator()
'''
pass
def isContraintsEnabled():
'''public boolean isContraintsEnabled()
'''
pass
def setContraintsEnabled():
'''public void setContraintsEnabled(final boolean contraintsEnabled)
'''
pass
