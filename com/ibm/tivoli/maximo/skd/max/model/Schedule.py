def Schedule():
    '''public Schedule()
    public Schedule(final MboRemote project)
    '''
def getCurrentUserInfo():
    '''public UserInfo getCurrentUserInfo()
    '''
def getCreatedUserInfo():
    '''public UserInfo getCreatedUserInfo()
    '''
def getTableConfig():
    '''public TableConfig getTableConfig()
    '''
def getGanttConfig():
    '''public GanttConfig getGanttConfig()
    '''
def getToolbarConfig():
    '''public ToolbarConfig getToolbarConfig()
    '''
def getPrintConfig():
    '''public PrintConfig getPrintConfig()
    '''
def setCurrentUserInfo():
    '''public void setCurrentUserInfo(final UserInfo currentUserInfo)
    '''
def setCreatedUserInfo():
    '''public void setCreatedUserInfo(final UserInfo createdUserInfo)
    '''
def getProjectStartEnd():
    '''public DateRange getProjectStartEnd()
    '''
def setProjectId():
    '''public void setProjectId(final String id)
    '''
def getProjectId():
    '''public String getProjectId()
    '''
def setProjectName():
    '''public void setProjectName(final String name)
    '''
def setProjectDescription():
    '''public void setProjectDescription(final String projectDescription)
    '''
def setScenarioName():
    '''public void setScenarioName(final String name)
    '''
def setDefaultScenario():
    '''public void setDefaultScenario(final boolean isDefault)
    '''
def setLocalizedScenarioTitle():
    '''public void setLocalizedScenarioTitle(final String title)
    '''
def getProjectName():
    '''public String getProjectName()
    '''
def getProjectDescription():
    '''public String getProjectDescription()
    '''
def getScenarioName():
    '''public String getScenarioName()
    '''
def isDefaultScenario():
    '''public boolean isDefaultScenario()
    '''
def getLocalizedScenarioTitle():
    '''public String getLocalizedScenarioTitle()
    '''
def getCalculatedProjectMinMax():
    '''public DateRange getCalculatedProjectMinMax()
    '''
def getCalendarStartEnd():
    '''public DateRange getCalendarStartEnd()
    '''
def setUseWith():
    '''public void setUseWith(final String useWith)
    '''
def setProjectType():
    '''public void setProjectType(final String projectType)
    '''
def setCalendarNum():
    '''public void setCalendarNum(final String calNum)
    '''
def setOrgId():
    '''public void setOrgId(final String orgId)
    '''
def setAssignStartDate():
    '''public void setAssignStartDate(final Date date)
    '''
def setViewType():
    '''public void setViewType(final boolean viewType)
    '''
def getUseWith():
    '''public String getUseWith()
    '''
def getProjectType():
    '''public String getProjectType()
    '''
def getCalendarNum():
    '''public String getCalendarNum()
    '''
def getOrgId():
    '''public String getOrgId()
    '''
def getAssignStartDate():
    '''public Date getAssignStartDate()
    '''
def isViewType():
    '''public boolean isViewType()
    '''
def setShowMaintOperFlag():
    '''public void setShowMaintOperFlag(final boolean show)
    '''
def isShowMaintOperFlag():
    '''public boolean isShowMaintOperFlag()
    '''
def isRollingProject():
    '''public boolean isRollingProject()
    '''
def setRollingProject():
    '''public void setRollingProject(final boolean isRollingProject)
    '''
def isRestrictWorkToDates():
    '''public boolean isRestrictWorkToDates()
    '''
def setRestrictWorkToDates():
    '''public void setRestrictWorkToDates(final boolean restrictWorkToDates)
    '''
def normalizeDates():
    '''public void normalizeDates()
    '''
def getActualProjectStartEnd():
    '''public Range<Date> getActualProjectStartEnd()
    '''
def getShiftCalendarInfo():
    '''public HashMap<String, SKDCalendarInfo> getShiftCalendarInfo()
    '''
def setShiftCalendarInfo():
    '''public void setShiftCalendarInfo(final HashMap<String, SKDCalendarInfo> shiftCalendarInfo)
    '''
def getShiftData():
    '''public Map<String, SKDShiftWorkTime> getShiftData()
    '''
def getMergedWorkPeriods():
    '''public ArrayList<Date> getMergedWorkPeriods()
    '''
def getShifts():
    '''public List<String> getShifts()
    '''
def getShiftWorkTime():
    '''public SKDShiftWorkTime getShiftWorkTime(final String shift)
    '''
def getProperties():
    '''public Properties getProperties()
    '''
def setProperties():
    '''public void setProperties(final Properties properties)
    '''
