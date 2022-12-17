OBJECTNAME_SKDACTIVITY = "String  \"SKDACTIVITY\""
OBJECTNAME_SKDRESOURCE = "String  \"SKDRESOURCE\""
OBJECTNAME_SKDRESERVATION = "String  \"SKDRESERVATION\""
OBJECTNAME_SKDCONSTRAINT = "String  \"SKDCONSTRAINT\""
SCHEDULER_SQLLOGGER = "String  \"maximo.scheduler.sql\""
MAP_LOGGER = "String  \"maximo.map\""
APPLINK_OBJECTNAME = "String  \"SKDAPPLINKOBJ\""
APPLINK_APPNAME = "String  \"SKDAPPLINKAPP\""
SKDACTIONINFOMAP_SEPARATOR = "String  \"\u00ef¿½\""
def ():
    '''returns ObjectSeqComparator\n\n
    (final MXServer mxServer)\n
    ()\n
    ()\n
    ()\n
    ()\n
    (final HashMap<String, SKDDataGroupInfo> groupInfoMap, final HashMap<String, SKDObjectInfo> objInfoMap)\n
    (final HashMap<String, SKDObjectInfo> objInfoMap)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def getSKDAppServiceBean():
    '''returns SKDAppServiceBeanRemote\n\n
    getSKDAppServiceBean(final UserInfo userInfo)\n
    '''
def populateProjectData():
    '''returns None\n\n
    populateProjectData(final UserInfo userInfo, final String projectId)\n
    populateProjectData(final UserInfo userInfo, final MboRemote projectMbo)\n
    '''
def refreshSelectedActivities():
    '''returns List<IMXActivity>\n\n
    refreshSelectedActivities(final IMXGanttModel model, final UserInfo userInfo, final MboRemote projectMbo, final List<IMXActivity> selectedActivities, final boolean preserveSkdData)\n
    '''
def loadScheduleMax():
    '''returns Future<Schedule>\n\n
    loadScheduleMax(final String projectId, final IProjectManagerCallback helper)\n
    '''
def call():
    '''returns MXGanttModel\n\n
    call()\n
    call()\n
    call()\n
    call()\n
    '''
def loadScheduleGWA():
    '''returns Future<GWASchedule>\n\n
    loadScheduleGWA(final String projectId, final IProjectManagerCallback helper)\n
    '''
def loadScheduleGR():
    '''returns Future<GRSchedule>\n\n
    loadScheduleGR(final String projectId, final IProjectManagerCallback helper)\n
    '''
def getFutureModel():
    '''returns Future<MXGanttModel>\n\n
    getFutureModel(final UserInfo userInfo, final String projectId)\n
    getFutureModel(final UserInfo userInfo, final String projectId, final SKDAppServiceCache appCache)\n
    '''
def removeCachedModels():
    '''returns None\n\n
    removeCachedModels(final UserInfo info)\n
    '''
def removeFutureModel():
    '''returns None\n\n
    removeFutureModel(final UserInfo info, final String projectId)\n
    '''
def removeCachedModel():
    '''returns None\n\n
    removeCachedModel(final UserInfo info)\n
    '''
def getModel():
    '''returns IlvGanttModel\n\n
    getModel(final UserInfo userInfo, final String projectId)\n
    getModel(final UserInfo userInfo, final MboRemote project, final UserInfo createdByUserInfo, final boolean getModelForCreatedUser)\n
    '''
def getActivitiesModel():
    '''returns MXGanttModel\n\n
    getActivitiesModel(final UserInfo userInfo, final String projectId)\n
    '''
def updateCalendarInfoInProject():
    '''returns None\n\n
    updateCalendarInfoInProject(final MboRemote project, final UserInfo userInfo, final IMXGanttModel model, final Date startDate, final Date endDate, final SKDAppServiceCache appCache, final boolean getModelForCreatedUser)\n
    '''
def duplicateProjectData():
    '''returns None\n\n
    duplicateProjectData(final UserInfo userInfo, final String orgProjectId, final MboRemote duplicateProjectMbo)\n
    '''
def duplicateObjectData():
    '''returns None\n\n
    duplicateObjectData(final UserInfo userInfo, final String orgProjectId, final MboRemote duplicateProjectMbo)\n
    '''
def duplicateSKDAlternateAvail():
    '''returns None\n\n
    duplicateSKDAlternateAvail(final UserInfo userInfo, final String originalProjectID, final MboRemote duplicateProjectMbo)\n
    '''
def duplicateSKDData():
    '''returns None\n\n
    duplicateSKDData(final UserInfo userInfo, final String orgProjectId, final MboRemote duplicateProjectMbo)\n
    '''
def populateSKDPropValue():
    '''returns None\n\n
    populateSKDPropValue(final IlvUserPropertyHolder propValue, final String propertyName, final int maxtype, final MboRemote mbo, final String attributeName)\n
    '''
def getNewMXActivityFactoryInstance():
    '''returns MXActivityFactory\n\n
    getNewMXActivityFactoryInstance()\n
    '''
def getNewMXReservationFactoryInstance():
    '''returns MXReservationFactory\n\n
    getNewMXReservationFactoryInstance()\n
    '''
def saveInitializedReservationChanges():
    '''returns None\n\n
    saveInitializedReservationChanges(final UserInfo userInfo, final MboRemote project, final ArrayList<MXReservation> modifiedReservations)\n
    '''
def loadAdditionalReservations():
    '''returns None\n\n
    loadAdditionalReservations(final UserInfo userInfo, final MXGanttModel model, final MboRemote project, final ActivityData activityData, final ResourceData resourceData, final ReservationData reservationData)\n
    '''
def getSqlLogger():
    '''returns MXLogger\n\n
    getSqlLogger()\n
    '''
def getMapLogger():
    '''returns MXLogger\n\n
    getMapLogger()\n
    '''
def commitScenario():
    '''returns None\n\n
    commitScenario(final UserInfo userInfo, final String ScenarioProjectid)\n
    commitScenario(final UserInfo userInfo, final String ScenarioProjectid, final String ids)\n
    '''
def commitModifiedModelChanges():
    '''returns None\n\n
    commitModifiedModelChanges(final UserInfo userInfo, final String projectId)\n
    commitModifiedModelChanges(final UserInfo userInfo, final String projectId, final boolean commitConstraintsOnly)\n
    commitModifiedModelChanges(final UserInfo userInfo, final String projectId, final String ids, final String objectName)\n
    commitModifiedModelChanges(final UserInfo userInfo, final String projectId, String ids, final String objectName, final boolean commitConstraintsOnly)\n
    '''
def getGanttConfigInfo():
    '''returns GanttConfigInfo\n\n
    getGanttConfigInfo(final UserInfo userInfo, final String projectId)\n
    getGanttConfigInfo(final UserInfo userInfo, final MboRemote project)\n
    getGanttConfigInfo(final UserInfo userInfo, final MboRemote project, final ActivityData activityData, final ResourceData resourceData, final ReservationData reservationData, final ConstraintData constraintData, HashMap<String, String> appDescMap)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Object o1, final Object o2)\n
    compare(final Object o1, final Object o2)\n
    compare(final Object o1, final Object o2)\n
    compare(final Object o1, final Object o2)\n
    compare(final MXGanttPropertyInfo obj1, final MXGanttPropertyInfo obj2)\n
    compare(final SKDObjectInfo info1, final SKDObjectInfo info2)\n
    compare(final SKDDataGroupInfo info1, final SKDDataGroupInfo info2)\n
    compare(final String objectName1, final String objectName2)\n
    compare(final MXActivity act1, final MXActivity act2)\n
    '''
def getAppDescForApp():
    '''returns String\n\n
    getAppDescForApp(final String appName, final UserInfo userInfo)\n
    '''
def getOriginalAppForApp():
    '''returns String\n\n
    getOriginalAppForApp(final String appName, final UserInfo userInfo)\n
    '''
def getSKDUserLocaleData():
    '''returns SKDUserLocaleData\n\n
    getSKDUserLocaleData(final UserInfo userInfo)\n
    '''
def getSKDUIInfo():
    '''returns ISKDUIInfo\n\n
    getSKDUIInfo(final UserInfo userInfo)\n
    getSKDUIInfo(final UserInfo userInfo, final String appName)\n
    getSKDUIInfo(final UserInfo userInfo, final String appName, final String projectId)\n
    '''
def isWorkorderSchedule():
    '''returns boolean\n\n
    isWorkorderSchedule(final UserInfo userInfo, final String skdProjectId)\n
    '''
def getDisplayDateTimePattern():
    '''returns String\n\n
    getDisplayDateTimePattern(final UserInfo userInfo)\n
    '''
def getCalendarDates():
    '''returns DateRange\n\n
    getCalendarDates(final MboRemote project)\n
    '''
def getProjectDates():
    '''returns DateRange\n\n
    getProjectDates(final MboRemote project)\n
    '''
def getProjectDatesAdjustedForCalendar():
    '''returns DateRange\n\n
    getProjectDatesAdjustedForCalendar(final MboRemote project, final DateRange calDates, final boolean trimByProject)\n
    '''
def getCalendarMbo():
    '''returns MboRemote\n\n
    getCalendarMbo(final MboRemote project)\n
    '''
def getDataGroupInfoSet():
    '''returns TreeSet<SKDDataGroupInfo>\n\n
    getDataGroupInfoSet(final UserInfo userInfo, final String projectId, final String skdObjectName)\n
    '''
def asyncCommitNeeded():
    '''returns boolean\n\n
    asyncCommitNeeded(final MboRemote projectMbo)\n
    '''
def performSkdAction():
    '''returns Object\n\n
    performSkdAction(final String projectId, final UserInfo ui, final String actionId, final Object actionObject, final boolean saveBeforeAction, final SKDAppServiceBeanRemote serviceBean)\n
    '''
def deleteProjectData():
    '''returns None\n\n
    deleteProjectData(final UserInfo userInfo, final MboRemote projectMbo)\n
    '''
def deleteSKDData():
    '''returns None\n\n
    deleteSKDData(final UserInfo userInfo, final MboRemote projectMbo)\n
    '''
def deleteObjectData():
    '''returns None\n\n
    deleteObjectData(final UserInfo userInfo, final MboRemote projectMbo)\n
    '''
def getServerDate():
    '''returns Date\n\n
    getServerDate()\n
    '''
def getAsyncCount():
    '''returns int\n\n
    getAsyncCount(final MboRemote projectMbo, final MboSetRemote activitySet)\n
    '''
def getAvailabilities():
    '''returns ISKDAvailability\n\n
    getAvailabilities(final UserInfo ui, final String[] availParam)\n
    '''
def getItemAvailabilities():
    '''returns SKDItemAvailability\n\n
    getItemAvailabilities(final UserInfo ui, final String[] availParam)\n
    '''
def getShiftInfoForDispatch():
    '''returns None\n\n
    getShiftInfoForDispatch(final UserInfo userInfo, final MXGanttModel model, final MboRemote project, final boolean trimByProject)\n
    '''
def activitiesInitialized():
    '''returns boolean\n\n
    activitiesInitialized(final MboRemote projectMbo)\n
    '''
def getParentActivity():
    '''returns MboRemote\n\n
    getParentActivity(final MboRemote project, final String parentid)\n
    '''
def getCapacityPlanningGapModel():
    '''returns IlvGanttModel\n\n
    getCapacityPlanningGapModel(final UserInfo userInfo, final SKDCapacityPlanningGapRequestParams params)\n
    '''
def PopulateSKDOrigiDestMatrix():
    '''returns boolean\n\n
    PopulateSKDOrigiDestMatrix(final MboRemote projectMbo)\n
    '''
def getTaskSACodeList():
    '''returns HashMap\n\n
    getTaskSACodeList(final MboRemote projectMbo)\n
    '''
def getResourceSACodeList():
    '''returns HashMap\n\n
    getResourceSACodeList(final MboRemote projectMbo)\n
    '''
def getCrewResourceSACodeList():
    '''returns HashMap\n\n
    getCrewResourceSACodeList(final HashMap<String, HashMap<String, SKDMAPInputParamInfo>> laborResourceSACodeList, final MboRemote projectMbo)\n
    '''
def updateTravelTimeMatrixFor():
    '''returns int\n\n
    updateTravelTimeMatrixFor(final String orgId, final Map<String, SKDMAPInputParamInfo> taskSACodeMap, final Map<String, SKDMAPInputParamInfo> onTheFlyWOIDMap, final Map<String, SKDMAPInputParamInfo> resourceStartSACodeMap, final Map<String, SKDMAPInputParamInfo> resourceEndSACodeMap, final UserInfo userInfo)\n
    '''
def dynamicScheduling():
    '''returns int\n\n
    dynamicScheduling(final UserInfo userInfo, final long skdprojectid, final String emQuery, final boolean autoassign)\n
    '''
def deleteSuggestResourceListtoEMWO():
    '''returns None\n\n
    deleteSuggestResourceListtoEMWO(final long skdprojectid, final UserInfo userInfo, final String assignmentids)\n
    '''
def saveSuggestResourceListtoEMWO():
    '''returns None\n\n
    saveSuggestResourceListtoEMWO(final List resoureSet, final MboRemote wo, final MboRemote reqtoassign, final HashMap<String, HashMap<String, Double>> woandtraveltime, final long skdprojectid, final UserInfo userInfo)\n
    '''
def assignLaborCrewtoEMWO():
    '''returns None\n\n
    assignLaborCrewtoEMWO(final MboRemote wo, final MboRemote reqtoassign, final String assigncrew, final String assignlaborcode, final Date currentTime)\n
    '''
def autoAssignLaborCrewtoEMWO():
    '''returns boolean\n\n
    autoAssignLaborCrewtoEMWO(final ResourceFinder resFinder, List resources, final String resourcetype, final MboRemote wo, final MboRemote req, final boolean assignedlist, final Date currentTime, final HashMap<String, MboRemote> AssignedEMResource)\n
    '''
def assignLaborCrewFromSuggestSet():
    '''returns None\n\n
    assignLaborCrewFromSuggestSet(final MboSetRemote emWOAvailResSet, final UserInfo userInfo, final Date currentTime)\n
    '''
def removeAssignedEMResource():
    '''returns List\n\n
    removeAssignedEMResource(final List resoureSet, final String resourcetype, final HashMap<String, MboRemote> AssignedEMResource)\n
    '''
def getALLSKDViewerProperties():
    '''returns Properties\n\n
    getALLSKDViewerProperties()\n
    '''
def getSKDViewerProperties():
    '''returns Properties\n\n
    getSKDViewerProperties()\n
    '''
def getSKDDD():
    '''returns SKDDD\n\n
    getSKDDD()\n
    '''
def saveState():
    '''returns None\n\n
    saveState(final SKDState lastSavedState)\n
    '''
def loadState():
    '''returns SKDState\n\n
    loadState(final SKDState lastSavedState)\n
    '''
def getTemplatesMboSet():
    '''returns MboSetRemote\n\n
    getTemplatesMboSet(final String templateName, final MboRemote projectMbo)\n
    '''
def loadTemplate():
    '''returns String\n\n
    loadTemplate(final String templateName, final MboRemote projectMbo, final SKDTemplateResolver alternateResolver)\n
    '''
def clearState():
    '''returns None\n\n
    clearState(final SKDState lastSavedState)\n
    clearState(final String skdProjectId, final UserInfo info)\n
    '''
def commitMaxSchedule():
    '''returns None\n\n
    commitMaxSchedule(final UserInfo userInfo, final String projectid, final boolean commitConstraintsOnly)\n
    commitMaxSchedule(final UserInfo userInfo, final String projectid, final String ids, final boolean commitConstraintsOnly)\n
    '''
def refreshModel():
    '''returns List<MXReservation>\n\n
    refreshModel(final UserInfo userInfo, final MboRemote project, final MXGanttModel model)\n
    '''
def refreshActivity():
    '''returns None\n\n
    refreshActivity(final IMXActivity activity, final Map<Long, MboRemote> workOrdersByID)\n
    '''
def createNewAssignment():
    '''returns None\n\n
    createNewAssignment(final MboRemote assignment, final MboRemote workOrder, final MXGanttModel model, final UserInfo userInfo)\n
    '''
def deleteAssignment():
    '''returns None\n\n
    deleteAssignment(final long objectID, final UserInfo userInfo)\n
    '''
def updateAssignment():
    '''returns None\n\n
    updateAssignment(final MboRemote assignment, final UserInfo userInfo)\n
    '''
def deleteUncommitedDuplicateConstraints():
    '''returns None\n\n
    deleteUncommitedDuplicateConstraints(final long skdProjectID, final UserInfo userInfo)\n
    '''
def getPopulateDataObjectsWhere():
    '''returns String\n\n
    getPopulateDataObjectsWhere(final SKDProject projectMbo)\n
    '''
def clearPopulateDataObjectsWhere():
    '''returns None\n\n
    clearPopulateDataObjectsWhere()\n
    '''
def getAllObjectNames():
    '''returns Set<String>\n\n
    getAllObjectNames()\n
    getAllObjectNames()\n
    getAllObjectNames()\n
    getAllObjectNames()\n
    '''
def setObjectNames():
    '''returns None\n\n
    setObjectNames(final HashMap<String, TreeSet<String>> objectNames)\n
    setObjectNames(final HashMap<String, TreeSet<String>> objectNames)\n
    setObjectNames(final HashMap<String, TreeSet<String>> objectNames)\n
    setObjectNames(final HashMap<String, TreeSet<String>> objectNames)\n
    '''
def setActivityMap():
    '''returns None\n\n
    setActivityMap(final HashMap<String, MXActivity> activityMap)\n
    '''
def isInitializationNeeded():
    '''returns boolean\n\n
    isInitializationNeeded()\n
    isInitializationNeeded()\n
    isInitializationNeeded()\n
    isInitializationNeeded()\n
    '''
def setInitializationNeeded():
    '''returns None\n\n
    setInitializationNeeded(final boolean initializationNeeded)\n
    setInitializationNeeded(final boolean initializationNeeded)\n
    setInitializationNeeded(final boolean initializationNeeded)\n
    setInitializationNeeded(final boolean initializationNeeded)\n
    '''
def setResourceMap():
    '''returns None\n\n
    setResourceMap(final HashMap<String, MXResource> resourceMap)\n
    '''
def getReservationList():
    '''returns ArrayList<MXReservation>\n\n
    getReservationList()\n
    '''
def setReservationList():
    '''returns None\n\n
    setReservationList(final ArrayList<MXReservation> reservationList)\n
    '''
def getConstraintList():
    '''returns ArrayList<MXConstraint>\n\n
    getConstraintList()\n
    '''
def setConstraintList():
    '''returns None\n\n
    setConstraintList(final ArrayList<MXConstraint> constraintList)\n
    '''
def getNewConstraints():
    '''returns ArrayList<MXConstraint>\n\n
    getNewConstraints(final String constraintObjectName)\n
    '''
def setPatternStartDate():
    '''returns None\n\n
    setPatternStartDate(final Date date)\n
    '''
def getPatternStartDate():
    '''returns Date\n\n
    getPatternStartDate()\n
    '''
def setPatternStartIndex():
    '''returns None\n\n
    setPatternStartIndex(final int index)\n
    '''
def getPatternStartIndex():
    '''returns int\n\n
    getPatternStartIndex()\n
    '''
def setPatternStartDay():
    '''returns None\n\n
    setPatternStartDay(final int dayInt)\n
    '''
def getPatternStartDay():
    '''returns int\n\n
    getPatternStartDay()\n
    '''
def setPatternEndDay():
    '''returns None\n\n
    setPatternEndDay(final int dayInt)\n
    '''
def getPatternEndDay():
    '''returns int\n\n
    getPatternEndDay()\n
    '''
