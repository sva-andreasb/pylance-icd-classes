def ActivityMaxDataManager():
    '''    public ActivityMaxDataManager(final MXServer mxServer)
    '''
def populateDataObjects():
    '''    public void populateDataObjects(final MboRemote projectMbo, final Map<String, ArrayList<String>> queryMap)
    '''
def findById():
    '''    public Activity findById(final Schedule schedule, final String id, final DataSpec dataSpec)
    '''
def loadDataObjects():
    '''    public JSONArray loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final Long offsetRecord, boolean parentOnly)
    public JSONArray loadDataObjects(final Schedule schedule, final DataSpec dataSpec, final List<String> activityIDs)
    '''
def processChanges():
    '''    public void processChanges(final MboRemote projectMbo, final List<Activity> activityChanges)
    '''
def commitChanges():
    '''    public void commitChanges(final MboRemote projectMbo, final MboSetRemote activitySet, final String selectedIDs)
    '''
def getPageCount():
    '''    public int getPageCount(final Schedule schedule, final DataSpec dataSpec, final boolean parentOnly)
    '''
def getRowCount():
    '''    public int getRowCount(final Schedule schedule, final DataSpec dataSpec, final boolean parentOnly)
    '''
def getCompareRowCount():
    '''    public int getCompareRowCount(final Schedule leftModel, final long rightModelId, final DataSpec dataSpec)
    '''
def fetchChildren():
    '''    public JSONArray fetchChildren(final Schedule schedule, final DataSpec dataSpec, final String workOrderNumber, final Long offsetRecord, final Integer level)
    '''
def loadDiffDataObjects():
    '''    public JSONArray loadDiffDataObjects(final Schedule leftSchedule, final long otherProjectID, final DataSpec dataSpec, final Long offsetRecord)
    '''
def bulkLoadDataObjects():
    '''    public JSONArray bulkLoadDataObjects(final Schedule schedule, final DataSpec dataSpec, final Long offsetRecord)
    '''
def loadMissingDataObjects():
    '''    public JSONArray loadMissingDataObjects(final Schedule leftSchedule, final long otherProjectID, final DataSpec dataSpec)
    '''
