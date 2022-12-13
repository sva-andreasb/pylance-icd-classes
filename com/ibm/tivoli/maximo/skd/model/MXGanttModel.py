def MXGanttModel():
    '''    public MXGanttModel()
    '''
def getUserData():
    '''    public <T> T getUserData(final String key)
    '''
def setUserData():
    '''    public void setUserData(final String key, final Object data)
    '''
def getGanttConfigInfo():
    '''    public IGanttConfigInfo getGanttConfigInfo()
    '''
def setGanttConfigInfo():
    '''    public void setGanttConfigInfo(final IGanttConfigInfo ganttConfigInfo)
    '''
def setWorkHourList():
    '''    public void setWorkHourList(final HashMap<String, SKDCalendarInfo> skdCals)
    '''
def setSkdActionInfo():
    '''    public void setSkdActionInfo(final HashMap<String, HashMap<String, SKDActionInfo>> info)
    '''
def getSkdActionInfo():
    '''    public HashMap<String, HashMap<String, SKDActionInfo>> getSkdActionInfo()
    public HashMap<String, HashMap<String, SKDActionInfo>> getSkdActionInfo(final String useWith)
    '''
def setSkdActionUidInfo():
    '''    public void setSkdActionUidInfo(final HashMap<Long, SKDActionInfo> info)
    '''
def getSkdActionUidInfo():
    '''    public HashMap<Long, SKDActionInfo> getSkdActionUidInfo()
    '''
def getWorkHourList():
    '''    public HashMap<String, SKDCalendarInfo> getWorkHourList()
    '''
def setProjectStartDate():
    '''    public void setProjectStartDate(final Date start)
    '''
def getProjectStartDate():
    '''    public Date getProjectStartDate()
    '''
def setMergedNonWorkPeriod():
    '''    public void setMergedNonWorkPeriod(final ArrayList<Date> mergedWorkPeriods)
    '''
def getMergedNonWorkPeriod():
    '''    public ArrayList<Date> getMergedNonWorkPeriod()
    '''
def setMergedWorkPeriod():
    '''    public void setMergedWorkPeriod(final ArrayList<Date> mergedWorkPeriods)
    '''
def getMergedWorkPeriods():
    '''    public ArrayList<Date> getMergedWorkPeriods()
    '''
def setSortedActivityChildren():
    '''    public void setSortedActivityChildren(final Map<IlvActivity, List<IlvActivity>> sortedActivityChildren)
    '''
def getSortedActivityChildren():
    '''    public Map<IlvActivity, List<IlvActivity>> getSortedActivityChildren()
    '''
def setSortedResourceChildren():
    '''    public void setSortedResourceChildren(final Map<IlvResource, List<IlvResource>> sortedResourceChildren)
    '''
def getSortedResourceChildren():
    '''    public Map<IlvResource, List<IlvResource>> getSortedResourceChildren()
    '''
def getParentActivityIndex():
    '''    public int getParentActivityIndex(final IlvActivity activity)
    '''
def getChildActivity():
    '''    public IlvActivity getChildActivity(final IlvActivity parent, final int index)
    '''
def getChildActivityIndex():
    '''    public int getChildActivityIndex(final IlvActivity parent, final IlvActivity child)
    '''
def childActivityIterator():
    '''    public Iterator<IlvActivity> childActivityIterator(final IlvActivity parent)
    '''
def getChildIndex():
    '''    public int getChildIndex(final IlvHierarchyNode parent, final IlvHierarchyNode child)
    '''
def getParentResourceIndex():
    '''    public int getParentResourceIndex(final IlvResource resource)
    '''
def getChildResource():
    '''    public IlvResource getChildResource(final IlvResource parent, final int index)
    '''
def getChildResourceIndex():
    '''    public int getChildResourceIndex(final IlvResource parent, final IlvResource child)
    '''
def childResourceIterator():
    '''    public Iterator<IlvResource> childResourceIterator(final IlvResource parent)
    '''
def setActivityApplinkList():
    '''    public void setActivityApplinkList(final String className, final HashMap<String, HashMap<String, String>> list)
    '''
def getActivityApplinkList():
    '''    public HashMap<String, HashMap<String, String>> getActivityApplinkList(final String className)
    '''
def setCalendarBreakPatternMap():
    '''    public void setCalendarBreakPatternMap(final HashMap<String, ArrayList> calendarBreakPattern)
    '''
