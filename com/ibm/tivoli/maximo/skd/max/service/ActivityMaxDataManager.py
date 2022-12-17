def ():
    '''returns ActivityMaxDataManager\n\n
    (final MXServer mxServer)\n
    '''
def populateDataObjects():
    '''returns None\n\n
    populateDataObjects(final MboRemote projectMbo, final Map<String, ArrayList<String>> queryMap)\n
    '''
def findById():
    '''returns Activity\n\n
    findById(final Schedule schedule, final String id, final DataSpec dataSpec)\n
    '''
def loadDataObjects():
    '''returns JSONArray\n\n
    loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final Long offsetRecord, boolean parentOnly)\n
    loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final List<String> activityIDs)\n
    '''
def processChanges():
    '''returns None\n\n
    processChanges(final MboRemote projectMbo, final List<Activity> activityChanges)\n
    '''
def commitChanges():
    '''returns None\n\n
    commitChanges(final MboRemote projectMbo, final MboSetRemote activitySet, final String selectedIDs)\n
    '''
def getPageCount():
    '''returns int\n\n
    getPageCount(final Schedule schedule, final DataSpec dataSpec, final boolean parentOnly)\n
    '''
def getRowCount():
    '''returns int\n\n
    getRowCount(final Schedule schedule, final DataSpec dataSpec, final boolean parentOnly)\n
    '''
def getCompareRowCount():
    '''returns int\n\n
    getCompareRowCount(final Schedule leftModel, final long rightModelId, final DataSpec dataSpec)\n
    '''
def fetchChildren():
    '''returns JSONArray\n\n
    fetchChildren(final Schedule schedule, final DataSpec dataSpec, final String workOrderNumber, final Long offsetRecord, final Integer level)\n
    '''
def loadDiffDataObjects():
    '''returns JSONArray\n\n
    loadDiffDataObjects(final Schedule leftSchedule, final long otherProjectID, final DataSpec dataSpec, final Long offsetRecord)\n
    '''
def bulkLoadDataObjects():
    '''returns JSONArray\n\n
    bulkLoadDataObjects(final Schedule schedule, final DataSpec dataSpec, final Long offsetRecord)\n
    '''
def loadMissingDataObjects():
    '''returns JSONArray\n\n
    loadMissingDataObjects(final Schedule leftSchedule, final long otherProjectID, final DataSpec dataSpec)\n
    '''
