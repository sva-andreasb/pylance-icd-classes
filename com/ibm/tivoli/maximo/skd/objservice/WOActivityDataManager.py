CACHEKEY_ASSIGNMENTACTIVITYMAP = "String  \"WOActivityDataManager-assignmentmap\""
CACHEKEY_COSTTYPEDATA_LOADED = "String  \"WOActivityDataManager-CostTypeDataLoaded\""
CACHEKEY_COSTTYPEDATA = "String  \"WOActivityDataManager-CostTypeData\""
CACHEKEY_WOMBOMAP = "String  \"WOActivityDataManager-WOMboMap\""
CACHEKEY_ASSSIGNMENTMBOMAP = "String  \"WOActivityDataManager-AssignmentMboMap\""
CACHEKEY_GROUPINFOSET = "String  \"WOActivityDataManager-groupInfoSet\""
CACHEKEY_WOWEATHERALERT = "String  \"WOActivityDataManager-WOWeatherAlertData\""
CACHEKEY_WORKLOG = "String  \"WOActivityDataManager-WorkLogData\""
CACHEKEY_CREWTYPEWORKZONE = "String  \"WOActivityDataManager-CrewTypeWorkZoneData\""
CACHEKEY_CRAFTWORKZONE = "String  \"WOActivityDataManager-CraftWorkZoneData\""
CACHEKEY_ASSIGNREPLOC = "String  \"WOActivityDataManager-AssignRepLocData\""
def ():
    '''returns WOActivityDataManager\n\n
    ()\n
    '''
def initializeActivity():
    '''returns None\n\n
    initializeActivity(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)\n
    '''
def initializeActivityChildren():
    '''returns None\n\n
    initializeActivityChildren(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)\n
    '''
def loadActivity():
    '''returns None\n\n
    loadActivity(final MXActivity activity, final String objectName, final MXGanttModel model)\n
    loadActivity(final MXActivity activity, final String objectName, final MboRemote mboObject)\n
    '''
def calculateHours():
    '''returns double\n\n
    calculateHours(final Date date1, final Date date2)\n
    '''
def getWOClassRestriction():
    '''returns String\n\n
    getWOClassRestriction(final String objectName)\n
    '''
def getDefaultRestriction():
    '''returns String\n\n
    getDefaultRestriction(final String objectName)\n
    '''
def getCompleteQueryWhere():
    '''returns String\n\n
    getCompleteQueryWhere(final String objectName, final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def activityRecordCount():
    '''returns int\n\n
    activityRecordCount(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def populateActivities():
    '''returns None\n\n
    populateActivities(final HashMap<String, ArrayList<String>> queryMap)\n
    '''
def loadAdditionalActivities():
    '''returns None\n\n
    loadAdditionalActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)\n
    '''
def loadWorkAndNonWorkActivities():
    '''returns None\n\n
    loadWorkAndNonWorkActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)\n
    '''
def populateActivityPropertyDetails():
    '''returns None\n\n
    populateActivityPropertyDetails()\n
    '''
def applyActivityChange():
    '''returns None\n\n
    applyActivityChange(final MboRemote activityMboRemote, final MXTransaction txn)\n
    applyActivityChange(final MboRemote activityMboRemote, final String ids, final MXTransaction txn)\n
    '''
def applyScenarioChange():
    '''returns None\n\n
    applyScenarioChange(final MboRemote activity, final MboRemote parentactivity, final MXTransaction txn)\n
    applyScenarioChange(final MboRemote activity, final MboRemote parentactivity, final String ids, final MXTransaction txn)\n
    '''
def sortActivityChildren():
    '''returns List<IlvActivity>\n\n
    sortActivityChildren(final IlvActivity activity, final String objectName, final MXGanttModel model)\n
    '''
def linkChildDummyNode():
    '''returns List<IlvActivity>\n\n
    linkChildDummyNode(final MXActivity activity, final MXGanttModel model, final SKDAppService.ActivityData activityData)\n
    '''
def saveActivities():
    '''returns None\n\n
    saveActivities(final IlvGeneralActivity activity, final MXTransaction txn)\n
    '''
def applyAssignmentChanges():
    '''returns None\n\n
    applyAssignmentChanges(final IlvGeneralActivity activity, final MXTransaction txn)\n
    '''
def getModifiedActivityChildren():
    '''returns List<IlvActivity>\n\n
    getModifiedActivityChildren(final MXActivity activity, final String objectName, final MboRemote mboObject, final MXGanttModel model)\n
    '''
def loadCrewWorkAndNonWorkActivities():
    '''returns None\n\n
    loadCrewWorkAndNonWorkActivities(final MXGanttModel model, final SKDAppService.ActivityData activityData)\n
    '''
def loadCostTypeReservations():
    '''returns None\n\n
    loadCostTypeReservations(final MXGanttModel model, final SKDAppService.ActivityData activityData)\n
    '''
def populateActivityParentFromAsset():
    '''returns None\n\n
    populateActivityParentFromAsset(final String objectname, final String uniqueidname)\n
    '''
def populateActivityParentFromLocation():
    '''returns None\n\n
    populateActivityParentFromLocation(final String objectname, final String uniqueidname)\n
    '''
def setPLUSAReservation():
    '''returns None\n\n
    setPLUSAReservation(final MXGanttModel model, final IlvGeneralActivity currentActivity, final MboRemote asstMbo)\n
    '''
def compare():
    '''returns int\n\n
    compare(final IlvActivity a01, final IlvActivity a02)\n
    '''
