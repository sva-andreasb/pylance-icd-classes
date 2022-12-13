RESOURCE_USERDATA_SHIFTDATES = "String  \"SHIFTDATES\""
BUCKET_BASED = "int  0"
TIME_BASED = "int  1"
ALL = "int  2"
def findActivityById():
    '''    public static IMXActivity findActivityById(final String id, final IMXGanttModel model)
    public static IlvActivity findActivityById(String id, final IlvHierarchyNode start, final IlvGanttModel model)
    '''
def writeAdditionalWorkOrderFieldsForAssignment():
    '''    public static void writeAdditionalWorkOrderFieldsForAssignment(final MXActivity act, final MXGanttModel model, final TGJsonWriter jsonWriter, final TreeGridUtil.ITGSerializationHelper helper)
    '''
def findResourceById():
    '''    public static IlvResource findResourceById(final String id, final IlvHierarchyNode start, final MXGanttModel model)
    public static IlvResource findResourceById(final String id, final MXGanttModel model)
    '''
def find():
    '''    public static IlvHierarchyNode find(final Predicate idp, final IlvHierarchyNode start, final IlvGanttModel model)
    public static IMXActivity find(final Predicate idp, final IMXActivity start, final IMXGanttModel model)
    '''
def toTreeGridDate():
    '''    public static long toTreeGridDate(final Date d, final TimeZone tz)
    '''
def toTreeGridUTCDate():
    '''    public static long toTreeGridUTCDate(final Date d)
    '''
def fromTreeGridDate():
    '''    public static Date fromTreeGridDate(final long ms, final TimeZone tz)
    '''
def getReadOnlyStyledText():
    '''    public static String getReadOnlyStyledText(final String value, final boolean readOnly)
    '''
def getProjectStartEnd():
    '''    public static Range<Date> getProjectStartEnd(final IMXGanttModel model)
    '''
def getActualStartEnd():
    '''    public static Range<Date> getActualStartEnd(final MXGanttModel model)
    '''
def addCellIcon():
    '''    public static void addCellIcon(final TGJsonWriter writer, final String colName, final String imageUrl, final int iconWidth, String align, final TMenuItem item)
    '''
def addLeftIconClass():
    '''    public static void addLeftIconClass(final TGJsonWriter jsonWriter, final String className)
    public static void addLeftIconClass(final TGJsonWriter jsonWriter, final String className, final String tip)
    '''
def addLeftIconClick():
    '''    public static void addLeftIconClick(final TGJsonWriter jsonWriter, final String eventName)
    '''
def addRightIconClass():
    '''    public static void addRightIconClass(final TGJsonWriter jsonWriter, final String className)
    public static void addRightIconClass(final TGJsonWriter jsonWriter, final String className, final String tip)
    '''
def addRightIconClick():
    '''    public static void addRightIconClick(final TGJsonWriter jsonWriter, final String eventName)
    '''
def isGanttColumn():
    '''    public static boolean isGanttColumn(final String col)
    '''
def isAssignment():
    '''    public static boolean isAssignment(final MXActivity mxa)
    '''
def isNonWork():
    '''    public static boolean isNonWork(final MXActivity mxa)
    '''
def getShiftPeriodsForResource():
    '''    public static List<Date> getShiftPeriodsForResource(final MXResource mxr, final MXGanttModel model)
    '''
def isWorkorder():
    '''    public static boolean isWorkorder(final IMXActivity mxa)
    '''
def isLabor():
    '''    public static boolean isLabor(final IMXResource mxr)
    '''
def isCrew():
    '''    public static boolean isCrew(final IMXResource mxr)
    '''
def isLocations():
    '''    public static boolean isLocations(final IMXResource mxr)
    '''
def isLaborOrCrew():
    '''    public static boolean isLaborOrCrew(final IMXResource mxr)
    '''
def isLaborOrCrewOrLocations():
    '''    public static boolean isLaborOrCrewOrLocations(final IMXResource mxr)
    '''
def isTask():
    '''    public static boolean isTask(final IMXActivity act)
    '''
def isReadOnly():
    '''    public static boolean isReadOnly(final MXActivity mxa)
    '''
def isLocked():
    '''    public static boolean isLocked(final MXActivity activity)
    '''
def isSecondary():
    '''    public static boolean isSecondary(final MXActivity mxa)
    '''
def isHidden():
    '''    public static boolean isHidden(final MXActivity mxa)
    '''
