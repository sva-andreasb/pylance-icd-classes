def ():
    '''returns Schedule\n\n
    ()\n
    (final MboRemote project)\n
    '''
def getCurrentUserInfo():
    '''returns UserInfo\n\n
    getCurrentUserInfo()\n
    '''
def getCreatedUserInfo():
    '''returns UserInfo\n\n
    getCreatedUserInfo()\n
    '''
def getTableConfig():
    '''returns TableConfig\n\n
    getTableConfig()\n
    '''
def getGanttConfig():
    '''returns GanttConfig\n\n
    getGanttConfig()\n
    '''
def getToolbarConfig():
    '''returns ToolbarConfig\n\n
    getToolbarConfig()\n
    '''
def getPrintConfig():
    '''returns PrintConfig\n\n
    getPrintConfig()\n
    '''
def setCurrentUserInfo():
    '''returns None\n\n
    setCurrentUserInfo(final UserInfo currentUserInfo)\n
    '''
def setCreatedUserInfo():
    '''returns None\n\n
    setCreatedUserInfo(final UserInfo createdUserInfo)\n
    '''
def getProjectStartEnd():
    '''returns DateRange\n\n
    getProjectStartEnd()\n
    '''
def setProjectId():
    '''returns None\n\n
    setProjectId(final String id)\n
    '''
def getProjectId():
    '''returns String\n\n
    getProjectId()\n
    '''
def setProjectName():
    '''returns None\n\n
    setProjectName(final String name)\n
    '''
def setProjectDescription():
    '''returns None\n\n
    setProjectDescription(final String projectDescription)\n
    '''
def setScenarioName():
    '''returns None\n\n
    setScenarioName(final String name)\n
    '''
def setDefaultScenario():
    '''returns None\n\n
    setDefaultScenario(final boolean isDefault)\n
    '''
def setLocalizedScenarioTitle():
    '''returns None\n\n
    setLocalizedScenarioTitle(final String title)\n
    '''
def getProjectName():
    '''returns String\n\n
    getProjectName()\n
    '''
def getProjectDescription():
    '''returns String\n\n
    getProjectDescription()\n
    '''
def getScenarioName():
    '''returns String\n\n
    getScenarioName()\n
    '''
def isDefaultScenario():
    '''returns boolean\n\n
    isDefaultScenario()\n
    '''
def getLocalizedScenarioTitle():
    '''returns String\n\n
    getLocalizedScenarioTitle()\n
    '''
def getCalculatedProjectMinMax():
    '''returns DateRange\n\n
    getCalculatedProjectMinMax()\n
    '''
def getCalendarStartEnd():
    '''returns DateRange\n\n
    getCalendarStartEnd()\n
    '''
def setUseWith():
    '''returns None\n\n
    setUseWith(final String useWith)\n
    '''
def setProjectType():
    '''returns None\n\n
    setProjectType(final String projectType)\n
    '''
def setCalendarNum():
    '''returns None\n\n
    setCalendarNum(final String calNum)\n
    '''
def setOrgId():
    '''returns None\n\n
    setOrgId(final String orgId)\n
    '''
def setAssignStartDate():
    '''returns None\n\n
    setAssignStartDate(final Date date)\n
    '''
def setViewType():
    '''returns None\n\n
    setViewType(final boolean viewType)\n
    '''
def getUseWith():
    '''returns String\n\n
    getUseWith()\n
    '''
def getProjectType():
    '''returns String\n\n
    getProjectType()\n
    '''
def getCalendarNum():
    '''returns String\n\n
    getCalendarNum()\n
    '''
def getOrgId():
    '''returns String\n\n
    getOrgId()\n
    '''
def getAssignStartDate():
    '''returns Date\n\n
    getAssignStartDate()\n
    '''
def isViewType():
    '''returns boolean\n\n
    isViewType()\n
    '''
def setShowMaintOperFlag():
    '''returns None\n\n
    setShowMaintOperFlag(final boolean show)\n
    '''
