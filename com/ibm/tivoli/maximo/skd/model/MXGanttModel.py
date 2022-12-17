def ():
    '''returns MXGanttModel\n\n
    ()\n
    '''
def setUserData():
    '''returns None\n\n
    setUserData(final String key, final Object data)\n
    '''
def getGanttConfigInfo():
    '''returns IGanttConfigInfo\n\n
    getGanttConfigInfo()\n
    '''
def setGanttConfigInfo():
    '''returns None\n\n
    setGanttConfigInfo(final IGanttConfigInfo ganttConfigInfo)\n
    '''
def setWorkHourList():
    '''returns None\n\n
    setWorkHourList(final HashMap<String, SKDCalendarInfo> skdCals)\n
    '''
def setSkdActionInfo():
    '''returns None\n\n
    setSkdActionInfo(final HashMap<String, HashMap<String, SKDActionInfo>> info)\n
    '''
def setSkdActionUidInfo():
    '''returns None\n\n
    setSkdActionUidInfo(final HashMap<Long, SKDActionInfo> info)\n
    '''
def setProjectStartDate():
    '''returns None\n\n
    setProjectStartDate(final Date start)\n
    '''
def getProjectStartDate():
    '''returns Date\n\n
    getProjectStartDate()\n
    '''
def setMergedNonWorkPeriod():
    '''returns None\n\n
    setMergedNonWorkPeriod(final ArrayList<Date> mergedWorkPeriods)\n
    '''
def getMergedNonWorkPeriod():
    '''returns ArrayList<Date>\n\n
    getMergedNonWorkPeriod()\n
    '''
def setMergedWorkPeriod():
    '''returns None\n\n
    setMergedWorkPeriod(final ArrayList<Date> mergedWorkPeriods)\n
    '''
def getMergedWorkPeriods():
    '''returns ArrayList<Date>\n\n
    getMergedWorkPeriods()\n
    '''
def setSortedActivityChildren():
    '''returns None\n\n
    setSortedActivityChildren(final Map<IlvActivity, List<IlvActivity>> sortedActivityChildren)\n
    '''
def setSortedResourceChildren():
    '''returns None\n\n
    setSortedResourceChildren(final Map<IlvResource, List<IlvResource>> sortedResourceChildren)\n
    '''
def getParentActivityIndex():
    '''returns int\n\n
    getParentActivityIndex(final IlvActivity activity)\n
    '''
def getChildActivity():
    '''returns IlvActivity\n\n
    getChildActivity(final IlvActivity parent, final int index)\n
    '''
def getChildActivityIndex():
    '''returns int\n\n
    getChildActivityIndex(final IlvActivity parent, final IlvActivity child)\n
    '''
def childActivityIterator():
    '''returns Iterator<IlvActivity>\n\n
    childActivityIterator(final IlvActivity parent)\n
    '''
def getChildIndex():
    '''returns int\n\n
    getChildIndex(final IlvHierarchyNode parent, final IlvHierarchyNode child)\n
    '''
def getParentResourceIndex():
    '''returns int\n\n
    getParentResourceIndex(final IlvResource resource)\n
    '''
def getChildResource():
    '''returns IlvResource\n\n
    getChildResource(final IlvResource parent, final int index)\n
    '''
def getChildResourceIndex():
    '''returns int\n\n
    getChildResourceIndex(final IlvResource parent, final IlvResource child)\n
    '''
def childResourceIterator():
    '''returns Iterator<IlvResource>\n\n
    childResourceIterator(final IlvResource parent)\n
    '''
def setActivityApplinkList():
    '''returns None\n\n
    setActivityApplinkList(final String className, final HashMap<String, HashMap<String, String>> list)\n
    '''
def setCalendarBreakPatternMap():
    '''returns None\n\n
    setCalendarBreakPatternMap(final HashMap<String, ArrayList> calendarBreakPattern)\n
    '''
def getCalendarBreakPatternMap():
    '''returns HashMap\n\n
    getCalendarBreakPatternMap()\n
    '''
def setCalendarBreakPatternCount():
    '''returns None\n\n
    setCalendarBreakPatternCount(final HashMap<String, Integer> daysInShiftPattern)\n
    '''
def getCalendarBreakPatternCount():
    '''returns HashMap\n\n
    getCalendarBreakPatternCount()\n
    '''
