def ActivityMaxDataManager():
'''public ActivityMaxDataManager(final MXServer mxServer)
'''
pass
def populateDataObjects():
'''public void populateDataObjects(final MboRemote projectMbo, final Map<String, ArrayList<String>> queryMap)
'''
pass
def findById():
'''public Activity findById(final Schedule schedule, final String id, final DataSpec dataSpec)
'''
pass
def loadDataObjects():
'''public JSONArray loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final Long offsetRecord, boolean parentOnly)
public JSONArray loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final List<String> activityIDs)
'''
pass
def processChanges():
'''public void processChanges(final MboRemote projectMbo, final List<Activity> activityChanges)
'''
pass
def commitChanges():
'''public void commitChanges(final MboRemote projectMbo, final MboSetRemote activitySet, final String selectedIDs)
'''
pass
def getPageCount():
'''public int getPageCount(final Schedule schedule, final DataSpec dataSpec, final boolean parentOnly)
'''
pass
def getRowCount():
'''public int getRowCount(final Schedule schedule, final DataSpec dataSpec, final boolean parentOnly)
'''
pass
def getCompareRowCount():
'''public int getCompareRowCount(final Schedule leftModel, final long rightModelId, final DataSpec dataSpec)
'''
pass
def fetchChildren():
'''public JSONArray fetchChildren(final Schedule schedule, final DataSpec dataSpec, final String workOrderNumber, final Long offsetRecord, final Integer level)
'''
pass
def loadDiffDataObjects():
'''public JSONArray loadDiffDataObjects(final Schedule leftSchedule, final long otherProjectID, final DataSpec dataSpec, final Long offsetRecord)
'''
pass
def bulkLoadDataObjects():
'''public JSONArray bulkLoadDataObjects(final Schedule schedule, final DataSpec dataSpec, final Long offsetRecord)
'''
pass
def loadMissingDataObjects():
'''public JSONArray loadMissingDataObjects(final Schedule leftSchedule, final long otherProjectID, final DataSpec dataSpec)
'''
pass
