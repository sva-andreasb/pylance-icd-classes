def ():
    '''returns WMActivityDataManager\n\n
    (final MXServer mxServer)\n
    '''
def applyActivityChange():
    '''returns None\n\n
    applyActivityChange(final MboRemote activityMboRemote, final String ids, final MXTransaction txn)\n
    applyActivityChange(final MboRemote activityMboRemote, final MXTransaction txn)\n
    '''
def loadActivities():
    '''returns JSONArray\n\n
    loadActivities(final GWASchedule schedule)\n
    '''
def loadActivity():
    '''returns None\n\n
    loadActivity(final IMXActivity activity, final String objectName, final MboRemote mboObject)\n
    loadActivity(final IMXActivity activity, final String objectName, final IMXGanttModel model)\n
    '''
def saveActivities():
    '''returns None\n\n
    saveActivities(final IMXActivity activity)\n
    saveActivities(final IMXActivity activity, final MXTransaction txn)\n
    '''
def getPopulateDataObjectsWhere():
    '''returns String\n\n
    getPopulateDataObjectsWhere()\n
    '''
def activityRecordCount():
    '''returns int\n\n
    activityRecordCount(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def setPopulateObjectsWhere():
    '''returns None\n\n
    setPopulateObjectsWhere(final String populateObjectsWhere)\n
    '''
def populateDataObjectsWhere():
    '''returns String\n\n
    populateDataObjectsWhere(final MboRemote projectMbo, final Map<String, ArrayList<String>> queryMap)\n
    populateDataObjectsWhere(final MboRemote projectMbo, final Map<String, ArrayList<String>> queryMap, final boolean forNullDates)\n
    '''
def processChanges():
    '''returns None\n\n
    processChanges(final MboRemote projectMbo, final List<Activity> activityChanges)\n
    '''
def activityNullRecordCount():
    '''returns int\n\n
    activityNullRecordCount(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def setWOScheduleStartDateForNullDates():
    '''returns int\n\n
    setWOScheduleStartDateForNullDates(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