def getProjectEndDate():
    '''returns Date\n\n
    getProjectEndDate()\n
    '''
def setProjectEndDate():
    '''returns None\n\n
    setProjectEndDate(final Date endDate)\n
    '''
def isProjectReadOnly():
    '''returns boolean\n\n
    isProjectReadOnly()\n
    '''
def setProjectReadOnly():
    '''returns None\n\n
    setProjectReadOnly(final boolean projectReadOnly)\n
    '''
def setWorkPeriodPatternDaySeq():
    '''returns None\n\n
    setWorkPeriodPatternDaySeq(final TreeMap<Date, String> workPeriodPatternDaySeq)\n
    '''
def setAssetLocOverlapMap():
    '''returns None\n\n
    setAssetLocOverlapMap(final HashMap<String, ArrayList<SKDDateInterval>> assetLocOverlapCalMap)\n
    '''
def setAssetLocNonWorkHourList():
    '''returns None\n\n
    setAssetLocNonWorkHourList(final HashMap<String, SKDCalendarInfo> skdAssetLocNonWorkHourCals)\n
    '''
def setAssetLocWorkHourList():
    '''returns None\n\n
    setAssetLocWorkHourList(final HashMap<String, SKDCalendarInfo> skdAssetLocWorkHourCals)\n
    '''
def setProjectType():
    '''returns None\n\n
    setProjectType(final String projectType)\n
    '''
def getProjectType():
    '''returns String\n\n
    getProjectType()\n
    '''
def setShowMaintOperFlag():
    '''returns None\n\n
    setShowMaintOperFlag(final boolean showMaintOper)\n
    '''
def getShowMaintOperFlag():
    '''returns boolean\n\n
    getShowMaintOperFlag()\n
    '''
def getProjectId():
    '''returns String\n\n
    getProjectId()\n
    '''
def setProjectId():
    '''returns None\n\n
    setProjectId(final String projectId)\n
    '''
def getProjectName():
    '''returns String\n\n
    getProjectName()\n
    '''
def setProjectName():
    '''returns None\n\n
    setProjectName(final String projectName)\n
    '''
def getProjectDescription():
    '''returns String\n\n
    getProjectDescription()\n
    '''
def setProjectDescription():
    '''returns None\n\n
    setProjectDescription(final String projectDescription)\n
    '''
def getScenarioName():
    '''returns String\n\n
    getScenarioName()\n
    '''
def getUseWith():
    '''returns String\n\n
    getUseWith()\n
    '''
def setScenarioName():
    '''returns None\n\n
    setScenarioName(final String scenarioName)\n
    '''
def isDefaultScenario():
    '''returns boolean\n\n
    isDefaultScenario()\n
    '''
def setDefaultScenario():
    '''returns None\n\n
    setDefaultScenario(final boolean isDefaultScenario)\n
    '''
def getLocalizedScenarioFieldTitle():
    '''returns String\n\n
    getLocalizedScenarioFieldTitle()\n
    '''
def setLocalizedScenarioFieldTitle():
    '''returns None\n\n
    setLocalizedScenarioFieldTitle(final String localizedScenarioFieldTitle)\n
    '''
def setUseWith():
    '''returns None\n\n
    setUseWith(final String useWith)\n
    '''
def getShifts():
    '''returns List<String>\n\n
    getShifts()\n
    '''
def getShiftWorkTime():
    '''returns SKDShiftWorkTime\n\n
    getShiftWorkTime(final String shift)\n
    '''