def isShowMaintOperFlag():
    '''returns boolean\n\n
    isShowMaintOperFlag()\n
    '''
def isRollingProject():
    '''returns boolean\n\n
    isRollingProject()\n
    '''
def setRollingProject():
    '''returns None\n\n
    setRollingProject(final boolean isRollingProject)\n
    '''
def isRestrictWorkToDates():
    '''returns boolean\n\n
    isRestrictWorkToDates()\n
    '''
def setRestrictWorkToDates():
    '''returns None\n\n
    setRestrictWorkToDates(final boolean restrictWorkToDates)\n
    '''
def normalizeDates():
    '''returns None\n\n
    normalizeDates()\n
    '''
def getActualProjectStartEnd():
    '''returns Range<Date>\n\n
    getActualProjectStartEnd()\n
    '''
def setShiftCalendarInfo():
    '''returns None\n\n
    setShiftCalendarInfo(final HashMap<String, SKDCalendarInfo> shiftCalendarInfo)\n
    '''
def getMergedWorkPeriods():
    '''returns ArrayList<Date>\n\n
    getMergedWorkPeriods()\n
    '''
def getShifts():
    '''returns List<String>\n\n
    getShifts()\n
    '''
def getShiftWorkTime():
    '''returns SKDShiftWorkTime\n\n
    getShiftWorkTime(final String shift)\n
    '''
def getProperties():
    '''returns Properties\n\n
    getProperties()\n
    '''
def setProperties():
    '''returns None\n\n
    setProperties(final Properties properties)\n
    '''
def setSkdActionInfo():
    '''returns None\n\n
    setSkdActionInfo(final HashMap<String, HashMap<String, SKDActionInfo>> info)\n
    '''
def setSkdActionUidInfo():
    '''returns None\n\n
    setSkdActionUidInfo(final HashMap<Long, SKDActionInfo> info)\n
    '''
def setUserData():
    '''returns None\n\n
    setUserData(final String key, final Object data)\n
    '''
def getPagingManager():
    '''returns PagingManager\n\n
    getPagingManager()\n
    '''
def setPagingManager():
    '''returns None\n\n
    setPagingManager(final PagingManager pagingManager)\n
    '''
def getResourceManager():
    '''returns IResourceManager\n\n
    getResourceManager()\n
    '''
def setResourceManager():
    '''returns None\n\n
    setResourceManager(final IResourceManager resManager)\n
    '''
def getProjectMbo():
    '''returns MboRemote\n\n
    getProjectMbo()\n
    '''
def setProjectMbo():
    '''returns None\n\n
    setProjectMbo(final MboRemote projectMbo)\n
    '''
def applyConfigurationChange():
    '''returns None\n\n
    applyConfigurationChange(final JSONObject changes)\n
    '''
def getToolbarActions():
    '''returns List<SKDActionInfo>\n\n
    getToolbarActions()\n
    '''
def clone():
    '''returns Schedule\n\n
    clone()\n
    '''
def getShiftWorkPeriod():
    '''returns ArrayList<Date>\n\n
    getShiftWorkPeriod(final String shift)\n
    '''
def setActivityApplinkList():
    '''returns None\n\n
    setActivityApplinkList(final String className, final HashMap<String, HashMap<String, String>> list)\n
    '''
def getChangedActivities():
    '''returns Set<Activity>\n\n
    getChangedActivities()\n
    '''
def getChangedConstraints():
    '''returns Set<Constraint>\n\n
    getChangedConstraints()\n
    '''
def saveChangedActivities():
    '''returns None\n\n
    saveChangedActivities()\n
    '''
def saveChangedConstraints():
    '''returns None\n\n
    saveChangedConstraints()\n
    '''
def getActualStartEnd():
    '''returns Range<Date>\n\n
    getActualStartEnd()\n
    '''
def reservationIteratorForResource():
    '''returns Iterator<IMXReservation>\n\n
    reservationIteratorForResource(final IMXResource resource)\n
    '''
