def WMActivityDataManager():
    '''public WMActivityDataManager(final MXServer mxServer)
    '''
def applyActivityChange():
    '''public void applyActivityChange(final MboRemote activityMboRemote, final String ids, final MXTransaction txn)
    public void applyActivityChange(final MboRemote activityMboRemote, final MXTransaction txn)
    '''
def loadActivities():
    '''public JSONArray loadActivities(final GWASchedule schedule)
    '''
def loadActivity():
    '''public void loadActivity(final IMXActivity activity, final String objectName, final MboRemote mboObject)
    public void loadActivity(final IMXActivity activity, final String objectName, final IMXGanttModel model)
    '''
def saveActivities():
    '''public void saveActivities(final IMXActivity activity)
    public void saveActivities(final IMXActivity activity, final MXTransaction txn)
    '''
def getPopulateDataObjectsWhere():
    '''public String getPopulateDataObjectsWhere()
    '''
def activityRecordCount():
    '''public int activityRecordCount(final HashMap<String, ArrayList<String>> queryMap)
    '''
def setPopulateObjectsWhere():
    '''public void setPopulateObjectsWhere(final String populateObjectsWhere)
    '''
def populateDataObjectsWhere():
    '''public String populateDataObjectsWhere(final MboRemote projectMbo, final Map<String, ArrayList<String>> queryMap)
    public String populateDataObjectsWhere(final MboRemote projectMbo, final Map<String, ArrayList<String>> queryMap, final boolean forNullDates)
    '''
def processChanges():
    '''public void processChanges(final MboRemote projectMbo, final List<Activity> activityChanges)
    '''
def activityNullRecordCount():
    '''public int activityNullRecordCount(final HashMap<String, ArrayList<String>> queryMap)
    '''
def setWOScheduleStartDateForNullDates():
    '''public int setWOScheduleStartDateForNullDates(final HashMap<String, ArrayList<String>> queryMap)
    '''
