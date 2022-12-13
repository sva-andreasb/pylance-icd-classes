OBJECTNAME_SKDACTIVITY = "String  \"SKDACTIVITY\""
OBJECTNAME_SKDRESOURCE = "String  \"SKDRESOURCE\""
OBJECTNAME_SKDRESERVATION = "String  \"SKDRESERVATION\""
OBJECTNAME_SKDCONSTRAINT = "String  \"SKDCONSTRAINT\""
SCHEDULER_SQLLOGGER = "String  \"maximo.scheduler.sql\""
MAP_LOGGER = "String  \"maximo.map\""
APPLINK_OBJECTNAME = "String  \"SKDAPPLINKOBJ\""
APPLINK_APPNAME = "String  \"SKDAPPLINKAPP\""
SKDACTIONINFOMAP_SEPARATOR = "String  \"\u00ef¿½\""
def SKDAppService():
    '''    public SKDAppService(final MXServer mxServer)
    '''
def init():
    '''    public void init()
    '''
def destroy():
    '''    public void destroy()
    '''
def getSKDAppServiceBean():
    '''    public SKDAppServiceBeanRemote getSKDAppServiceBean(final UserInfo userInfo)
    '''
def populateProjectData():
    '''    public void populateProjectData(final UserInfo userInfo, final String projectId)
    public void populateProjectData(final UserInfo userInfo, final MboRemote projectMbo)
    '''
def refreshSelectedActivities():
    '''    public List<IMXActivity> refreshSelectedActivities(final IMXGanttModel model, final UserInfo userInfo, final MboRemote projectMbo, final List<IMXActivity> selectedActivities, final boolean preserveSkdData)
    '''
def runtTask():
    '''    public <T> Future<T> runtTask(final Callable<T> task)
    '''
def loadScheduleMax():
    '''    public Future<Schedule> loadScheduleMax(final String projectId, final IProjectManagerCallback helper)
    '''
def call():
    '''    public Schedule call()
    public GWASchedule call()
    public GRSchedule call()
    public MXGanttModel call()
    '''
def loadScheduleGWA():
    '''    public Future<GWASchedule> loadScheduleGWA(final String projectId, final IProjectManagerCallback helper)
    '''
def loadScheduleGR():
    '''    public Future<GRSchedule> loadScheduleGR(final String projectId, final IProjectManagerCallback helper)
    '''
def getFutureModel():
    '''    public Future<MXGanttModel> getFutureModel(final UserInfo userInfo, final String projectId)
    public Future<MXGanttModel> getFutureModel(final UserInfo userInfo, final String projectId, final SKDAppServiceCache appCache)
    '''
def removeCachedModels():
    '''    public void removeCachedModels(final UserInfo info)
    '''
def removeFutureModel():
    '''    public void removeFutureModel(final UserInfo info, final String projectId)
    '''
def removeCachedModel():
    '''    public void removeCachedModel(final UserInfo info)
    '''
def getModel():
    '''    public IlvGanttModel getModel(final UserInfo userInfo, final String projectId)
    public IlvGanttModel getModel(final UserInfo userInfo, final MboRemote project, final UserInfo createdByUserInfo, final boolean getModelForCreatedUser)
    '''
def getActivitiesModel():
    '''    public MXGanttModel getActivitiesModel(final UserInfo userInfo, final String projectId)
    '''
def updateCalendarInfoInProject():
    '''    public void updateCalendarInfoInProject(final MboRemote project, final UserInfo userInfo, final IMXGanttModel model, final Date startDate, final Date endDate, final SKDAppServiceCache appCache, final boolean getModelForCreatedUser)
    '''
def duplicateProjectData():
    '''    public void duplicateProjectData(final UserInfo userInfo, final String orgProjectId, final MboRemote duplicateProjectMbo)
    '''
def duplicateObjectData():
    '''    public void duplicateObjectData(final UserInfo userInfo, final String orgProjectId, final MboRemote duplicateProjectMbo)
    '''
def duplicateSKDAlternateAvail():
    '''    public void duplicateSKDAlternateAvail(final UserInfo userInfo, final String originalProjectID, final MboRemote duplicateProjectMbo)
    '''