def write():
    '''    public static void write(final JSONObject json, final String name, final Object value, final TreeGridUtil.ITGSerializationHelper helper)
    public static void write(final TGJsonWriter jsonWriter, final String name, final Object value, final TreeGridUtil.ITGSerializationHelper helper)
    '''
def toSerializedValue():
    '''    public static Object toSerializedValue(final Object o, final TreeGridUtil.ITGSerializationHelper helper)
    '''
def showWorklogIcon():
    '''    public static boolean showWorklogIcon(final MXActivity mxa)
    '''
def getBoolean():
    '''    public static boolean getBoolean(final Object value)
    '''
def showRequirementIcon():
    '''    public static boolean showRequirementIcon(final MXActivity mxa)
    '''
def showWeatherAlertIcon():
    '''    public static boolean showWeatherAlertIcon(final MXActivity mxa)
    '''
def addClass():
    '''    public static void addClass(final TGJsonWriter writer, final String classUrl)
    '''
def addBold():
    '''    public static void addBold(final TGJsonWriter writer, final String boldUrl)
    '''
def showBoldResourceName():
    '''    public static boolean showBoldResourceName(final MXResource mxr)
    '''
def isSerializable():
    '''    public static boolean isSerializable(final String columnName, final Object data)
    '''
def isDummy():
    '''    public static boolean isDummy(final IlvResource next)
    '''
def applyReadonlyOrLocked():
    '''    public static void applyReadonlyOrLocked(final TGJsonWriter jsonWriter, final MXActivity mxa, final boolean isRunBar)
    '''
def isCompleted():
    '''    public static boolean isCompleted(final MXActivity mxa)
    '''
def newActivityColumn():
    '''    public static MXGanttPropertyInfo newActivityColumn(final String name, final int type)
    '''
def newResourceColumn():
    '''    public static MXGanttPropertyInfo newResourceColumn(final String name, final int type)
    '''
def sanitizeDateTimeFormatForTreeGrid():
    '''    public static String sanitizeDateTimeFormatForTreeGrid(final String mask)
    '''
def applyDefaultStyle():
    '''    public static void applyDefaultStyle(final JSONObject Cfg)
    '''
def getTGStyle():
    '''    public static String getTGStyle()
    '''
def getTGStylePrefix():
    '''    public static String getTGStylePrefix()
    '''
def addWorkPeriodInfo():
    '''    public static JSONObject addWorkPeriodInfo(final JSONObject gantt, final IMXGanttModel model, final Properties props, final List<String> shifts)
    '''
def getShiftColorId():
    '''    public static String getShiftColorId(final IMXGanttModel schedule, final Properties props, final String shift)
    '''
def getShiftColor():
    '''    public static String getShiftColor(final IMXGanttModel schedule, final Properties props, final String shift)
    '''
def getMergedShiftsAsBackground():
    '''    public static String getMergedShiftsAsBackground(final IMXGanttModel schedule)
    '''
def getShiftsAsBackground():
    '''    public static String getShiftsAsBackground(final IMXGanttModel schedule, final Properties props, final List<String> shifts)
    '''
def addWorkPeriodInfoAsTGInclude():
    '''    public static JSONObject addWorkPeriodInfoAsTGInclude(final JSONObject gantt, final MXGanttModel model, final UserInfo userInfo)
    '''
def getMergedShiftsAsInclude():
    '''    public static String getMergedShiftsAsInclude(final IMXGanttModel model, final UserInfo userInfo)
    '''
def appendBackground():
    '''    public static StringBuilder appendBackground(final StringBuilder sb, final Date start, final Date end, final TimeZone tz, final String tgColor)
    '''
def createBackground():
    '''    public static String createBackground(final Date start, final Date end, final TimeZone tz, final String tgColor)
    '''
def updateFormatForLocale():
    '''    public static void updateFormatForLocale(final JSONObject format, final UserInfo userInfo, final ISKDUIInfo skdUIInfo)
    '''
def getShortDateFormat():
    '''    public static String getShortDateFormat(final ISKDUIInfo skdUIInfo)
    '''
def addGanttZooms():
    '''    public static void addGanttZooms(final JSONObject root, final ISKDUIInfo skdUIInfo, final UIOptions options, final AbstractTreeGridMiniAppBean bean, final JSONObject Gantt)
    '''