def getCalendarBreakPatternMap():
    '''    public HashMap getCalendarBreakPatternMap()
    '''
def setCalendarBreakPatternCount():
    '''    public void setCalendarBreakPatternCount(final HashMap<String, Integer> daysInShiftPattern)
    '''
def getCalendarBreakPatternCount():
    '''    public HashMap getCalendarBreakPatternCount()
    '''
def getProjectEndDate():
    '''    public Date getProjectEndDate()
    '''
def setProjectEndDate():
    '''    public void setProjectEndDate(final Date endDate)
    '''
def isProjectReadOnly():
    '''    public boolean isProjectReadOnly()
    '''
def setProjectReadOnly():
    '''    public void setProjectReadOnly(final boolean projectReadOnly)
    '''
def setWorkPeriodPatternDaySeq():
    '''    public void setWorkPeriodPatternDaySeq(final TreeMap<Date, String> workPeriodPatternDaySeq)
    '''
def getWorkPeriodPatternDaySeq():
    '''    public TreeMap<Date, String> getWorkPeriodPatternDaySeq()
    '''
def setAssetLocOverlapMap():
    '''    public void setAssetLocOverlapMap(final HashMap<String, ArrayList<SKDDateInterval>> assetLocOverlapCalMap)
    '''
def getAssetLocOverlapMap():
    '''    public HashMap<String, ArrayList<SKDDateInterval>> getAssetLocOverlapMap()
    '''
def setAssetLocNonWorkHourList():
    '''    public void setAssetLocNonWorkHourList(final HashMap<String, SKDCalendarInfo> skdAssetLocNonWorkHourCals)
    '''
def getAssetLocNonWorkHourList():
    '''    public HashMap<String, SKDCalendarInfo> getAssetLocNonWorkHourList()
    '''
def setAssetLocWorkHourList():
    '''    public void setAssetLocWorkHourList(final HashMap<String, SKDCalendarInfo> skdAssetLocWorkHourCals)
    '''
def getAssetLocWorkHourList():
    '''    public HashMap<String, SKDCalendarInfo> getAssetLocWorkHourList()
    '''
def setProjectType():
    '''    public void setProjectType(final String projectType)
    '''
def getProjectType():
    '''    public String getProjectType()
    '''
def setShowMaintOperFlag():
    '''    public void setShowMaintOperFlag(final boolean showMaintOper)
    '''
def getShowMaintOperFlag():
    '''    public boolean getShowMaintOperFlag()
    '''
def getProjectId():
    '''    public String getProjectId()
    '''
def setProjectId():
    '''    public void setProjectId(final String projectId)
    '''
def getProjectName():
    '''    public String getProjectName()
    '''
def setProjectName():
    '''    public void setProjectName(final String projectName)
    '''
def getProjectDescription():
    '''    public String getProjectDescription()
    '''
def setProjectDescription():
    '''    public void setProjectDescription(final String projectDescription)
    '''
def getScenarioName():
    '''    public String getScenarioName()
    '''
def getUseWith():
    '''    public String getUseWith()
    '''
def setScenarioName():
    '''    public void setScenarioName(final String scenarioName)
    '''
def isDefaultScenario():
    '''    public boolean isDefaultScenario()
    '''
def setDefaultScenario():
    '''    public void setDefaultScenario(final boolean isDefaultScenario)
    '''
def getLocalizedScenarioFieldTitle():
    '''    public String getLocalizedScenarioFieldTitle()
    '''
def setLocalizedScenarioFieldTitle():
    '''    public void setLocalizedScenarioFieldTitle(final String localizedScenarioFieldTitle)
    '''
def setUseWith():
    '''    public void setUseWith(final String useWith)
    '''
def getShifts():
    '''    public List<String> getShifts()
    '''
def getShiftWorkTime():
    '''    public SKDShiftWorkTime getShiftWorkTime(final String shift)
    '''
def setAllowPastLoad():
    '''    public void setAllowPastLoad(final boolean allowPastLoad)
    '''
def setAlternateAvail():
    '''    public void setAlternateAvail(final boolean useAlternateAvail)
    '''
def setResourceDisplay():
    '''    public void setResourceDisplay(final String resourceDisplay)
    '''
def setWeekday():
    '''    public void setWeekday(final String weekday)
    '''
def setProperties():
    '''    public void setProperties(final Properties viewerProperties)
    '''
def getProperties():
    '''    public Properties getProperties()
    '''
def setUserTimezone():
    '''    public void setUserTimezone(final TimeZone timeZone)
    '''
