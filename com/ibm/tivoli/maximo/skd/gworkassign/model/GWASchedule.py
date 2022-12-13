def GWASchedule():
'''public GWASchedule()
public GWASchedule(final MboRemote project)
'''
pass
def getCurrentUserInfo():
'''public UserInfo getCurrentUserInfo()
'''
pass
def getCreatedUserInfo():
'''public UserInfo getCreatedUserInfo()
'''
pass
def getTableConfig():
'''public TableConfig getTableConfig()
'''
pass
def getGanttConfig():
'''public GanttConfig getGanttConfig()
'''
pass
def getToolbarConfig():
'''public ToolbarConfig getToolbarConfig()
'''
pass
def getPrintConfig():
'''public PrintConfig getPrintConfig()
'''
pass
def setCurrentUserInfo():
'''public void setCurrentUserInfo(final UserInfo currentUserInfo)
'''
pass
def setCreatedUserInfo():
'''public void setCreatedUserInfo(final UserInfo createdUserInfo)
'''
pass
def getProjectStartEnd():
'''public DateRange getProjectStartEnd()
'''
pass
def setProjectId():
'''public void setProjectId(final String id)
'''
pass
def getProjectId():
'''public String getProjectId()
'''
pass
def setProjectName():
'''public void setProjectName(final String name)
'''
pass
def setProjectDescription():
'''public void setProjectDescription(final String projectDescription)
'''
pass
def setScenarioName():
'''public void setScenarioName(final String name)
'''
pass
def setDefaultScenario():
'''public void setDefaultScenario(final boolean isDefault)
'''
pass
def setLocalizedScenarioTitle():
'''public void setLocalizedScenarioTitle(final String title)
'''
pass
def getProjectName():
'''public String getProjectName()
'''
pass
def getProjectDescription():
'''public String getProjectDescription()
'''
pass
def getScenarioName():
'''public String getScenarioName()
'''
pass
def isDefaultScenario():
'''public boolean isDefaultScenario()
'''
pass
def getLocalizedScenarioTitle():
'''public String getLocalizedScenarioTitle()
'''
pass
def getCalculatedProjectMinMax():
'''public DateRange getCalculatedProjectMinMax()
'''
pass
def getCalendarStartEnd():
'''public DateRange getCalendarStartEnd()
'''
pass
def setUseWith():
'''public void setUseWith(final String useWith)
'''
pass
def setProjectType():
'''public void setProjectType(final String projectType)
'''
pass
def setCalendarNum():
'''public void setCalendarNum(final String calNum)
'''
pass
def setOrgId():
'''public void setOrgId(final String orgId)
'''
pass
def setAssignStartDate():
'''public void setAssignStartDate(final Date date)
'''
pass
def setViewType():
'''public void setViewType(final boolean viewType)
'''
pass
def getUseWith():
'''public String getUseWith()
'''
pass
def getProjectType():
'''public String getProjectType()
'''
pass
def getCalendarNum():
'''public String getCalendarNum()
'''
pass
def getOrgId():
'''public String getOrgId()
'''
pass
def getAssignStartDate():
'''public Date getAssignStartDate()
'''
pass
def isViewType():
'''public boolean isViewType()
'''
pass
def setShowMaintOperFlag():
'''public void setShowMaintOperFlag(final boolean show)
'''
pass
def isShowMaintOperFlag():
'''public boolean isShowMaintOperFlag()
'''
pass
def isRollingProject():
'''public boolean isRollingProject()
'''
pass
def setRollingProject():
'''public void setRollingProject(final boolean isRollingProject)
'''
pass
def isRestrictWorkToDates():
'''public boolean isRestrictWorkToDates()
'''
pass
def setRestrictWorkToDates():
'''public void setRestrictWorkToDates(final boolean restrictWorkToDates)
'''
pass
def normalizeDates():
'''public void normalizeDates()
'''
pass
def getActualProjectStartEnd():
'''public Range<Date> getActualProjectStartEnd()
'''
pass
def getShiftCalendarInfo():
'''public HashMap<String, SKDCalendarInfo> getShiftCalendarInfo()
'''
pass
def setShiftCalendarInfo():
'''public void setShiftCalendarInfo(final HashMap<String, SKDCalendarInfo> shiftCalendarInfo)
'''
pass
def getShiftData():
'''public Map<String, SKDShiftWorkTime> getShiftData()
'''
pass
def getMergedWorkPeriods():
'''public ArrayList<Date> getMergedWorkPeriods()
'''
pass
def getShifts():
'''public List<String> getShifts()
'''
pass
def getShiftWorkTime():
'''public SKDShiftWorkTime getShiftWorkTime(final String shift)
'''
pass
def getProperties():
'''public Properties getProperties()
'''
pass
def setProperties():
'''public void setProperties(final Properties properties)
'''
pass
def setSkdActionInfo():
'''public void setSkdActionInfo(final HashMap<String, HashMap<String, SKDActionInfo>> info)
'''
pass
def getSkdActionInfo():
'''public HashMap<String, HashMap<String, SKDActionInfo>> getSkdActionInfo()
public HashMap<String, HashMap<String, SKDActionInfo>> getSkdActionInfo(final String useWith)
'''
pass
def setSkdActionUidInfo():
'''public void setSkdActionUidInfo(final HashMap<Long, SKDActionInfo> info)
'''
pass
def getSkdActionUidInfo():
'''public HashMap<Long, SKDActionInfo> getSkdActionUidInfo()
'''
pass
def getUserData():
'''public <T> T getUserData(final String key)
'''
pass
def setUserData():
'''public void setUserData(final String key, final Object data)
'''
pass
def getProjectMbo():
'''public MboRemote getProjectMbo()
'''
pass
def setProjectMbo():
'''public void setProjectMbo(final MboRemote projectMbo)
'''
pass
def getToolbarActions():
'''public List<SKDActionInfo> getToolbarActions()
'''
pass
def getShiftWorkPeriod():
'''public ArrayList<Date> getShiftWorkPeriod(final String shift)
'''
pass
def setActivityApplinkList():
'''public void setActivityApplinkList(final String className, final HashMap<String, HashMap<String, String>> list)
'''
pass
def getActivityApplinkList():
'''public HashMap<String, HashMap<String, String>> getActivityApplinkList(final String className)
'''
pass
def getChangedActivities():
'''public Set<Activity> getChangedActivities()
'''
pass
def getActualStartEnd():
'''public Range<Date> getActualStartEnd()
'''
pass
def reservationIteratorForResource():
'''public Iterator<IMXReservation> reservationIteratorForResource(final IMXResource resource)
'''
pass
def getNonEmptyTitleForProject():
'''public String getNonEmptyTitleForProject()
'''
pass
def getMergedNonWorkPeriod():
'''public ArrayList<Date> getMergedNonWorkPeriod()
'''
pass
def getGanttConfigInfo():
'''public IGanttConfigInfo getGanttConfigInfo()
'''
pass
def containsActivity():
'''public boolean containsActivity(final IMXActivity data)
'''
pass
def getParentForActivity():
'''public IMXActivity getParentForActivity(final IMXActivity data)
'''
pass
def getCalendarBreakPatternMap():
'''public HashMap getCalendarBreakPatternMap()
'''
pass
def getWorkPeriodPatternDaySeq():
'''public TreeMap<Date, String> getWorkPeriodPatternDaySeq()
'''
pass
def getCalendarBreakPatternCount():
'''public HashMap getCalendarBreakPatternCount()
'''
pass
def getLocalizedScenarioFieldTitle():
'''public String getLocalizedScenarioFieldTitle()
'''
pass
def getWorkHourList():
'''public HashMap<String, SKDCalendarInfo> getWorkHourList()
'''
pass
def setAssetLocWorkHourList():
'''public void setAssetLocWorkHourList(final HashMap<String, SKDCalendarInfo> assetMntCalMap)
'''
pass
def setAssetLocNonWorkHourList():
'''public void setAssetLocNonWorkHourList(final HashMap<String, SKDCalendarInfo> assetOpCalMap)
'''
pass
def setAssetLocOverlapMap():
'''public void setAssetLocOverlapMap(final HashMap<String, ArrayList<SKDDateInterval>> assetOverlapCalMap)
'''
pass
def setMergedNonWorkPeriod():
'''public void setMergedNonWorkPeriod(final ArrayList<Date> mergedNonWorkPeriods)
'''
pass
def setMergedWorkPeriod():
'''public void setMergedWorkPeriod(final ArrayList<Date> workPeriod)
'''
pass
def setWorkHourList():
'''public void setWorkHourList(final HashMap<String, SKDCalendarInfo> shiftCalMap)
'''
pass
def setCalendarBreakPatternMap():
'''public void setCalendarBreakPatternMap(final HashMap<String, ArrayList> calendarBreaks)
'''
pass
def setCalendarBreakPatternCount():
'''public void setCalendarBreakPatternCount(final HashMap<String, Integer> daysInShiftPattern)
'''
pass
def setWorkPeriodPatternDaySeq():
'''public void setWorkPeriodPatternDaySeq(final TreeMap<Date, String> workPeriodPatternDaySeq)
'''
pass
def getAppServiceCache():
'''public SKDAppServiceCache getAppServiceCache()
'''
pass
def setAppServiceCache():
'''public void setAppServiceCache(final SKDAppServiceCache cache)
'''
pass
def setAlternateAvail():
'''public void setAlternateAvail(final boolean useAlternateAvail)
'''
pass
def setResourceDisplay():
'''public void setResourceDisplay(final String resourceDisplay)
'''
pass
def setWeekday():
'''public void setWeekday(final String weekday)
'''
pass
def getActivityForId():
'''public IMXActivity getActivityForId(final String id)
'''
pass
def getActivitiesForWorkOrderId():
'''public List<Activity> getActivitiesForWorkOrderId(final Long workOrderId)
'''
pass
def addActivity():
'''public void addActivity(final String id, final Activity activity)
'''
pass
def removeActivity():
'''public void removeActivity(final Activity activity)
'''
pass
def addResource():
'''public void addResource(final String id, final Resource resource)
'''
pass
def getResourceForId():
'''public IMXResource getResourceForId(final String id)
'''
pass
def getActivities():
'''public Collection<Activity> getActivities()
'''
pass
def getResources():
'''public JSONArray getResources()
'''
pass
def setResources():
'''public void setResources(final JSONArray resources)
'''
pass
def getProjectPercentComplete():
'''public int getProjectPercentComplete(final IMXGanttModel.PercentCompleteType pcType)
'''
pass
def setProjectPercentComplete():
'''public void setProjectPercentComplete(final IMXGanttModel.PercentCompleteType pcType, final int val)
'''
pass
def getDisplayRowCount():
'''public int getDisplayRowCount()
'''
pass
def isPagingModel():
'''public boolean isPagingModel()
'''
pass
def getPages():
'''public int getPages()
'''
pass
def getPageSize():
'''public int getPageSize()
'''
pass
def setComplianceEnabled():
'''public void setComplianceEnabled(final boolean val)
'''
pass
def isComplianceEnabled():
'''public boolean isComplianceEnabled()
'''
pass
def getUserLocale():
'''public Locale getUserLocale()
'''
pass
def getUserULocale():
'''public ULocale getUserULocale()
'''
pass
def getUserTimezone():
'''public TimeZone getUserTimezone()
'''
pass
def isAlternateAvailEnabled():
'''public boolean isAlternateAvailEnabled()
'''
pass
def getResourceDisplay():
'''public String getResourceDisplay()
'''
pass
def getWeekDay():
'''public String getWeekDay()
'''
pass
def getProjectStartOffsetDays():
'''public int getProjectStartOffsetDays()
'''
pass
def getProjectEndOffsetDays():
'''public int getProjectEndOffsetDays()
'''
pass
def setProjectStartEnd():
'''public void setProjectStartEnd(final DateRange projectStartEnd)
'''
pass
def setProjectStartOffsetDays():
'''public void setProjectStartOffsetDays(final int projectStartOffsetDays)
'''
pass
def setProjectEndOffsetDays():
'''public void setProjectEndOffsetDays(final int projectEndOffsetDays)
'''
pass
def setCurrentVisibleRange():
'''public void setCurrentVisibleRange(final Range<Date> dateRange)
'''
pass
def getCurrentVisibleRange():
'''public Range<Date> getCurrentVisibleRange()
'''
pass
def iterateConstraintsFromActivity():
'''public Iterator<IMXConstraint> iterateConstraintsFromActivity(final IMXActivity activity)
'''
pass
def newConstraintFromActivity():
'''public void newConstraintFromActivity(final Object projectMbo, final IMXActivity activity, final ResultSet resultSet)
'''
pass
def getChildNodeCount():
'''public int getChildNodeCount(final IMXActivity activity)
'''
pass
def getChildNode():
'''public IMXActivity getChildNode(final IMXActivity activity, final int index)
'''
pass
def getRootNode():
'''public IMXActivity getRootNode()
'''
pass
def isAllowPastLoadEnabled():
'''public boolean isAllowPastLoadEnabled()
'''
pass
def setAllowPastLoad():
'''public void setAllowPastLoad(final boolean allowPastLoad)
'''
pass
def mergeChangedActivity():
'''public void mergeChangedActivity(final Activity activity)
'''
pass
def getResourceManager():
'''public WMAResourceManager getResourceManager()
'''
pass
def setResourceManager():
'''public void setResourceManager(final WMAResourceManager resManager)
'''
pass
def getDataManager():
'''public WMActivityDataManager getDataManager()
'''
pass
def setDataManager():
'''public void setDataManager(final WMActivityDataManager dataManager)
'''
pass
def reservationIteratorForActivity():
'''public Iterator<IMXReservation> reservationIteratorForActivity(final Activity activity)
'''
pass
def getSelectedFirstDayWeek():
'''public Date getSelectedFirstDayWeek()
'''
pass
def setSelectedFirstDayWeek():
'''public void setSelectedFirstDayWeek(final Date selectedFirstDayWeek)
'''
pass
def loadWeekData():
'''public void loadWeekData()
'''
pass
def reloadWeekData():
'''public void reloadWeekData()
'''
pass
def addMinimalResource():
'''public MinimalResource addMinimalResource(final String key, final String description, final String objectName)
'''
pass
def getMinimalResource():
'''public MinimalResource getMinimalResource(final String key)
'''
pass
def getWeekUtility():
'''public WeekUtility getWeekUtility()
'''
pass
def getResourceUtility():
'''public ResourceUtility getResourceUtility()
'''
pass
def initWeekUtility():
'''public void initWeekUtility()
'''
pass
def resetWeekUtility():
'''public void resetWeekUtility()
'''
pass
def saveChangedActivities():
'''public void saveChangedActivities()
'''
pass
def loadResource():
'''public void loadResource(final IMXResource resource)
'''
pass
def getAssignmentIDs():
'''public Set<Long> getAssignmentIDs()
'''
pass
def getActivitiesByResource():
'''public List<Activity> getActivitiesByResource(final String resource)
'''
pass
def addActivityByResource():
'''public void addActivityByResource(final String resource, final Activity activity)
'''
pass
def addCraftSkillRank():
'''public void addCraftSkillRank(final String craft, String skillLevel, final Integer rank)
'''
pass
def getCraftSkillRank():
'''public Integer getCraftSkillRank(final String craft, String skillLevel)
'''
pass