def setSkdActionInfo():
    '''public void setSkdActionInfo(final HashMap<String, HashMap<String, SKDActionInfo>> info)
    '''
def getSkdActionInfo():
    '''public HashMap<String, HashMap<String, SKDActionInfo>> getSkdActionInfo()
    public HashMap<String, HashMap<String, SKDActionInfo>> getSkdActionInfo(final String useWith)
    '''
def setSkdActionUidInfo():
    '''public void setSkdActionUidInfo(final HashMap<Long, SKDActionInfo> info)
    '''
def getSkdActionUidInfo():
    '''public HashMap<Long, SKDActionInfo> getSkdActionUidInfo()
    '''
def getUserData():
    '''public <T> T getUserData(final String key)
    '''
def setUserData():
    '''public void setUserData(final String key, final Object data)
    '''
def getPagingManager():
    '''public PagingManager getPagingManager()
    '''
def setPagingManager():
    '''public void setPagingManager(final PagingManager pagingManager)
    '''
def getResourceManager():
    '''public IResourceManager getResourceManager()
    '''
def setResourceManager():
    '''public void setResourceManager(final IResourceManager resManager)
    '''
def getProjectMbo():
    '''public MboRemote getProjectMbo()
    '''
def setProjectMbo():
    '''public void setProjectMbo(final MboRemote projectMbo)
    '''
def applyConfigurationChange():
    '''public void applyConfigurationChange(final JSONObject changes)
    '''
def getToolbarActions():
    '''public List<SKDActionInfo> getToolbarActions()
    '''
def clone():
    '''public Schedule clone()
    '''
def getShiftWorkPeriod():
    '''public ArrayList<Date> getShiftWorkPeriod(final String shift)
    '''
def setActivityApplinkList():
    '''public void setActivityApplinkList(final String className, final HashMap<String, HashMap<String, String>> list)
    '''
def getActivityApplinkList():
    '''public HashMap<String, HashMap<String, String>> getActivityApplinkList(final String className)
    '''
def getChangedActivities():
    '''public Set<Activity> getChangedActivities()
    '''
def getChangedConstraints():
    '''public Set<Constraint> getChangedConstraints()
    '''
def saveChangedActivities():
    '''public void saveChangedActivities()
    '''
def saveChangedConstraints():
    '''public void saveChangedConstraints()
    '''
def getActualStartEnd():
    '''public Range<Date> getActualStartEnd()
    '''
def reservationIteratorForResource():
    '''public Iterator<IMXReservation> reservationIteratorForResource(final IMXResource resource)
    '''
def getNonEmptyTitleForProject():
    '''public String getNonEmptyTitleForProject()
    '''
def getMergedNonWorkPeriod():
    '''public ArrayList<Date> getMergedNonWorkPeriod()
    '''
def getGanttConfigInfo():
    '''public IGanttConfigInfo getGanttConfigInfo()
    '''
def containsActivity():
    '''public boolean containsActivity(final IMXActivity data)
    '''
def getParentForActivity():
    '''public IMXActivity getParentForActivity(final IMXActivity data)
    '''
def getCalendarBreakPatternMap():
    '''public HashMap getCalendarBreakPatternMap()
    '''
def getWorkPeriodPatternDaySeq():
    '''public TreeMap<Date, String> getWorkPeriodPatternDaySeq()
    '''
def getCalendarBreakPatternCount():
    '''public HashMap getCalendarBreakPatternCount()
    '''
def getLocalizedScenarioFieldTitle():
    '''public String getLocalizedScenarioFieldTitle()
    '''
def getWorkHourList():
    '''public HashMap<String, SKDCalendarInfo> getWorkHourList()
    '''
def setAssetLocWorkHourList():
    '''public void setAssetLocWorkHourList(final HashMap<String, SKDCalendarInfo> assetMntCalMap)
    '''
def setAssetLocNonWorkHourList():
    '''public void setAssetLocNonWorkHourList(final HashMap<String, SKDCalendarInfo> assetOpCalMap)
    '''
def setAssetLocOverlapMap():
    '''public void setAssetLocOverlapMap(final HashMap<String, ArrayList<SKDDateInterval>> assetOverlapCalMap)
    '''
def setMergedNonWorkPeriod():
    '''public void setMergedNonWorkPeriod(final ArrayList<Date> mergedNonWorkPeriods)
    '''
def setMergedWorkPeriod():
    '''public void setMergedWorkPeriod(final ArrayList<Date> workPeriod)
    '''
def setWorkHourList():
    '''public void setWorkHourList(final HashMap<String, SKDCalendarInfo> shiftCalMap)
    '''