def setUserLocale():
    '''    public void setUserLocale(final Locale locale)
    '''
def getUserLocale():
    '''    public Locale getUserLocale()
    '''
def getUserTimezone():
    '''    public TimeZone getUserTimezone()
    '''
def getUserULocale():
    '''    public ULocale getUserULocale()
    '''
def getActualStartEnd():
    '''    public Range<Date> getActualStartEnd()
    '''
def getProjectStartEnd():
    '''    public Range<Date> getProjectStartEnd()
    '''
def getShiftCalendarInfo():
    '''    public HashMap<String, SKDCalendarInfo> getShiftCalendarInfo()
    '''
def reservationIteratorForResource():
    '''    public Iterator<IMXReservation> reservationIteratorForResource(final IMXResource resource)
    '''
def containsActivity():
    '''    public boolean containsActivity(final IMXActivity data)
    '''
def getParentForActivity():
    '''    public IMXActivity getParentForActivity(final IMXActivity data)
    '''
def getPercentCompleteType():
    '''    public PercentCompleteType getPercentCompleteType()
    '''
def setPercentCompleteType():
    '''    public void setPercentCompleteType(PercentCompleteType type)
    '''
def getLoadDateTime():
    '''    public Date getLoadDateTime()
    '''
def setLoadDateTime():
    '''    public void setLoadDateTime(final Date loadDateTime)
    '''
def getCalendarStartEnd():
    '''    public DateRange getCalendarStartEnd()
    '''
def getCalculatedProjectMinMax():
    '''    public DateRange getCalculatedProjectMinMax()
    '''
def getProjectPercentComplete():
    '''    public int getProjectPercentComplete(final PercentCompleteType pcType)
    '''
def setProjectPercentComplete():
    '''    public void setProjectPercentComplete(final PercentCompleteType pcType, final int val)
    '''
def getDisplayRowCount():
    '''    public int getDisplayRowCount()
    '''
def isPagingModel():
    '''    public boolean isPagingModel()
    '''
def getPages():
    '''    public int getPages()
    '''
def getPageSize():
    '''    public int getPageSize()
    '''
def getActivityForId():
    '''    public IMXActivity getActivityForId(final String id)
    '''
def getResourceForId():
    '''    public IMXResource getResourceForId(final String id)
    '''
def setComplianceEnabled():
    '''    public void setComplianceEnabled(final boolean val)
    '''
def isComplianceEnabled():
    '''    public boolean isComplianceEnabled()
    '''
def getProjectStartOffsetDays():
    '''    public int getProjectStartOffsetDays()
    '''
def getProjectEndOffsetDays():
    '''    public int getProjectEndOffsetDays()
    '''
def setProjectStartOffsetDays():
    '''    public void setProjectStartOffsetDays(final int projectStartOffsetDays)
    '''
def setProjectEndOffsetDays():
    '''    public void setProjectEndOffsetDays(final int projectEndOffsetDays)
    '''
def isAlternateAvailEnabled():
    '''    public boolean isAlternateAvailEnabled()
    '''
def isAllowPastLoadEnabled():
    '''    public boolean isAllowPastLoadEnabled()
    '''
def getResourceDisplay():
    '''    public String getResourceDisplay()
    '''
def getWeekDay():
    '''    public String getWeekDay()
    '''
def iterateConstraintsFromActivity():
    '''    public Iterator<IMXConstraint> iterateConstraintsFromActivity(final IMXActivity activity)
    '''
def newConstraintFromActivity():
    '''    public void newConstraintFromActivity(final Object projectMbo, final IMXActivity fromActivity, final ResultSet resultSet)
    '''
def getChildNodeCount():
    '''    public int getChildNodeCount(final IMXActivity activity)
    '''
def getChildNode():
    '''    public IMXActivity getChildNode(final IMXActivity activity, final int index)
    '''
def getRootNode():
    '''    public IMXActivity getRootNode()
    '''
def setRestrictWorkToDates():
    '''    public void setRestrictWorkToDates(final boolean isRestrictWorkToDates)
    '''
def isRestrictWorkToDates():
    '''    public boolean isRestrictWorkToDates()
    '''
def setEnabledRelatedAttributes():
    '''    public void setEnabledRelatedAttributes(final boolean isEnabledRelatedAttributes)
    '''
def isEnabledRelatedAttributes():
    '''    public boolean isEnabledRelatedAttributes()
    '''
