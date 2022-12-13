def WMActivityDataManager():
'''public WMActivityDataManager(final MXServer mxServer)
'''
pass
def applyActivityChange():
'''public void applyActivityChange(final MboRemote activityMboRemote, final String ids, final MXTransaction txn)
public void applyActivityChange(final MboRemote activityMboRemote, final MXTransaction txn)
'''
pass
def loadActivities():
'''public JSONArray loadActivities(final GWASchedule schedule)
'''
pass
def loadActivity():
'''public void loadActivity(final IMXActivity activity, final String objectName, final MboRemote mboObject)
public void loadActivity(final IMXActivity activity, final String objectName, final IMXGanttModel model)
'''
pass
def saveActivities():
'''public void saveActivities(final IMXActivity activity)
public void saveActivities(final IMXActivity activity, final MXTransaction txn)
'''
pass
def getPopulateDataObjectsWhere():
'''public String getPopulateDataObjectsWhere()
'''
pass
def activityRecordCount():
'''public int activityRecordCount(final HashMap<String, ArrayList<String>> queryMap)
'''
pass
def setPopulateObjectsWhere():
'''public void setPopulateObjectsWhere(final String populateObjectsWhere)
'''
pass
def populateDataObjectsWhere():
'''public String populateDataObjectsWhere(final MboRemote projectMbo, final Map<String, ArrayList<String>> queryMap)
public String populateDataObjectsWhere(final MboRemote projectMbo, final Map<String, ArrayList<String>> queryMap, final boolean forNullDates)
'''
pass
def processChanges():
'''public void processChanges(final MboRemote projectMbo, final List<Activity> activityChanges)
'''
pass
def activityNullRecordCount():
'''public int activityNullRecordCount(final HashMap<String, ArrayList<String>> queryMap)
'''
pass
def setWOScheduleStartDateForNullDates():
'''public int setWOScheduleStartDateForNullDates(final HashMap<String, ArrayList<String>> queryMap)
'''
pass