def duplicateSKDData():
    '''    public void duplicateSKDData(final UserInfo userInfo, final String orgProjectId, final MboRemote duplicateProjectMbo)
    '''
def getSKDDataGroupTitle():
    '''    public HashMap<String, String> getSKDDataGroupTitle(final UserInfo userInfo, final String projectId, final String skdObjectName)
    '''
def populateSKDPropValue():
    '''    public void populateSKDPropValue(final IlvUserPropertyHolder propValue, final String propertyName, final int maxtype, final MboRemote mbo, final String attributeName)
    '''
def getNewMXActivityFactoryInstance():
    '''    public MXActivityFactory getNewMXActivityFactoryInstance()
    '''
def getNewMXReservationFactoryInstance():
    '''    public MXReservationFactory getNewMXReservationFactoryInstance()
    '''
def saveInitializedReservationChanges():
    '''    public void saveInitializedReservationChanges(final UserInfo userInfo, final MboRemote project, final ArrayList<MXReservation> modifiedReservations)
    '''
def loadAdditionalReservations():
    '''    public void loadAdditionalReservations(final UserInfo userInfo, final MXGanttModel model, final MboRemote project, final ActivityData activityData, final ResourceData resourceData, final ReservationData reservationData)
    '''
def getSqlLogger():
    '''    public MXLogger getSqlLogger()
    '''
def getMapLogger():
    '''    public MXLogger getMapLogger()
    '''
def populateResourceUse():
    '''    public static void populateResourceUse(final Connection conn, final UserInfo userInfo, final String projectId, final MXLogger sqlLogger)
    public static void populateResourceUse(final Connection conn, final UserInfo userInfo, final String projectId, final MXLogger sqlLogger, final String refObjName)
    '''
def commitScenario():
    '''    public void commitScenario(final UserInfo userInfo, final String ScenarioProjectid)
    public void commitScenario(final UserInfo userInfo, final String ScenarioProjectid, final String ids)
    '''
def commitModifiedModelChanges():
    '''    public void commitModifiedModelChanges(final UserInfo userInfo, final String projectId)
    public void commitModifiedModelChanges(final UserInfo userInfo, final String projectId, final boolean commitConstraintsOnly)
    public void commitModifiedModelChanges(final UserInfo userInfo, final String projectId, final String ids, final String objectName)
    public void commitModifiedModelChanges(final UserInfo userInfo, final String projectId, String ids, final String objectName, final boolean commitConstraintsOnly)
    '''
def getGanttConfigInfo():
    '''    public GanttConfigInfo getGanttConfigInfo(final UserInfo userInfo, final String projectId)
    public GanttConfigInfo getGanttConfigInfo(final UserInfo userInfo, final MboRemote project)
    public GanttConfigInfo getGanttConfigInfo(final UserInfo userInfo, final MboRemote project, final ActivityData activityData, final ResourceData resourceData, final ReservationData reservationData, final ConstraintData constraintData, HashMap<String, String> appDescMap)
    '''
def loadSystemPropMap():
    '''    public HashMap<String, Object> loadSystemPropMap(final UserInfo ui)
    '''
def compare():
    '''    public int compare(final Object o1, final Object o2)
    public int compare(final Object o1, final Object o2)
    public int compare(final Object o1, final Object o2)
    public int compare(final Object o1, final Object o2)
    public int compare(final MXGanttPropertyInfo obj1, final MXGanttPropertyInfo obj2)
    public int compare(final SKDObjectInfo info1, final SKDObjectInfo info2)
    public int compare(final SKDDataGroupInfo info1, final SKDDataGroupInfo info2)
    public int compare(final String objectName1, final String objectName2)
    public int compare(final MXActivity act1, final MXActivity act2)
    '''
def getPropertyTitle():
    '''    public HashMap<String, String> getPropertyTitle(final UserInfo userInfo, final String skdObjectName)
    '''