def getNonEmptyTitleForProject():
    '''returns String\n\n
    getNonEmptyTitleForProject()\n
    '''
def getMergedNonWorkPeriod():
    '''returns ArrayList<Date>\n\n
    getMergedNonWorkPeriod()\n
    '''
def getGanttConfigInfo():
    '''returns IGanttConfigInfo\n\n
    getGanttConfigInfo()\n
    '''
def containsActivity():
    '''returns boolean\n\n
    containsActivity(final IMXActivity data)\n
    '''
def getParentForActivity():
    '''returns IMXActivity\n\n
    getParentForActivity(final IMXActivity data)\n
    '''
def getCalendarBreakPatternMap():
    '''returns HashMap\n\n
    getCalendarBreakPatternMap()\n
    '''
def getCalendarBreakPatternCount():
    '''returns HashMap\n\n
    getCalendarBreakPatternCount()\n
    '''
def getLocalizedScenarioFieldTitle():
    '''returns String\n\n
    getLocalizedScenarioFieldTitle()\n
    '''
def setAssetLocWorkHourList():
    '''returns None\n\n
    setAssetLocWorkHourList(final HashMap<String, SKDCalendarInfo> assetMntCalMap)\n
    '''
def setAssetLocNonWorkHourList():
    '''returns None\n\n
    setAssetLocNonWorkHourList(final HashMap<String, SKDCalendarInfo> assetOpCalMap)\n
    '''
def setAssetLocOverlapMap():
    '''returns None\n\n
    setAssetLocOverlapMap(final HashMap<String, ArrayList<SKDDateInterval>> assetOverlapCalMap)\n
    '''
def setMergedNonWorkPeriod():
    '''returns None\n\n
    setMergedNonWorkPeriod(final ArrayList<Date> mergedNonWorkPeriods)\n
    '''
def setMergedWorkPeriod():
    '''returns None\n\n
    setMergedWorkPeriod(final ArrayList<Date> workPeriod)\n
    '''
def setWorkHourList():
    '''returns None\n\n
    setWorkHourList(final HashMap<String, SKDCalendarInfo> shiftCalMap)\n
    '''
def setCalendarBreakPatternMap():
    '''returns None\n\n
    setCalendarBreakPatternMap(final HashMap<String, ArrayList> calendarBreaks)\n
    '''
def setCalendarBreakPatternCount():
    '''returns None\n\n
    setCalendarBreakPatternCount(final HashMap<String, Integer> daysInShiftPattern)\n
    '''
def setWorkPeriodPatternDaySeq():
    '''returns None\n\n
    setWorkPeriodPatternDaySeq(final TreeMap<Date, String> workPeriodPatternDaySeq)\n
    '''
def getAppServiceCache():
    '''returns SKDAppServiceCache\n\n
    getAppServiceCache()\n
    '''
def setAppServiceCache():
    '''returns None\n\n
    setAppServiceCache(final SKDAppServiceCache cache)\n
    '''
def setAlternateAvail():
    '''returns None\n\n
    setAlternateAvail(final boolean useAlternateAvail)\n
    '''
def setResourceDisplay():
    '''returns None\n\n
    setResourceDisplay(final String resourceDisplay)\n
    '''
def setWeekday():
    '''returns None\n\n
    setWeekday(final String weekday)\n
    '''
def getActivityForId():
    '''returns IMXActivity\n\n
    getActivityForId(final String id)\n
    '''
def getResourceForId():
    '''returns IMXResource\n\n
    getResourceForId(final String id)\n
    '''
def mergeChangedActivity():
    '''returns None\n\n
    mergeChangedActivity(final Activity activity)\n
    '''
def mergeChangedConstraint():
    '''returns None\n\n
    mergeChangedConstraint(final Constraint constraint)\n
    '''
def setPercentCompleteType():
    '''returns None\n\n
    setPercentCompleteType(final PercentCompleteType pcType)\n
    '''