def setAllowPastLoad():
    '''returns None\n\n
    setAllowPastLoad(final boolean allowPastLoad)\n
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
def setProperties():
    '''returns None\n\n
    setProperties(final Properties viewerProperties)\n
    '''
def getProperties():
    '''returns Properties\n\n
    getProperties()\n
    '''
def setUserTimezone():
    '''returns None\n\n
    setUserTimezone(final TimeZone timeZone)\n
    '''
def setUserLocale():
    '''returns None\n\n
    setUserLocale(final Locale locale)\n
    '''
def getUserLocale():
    '''returns Locale\n\n
    getUserLocale()\n
    '''
def getUserTimezone():
    '''returns TimeZone\n\n
    getUserTimezone()\n
    '''
def getUserULocale():
    '''returns ULocale\n\n
    getUserULocale()\n
    '''
def getActualStartEnd():
    '''returns Range<Date>\n\n
    getActualStartEnd()\n
    '''
def getProjectStartEnd():
    '''returns Range<Date>\n\n
    getProjectStartEnd()\n
    '''
def reservationIteratorForResource():
    '''returns Iterator<IMXReservation>\n\n
    reservationIteratorForResource(final IMXResource resource)\n
    '''
def containsActivity():
    '''returns boolean\n\n
    containsActivity(final IMXActivity data)\n
    '''
def getParentForActivity():
    '''returns IMXActivity\n\n
    getParentForActivity(final IMXActivity data)\n
    '''
def getPercentCompleteType():
    '''returns PercentCompleteType\n\n
    getPercentCompleteType()\n
    '''
def setPercentCompleteType():
    '''returns None\n\n
    setPercentCompleteType(PercentCompleteType type)\n
    '''
def getLoadDateTime():
    '''returns Date\n\n
    getLoadDateTime()\n
    '''
def setLoadDateTime():
    '''returns None\n\n
    setLoadDateTime(final Date loadDateTime)\n
    '''
def getCalendarStartEnd():
    '''returns DateRange\n\n
    getCalendarStartEnd()\n
    '''
def getCalculatedProjectMinMax():
    '''returns DateRange\n\n
    getCalculatedProjectMinMax()\n
    '''
def getProjectPercentComplete():
    '''returns int\n\n
    getProjectPercentComplete(final PercentCompleteType pcType)\n
    '''
def setProjectPercentComplete():
    '''returns None\n\n
    setProjectPercentComplete(final PercentCompleteType pcType, final int val)\n
    '''
def getDisplayRowCount():
    '''returns int\n\n
    getDisplayRowCount()\n
    '''
def isPagingModel():
    '''returns boolean\n\n
    isPagingModel()\n
    '''
def getPages():
    '''returns int\n\n
    getPages()\n
    '''
def getPageSize():
    '''returns int\n\n
    getPageSize()\n
    '''
def getActivityForId():
    '''returns IMXActivity\n\n
    getActivityForId(final String id)\n
    '''
def getResourceForId():
    '''returns IMXResource\n\n
    getResourceForId(final String id)\n
    '''
def setComplianceEnabled():
    '''returns None\n\n
    setComplianceEnabled(final boolean val)\n
    '''
def isComplianceEnabled():
    '''returns boolean\n\n
    isComplianceEnabled()\n
    '''
def getProjectStartOffsetDays():
    '''returns int\n\n
    getProjectStartOffsetDays()\n
    '''
def getProjectEndOffsetDays():
    '''returns int\n\n
    getProjectEndOffsetDays()\n
    '''
def setProjectStartOffsetDays():
    '''returns None\n\n
    setProjectStartOffsetDays(final int projectStartOffsetDays)\n
    '''
def setProjectEndOffsetDays():
    '''returns None\n\n
    setProjectEndOffsetDays(final int projectEndOffsetDays)\n
    '''
def isAlternateAvailEnabled():
    '''returns boolean\n\n
    isAlternateAvailEnabled()\n
    '''
def isAllowPastLoadEnabled():
    '''returns boolean\n\n
    isAllowPastLoadEnabled()\n
    '''
def getResourceDisplay():
    '''returns String\n\n
    getResourceDisplay()\n
    '''
def getWeekDay():
    '''returns String\n\n
    getWeekDay()\n
    '''
def iterateConstraintsFromActivity():
    '''returns Iterator<IMXConstraint>\n\n
    iterateConstraintsFromActivity(final IMXActivity activity)\n
    '''
def newConstraintFromActivity():
    '''returns None\n\n
    newConstraintFromActivity(final Object projectMbo, final IMXActivity fromActivity, final ResultSet resultSet)\n
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
def setRestrictWorkToDates():
    '''returns None\n\n
    setRestrictWorkToDates(final boolean isRestrictWorkToDates)\n
    '''
def isRestrictWorkToDates():
    '''returns boolean\n\n
    isRestrictWorkToDates()\n
    '''
def setEnabledRelatedAttributes():
    '''returns None\n\n
    setEnabledRelatedAttributes(final boolean isEnabledRelatedAttributes)\n
    '''
def isEnabledRelatedAttributes():
    '''returns boolean\n\n
    isEnabledRelatedAttributes()\n
    '''