def createZooms():
    '''    public static JSONArray createZooms(final Range<Date> range, int snapToGridInterval)
    '''
def createLevel():
    '''    public static JSONObject createLevel(final String name, final float width, final ZoomRangeSpec spec)
    '''
def getGanttUnits():
    '''    public static String getGanttUnits()
    '''
def addCommonGanttStartEnd():
    '''    public static void addCommonGanttStartEnd(final JSONObject Gantt, final IMXGanttModel model, final TimeZone timeZone)
    public static void addCommonGanttStartEnd(final JSONObject Gantt, final IMXGanttModel model, final TimeZone timeZone, final boolean fixedStartEnd)
    '''
def addCommonGantt():
    '''    public static void addCommonGantt(final JSONObject Gantt, final UIOptions opts)
    '''
def doReplacementsForZoom():
    '''    public static String doReplacementsForZoom(final String zoomJSON, final ISKDUIInfo skdUIInfo, final UIOptions options)
    '''
def createAndAddToolbar():
    '''    public static JSONObject createAndAddToolbar(final JSONObject root, final UIOptions options)
    '''
def addToolbarIcons():
    '''    public static JSONObject addToolbarIcons(final JSONObject Toolbar, final UIOptions options)
    '''
def addSafeCSS():
    '''    public static void addSafeCSS(final WebClientSession sess, final JSONObject Cfg)
    '''
def findContrantFor():
    '''    public static MXConstraint findContrantFor(final String fromId, final String toId, final MXGanttModel model)
    public static MXConstraint findContrantFor(final MXActivity from, final MXActivity to, final MXGanttModel model)
    '''
def getParentWorkorder():
    '''    public static MXActivity getParentWorkorder(final MXGanttModel model, final IlvActivity assignment)
    '''
def getParentWorkorderThatIsNotATask():
    '''    public static MXActivity getParentWorkorderThatIsNotATask(final MXGanttModel model, final IlvActivity assignment)
    '''
def getResourceForActivity():
    '''    public static MXResource getResourceForActivity(final MXGanttModel model, final MXActivity mxa)
    '''
def getSecondaryAssignmens():
    '''    public static List<MXActivity> getSecondaryAssignmens(final MXGanttModel model, final MXActivity primary)
    '''
def addCommonLangCFG():
    '''    public static void addCommonLangCFG(final JSONObject root, final UserInfo userInfo, final ISKDUIInfo skdUIInfo)
    '''
def setCommonPrintExportMenuOptions():
    '''    public static void setCommonPrintExportMenuOptions(final JSONObject root, final UserInfo userInfo)
    '''
def addCommonCFG():
    '''    public static void addCommonCFG(final WebClientSession sess, final JSONObject Cfg, final UIOptions options, final AbstractTreeGridMiniAppBean bean)
    '''
def addPerfOptions():
    '''    public static void addPerfOptions(final JSONObject Cfg, final UIOptions opts)
    '''
def addTreeDef():
    '''    public static void addTreeDef(final JSONArray Defs)
    '''
def addCommonActions():
    '''    public static void addCommonActions(final JSONObject root, final UIOptions options)
    '''
def ColMoveInSectionOnly():
    '''    public static JSONObject ColMoveInSectionOnly(final JSONObject col)
    '''
def writeIDFields():
    '''    public static void writeIDFields(final TGJsonWriter jsonWriter, final MXActivity mxa)
    public static void writeIDFields(final TGJsonWriter jsonWriter, final MXActivity mxa, final IDGenerator idGen)
    public static void writeIDFields(final TGJsonWriter jsonWriter, final IlvResource res, final IDGenerator idGen)
    '''
def getID():
    '''    public static String getID(final IMXActivity mxa)
    public static String getID(final IMXResource mxa)
    public static String getID(final IlvResource mxa)
    public static String getID(String actid)
    '''
def getTreeGridID():
    '''    public static String getTreeGridID(final String ilogID)
    '''
def isIDField():
    '''    public static boolean isIDField(final String s)
    '''
def IlvDurationToDouble():
    '''    public static double IlvDurationToDouble(final IlvDuration lv, final UserInfo ui)
    '''
def resolveSelectedActivities():
    '''    public static List<IlvActivity> resolveSelectedActivities(final MXGanttModel model, final List<String> activityIds)
    '''
def resolveSelectedActivitiesByUniqueIds():
    '''    public static List<IlvActivity> resolveSelectedActivitiesByUniqueIds(final MXGanttModel model, final List<Object> uniqueIds)
    '''
