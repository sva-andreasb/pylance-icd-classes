OBJECTNAME_SKDACTIVITY = "String  SKDACTIVITY""
OBJECTNAME_SKDRESOURCE = "String  SKDRESOURCE""
OBJECTNAME_SKDRESERVATION = "String  SKDRESERVATION""
OBJECTNAME_SKDCONSTRAINT = "String  SKDCONSTRAINT""
SCHEDULER_SQLLOGGER = "String  maximo.scheduler.sql""
MAP_LOGGER = "String  maximo.map""
APPLINK_OBJECTNAME = "String  SKDAPPLINKOBJ""
APPLINK_APPNAME = "String  SKDAPPLINKAPP""
SKDACTIONINFOMAP_SEPARATOR = "String  \u00ef¿½""
def SKDAppService():
'''public SKDAppService(final MXServer mxServer)
'''
pass
def init():
'''public void init()
'''
pass
def destroy():
'''public void destroy()
'''
pass
def getSKDAppServiceBean():
'''public SKDAppServiceBeanRemote getSKDAppServiceBean(final UserInfo userInfo)
'''
pass
def populateProjectData():
'''public void populateProjectData(final UserInfo userInfo, final String projectId)
public void populateProjectData(final UserInfo userInfo, final MboRemote projectMbo)
'''
pass
def refreshSelectedActivities():
'''public List<IMXActivity> refreshSelectedActivities(final IMXGanttModel model, final UserInfo userInfo, final MboRemote projectMbo, final List<IMXActivity> selectedActivities, final boolean preserveSkdData)
'''
pass
def runtTask():
'''public <T> Future<T> runtTask(final Callable<T> task)
'''
pass
def loadScheduleMax():
'''public Future<Schedule> loadScheduleMax(final String projectId, final IProjectManagerCallback helper)
'''
pass
def call():
'''public Schedule call()
public GWASchedule call()
public GRSchedule call()
public MXGanttModel call()
'''
pass
def loadScheduleGWA():
'''public Future<GWASchedule> loadScheduleGWA(final String projectId, final IProjectManagerCallback helper)
'''
pass
def loadScheduleGR():
'''public Future<GRSchedule> loadScheduleGR(final String projectId, final IProjectManagerCallback helper)
'''
pass
def getFutureModel():
'''public Future<MXGanttModel> getFutureModel(final UserInfo userInfo, final String projectId)
public Future<MXGanttModel> getFutureModel(final UserInfo userInfo, final String projectId, final SKDAppServiceCache appCache)
'''
pass
def removeCachedModels():
'''public void removeCachedModels(final UserInfo info)
'''
pass
def removeFutureModel():
'''public void removeFutureModel(final UserInfo info, final String projectId)
'''
pass
def removeCachedModel():
'''public void removeCachedModel(final UserInfo info)
'''
pass
def getModel():
'''public IlvGanttModel getModel(final UserInfo userInfo, final String projectId)
public IlvGanttModel getModel(final UserInfo userInfo, final MboRemote project, final UserInfo createdByUserInfo, final boolean getModelForCreatedUser)
'''
pass
def getActivitiesModel():
'''public MXGanttModel getActivitiesModel(final UserInfo userInfo, final String projectId)
'''
pass
def updateCalendarInfoInProject():
'''public void updateCalendarInfoInProject(final MboRemote project, final UserInfo userInfo, final IMXGanttModel model, final Date startDate, final Date endDate, final SKDAppServiceCache appCache, final boolean getModelForCreatedUser)
'''
pass
def duplicateProjectData():
'''public void duplicateProjectData(final UserInfo userInfo, final String orgProjectId, final MboRemote duplicateProjectMbo)
'''
pass
def duplicateObjectData():
'''public void duplicateObjectData(final UserInfo userInfo, final String orgProjectId, final MboRemote duplicateProjectMbo)
'''
pass
def duplicateSKDAlternateAvail():
'''public void duplicateSKDAlternateAvail(final UserInfo userInfo, final String originalProjectID, final MboRemote duplicateProjectMbo)
'''
pass
def duplicateSKDData():
'''public void duplicateSKDData(final UserInfo userInfo, final String orgProjectId, final MboRemote duplicateProjectMbo)
'''
pass
def getSKDDataGroupTitle():
'''public HashMap<String, String> getSKDDataGroupTitle(final UserInfo userInfo, final String projectId, final String skdObjectName)
'''
pass
def populateSKDPropValue():
'''public void populateSKDPropValue(final IlvUserPropertyHolder propValue, final String propertyName, final int maxtype, final MboRemote mbo, final String attributeName)
'''
pass
def getNewMXActivityFactoryInstance():
'''public MXActivityFactory getNewMXActivityFactoryInstance()
'''
pass
def getNewMXReservationFactoryInstance():
'''public MXReservationFactory getNewMXReservationFactoryInstance()
'''
pass
def saveInitializedReservationChanges():
'''public void saveInitializedReservationChanges(final UserInfo userInfo, final MboRemote project, final ArrayList<MXReservation> modifiedReservations)
'''
pass
def loadAdditionalReservations():
'''public void loadAdditionalReservations(final UserInfo userInfo, final MXGanttModel model, final MboRemote project, final ActivityData activityData, final ResourceData resourceData, final ReservationData reservationData)
'''
pass
def getSqlLogger():
'''public MXLogger getSqlLogger()
'''
pass
def getMapLogger():
'''public MXLogger getMapLogger()
'''
pass
def populateResourceUse():
'''public static void populateResourceUse(final Connection conn, final UserInfo userInfo, final String projectId, final MXLogger sqlLogger)
public static void populateResourceUse(final Connection conn, final UserInfo userInfo, final String projectId, final MXLogger sqlLogger, final String refObjName)
'''
pass
def commitScenario():
'''public void commitScenario(final UserInfo userInfo, final String ScenarioProjectid)
public void commitScenario(final UserInfo userInfo, final String ScenarioProjectid, final String ids)
'''
pass
def commitModifiedModelChanges():
'''public void commitModifiedModelChanges(final UserInfo userInfo, final String projectId)
public void commitModifiedModelChanges(final UserInfo userInfo, final String projectId, final boolean commitConstraintsOnly)
public void commitModifiedModelChanges(final UserInfo userInfo, final String projectId, final String ids, final String objectName)
public void commitModifiedModelChanges(final UserInfo userInfo, final String projectId, String ids, final String objectName, final boolean commitConstraintsOnly)
'''
pass
def getGanttConfigInfo():
'''public GanttConfigInfo getGanttConfigInfo(final UserInfo userInfo, final String projectId)
public GanttConfigInfo getGanttConfigInfo(final UserInfo userInfo, final MboRemote project)
public GanttConfigInfo getGanttConfigInfo(final UserInfo userInfo, final MboRemote project, final ActivityData activityData, final ResourceData resourceData, final ReservationData reservationData, final ConstraintData constraintData, HashMap<String, String> appDescMap)
'''
pass
def loadSystemPropMap():
'''public HashMap<String, Object> loadSystemPropMap(final UserInfo ui)
'''
pass
def compare():
'''public int compare(final Object o1, final Object o2)
public int compare(final Object o1, final Object o2)
public int compare(final Object o1, final Object o2)
public int compare(final Object o1, final Object o2)
public int compare(final MXGanttPropertyInfo obj1, final MXGanttPropertyInfo obj2)
public int compare(final SKDObjectInfo info1, final SKDObjectInfo info2)
public int compare(final SKDDataGroupInfo info1, final SKDDataGroupInfo info2)
public int compare(final String objectName1, final String objectName2)
public int compare(final MXActivity act1, final MXActivity act2)
'''
pass
def getPropertyTitle():
'''public HashMap<String, String> getPropertyTitle(final UserInfo userInfo, final String skdObjectName)
'''
pass
def getActionTitle():
'''public HashMap<String, HashMap<String, SKDActionInfo>> getActionTitle(final UserInfo userInfo, final HashMap<String, HashMap<String, SKDActionInfo>> actionInfo, final String useWith)
public HashMap<String, HashMap<String, SKDActionInfo>> getActionTitle(final UserInfo userInfo, final HashMap<String, HashMap<String, SKDActionInfo>> actionInfo)
'''
pass
def getAuthAppDescMap():
'''public HashMap<String, String> getAuthAppDescMap(final UserInfo userInfo, final List<String> appList, final HashMap<String, String> appDescMap)
'''
pass
def getAppDescForApp():
'''public String getAppDescForApp(final String appName, final UserInfo userInfo)
'''
pass
def getOriginalAppForApp():
'''public String getOriginalAppForApp(final String appName, final UserInfo userInfo)
'''
pass
def getSKDUserLocaleData():
'''public SKDUserLocaleData getSKDUserLocaleData(final UserInfo userInfo)
'''
pass
def getSKDUIInfo():
'''public ISKDUIInfo getSKDUIInfo(final UserInfo userInfo)
public ISKDUIInfo getSKDUIInfo(final UserInfo userInfo, final String appName)
public ISKDUIInfo getSKDUIInfo(final UserInfo userInfo, final String appName, final String projectId)
'''
pass
def isWorkorderSchedule():
'''public boolean isWorkorderSchedule(final UserInfo userInfo, final String skdProjectId)
'''
pass
def getDisplayDateTimePattern():
'''public String getDisplayDateTimePattern(final UserInfo userInfo)
'''
pass
def getSKDMaxMessages():
'''public HashMap<String, SKDMessage> getSKDMaxMessages(final UserInfo userInfo)
'''
pass
def getWorkingHours():
'''public HashMap<String, SKDCalendarInfo> getWorkingHours(final MboRemote project, final boolean trimByProject)
public HashMap<String, SKDCalendarInfo> getWorkingHours(final MboRemote project, final Range<Date> range)
'''
pass
def getCalendarDates():
'''public DateRange getCalendarDates(final MboRemote project)
'''
pass
def getProjectDates():
'''public DateRange getProjectDates(final MboRemote project)
'''
pass
def getProjectDatesAdjustedForCalendar():
'''public DateRange getProjectDatesAdjustedForCalendar(final MboRemote project, final DateRange calDates, final boolean trimByProject)
'''
pass
def getCalendarMbo():
'''public MboRemote getCalendarMbo(final MboRemote project)
'''
pass
def getDataGroupInfoSet():
'''public TreeSet<SKDDataGroupInfo> getDataGroupInfoSet(final UserInfo userInfo, final String projectId, final String skdObjectName)
'''
pass
def asyncCommitNeeded():
'''public boolean asyncCommitNeeded(final MboRemote projectMbo)
'''
pass
def logDebugStatementForTime():
'''public static void logDebugStatementForTime(final MXLogger sqlLogger, final UserInfo userInfo, final Connection connection, final String projectId, final long timeTaken, final String query)
'''
pass
def logDebugStatementForInfo():
'''public static void logDebugStatementForInfo(final MXLogger sqlLogger, final String msgId, final Object[] params)
'''
pass
def performSkdAction():
'''public Object performSkdAction(final String projectId, final UserInfo ui, final String actionId, final Object actionObject, final boolean saveBeforeAction, final SKDAppServiceBeanRemote serviceBean)
'''
pass
def deleteProjectData():
'''public void deleteProjectData(final UserInfo userInfo, final MboRemote projectMbo)
'''
pass
def deleteSKDData():
'''public void deleteSKDData(final UserInfo userInfo, final MboRemote projectMbo)
'''
pass
def deleteObjectData():
'''public void deleteObjectData(final UserInfo userInfo, final MboRemote projectMbo)
'''
pass
def getServerDate():
'''public Date getServerDate()
'''
pass
def getAsyncCount():
'''public int getAsyncCount(final MboRemote projectMbo, final MboSetRemote activitySet)
'''
pass
def isEAMSchedulerLicensePresent():
'''public static boolean isEAMSchedulerLicensePresent()
'''
pass
def isScheduler7510LicensePresent():
'''public static boolean isScheduler7510LicensePresent()
'''
pass
def isScheduler7520LicensePresent():
'''public static boolean isScheduler7520LicensePresent()
'''
pass
def isSchedulerAviationLicensePresent():
'''public static boolean isSchedulerAviationLicensePresent()
'''
pass
def isLicensePresent():
'''public static boolean isLicensePresent(final String lic)
'''
pass
def getAvailabilities():
'''public ISKDAvailability getAvailabilities(final UserInfo ui, final String[] availParam)
'''
pass
def getItemAvailabilities():
'''public SKDItemAvailability getItemAvailabilities(final UserInfo ui, final String[] availParam)
'''
pass
def getShiftInfoForDispatch():
'''public void getShiftInfoForDispatch(final UserInfo userInfo, final MXGanttModel model, final MboRemote project, final boolean trimByProject)
'''
pass
def activitiesInitialized():
'''public boolean activitiesInitialized(final MboRemote projectMbo)
'''
pass
def getParentActivity():
'''public MboRemote getParentActivity(final MboRemote project, final String parentid)
'''
pass
def getCapacityPlanningGapModel():
'''public IlvGanttModel getCapacityPlanningGapModel(final UserInfo userInfo, final SKDCapacityPlanningGapRequestParams params)
'''
pass
def PopulateSKDOrigiDestMatrix():
'''public boolean PopulateSKDOrigiDestMatrix(final MboRemote projectMbo)
'''
pass
def getTaskSACodeList():
'''public HashMap getTaskSACodeList(final MboRemote projectMbo)
'''
pass
def getResourceSACodeList():
'''public HashMap getResourceSACodeList(final MboRemote projectMbo)
'''
pass
def getCrewResourceSACodeList():
'''public HashMap getCrewResourceSACodeList(final HashMap<String, HashMap<String, SKDMAPInputParamInfo>> laborResourceSACodeList, final MboRemote projectMbo)
'''
pass
def updateTravelTimeMatrixFor():
'''public int updateTravelTimeMatrixFor(final String orgId, final Map<String, SKDMAPInputParamInfo> taskSACodeMap, final Map<String, SKDMAPInputParamInfo> onTheFlyWOIDMap, final Map<String, SKDMAPInputParamInfo> resourceStartSACodeMap, final Map<String, SKDMAPInputParamInfo> resourceEndSACodeMap, final UserInfo userInfo)
'''
pass
def secondsToDuration():
'''public static Double secondsToDuration(long seconds)
'''
pass
def dynamicScheduling():
'''public int dynamicScheduling(final UserInfo userInfo, final long skdprojectid, final String emQuery, final boolean autoassign)
'''
pass
def deleteSuggestResourceListtoEMWO():
'''public void deleteSuggestResourceListtoEMWO(final long skdprojectid, final UserInfo userInfo, final String assignmentids)
'''
pass
def saveSuggestResourceListtoEMWO():
'''public void saveSuggestResourceListtoEMWO(final List resoureSet, final MboRemote wo, final MboRemote reqtoassign, final HashMap<String, HashMap<String, Double>> woandtraveltime, final long skdprojectid, final UserInfo userInfo)
'''
pass
def assignLaborCrewtoEMWO():
'''public void assignLaborCrewtoEMWO(final MboRemote wo, final MboRemote reqtoassign, final String assigncrew, final String assignlaborcode, final Date currentTime)
'''
pass
def autoAssignLaborCrewtoEMWO():
'''public boolean autoAssignLaborCrewtoEMWO(final ResourceFinder resFinder, List resources, final String resourcetype, final MboRemote wo, final MboRemote req, final boolean assignedlist, final Date currentTime, final HashMap<String, MboRemote> AssignedEMResource)
'''
pass
def assignLaborCrewFromSuggestSet():
'''public void assignLaborCrewFromSuggestSet(final MboSetRemote emWOAvailResSet, final UserInfo userInfo, final Date currentTime)
'''
pass
def removeAssignedEMResource():
'''public List removeAssignedEMResource(final List resoureSet, final String resourcetype, final HashMap<String, MboRemote> AssignedEMResource)
'''
pass
def getALLSKDViewerProperties():
'''public Properties getALLSKDViewerProperties()
'''
pass
def getSKDViewerProperties():
'''public Properties getSKDViewerProperties()
'''
pass
def getSKDDD():
'''public SKDDD getSKDDD()
'''
pass
def saveState():
'''public void saveState(final SKDState lastSavedState)
'''
pass
def loadState():
'''public SKDState loadState(final SKDState lastSavedState)
'''
pass
def getTemplatesMboSet():
'''public MboSetRemote getTemplatesMboSet(final String templateName, final MboRemote projectMbo)
'''
pass
def loadTemplate():
'''public String loadTemplate(final String templateName, final MboRemote projectMbo, final SKDTemplateResolver alternateResolver)
'''
pass
def getAssetMntOpMap():
'''public HashMap<String, SKDCalendarInfo> getAssetMntOpMap(final MboRemote project, final Date startDate, final Date endDate, final String objectName, final HashMap<String, SKDCalendarInfo> shiftCalMap)
'''
pass
def getAssetMntOpMapPM():
'''public HashMap<String, SKDCalendarInfo> getAssetMntOpMapPM(final MboRemote project, final Date startDate, final Date endDate, final String objectName, final HashMap<String, SKDCalendarInfo> shiftCalMap)
'''
pass
def getLocationMntOpMap():
'''public HashMap<String, SKDCalendarInfo> getLocationMntOpMap(final MboRemote project, final Date startDate, final Date endDate, final String objectName, final HashMap<String, SKDCalendarInfo> shiftCalMap)
'''
pass
def getLocationMntOpMapPM():
'''public HashMap<String, SKDCalendarInfo> getLocationMntOpMapPM(final MboRemote project, final Date startDate, final Date endDate, final String objectName, final HashMap<String, SKDCalendarInfo> shiftCalMap)
'''
pass
def getOverlappingMntOpSchedule():
'''public HashMap<String, ArrayList<SKDDateInterval>> getOverlappingMntOpSchedule(final HashMap<String, SKDCalendarInfo> assetLocMntCalMap, final HashMap<String, SKDCalendarInfo> assetLocOpCalMap)
'''
pass
def clearState():
'''public void clearState(final SKDState lastSavedState)
public void clearState(final String skdProjectId, final UserInfo info)
'''
pass
def commitMaxSchedule():
'''public void commitMaxSchedule(final UserInfo userInfo, final String projectid, final boolean commitConstraintsOnly)
public void commitMaxSchedule(final UserInfo userInfo, final String projectid, final String ids, final boolean commitConstraintsOnly)
'''
pass
def refreshModel():
'''public List<MXReservation> refreshModel(final UserInfo userInfo, final MboRemote project, final MXGanttModel model)
'''
pass
def reloadWorkOrders():
'''public Map<Long, MboRemote> reloadWorkOrders(final String projectID, final UserInfo userInfo)
'''
pass
def refreshActivity():
'''public void refreshActivity(final IMXActivity activity, final Map<Long, MboRemote> workOrdersByID)
'''
pass
def createNewAssignment():
'''public void createNewAssignment(final MboRemote assignment, final MboRemote workOrder, final MXGanttModel model, final UserInfo userInfo)
'''
pass
def deleteAssignment():
'''public void deleteAssignment(final long objectID, final UserInfo userInfo)
'''
pass
def updateAssignment():
'''public void updateAssignment(final MboRemote assignment, final UserInfo userInfo)
'''
pass
def deleteUncommitedDuplicateConstraints():
'''public void deleteUncommitedDuplicateConstraints(final long skdProjectID, final UserInfo userInfo)
'''
pass
def getPopulateDataObjectsWhere():
'''public String getPopulateDataObjectsWhere(final SKDProject projectMbo)
'''
pass
def clearPopulateDataObjectsWhere():
'''public void clearPopulateDataObjectsWhere()
'''
pass
def ActivityData():
'''public ActivityData()
'''
pass
def getObjectNames():
'''public HashMap<String, TreeSet<String>> getObjectNames()
public HashMap<String, TreeSet<String>> getObjectNames()
public HashMap<String, TreeSet<String>> getObjectNames()
public HashMap<String, TreeSet<String>> getObjectNames()
'''
pass
def getAllObjectNames():
'''public Set<String> getAllObjectNames()
public Set<String> getAllObjectNames()
public Set<String> getAllObjectNames()
public Set<String> getAllObjectNames()
'''
pass
def setObjectNames():
'''public void setObjectNames(final HashMap<String, TreeSet<String>> objectNames)
public void setObjectNames(final HashMap<String, TreeSet<String>> objectNames)
public void setObjectNames(final HashMap<String, TreeSet<String>> objectNames)
public void setObjectNames(final HashMap<String, TreeSet<String>> objectNames)
'''
pass
def getActivityMap():
'''public HashMap<String, MXActivity> getActivityMap()
'''
pass
def setActivityMap():
'''public void setActivityMap(final HashMap<String, MXActivity> activityMap)
'''
pass
def isInitializationNeeded():
'''public boolean isInitializationNeeded()
public boolean isInitializationNeeded()
public boolean isInitializationNeeded()
public boolean isInitializationNeeded()
'''
pass
def setInitializationNeeded():
'''public void setInitializationNeeded(final boolean initializationNeeded)
public void setInitializationNeeded(final boolean initializationNeeded)
public void setInitializationNeeded(final boolean initializationNeeded)
public void setInitializationNeeded(final boolean initializationNeeded)
'''
pass
def getActivities():
'''public HashMap<Long, MXActivity> getActivities(final String activityObjectName)
'''
pass
def ResourceData():
'''public ResourceData()
'''
pass
def getResourceMap():
'''public HashMap<String, MXResource> getResourceMap()
'''
pass
def setResourceMap():
'''public void setResourceMap(final HashMap<String, MXResource> resourceMap)
'''
pass
def getResources():
'''public HashMap<Long, MXResource> getResources(final String resObjectName)
'''
pass
def ReservationData():
'''public ReservationData()
'''
pass
def getReservationList():
'''public ArrayList<MXReservation> getReservationList()
'''
pass
def setReservationList():
'''public void setReservationList(final ArrayList<MXReservation> reservationList)
'''
pass
def getReservations():
'''public HashMap<Long, ArrayList<MXReservation>> getReservations(final String reservationObjectName)
'''
pass
def getConstraintList():
'''public ArrayList<MXConstraint> getConstraintList()
'''
pass
def setConstraintList():
'''public void setConstraintList(final ArrayList<MXConstraint> constraintList)
'''
pass
def getConstraints():
'''public HashMap<Long, MXConstraint> getConstraints(final String constraintObjectName)
'''
pass
def getNewConstraints():
'''public ArrayList<MXConstraint> getNewConstraints(final String constraintObjectName)
'''
pass
def comparePropertyInfo():
'''public comparePropertyInfo()
'''
pass
def setPatternStartDate():
'''public void setPatternStartDate(final Date date)
'''
pass
def getPatternStartDate():
'''public Date getPatternStartDate()
'''
pass
def setPatternStartIndex():
'''public void setPatternStartIndex(final int index)
'''
pass
def getPatternStartIndex():
'''public int getPatternStartIndex()
'''
pass
def setPatternStartDay():
'''public void setPatternStartDay(final int dayInt)
'''
pass
def getPatternStartDay():
'''public int getPatternStartDay()
'''
pass
def setPatternEndDay():
'''public void setPatternEndDay(final int dayInt)
'''
pass
def getPatternEndDay():
'''public int getPatternEndDay()
'''
pass
def GroupAndObjectSeqComparator():
'''public GroupAndObjectSeqComparator(final HashMap<String, SKDDataGroupInfo> groupInfoMap, final HashMap<String, SKDObjectInfo> objInfoMap)
'''
pass
def ObjectSeqComparator():
'''public ObjectSeqComparator(final HashMap<String, SKDObjectInfo> objInfoMap)
'''
pass