def getPercentCompleteType():
    '''returns PercentCompleteType\n\n
    getPercentCompleteType()\n
    '''
def getProjectPercentComplete():
    '''returns int\n\n
    getProjectPercentComplete(final PercentCompleteType pcType)\n
    '''
def setProjectPercentComplete():
    '''returns None\n\n
    setProjectPercentComplete(final PercentCompleteType pcType, final int val)\n
    '''
def getCompareRowCount():
    '''returns int\n\n
    getCompareRowCount(final Schedule leftModel, final long rightModelId)\n
    '''
def getDisplayRowCount():
    '''returns int\n\n
    getDisplayRowCount()\n
    '''
def isPagingModel():
    '''returns boolean\n\n
    isPagingModel()\n
    '''
def getComparePages():
    '''returns int\n\n
    getComparePages(final Schedule leftModel, final long rightModelId)\n
    '''
def getPages():
    '''returns int\n\n
    getPages()\n
    '''
def getPageSize():
    '''returns int\n\n
    getPageSize()\n
    '''
def setComplianceEnabled():
    '''returns None\n\n
    setComplianceEnabled(final boolean val)\n
    '''
def isComplianceEnabled():
    '''returns boolean\n\n
    isComplianceEnabled()\n
    '''
def getUserLocale():
    '''returns Locale\n\n
    getUserLocale()\n
    '''
def getUserULocale():
    '''returns ULocale\n\n
    getUserULocale()\n
    '''
def getUserTimezone():
    '''returns TimeZone\n\n
    getUserTimezone()\n
    '''
def isAlternateAvailEnabled():
    '''returns boolean\n\n
    isAlternateAvailEnabled()\n
    '''
def getResourceDisplay():
    '''returns String\n\n
    getResourceDisplay()\n
    '''
def getWeekDay():
    '''returns String\n\n
    getWeekDay()\n
    '''
def getProjectStartOffsetDays():
    '''returns int\n\n
    getProjectStartOffsetDays()\n
    '''
def getProjectEndOffsetDays():
    '''returns int\n\n
    getProjectEndOffsetDays()\n
    '''
def setProjectStartEnd():
    '''returns None\n\n
    setProjectStartEnd(final DateRange projectStartEnd)\n
    '''
def setProjectStartOffsetDays():
    '''returns None\n\n
    setProjectStartOffsetDays(final int projectStartOffsetDays)\n
    '''
def setProjectEndOffsetDays():
    '''returns None\n\n
    setProjectEndOffsetDays(final int projectEndOffsetDays)\n
    '''
def setCurrentVisibleRange():
    '''returns None\n\n
    setCurrentVisibleRange(final Range<Date> dateRange)\n
    '''
def getCurrentVisibleRange():
    '''returns Range<Date>\n\n
    getCurrentVisibleRange()\n
    '''
def iterateConstraintsFromActivity():
    '''returns Iterator<IMXConstraint>\n\n
    iterateConstraintsFromActivity(final IMXActivity activity)\n
    '''
def newConstraintFromActivity():
    '''returns None\n\n
    newConstraintFromActivity(final Object projectMbo, final IMXActivity activity, final ResultSet resultSet)\n
    '''
def getChildNodeCount():
    '''returns int\n\n
    getChildNodeCount(final IMXActivity activity)\n
    '''
def getChildNode():
    '''returns IMXActivity\n\n
    getChildNode(final IMXActivity activity, final int index)\n
    '''
def getRootNode():
    '''returns IMXActivity\n\n
    getRootNode()\n
    '''
def isAllowPastLoadEnabled():
    '''returns boolean\n\n
    isAllowPastLoadEnabled()\n
    '''
def setAllowPastLoad():
    '''returns None\n\n
    setAllowPastLoad(final boolean allowPastLoad)\n
    '''
def setCompareRowCount():
    '''returns None\n\n
    setCompareRowCount(final int rowCount)\n
    '''
def setComparePages():
    '''returns None\n\n
    setComparePages(final int pageCount)\n
    '''