def encodeTreeGridActivityContraints():
    '''    public static String encodeTreeGridActivityContraints(final MXGanttModel model, final MXActivity mxa, final UserInfo userInfo)
    '''
def writeJsonActivityContraints():
    '''    public static void writeJsonActivityContraints(final JSONObject json, final MXGanttModel model, final MXActivity mxa, final UserInfo userInfo)
    '''
def encodeModifiedFields():
    '''    public static void encodeModifiedFields(final MXActivity act, final ReplyBuilder builder, final TreeGridUtil.ITGSerializationHelper helper)
    '''
def encodeFields():
    '''    public static void encodeFields(final IMXActivity act, final String[] fields, final MXGanttModel model, final ReplyBuilder builder, final TreeGridUtil.ITGSerializationHelper helper)
    '''
def findAssignedResource():
    '''    public static IlvResource findAssignedResource(final MXGanttModel model, final MXActivity mxa)
    '''
def equals():
    '''    public static boolean equals(final MXActivity mx1, final MXActivity mx2, final String propName)
    '''
def updateSecondarAssignments():
    '''    public static void updateSecondarAssignments(final MXGanttModel model, final MXActivity act, final ReplyBuilder reply, final TreeGridUtil.ITGSerializationHelper helper)
    '''
def updateSecondAssignment():
    '''    public static void updateSecondAssignment(final MXActivity pri, final MXActivity sec, final ReplyBuilder reply, final TreeGridUtil.ITGSerializationHelper helper)
    '''
def canProcessUpdateSecondaryAssignments():
    '''    public static boolean canProcessUpdateSecondaryAssignments(final MXGanttModel model, final MXActivity mxa)
    '''
def setLeftPanelOptions():
    '''    public static void setLeftPanelOptions(final JSONObject Panel, final UIOptions options)
    '''
def isInterruptable():
    '''    public static boolean isInterruptable(final MXGanttModel model, final MXActivity mxa)
    '''
def getActivityColumns():
    '''    public static List<IMXGanttPropertyInfo> getActivityColumns(final IGanttConfigInfo info)
    '''
def getResourceColumns():
    '''    public static List<IMXGanttPropertyInfo> getResourceColumns(final IGanttConfigInfo info)
    '''
def getNodeLocationDetails():
    '''    public static NodeLocation getNodeLocationDetails(final IlvGanttModel model, final IlvHierarchyNode node)
    '''
def addCommonPrintOptions():
    '''    public static void addCommonPrintOptions(final WebClientSession clientSession, final JSONObject cfg, final UIOptions options, final AbstractTreeGridMiniAppBean bean)
    '''
def isOtherAssignment():
    '''    public static boolean isOtherAssignment(final MXActivity act)
    public static boolean isOtherAssignment(final MXReservation act)
    public static boolean isOtherAssignment(final MXActivity act, final MXGanttModel model)
    '''
def isPhysicalPercentComplete():
    '''    public static boolean isPhysicalPercentComplete(final IMXGanttModel model)
    '''
def isTaskPercentComplete():
    '''    public static boolean isTaskPercentComplete(final IMXGanttModel model)
    '''
def isActualPercentComplete():
    '''    public static boolean isActualPercentComplete(final IMXGanttModel model)
    '''
def isPercentCompleteNone():
    '''    public static boolean isPercentCompleteNone(final IMXGanttModel model)
    '''
def getGanttComplete():
    '''    public static String getGanttComplete(final IMXGanttModel model)
    '''
def addComplianceDetails():
    '''    public static void addComplianceDetails(final TGJsonWriter jsonWriter, final IMXGanttModel model, final IMXActivity mxa, final AbstractTreeGridMiniAppBean bean, final TreeGridUtil.ITGSerializationHelper helper)
    '''
def getAssignmentsAndNonWork():
    '''    public static List<MXActivity> getAssignmentsAndNonWork(final MXGanttModel model, final MXResource mxr)
    '''
def getExtaWork():
    '''    public static List<MXActivity> getExtaWork(final MXGanttModel model, final MXResource mxr)
    '''
def detectConflicts():
    '''    public static void detectConflicts(final MXGanttModel model, final MXResource mxr, final ReplyBuilder reply)
    '''