def getActionTitle():
    '''    public HashMap<String, HashMap<String, SKDActionInfo>> getActionTitle(final UserInfo userInfo, final HashMap<String, HashMap<String, SKDActionInfo>> actionInfo, final String useWith)
    public HashMap<String, HashMap<String, SKDActionInfo>> getActionTitle(final UserInfo userInfo, final HashMap<String, HashMap<String, SKDActionInfo>> actionInfo)
    '''
def getAuthAppDescMap():
    '''    public HashMap<String, String> getAuthAppDescMap(final UserInfo userInfo, final List<String> appList, final HashMap<String, String> appDescMap)
    '''
def getAppDescForApp():
    '''    public String getAppDescForApp(final String appName, final UserInfo userInfo)
    '''
def getOriginalAppForApp():
    '''    public String getOriginalAppForApp(final String appName, final UserInfo userInfo)
    '''
def getSKDUserLocaleData():
    '''    public SKDUserLocaleData getSKDUserLocaleData(final UserInfo userInfo)
    '''
def getSKDUIInfo():
    '''    public ISKDUIInfo getSKDUIInfo(final UserInfo userInfo)
    public ISKDUIInfo getSKDUIInfo(final UserInfo userInfo, final String appName)
    public ISKDUIInfo getSKDUIInfo(final UserInfo userInfo, final String appName, final String projectId)
    '''
def isWorkorderSchedule():
    '''    public boolean isWorkorderSchedule(final UserInfo userInfo, final String skdProjectId)
    '''
def getDisplayDateTimePattern():
    '''    public String getDisplayDateTimePattern(final UserInfo userInfo)
    '''
def getSKDMaxMessages():
    '''    public HashMap<String, SKDMessage> getSKDMaxMessages(final UserInfo userInfo)
    '''
def getWorkingHours():
    '''    public HashMap<String, SKDCalendarInfo> getWorkingHours(final MboRemote project, final boolean trimByProject)
    public HashMap<String, SKDCalendarInfo> getWorkingHours(final MboRemote project, final Range<Date> range)
    '''
def getCalendarDates():
    '''    public DateRange getCalendarDates(final MboRemote project)
    '''
def getProjectDates():
    '''    public DateRange getProjectDates(final MboRemote project)
    '''
def getProjectDatesAdjustedForCalendar():
    '''    public DateRange getProjectDatesAdjustedForCalendar(final MboRemote project, final DateRange calDates, final boolean trimByProject)
    '''
def getCalendarMbo():
    '''    public MboRemote getCalendarMbo(final MboRemote project)
    '''
def getDataGroupInfoSet():
    '''    public TreeSet<SKDDataGroupInfo> getDataGroupInfoSet(final UserInfo userInfo, final String projectId, final String skdObjectName)
    '''
def asyncCommitNeeded():
    '''    public boolean asyncCommitNeeded(final MboRemote projectMbo)
    '''
def logDebugStatementForTime():
    '''    public static void logDebugStatementForTime(final MXLogger sqlLogger, final UserInfo userInfo, final Connection connection, final String projectId, final long timeTaken, final String query)
    '''
def logDebugStatementForInfo():
    '''    public static void logDebugStatementForInfo(final MXLogger sqlLogger, final String msgId, final Object[] params)
    '''
def performSkdAction():
    '''    public Object performSkdAction(final String projectId, final UserInfo ui, final String actionId, final Object actionObject, final boolean saveBeforeAction, final SKDAppServiceBeanRemote serviceBean)
    '''
def deleteProjectData():
    '''    public void deleteProjectData(final UserInfo userInfo, final MboRemote projectMbo)
    '''
def deleteSKDData():
    '''    public void deleteSKDData(final UserInfo userInfo, final MboRemote projectMbo)
    '''
def deleteObjectData():
    '''    public void deleteObjectData(final UserInfo userInfo, final MboRemote projectMbo)
    '''
def getServerDate():
    '''    public Date getServerDate()
    '''
def getAsyncCount():
    '''    public int getAsyncCount(final MboRemote projectMbo, final MboSetRemote activitySet)
    '''
def isEAMSchedulerLicensePresent():
    '''    public static boolean isEAMSchedulerLicensePresent()
    '''
