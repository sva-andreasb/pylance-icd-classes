def MXGanttModel():
'''public MXGanttModel()
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
def getGanttConfigInfo():
'''public IGanttConfigInfo getGanttConfigInfo()
'''
pass
def setGanttConfigInfo():
'''public void setGanttConfigInfo(final IGanttConfigInfo ganttConfigInfo)
'''
pass
def setWorkHourList():
'''public void setWorkHourList(final HashMap<String, SKDCalendarInfo> skdCals)
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
def getWorkHourList():
'''public HashMap<String, SKDCalendarInfo> getWorkHourList()
'''
pass
def setProjectStartDate():
'''public void setProjectStartDate(final Date start)
'''
pass
def getProjectStartDate():
'''public Date getProjectStartDate()
'''
pass
def setMergedNonWorkPeriod():
'''public void setMergedNonWorkPeriod(final ArrayList<Date> mergedWorkPeriods)
'''
pass
def getMergedNonWorkPeriod():
'''public ArrayList<Date> getMergedNonWorkPeriod()
'''
pass
def setMergedWorkPeriod():
'''public void setMergedWorkPeriod(final ArrayList<Date> mergedWorkPeriods)
'''
pass
def getMergedWorkPeriods():
'''public ArrayList<Date> getMergedWorkPeriods()
'''
pass
def setSortedActivityChildren():
'''public void setSortedActivityChildren(final Map<IlvActivity, List<IlvActivity>> sortedActivityChildren)
'''
pass
def getSortedActivityChildren():
'''public Map<IlvActivity, List<IlvActivity>> getSortedActivityChildren()
'''
pass
def setSortedResourceChildren():
'''public void setSortedResourceChildren(final Map<IlvResource, List<IlvResource>> sortedResourceChildren)
'''
pass
def getSortedResourceChildren():
'''public Map<IlvResource, List<IlvResource>> getSortedResourceChildren()
'''
pass
def getParentActivityIndex():
'''public int getParentActivityIndex(final IlvActivity activity)
'''
pass
def getChildActivity():
'''public IlvActivity getChildActivity(final IlvActivity parent, final int index)
'''
pass
def getChildActivityIndex():
'''public int getChildActivityIndex(final IlvActivity parent, final IlvActivity child)
'''
pass
def childActivityIterator():
'''public Iterator<IlvActivity> childActivityIterator(final IlvActivity parent)
'''
pass
def getChildIndex():
'''public int getChildIndex(final IlvHierarchyNode parent, final IlvHierarchyNode child)
'''
pass
def getParentResourceIndex():
'''public int getParentResourceIndex(final IlvResource resource)
'''
pass
def getChildResource():
'''public IlvResource getChildResource(final IlvResource parent, final int index)
'''
pass
def getChildResourceIndex():
'''public int getChildResourceIndex(final IlvResource parent, final IlvResource child)
'''
pass
def childResourceIterator():
'''public Iterator<IlvResource> childResourceIterator(final IlvResource parent)
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
def setCalendarBreakPatternMap():
'''public void setCalendarBreakPatternMap(final HashMap<String, ArrayList> calendarBreakPattern)
'''
pass
def getCalendarBreakPatternMap():
'''public HashMap getCalendarBreakPatternMap()
'''
pass
def setCalendarBreakPatternCount():
'''public void setCalendarBreakPatternCount(final HashMap<String, Integer> daysInShiftPattern)
'''
pass
def getCalendarBreakPatternCount():
'''public HashMap getCalendarBreakPatternCount()
'''
pass
def getProjectEndDate():
'''public Date getProjectEndDate()
'''
pass
def setProjectEndDate():
'''public void setProjectEndDate(final Date endDate)
'''
pass
def isProjectReadOnly():
'''public boolean isProjectReadOnly()
'''
pass
def setProjectReadOnly():
'''public void setProjectReadOnly(final boolean projectReadOnly)
'''
pass
def setWorkPeriodPatternDaySeq():
'''public void setWorkPeriodPatternDaySeq(final TreeMap<Date, String> workPeriodPatternDaySeq)
'''
pass
def getWorkPeriodPatternDaySeq():
'''public TreeMap<Date, String> getWorkPeriodPatternDaySeq()
'''
pass
def setAssetLocOverlapMap():
'''public void setAssetLocOverlapMap(final HashMap<String, ArrayList<SKDDateInterval>> assetLocOverlapCalMap)
'''
pass
def getAssetLocOverlapMap():
'''public HashMap<String, ArrayList<SKDDateInterval>> getAssetLocOverlapMap()
'''
pass
def setAssetLocNonWorkHourList():
'''public void setAssetLocNonWorkHourList(final HashMap<String, SKDCalendarInfo> skdAssetLocNonWorkHourCals)
'''
pass
def getAssetLocNonWorkHourList():
'''public HashMap<String, SKDCalendarInfo> getAssetLocNonWorkHourList()
'''
pass
def setAssetLocWorkHourList():
'''public void setAssetLocWorkHourList(final HashMap<String, SKDCalendarInfo> skdAssetLocWorkHourCals)
'''
pass
def getAssetLocWorkHourList():
'''public HashMap<String, SKDCalendarInfo> getAssetLocWorkHourList()
'''
pass
def setProjectType():
'''public void setProjectType(final String projectType)
'''
pass
def getProjectType():
'''public String getProjectType()
'''
pass
def setShowMaintOperFlag():
'''public void setShowMaintOperFlag(final boolean showMaintOper)
'''
pass
def getShowMaintOperFlag():
'''public boolean getShowMaintOperFlag()
'''
pass
def getProjectId():
'''public String getProjectId()
'''
pass
def setProjectId():
'''public void setProjectId(final String projectId)
'''
pass
def getProjectName():
'''public String getProjectName()
'''
pass
def setProjectName():
'''public void setProjectName(final String projectName)
'''
pass
def getProjectDescription():
'''public String getProjectDescription()
'''
pass
def setProjectDescription():
'''public void setProjectDescription(final String projectDescription)
'''
pass
def getScenarioName():
'''public String getScenarioName()
'''
pass
def getUseWith():
'''public String getUseWith()
'''
pass
def setScenarioName():
'''public void setScenarioName(final String scenarioName)
'''
pass
def isDefaultScenario():
'''public boolean isDefaultScenario()
'''
pass
def setDefaultScenario():
'''public void setDefaultScenario(final boolean isDefaultScenario)
'''
pass
def getLocalizedScenarioFieldTitle():
'''public String getLocalizedScenarioFieldTitle()
'''
pass
def setLocalizedScenarioFieldTitle():
'''public void setLocalizedScenarioFieldTitle(final String localizedScenarioFieldTitle)
'''
pass
def setUseWith():
'''public void setUseWith(final String useWith)
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
def setAllowPastLoad():
'''public void setAllowPastLoad(final boolean allowPastLoad)
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
def setProperties():
'''public void setProperties(final Properties viewerProperties)
'''
pass
def getProperties():
'''public Properties getProperties()
'''
pass
def setUserTimezone():
'''public void setUserTimezone(final TimeZone timeZone)
'''
pass
def setUserLocale():
'''public void setUserLocale(final Locale locale)
'''
pass
def getUserLocale():
'''public Locale getUserLocale()
'''
pass
def getUserTimezone():
'''public TimeZone getUserTimezone()
'''
pass
def getUserULocale():
'''public ULocale getUserULocale()
'''
pass
def getActualStartEnd():
'''public Range<Date> getActualStartEnd()
'''
pass
def getProjectStartEnd():
'''public Range<Date> getProjectStartEnd()
'''
pass
def getShiftCalendarInfo():
'''public HashMap<String, SKDCalendarInfo> getShiftCalendarInfo()
'''
pass
def reservationIteratorForResource():
'''public Iterator<IMXReservation> reservationIteratorForResource(final IMXResource resource)
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
def getPercentCompleteType():
'''public PercentCompleteType getPercentCompleteType()
'''
pass
def setPercentCompleteType():
'''public void setPercentCompleteType(PercentCompleteType type)
'''
pass
def getLoadDateTime():
'''public Date getLoadDateTime()
'''
pass
def setLoadDateTime():
'''public void setLoadDateTime(final Date loadDateTime)
'''
pass
def getCalendarStartEnd():
'''public DateRange getCalendarStartEnd()
'''
pass
def getCalculatedProjectMinMax():
'''public DateRange getCalculatedProjectMinMax()
'''
pass
def getProjectPercentComplete():
'''public int getProjectPercentComplete(final PercentCompleteType pcType)
'''
pass
def setProjectPercentComplete():
'''public void setProjectPercentComplete(final PercentCompleteType pcType, final int val)
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
def getActivityForId():
'''public IMXActivity getActivityForId(final String id)
'''
pass
def getResourceForId():
'''public IMXResource getResourceForId(final String id)
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
def getProjectStartOffsetDays():
'''public int getProjectStartOffsetDays()
'''
pass
def getProjectEndOffsetDays():
'''public int getProjectEndOffsetDays()
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
def isAlternateAvailEnabled():
'''public boolean isAlternateAvailEnabled()
'''
pass
def isAllowPastLoadEnabled():
'''public boolean isAllowPastLoadEnabled()
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
def iterateConstraintsFromActivity():
'''public Iterator<IMXConstraint> iterateConstraintsFromActivity(final IMXActivity activity)
'''
pass
def newConstraintFromActivity():
'''public void newConstraintFromActivity(final Object projectMbo, final IMXActivity fromActivity, final ResultSet resultSet)
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
def setRestrictWorkToDates():
'''public void setRestrictWorkToDates(final boolean isRestrictWorkToDates)
'''
pass
def isRestrictWorkToDates():
'''public boolean isRestrictWorkToDates()
'''
pass
def setEnabledRelatedAttributes():
'''public void setEnabledRelatedAttributes(final boolean isEnabledRelatedAttributes)
'''
pass
def isEnabledRelatedAttributes():
'''public boolean isEnabledRelatedAttributes()
'''
pass
