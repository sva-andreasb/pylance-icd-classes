def ():
    '''returns AssetActivityDataManager\n\n
    ()\n
    '''
def populate():
    '''returns boolean\n\n
    populate()\n
    '''
def populateActivities():
    '''returns None\n\n
    populateActivities(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def getDateDBSqlString():
    '''returns String[]\n\n
    getDateDBSqlString(final int dbType)\n
    '''
def getOrgQuery():
    '''returns String\n\n
    getOrgQuery()\n
    '''
def populateActivityPropertyDetails():
    '''returns None\n\n
    populateActivityPropertyDetails()\n
    '''
def populateActivityParentFromAsset():
    '''returns None\n\n
    populateActivityParentFromAsset(final String uniqueidname)\n
    '''
def populateActivityDatesFromSkdproject():
    '''returns None\n\n
    populateActivityDatesFromSkdproject()\n
    '''
def getCompleteQueryWhere():
    '''returns String\n\n
    getCompleteQueryWhere(final String objectName, final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def getDefaultRestriction():
    '''returns String\n\n
    getDefaultRestriction(final String objectName)\n
    '''
def loadActivity():
    '''returns None\n\n
    loadActivity(final MXActivity activity, final String objectName, final MXGanttModel model)\n
    '''
def activityRecordCount():
    '''returns int\n\n
    activityRecordCount(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def saveActivities():
    '''returns None\n\n
    saveActivities(final IlvGeneralActivity activity)\n
    '''
def applyActivityChange():
    '''returns None\n\n
    applyActivityChange(final MboRemote activityMboRemote, final MXTransaction txn)\n
    applyActivityChange(final MboRemote activityMboRemote, final String ids, final MXTransaction txn)\n
    '''
