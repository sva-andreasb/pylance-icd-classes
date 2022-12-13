RESOURCE_USERDATA_SHIFTDATES = "String  SHIFTDATES""
BUCKET_BASED = "int  0"
TIME_BASED = "int  1"
ALL = "int  2"
def findActivityById():
'''public static IMXActivity findActivityById(final String id, final IMXGanttModel model)
public static IlvActivity findActivityById(String id, final IlvHierarchyNode start, final IlvGanttModel model)
'''
pass
def writeAdditionalWorkOrderFieldsForAssignment():
'''public static void writeAdditionalWorkOrderFieldsForAssignment(final MXActivity act, final MXGanttModel model, final TGJsonWriter jsonWriter, final TreeGridUtil.ITGSerializationHelper helper)
'''
pass
def findResourceById():
'''public static IlvResource findResourceById(final String id, final IlvHierarchyNode start, final MXGanttModel model)
public static IlvResource findResourceById(final String id, final MXGanttModel model)
'''
pass
def find():
'''public static IlvHierarchyNode find(final Predicate idp, final IlvHierarchyNode start, final IlvGanttModel model)
public static IMXActivity find(final Predicate idp, final IMXActivity start, final IMXGanttModel model)
'''
pass
def toTreeGridDate():
'''public static long toTreeGridDate(final Date d, final TimeZone tz)
'''
pass
def toTreeGridUTCDate():
'''public static long toTreeGridUTCDate(final Date d)
'''
pass
def fromTreeGridDate():
'''public static Date fromTreeGridDate(final long ms, final TimeZone tz)
'''
pass
def getReadOnlyStyledText():
'''public static String getReadOnlyStyledText(final String value, final boolean readOnly)
'''
pass
def getProjectStartEnd():
'''public static Range<Date> getProjectStartEnd(final IMXGanttModel model)
'''
pass
def getActualStartEnd():
'''public static Range<Date> getActualStartEnd(final MXGanttModel model)
'''
pass
def addCellIcon():
'''public static void addCellIcon(final TGJsonWriter writer, final String colName, final String imageUrl, final int iconWidth, String align, final TMenuItem item)
'''
pass
def addLeftIconClass():
'''public static void addLeftIconClass(final TGJsonWriter jsonWriter, final String className)
public static void addLeftIconClass(final TGJsonWriter jsonWriter, final String className, final String tip)
'''
pass
def addLeftIconClick():
'''public static void addLeftIconClick(final TGJsonWriter jsonWriter, final String eventName)
'''
pass
def addRightIconClass():
'''public static void addRightIconClass(final TGJsonWriter jsonWriter, final String className)
public static void addRightIconClass(final TGJsonWriter jsonWriter, final String className, final String tip)
'''
pass
def addRightIconClick():
'''public static void addRightIconClick(final TGJsonWriter jsonWriter, final String eventName)
'''
pass
def isGanttColumn():
'''public static boolean isGanttColumn(final String col)
'''
pass
def isAssignment():
'''public static boolean isAssignment(final MXActivity mxa)
'''
pass
def isNonWork():
'''public static boolean isNonWork(final MXActivity mxa)
'''
pass
def getShiftPeriodsForResource():
'''public static List<Date> getShiftPeriodsForResource(final MXResource mxr, final MXGanttModel model)
'''
pass
def isWorkorder():
'''public static boolean isWorkorder(final IMXActivity mxa)
'''
pass
def isLabor():
'''public static boolean isLabor(final IMXResource mxr)
'''
pass
def isCrew():
'''public static boolean isCrew(final IMXResource mxr)
'''
pass
def isLocations():
'''public static boolean isLocations(final IMXResource mxr)
'''
pass
def isLaborOrCrew():
'''public static boolean isLaborOrCrew(final IMXResource mxr)
'''
pass
def isLaborOrCrewOrLocations():
'''public static boolean isLaborOrCrewOrLocations(final IMXResource mxr)
'''
pass
def isTask():
'''public static boolean isTask(final IMXActivity act)
'''
pass
def isReadOnly():
'''public static boolean isReadOnly(final MXActivity mxa)
'''
pass
def isLocked():
'''public static boolean isLocked(final MXActivity activity)
'''
pass
def isSecondary():
'''public static boolean isSecondary(final MXActivity mxa)
'''
pass
def isHidden():
'''public static boolean isHidden(final MXActivity mxa)
'''
pass
def write():
'''public static void write(final JSONObject json, final String name, final Object value, final TreeGridUtil.ITGSerializationHelper helper)
public static void write(final TGJsonWriter jsonWriter, final String name, final Object value, final TreeGridUtil.ITGSerializationHelper helper)
'''
pass
def toSerializedValue():
'''public static Object toSerializedValue(final Object o, final TreeGridUtil.ITGSerializationHelper helper)
'''
pass
def showWorklogIcon():
'''public static boolean showWorklogIcon(final MXActivity mxa)
'''
pass
def getBoolean():
'''public static boolean getBoolean(final Object value)
'''
pass
def showRequirementIcon():
'''public static boolean showRequirementIcon(final MXActivity mxa)
'''
pass
def showWeatherAlertIcon():
'''public static boolean showWeatherAlertIcon(final MXActivity mxa)
'''
pass
def addClass():
'''public static void addClass(final TGJsonWriter writer, final String classUrl)
'''
pass
def addBold():
'''public static void addBold(final TGJsonWriter writer, final String boldUrl)
'''
pass
def showBoldResourceName():
'''public static boolean showBoldResourceName(final MXResource mxr)
'''
pass
def isSerializable():
'''public static boolean isSerializable(final String columnName, final Object data)
'''
pass
def isDummy():
'''public static boolean isDummy(final IlvResource next)
'''
pass
def applyReadonlyOrLocked():
'''public static void applyReadonlyOrLocked(final TGJsonWriter jsonWriter, final MXActivity mxa, final boolean isRunBar)
'''
pass
def isCompleted():
'''public static boolean isCompleted(final MXActivity mxa)
'''
pass
def newActivityColumn():
'''public static MXGanttPropertyInfo newActivityColumn(final String name, final int type)
'''
pass
def newResourceColumn():
'''public static MXGanttPropertyInfo newResourceColumn(final String name, final int type)
'''
pass
def sanitizeDateTimeFormatForTreeGrid():
'''public static String sanitizeDateTimeFormatForTreeGrid(final String mask)
'''
pass
def applyDefaultStyle():
'''public static void applyDefaultStyle(final JSONObject Cfg)
'''
pass
def getTGStyle():
'''public static String getTGStyle()
'''
pass
def getTGStylePrefix():
'''public static String getTGStylePrefix()
'''
pass
def addWorkPeriodInfo():
'''public static JSONObject addWorkPeriodInfo(final JSONObject gantt, final IMXGanttModel model, final Properties props, final List<String> shifts)
'''
pass
def getShiftColorId():
'''public static String getShiftColorId(final IMXGanttModel schedule, final Properties props, final String shift)
'''
pass
def getShiftColor():
'''public static String getShiftColor(final IMXGanttModel schedule, final Properties props, final String shift)
'''
pass
def getMergedShiftsAsBackground():
'''public static String getMergedShiftsAsBackground(final IMXGanttModel schedule)
'''
pass
def getShiftsAsBackground():
'''public static String getShiftsAsBackground(final IMXGanttModel schedule, final Properties props, final List<String> shifts)
'''
pass
def addWorkPeriodInfoAsTGInclude():
'''public static JSONObject addWorkPeriodInfoAsTGInclude(final JSONObject gantt, final MXGanttModel model, final UserInfo userInfo)
'''
pass
def getMergedShiftsAsInclude():
'''public static String getMergedShiftsAsInclude(final IMXGanttModel model, final UserInfo userInfo)
'''
pass
def appendBackground():
'''public static StringBuilder appendBackground(final StringBuilder sb, final Date start, final Date end, final TimeZone tz, final String tgColor)
'''
pass
def createBackground():
'''public static String createBackground(final Date start, final Date end, final TimeZone tz, final String tgColor)
'''
pass
def updateFormatForLocale():
'''public static void updateFormatForLocale(final JSONObject format, final UserInfo userInfo, final ISKDUIInfo skdUIInfo)
'''
pass
def getShortDateFormat():
'''public static String getShortDateFormat(final ISKDUIInfo skdUIInfo)
'''
pass
def addGanttZooms():
'''public static void addGanttZooms(final JSONObject root, final ISKDUIInfo skdUIInfo, final UIOptions options, final AbstractTreeGridMiniAppBean bean, final JSONObject Gantt)
'''
pass
def createZooms():
'''public static JSONArray createZooms(final Range<Date> range, int snapToGridInterval)
'''
pass
def createLevel():
'''public static JSONObject createLevel(final String name, final float width, final ZoomRangeSpec spec)
'''
pass
def getGanttUnits():
'''public static String getGanttUnits()
'''
pass
def addCommonGanttStartEnd():
'''public static void addCommonGanttStartEnd(final JSONObject Gantt, final IMXGanttModel model, final TimeZone timeZone)
public static void addCommonGanttStartEnd(final JSONObject Gantt, final IMXGanttModel model, final TimeZone timeZone, final boolean fixedStartEnd)
'''
pass
def addCommonGantt():
'''public static void addCommonGantt(final JSONObject Gantt, final UIOptions opts)
'''
pass
def doReplacementsForZoom():
'''public static String doReplacementsForZoom(final String zoomJSON, final ISKDUIInfo skdUIInfo, final UIOptions options)
'''
pass
def createAndAddToolbar():
'''public static JSONObject createAndAddToolbar(final JSONObject root, final UIOptions options)
'''
pass
def addToolbarIcons():
'''public static JSONObject addToolbarIcons(final JSONObject Toolbar, final UIOptions options)
'''
pass
def addSafeCSS():
'''public static void addSafeCSS(final WebClientSession sess, final JSONObject Cfg)
'''
pass
def findContrantFor():
'''public static MXConstraint findContrantFor(final String fromId, final String toId, final MXGanttModel model)
public static MXConstraint findContrantFor(final MXActivity from, final MXActivity to, final MXGanttModel model)
'''
pass
def getParentWorkorder():
'''public static MXActivity getParentWorkorder(final MXGanttModel model, final IlvActivity assignment)
'''
pass
def getParentWorkorderThatIsNotATask():
'''public static MXActivity getParentWorkorderThatIsNotATask(final MXGanttModel model, final IlvActivity assignment)
'''
pass
def getResourceForActivity():
'''public static MXResource getResourceForActivity(final MXGanttModel model, final MXActivity mxa)
'''
pass
def getSecondaryAssignmens():
'''public static List<MXActivity> getSecondaryAssignmens(final MXGanttModel model, final MXActivity primary)
'''
pass
def addCommonLangCFG():
'''public static void addCommonLangCFG(final JSONObject root, final UserInfo userInfo, final ISKDUIInfo skdUIInfo)
'''
pass
def setCommonPrintExportMenuOptions():
'''public static void setCommonPrintExportMenuOptions(final JSONObject root, final UserInfo userInfo)
'''
pass
def addCommonCFG():
'''public static void addCommonCFG(final WebClientSession sess, final JSONObject Cfg, final UIOptions options, final AbstractTreeGridMiniAppBean bean)
'''
pass
def addPerfOptions():
'''public static void addPerfOptions(final JSONObject Cfg, final UIOptions opts)
'''
pass
def addTreeDef():
'''public static void addTreeDef(final JSONArray Defs)
'''
pass
def addCommonActions():
'''public static void addCommonActions(final JSONObject root, final UIOptions options)
'''
pass
def ColMoveInSectionOnly():
'''public static JSONObject ColMoveInSectionOnly(final JSONObject col)
'''
pass
def writeIDFields():
'''public static void writeIDFields(final TGJsonWriter jsonWriter, final MXActivity mxa)
public static void writeIDFields(final TGJsonWriter jsonWriter, final MXActivity mxa, final IDGenerator idGen)
public static void writeIDFields(final TGJsonWriter jsonWriter, final IlvResource res, final IDGenerator idGen)
'''
pass
def getID():
'''public static String getID(final IMXActivity mxa)
public static String getID(final IMXResource mxa)
public static String getID(final IlvResource mxa)
public static String getID(String actid)
'''
pass
def getTreeGridID():
'''public static String getTreeGridID(final String ilogID)
'''
pass
def isIDField():
'''public static boolean isIDField(final String s)
'''
pass
def IlvDurationToDouble():
'''public static double IlvDurationToDouble(final IlvDuration lv, final UserInfo ui)
'''
pass
def resolveSelectedActivities():
'''public static List<IlvActivity> resolveSelectedActivities(final MXGanttModel model, final List<String> activityIds)
'''
pass
def resolveSelectedActivitiesByUniqueIds():
'''public static List<IlvActivity> resolveSelectedActivitiesByUniqueIds(final MXGanttModel model, final List<Object> uniqueIds)
'''
pass
def encodeTreeGridActivityContraints():
'''public static String encodeTreeGridActivityContraints(final MXGanttModel model, final MXActivity mxa, final UserInfo userInfo)
'''
pass
def writeJsonActivityContraints():
'''public static void writeJsonActivityContraints(final JSONObject json, final MXGanttModel model, final MXActivity mxa, final UserInfo userInfo)
'''
pass
def encodeModifiedFields():
'''public static void encodeModifiedFields(final MXActivity act, final ReplyBuilder builder, final TreeGridUtil.ITGSerializationHelper helper)
'''
pass
def encodeFields():
'''public static void encodeFields(final IMXActivity act, final String[] fields, final MXGanttModel model, final ReplyBuilder builder, final TreeGridUtil.ITGSerializationHelper helper)
'''
pass
def findAssignedResource():
'''public static IlvResource findAssignedResource(final MXGanttModel model, final MXActivity mxa)
'''
pass
def equals():
'''public static boolean equals(final MXActivity mx1, final MXActivity mx2, final String propName)
'''
pass
def updateSecondarAssignments():
'''public static void updateSecondarAssignments(final MXGanttModel model, final MXActivity act, final ReplyBuilder reply, final TreeGridUtil.ITGSerializationHelper helper)
'''
pass
def updateSecondAssignment():
'''public static void updateSecondAssignment(final MXActivity pri, final MXActivity sec, final ReplyBuilder reply, final TreeGridUtil.ITGSerializationHelper helper)
'''
pass
def canProcessUpdateSecondaryAssignments():
'''public static boolean canProcessUpdateSecondaryAssignments(final MXGanttModel model, final MXActivity mxa)
'''
pass
def setLeftPanelOptions():
'''public static void setLeftPanelOptions(final JSONObject Panel, final UIOptions options)
'''
pass
def isInterruptable():
'''public static boolean isInterruptable(final MXGanttModel model, final MXActivity mxa)
'''
pass
def getActivityColumns():
'''public static List<IMXGanttPropertyInfo> getActivityColumns(final IGanttConfigInfo info)
'''
pass
def getResourceColumns():
'''public static List<IMXGanttPropertyInfo> getResourceColumns(final IGanttConfigInfo info)
'''
pass
def getNodeLocationDetails():
'''public static NodeLocation getNodeLocationDetails(final IlvGanttModel model, final IlvHierarchyNode node)
'''
pass
def addCommonPrintOptions():
'''public static void addCommonPrintOptions(final WebClientSession clientSession, final JSONObject cfg, final UIOptions options, final AbstractTreeGridMiniAppBean bean)
'''
pass
def isOtherAssignment():
'''public static boolean isOtherAssignment(final MXActivity act)
public static boolean isOtherAssignment(final MXReservation act)
public static boolean isOtherAssignment(final MXActivity act, final MXGanttModel model)
'''
pass
def isPhysicalPercentComplete():
'''public static boolean isPhysicalPercentComplete(final IMXGanttModel model)
'''
pass
def isTaskPercentComplete():
'''public static boolean isTaskPercentComplete(final IMXGanttModel model)
'''
pass
def isActualPercentComplete():
'''public static boolean isActualPercentComplete(final IMXGanttModel model)
'''
pass
def isPercentCompleteNone():
'''public static boolean isPercentCompleteNone(final IMXGanttModel model)
'''
pass
def getGanttComplete():
'''public static String getGanttComplete(final IMXGanttModel model)
'''
pass
def addComplianceDetails():
'''public static void addComplianceDetails(final TGJsonWriter jsonWriter, final IMXGanttModel model, final IMXActivity mxa, final AbstractTreeGridMiniAppBean bean, final TreeGridUtil.ITGSerializationHelper helper)
'''
pass
def getAssignmentsAndNonWork():
'''public static List<MXActivity> getAssignmentsAndNonWork(final MXGanttModel model, final MXResource mxr)
'''
pass
def getExtaWork():
'''public static List<MXActivity> getExtaWork(final MXGanttModel model, final MXResource mxr)
'''
pass
def detectConflicts():
'''public static void detectConflicts(final MXGanttModel model, final MXResource mxr, final ReplyBuilder reply)
'''
pass
def detectAllConflicts():
'''public static void detectAllConflicts(final MXActivity resv, final MXGanttModel model, final MXResource mxr, List<MXActivity> nonWork, final ReplyBuilder reply)
'''
pass
def isModAvail():
'''public static boolean isModAvail(final MXActivity a)
'''
pass
def isExtraTime():
'''public static boolean isExtraTime(final MXActivity a)
'''
pass
def detectShiftConflicts():
'''public static void detectShiftConflicts(final MXActivity resv, final MXGanttModel model, final MXResource mxr, final ReplyBuilder reply)
'''
pass
def getSequenceDay():
'''public static long getSequenceDay(final Date workPeriodBeginDate, final Date tempVisibleStartDate, final long patternDays, final TimeZone userTz, final Locale userLocale)
'''
pass
def getCalendarBreakRanges():
'''public static List<DateRange> getCalendarBreakRanges(final MXResource mxr, final MXGanttModel model)
'''
pass
def detectCalendarBreakConflicts():
'''public static void detectCalendarBreakConflicts(final MXActivity resv, final MXGanttModel model, final MXResource mxr, final ReplyBuilder reply)
'''
pass
def detectNonWorkAndDoubleBookedConflicts():
'''public static void detectNonWorkAndDoubleBookedConflicts(final MXActivity resv, final MXGanttModel model, final List<MXActivity> nonWork, final ReplyBuilder reply)
'''
pass
def buildInfoRow():
'''public static void buildInfoRow(final UIBuilder data, final IMXGanttModel schedule, final UIOptions options)
'''
pass
def getInfoRowText():
'''public static String getInfoRowText(final IMXGanttModel schedule, final UIOptions options)
'''
pass
def resolve():
'''public String resolve(final MapResolver resolver, final String functionName, final String[] args)
'''
pass
def getRelatedActivity():
'''public static MXActivity getRelatedActivity(final MXGanttModel model, final MXActivity activity, final MXResource resource, final NodeDirection location)
'''
pass
def compare():
'''public int compare(final MXActivity o1, final MXActivity o2)
'''
pass
def getStartLocation():
'''public static MXActivity getStartLocation(final MXGanttModel model, final MXResource resource)
'''
pass
def getEndLocation():
'''public static MXActivity getEndLocation(final MXGanttModel model, final MXResource resource)
'''
pass
def updateResourceTravelTimes():
'''public static MXResource updateResourceTravelTimes(final MXGanttModel model, final DispatchViewBean bean, final MXResource resource)
'''
pass
def cleanProperty():
'''public static String cleanProperty(final String in)
'''
pass
def convertDate():
'''public static Date convertDate(final Date date, final TimeZone timezone)
'''
pass
def getTGNWParts():
'''public static String getTGNWParts(final MXGanttModel model, final MXActivity mxa, final TreeGridUtil.ITGSerializationHelper helper)
'''
pass
def buildActivityID():
'''public static String buildActivityID(final MboRemote mbo, final String objectName, final String key)
'''
pass
def buildResourceID():
'''public static String buildResourceID(final String key, final String orgID)
'''
pass
def buildGResourceID():
'''public static String buildGResourceID(final String craft, final String key, final String orgID)
'''
pass
def getResourceObjectNames():
'''public static List<String> getResourceObjectNames(final int type)
'''
pass
def getMinRowHeight():
'''public static int getMinRowHeight()
'''
pass
def getDefaultRowHeight():
'''public static int getDefaultRowHeight()
'''
pass
def generateId():
'''public String generateId(final IlvHierarchyNode node)
'''
pass
def IDPredicate():
'''public IDPredicate(final String id)
'''
pass
def test():
'''public boolean test(final IMXActivity in)
public boolean test(final IMXActivity in)
public boolean test(final IlvResource in)
public boolean test(final IlvResource in)
'''
pass
def FieldPredicate():
'''public FieldPredicate(final String fld, final Object value)
'''
pass
def ResourceIDPredicate():
'''public ResourceIDPredicate(final String id)
'''
pass
def ResourceFieldPredicate():
'''public ResourceFieldPredicate(final String fld, final Object value)
'''
pass
def ZoomRangeSpec():
'''public ZoomRangeSpec(final String name, final float maxWidth, final float minWidth, final int levels, final String units, final String roundUnits, final String dragUnits, final String h1, final String h2, final String h3, final int left, final int right, final String ganttBackground)
'''
pass
def NodeLocation():
'''public NodeLocation()
'''
pass