def isScheduler7510LicensePresent():
    '''    public static boolean isScheduler7510LicensePresent()
    '''
def isScheduler7520LicensePresent():
    '''    public static boolean isScheduler7520LicensePresent()
    '''
def isSchedulerAviationLicensePresent():
    '''    public static boolean isSchedulerAviationLicensePresent()
    '''
def isLicensePresent():
    '''    public static boolean isLicensePresent(final String lic)
    '''
def getAvailabilities():
    '''    public ISKDAvailability getAvailabilities(final UserInfo ui, final String[] availParam)
    '''
def getItemAvailabilities():
    '''    public SKDItemAvailability getItemAvailabilities(final UserInfo ui, final String[] availParam)
    '''
def getShiftInfoForDispatch():
    '''    public void getShiftInfoForDispatch(final UserInfo userInfo, final MXGanttModel model, final MboRemote project, final boolean trimByProject)
    '''
def activitiesInitialized():
    '''    public boolean activitiesInitialized(final MboRemote projectMbo)
    '''
def getParentActivity():
    '''    public MboRemote getParentActivity(final MboRemote project, final String parentid)
    '''
def getCapacityPlanningGapModel():
    '''    public IlvGanttModel getCapacityPlanningGapModel(final UserInfo userInfo, final SKDCapacityPlanningGapRequestParams params)
    '''
def PopulateSKDOrigiDestMatrix():
    '''    public boolean PopulateSKDOrigiDestMatrix(final MboRemote projectMbo)
    '''
def getTaskSACodeList():
    '''    public HashMap getTaskSACodeList(final MboRemote projectMbo)
    '''
def getResourceSACodeList():
    '''    public HashMap getResourceSACodeList(final MboRemote projectMbo)
    '''
def getCrewResourceSACodeList():
    '''    public HashMap getCrewResourceSACodeList(final HashMap<String, HashMap<String, SKDMAPInputParamInfo>> laborResourceSACodeList, final MboRemote projectMbo)
    '''
def updateTravelTimeMatrixFor():
    '''    public int updateTravelTimeMatrixFor(final String orgId, final Map<String, SKDMAPInputParamInfo> taskSACodeMap, final Map<String, SKDMAPInputParamInfo> onTheFlyWOIDMap, final Map<String, SKDMAPInputParamInfo> resourceStartSACodeMap, final Map<String, SKDMAPInputParamInfo> resourceEndSACodeMap, final UserInfo userInfo)
    '''
def secondsToDuration():
    '''    public static Double secondsToDuration(long seconds)
    '''
def dynamicScheduling():
    '''    public int dynamicScheduling(final UserInfo userInfo, final long skdprojectid, final String emQuery, final boolean autoassign)
    '''
def deleteSuggestResourceListtoEMWO():
    '''    public void deleteSuggestResourceListtoEMWO(final long skdprojectid, final UserInfo userInfo, final String assignmentids)
    '''
def saveSuggestResourceListtoEMWO():
    '''    public void saveSuggestResourceListtoEMWO(final List resoureSet, final MboRemote wo, final MboRemote reqtoassign, final HashMap<String, HashMap<String, Double>> woandtraveltime, final long skdprojectid, final UserInfo userInfo)
    '''
def assignLaborCrewtoEMWO():
    '''    public void assignLaborCrewtoEMWO(final MboRemote wo, final MboRemote reqtoassign, final String assigncrew, final String assignlaborcode, final Date currentTime)
    '''
def autoAssignLaborCrewtoEMWO():
    '''    public boolean autoAssignLaborCrewtoEMWO(final ResourceFinder resFinder, List resources, final String resourcetype, final MboRemote wo, final MboRemote req, final boolean assignedlist, final Date currentTime, final HashMap<String, MboRemote> AssignedEMResource)
    '''
def assignLaborCrewFromSuggestSet():
    '''    public void assignLaborCrewFromSuggestSet(final MboSetRemote emWOAvailResSet, final UserInfo userInfo, final Date currentTime)
    '''
def removeAssignedEMResource():
    '''    public List removeAssignedEMResource(final List resoureSet, final String resourcetype, final HashMap<String, MboRemote> AssignedEMResource)
    '''