def setCalendarBreakPatternMap():
    '''public void setCalendarBreakPatternMap(final HashMap<String, ArrayList> calendarBreaks)
    '''
def setCalendarBreakPatternCount():
    '''public void setCalendarBreakPatternCount(final HashMap<String, Integer> daysInShiftPattern)
    '''
def setWorkPeriodPatternDaySeq():
    '''public void setWorkPeriodPatternDaySeq(final TreeMap<Date, String> workPeriodPatternDaySeq)
    '''
def getAppServiceCache():
    '''public SKDAppServiceCache getAppServiceCache()
    '''
def setAppServiceCache():
    '''public void setAppServiceCache(final SKDAppServiceCache cache)
    '''
def setAlternateAvail():
    '''public void setAlternateAvail(final boolean useAlternateAvail)
    '''
def setResourceDisplay():
    '''public void setResourceDisplay(final String resourceDisplay)
    '''
def setWeekday():
    '''public void setWeekday(final String weekday)
    '''
def getActivityForId():
    '''public IMXActivity getActivityForId(final String id)
    '''
def getResourceForId():
    '''public IMXResource getResourceForId(final String id)
    '''
def mergeChangedActivity():
    '''public void mergeChangedActivity(final Activity activity)
    '''
def mergeChangedConstraint():
    '''public void mergeChangedConstraint(final Constraint constraint)
    '''
def setPercentCompleteType():
    '''public void setPercentCompleteType(final PercentCompleteType pcType)
    '''
def getPercentCompleteType():
    '''public PercentCompleteType getPercentCompleteType()
    '''
def getProjectPercentComplete():
    '''public int getProjectPercentComplete(final PercentCompleteType pcType)
    '''
def setProjectPercentComplete():
    '''public void setProjectPercentComplete(final PercentCompleteType pcType, final int val)
    '''
def getCompareRowCount():
    '''public int getCompareRowCount(final Schedule leftModel, final long rightModelId)
    '''
def getDisplayRowCount():
    '''public int getDisplayRowCount()
    '''
def isPagingModel():
    '''public boolean isPagingModel()
    '''
def getComparePages():
    '''public int getComparePages(final Schedule leftModel, final long rightModelId)
    '''
def getPages():
    '''public int getPages()
    '''
def getPageSize():
    '''public int getPageSize()
    '''
def setComplianceEnabled():
    '''public void setComplianceEnabled(final boolean val)
    '''
def isComplianceEnabled():
    '''public boolean isComplianceEnabled()
    '''
def getUserLocale():
    '''public Locale getUserLocale()
    '''
def getUserULocale():
    '''public ULocale getUserULocale()
    '''
def getUserTimezone():
    '''public TimeZone getUserTimezone()
    '''
def isAlternateAvailEnabled():
    '''public boolean isAlternateAvailEnabled()
    '''
def getResourceDisplay():
    '''public String getResourceDisplay()
    '''
def getWeekDay():
    '''public String getWeekDay()
    '''
def getProjectStartOffsetDays():
    '''public int getProjectStartOffsetDays()
    '''
def getProjectEndOffsetDays():
    '''public int getProjectEndOffsetDays()
    '''
def setProjectStartEnd():
    '''public void setProjectStartEnd(final DateRange projectStartEnd)
    '''
def setProjectStartOffsetDays():
    '''public void setProjectStartOffsetDays(final int projectStartOffsetDays)
    '''
def setProjectEndOffsetDays():
    '''public void setProjectEndOffsetDays(final int projectEndOffsetDays)
    '''
def setCurrentVisibleRange():
    '''public void setCurrentVisibleRange(final Range<Date> dateRange)
    '''
def getCurrentVisibleRange():
    '''public Range<Date> getCurrentVisibleRange()
    '''
def iterateConstraintsFromActivity():
    '''public Iterator<IMXConstraint> iterateConstraintsFromActivity(final IMXActivity activity)
    '''
def newConstraintFromActivity():
    '''public void newConstraintFromActivity(final Object projectMbo, final IMXActivity activity, final ResultSet resultSet)
    '''
def getChildNodeCount():
    '''public int getChildNodeCount(final IMXActivity activity)
    '''
def getChildNode():
    '''public IMXActivity getChildNode(final IMXActivity activity, final int index)
    '''
def getRootNode():
    '''public IMXActivity getRootNode()
    '''
def isAllowPastLoadEnabled():
    '''public boolean isAllowPastLoadEnabled()
    '''
def setAllowPastLoad():
    '''public void setAllowPastLoad(final boolean allowPastLoad)
    '''
def setCompareRowCount():
    '''public void setCompareRowCount(final int rowCount)
    '''
def setComparePages():
    '''public void setComparePages(final int pageCount)
    '''