def detectAllConflicts():
    '''    public static void detectAllConflicts(final MXActivity resv, final MXGanttModel model, final MXResource mxr, List<MXActivity> nonWork, final ReplyBuilder reply)
    '''
def isModAvail():
    '''    public static boolean isModAvail(final MXActivity a)
    '''
def isExtraTime():
    '''    public static boolean isExtraTime(final MXActivity a)
    '''
def detectShiftConflicts():
    '''    public static void detectShiftConflicts(final MXActivity resv, final MXGanttModel model, final MXResource mxr, final ReplyBuilder reply)
    '''
def getSequenceDay():
    '''    public static long getSequenceDay(final Date workPeriodBeginDate, final Date tempVisibleStartDate, final long patternDays, final TimeZone userTz, final Locale userLocale)
    '''
def getCalendarBreakRanges():
    '''    public static List<DateRange> getCalendarBreakRanges(final MXResource mxr, final MXGanttModel model)
    '''
def detectCalendarBreakConflicts():
    '''    public static void detectCalendarBreakConflicts(final MXActivity resv, final MXGanttModel model, final MXResource mxr, final ReplyBuilder reply)
    '''
def detectNonWorkAndDoubleBookedConflicts():
    '''    public static void detectNonWorkAndDoubleBookedConflicts(final MXActivity resv, final MXGanttModel model, final List<MXActivity> nonWork, final ReplyBuilder reply)
    '''
def buildInfoRow():
    '''    public static void buildInfoRow(final UIBuilder data, final IMXGanttModel schedule, final UIOptions options)
    '''
def getInfoRowText():
    '''    public static String getInfoRowText(final IMXGanttModel schedule, final UIOptions options)
    '''
def resolve():
    '''    public String resolve(final MapResolver resolver, final String functionName, final String[] args)
    '''
def getRelatedActivity():
    '''    public static MXActivity getRelatedActivity(final MXGanttModel model, final MXActivity activity, final MXResource resource, final NodeDirection location)
    '''
def compare():
    '''    public int compare(final MXActivity o1, final MXActivity o2)
    '''
def getStartLocation():
    '''    public static MXActivity getStartLocation(final MXGanttModel model, final MXResource resource)
    '''
def getEndLocation():
    '''    public static MXActivity getEndLocation(final MXGanttModel model, final MXResource resource)
    '''
def updateResourceTravelTimes():
    '''    public static MXResource updateResourceTravelTimes(final MXGanttModel model, final DispatchViewBean bean, final MXResource resource)
    '''
def cleanProperty():
    '''    public static String cleanProperty(final String in)
    '''
def convertDate():
    '''    public static Date convertDate(final Date date, final TimeZone timezone)
    '''
def getTGNWParts():
    '''    public static String getTGNWParts(final MXGanttModel model, final MXActivity mxa, final TreeGridUtil.ITGSerializationHelper helper)
    '''
def buildActivityID():
    '''    public static String buildActivityID(final MboRemote mbo, final String objectName, final String key)
    '''
def buildResourceID():
    '''    public static String buildResourceID(final String key, final String orgID)
    '''
def buildGResourceID():
    '''    public static String buildGResourceID(final String craft, final String key, final String orgID)
    '''
def getResourceObjectNames():
    '''    public static List<String> getResourceObjectNames(final int type)
    '''
def getMinRowHeight():
    '''    public static int getMinRowHeight()
    '''
def getDefaultRowHeight():
    '''    public static int getDefaultRowHeight()
    '''
def generateId():
    '''    public String generateId(final IlvHierarchyNode node)
    '''
def IDPredicate():
    '''    public IDPredicate(final String id)
    '''
def test():
    '''    public boolean test(final IMXActivity in)
    public boolean test(final IMXActivity in)
    public boolean test(final IlvResource in)
    public boolean test(final IlvResource in)
    '''
def FieldPredicate():
    '''    public FieldPredicate(final String fld, final Object value)
    '''
def ResourceIDPredicate():
    '''    public ResourceIDPredicate(final String id)
    '''
def ResourceFieldPredicate():
    '''    public ResourceFieldPredicate(final String fld, final Object value)
    '''
def ZoomRangeSpec():
    '''    public ZoomRangeSpec(final String name, final float maxWidth, final float minWidth, final int levels, final String units, final String roundUnits, final String dragUnits, final String h1, final String h2, final String h3, final int left, final int right, final String ganttBackground)
    '''
def NodeLocation():
    '''    public NodeLocation()
    '''