def getALLSKDViewerProperties():
    '''    public Properties getALLSKDViewerProperties()
    '''
def getSKDViewerProperties():
    '''    public Properties getSKDViewerProperties()
    '''
def getSKDDD():
    '''    public SKDDD getSKDDD()
    '''
def saveState():
    '''    public void saveState(final SKDState lastSavedState)
    '''
def loadState():
    '''    public SKDState loadState(final SKDState lastSavedState)
    '''
def getTemplatesMboSet():
    '''    public MboSetRemote getTemplatesMboSet(final String templateName, final MboRemote projectMbo)
    '''
def loadTemplate():
    '''    public String loadTemplate(final String templateName, final MboRemote projectMbo, final SKDTemplateResolver alternateResolver)
    '''
def getAssetMntOpMap():
    '''    public HashMap<String, SKDCalendarInfo> getAssetMntOpMap(final MboRemote project, final Date startDate, final Date endDate, final String objectName, final HashMap<String, SKDCalendarInfo> shiftCalMap)
    '''
def getAssetMntOpMapPM():
    '''    public HashMap<String, SKDCalendarInfo> getAssetMntOpMapPM(final MboRemote project, final Date startDate, final Date endDate, final String objectName, final HashMap<String, SKDCalendarInfo> shiftCalMap)
    '''
def getLocationMntOpMap():
    '''    public HashMap<String, SKDCalendarInfo> getLocationMntOpMap(final MboRemote project, final Date startDate, final Date endDate, final String objectName, final HashMap<String, SKDCalendarInfo> shiftCalMap)
    '''
def getLocationMntOpMapPM():
    '''    public HashMap<String, SKDCalendarInfo> getLocationMntOpMapPM(final MboRemote project, final Date startDate, final Date endDate, final String objectName, final HashMap<String, SKDCalendarInfo> shiftCalMap)
    '''
def getOverlappingMntOpSchedule():
    '''    public HashMap<String, ArrayList<SKDDateInterval>> getOverlappingMntOpSchedule(final HashMap<String, SKDCalendarInfo> assetLocMntCalMap, final HashMap<String, SKDCalendarInfo> assetLocOpCalMap)
    '''
def clearState():
    '''    public void clearState(final SKDState lastSavedState)
    public void clearState(final String skdProjectId, final UserInfo info)
    '''
def commitMaxSchedule():
    '''    public void commitMaxSchedule(final UserInfo userInfo, final String projectid, final boolean commitConstraintsOnly)
    public void commitMaxSchedule(final UserInfo userInfo, final String projectid, final String ids, final boolean commitConstraintsOnly)
    '''
def refreshModel():
    '''    public List<MXReservation> refreshModel(final UserInfo userInfo, final MboRemote project, final MXGanttModel model)
    '''
def reloadWorkOrders():
    '''    public Map<Long, MboRemote> reloadWorkOrders(final String projectID, final UserInfo userInfo)
    '''
def refreshActivity():
    '''    public void refreshActivity(final IMXActivity activity, final Map<Long, MboRemote> workOrdersByID)
    '''
def createNewAssignment():
    '''    public void createNewAssignment(final MboRemote assignment, final MboRemote workOrder, final MXGanttModel model, final UserInfo userInfo)
    '''
def deleteAssignment():
    '''    public void deleteAssignment(final long objectID, final UserInfo userInfo)
    '''
def updateAssignment():
    '''    public void updateAssignment(final MboRemote assignment, final UserInfo userInfo)
    '''
def deleteUncommitedDuplicateConstraints():
    '''    public void deleteUncommitedDuplicateConstraints(final long skdProjectID, final UserInfo userInfo)
    '''
def getPopulateDataObjectsWhere():
    '''    public String getPopulateDataObjectsWhere(final SKDProject projectMbo)
    '''
def clearPopulateDataObjectsWhere():
    '''    public void clearPopulateDataObjectsWhere()
    '''
def ActivityData():
    '''    public ActivityData()
    '''
def getObjectNames():
    '''    public HashMap<String, TreeSet<String>> getObjectNames()
    public HashMap<String, TreeSet<String>> getObjectNames()
    public HashMap<String, TreeSet<String>> getObjectNames()
    public HashMap<String, TreeSet<String>> getObjectNames()
    '''
def getAllObjectNames():
    '''    public Set<String> getAllObjectNames()
    public Set<String> getAllObjectNames()
    public Set<String> getAllObjectNames()
    public Set<String> getAllObjectNames()
    '''
def setObjectNames():
    '''    public void setObjectNames(final HashMap<String, TreeSet<String>> objectNames)
    public void setObjectNames(final HashMap<String, TreeSet<String>> objectNames)
    public void setObjectNames(final HashMap<String, TreeSet<String>> objectNames)
    public void setObjectNames(final HashMap<String, TreeSet<String>> objectNames)
    '''
def getActivityMap():
    '''    public HashMap<String, MXActivity> getActivityMap()
    '''
def setActivityMap():
    '''    public void setActivityMap(final HashMap<String, MXActivity> activityMap)
    '''
def isInitializationNeeded():
    '''    public boolean isInitializationNeeded()
    public boolean isInitializationNeeded()
    public boolean isInitializationNeeded()
    public boolean isInitializationNeeded()
    '''
def setInitializationNeeded():
    '''    public void setInitializationNeeded(final boolean initializationNeeded)
    public void setInitializationNeeded(final boolean initializationNeeded)
    public void setInitializationNeeded(final boolean initializationNeeded)
    public void setInitializationNeeded(final boolean initializationNeeded)
    '''
def getActivities():
    '''    public HashMap<Long, MXActivity> getActivities(final String activityObjectName)
    '''
def ResourceData():
    '''    public ResourceData()
    '''
def getResourceMap():
    '''    public HashMap<String, MXResource> getResourceMap()
    '''
def setResourceMap():
    '''    public void setResourceMap(final HashMap<String, MXResource> resourceMap)
    '''
def getResources():
    '''    public HashMap<Long, MXResource> getResources(final String resObjectName)
    '''
def ReservationData():
    '''    public ReservationData()
    '''
def getReservationList():
    '''    public ArrayList<MXReservation> getReservationList()
    '''
def setReservationList():
    '''    public void setReservationList(final ArrayList<MXReservation> reservationList)
    '''
def getReservations():
    '''    public HashMap<Long, ArrayList<MXReservation>> getReservations(final String reservationObjectName)
    '''
def getConstraintList():
    '''    public ArrayList<MXConstraint> getConstraintList()
    '''
def setConstraintList():
    '''    public void setConstraintList(final ArrayList<MXConstraint> constraintList)
    '''
def getConstraints():
    '''    public HashMap<Long, MXConstraint> getConstraints(final String constraintObjectName)
    '''
def getNewConstraints():
    '''    public ArrayList<MXConstraint> getNewConstraints(final String constraintObjectName)
    '''
def comparePropertyInfo():
    '''    public comparePropertyInfo()
    '''
def setPatternStartDate():
    '''    public void setPatternStartDate(final Date date)
    '''
def getPatternStartDate():
    '''    public Date getPatternStartDate()
    '''
def setPatternStartIndex():
    '''    public void setPatternStartIndex(final int index)
    '''
def getPatternStartIndex():
    '''    public int getPatternStartIndex()
    '''
def setPatternStartDay():
    '''    public void setPatternStartDay(final int dayInt)
    '''
def getPatternStartDay():
    '''    public int getPatternStartDay()
    '''
def setPatternEndDay():
    '''    public void setPatternEndDay(final int dayInt)
    '''
def getPatternEndDay():
    '''    public int getPatternEndDay()
    '''
def GroupAndObjectSeqComparator():
    '''    public GroupAndObjectSeqComparator(final HashMap<String, SKDDataGroupInfo> groupInfoMap, final HashMap<String, SKDObjectInfo> objInfoMap)
    '''
def ObjectSeqComparator():
    '''    public ObjectSeqComparator(final HashMap<String, SKDObjectInfo> objInfoMap)
    '''
