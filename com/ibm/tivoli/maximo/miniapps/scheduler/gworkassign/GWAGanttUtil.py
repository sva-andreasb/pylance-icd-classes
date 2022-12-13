def isValid():
    '''    public static boolean isValid(final Activity from, final Activity to, final UserInfo userInfo)
    '''
def isWorkorder():
    '''    public static boolean isWorkorder(final Activity mxa)
    '''
def isTask():
    '''    public static boolean isTask(final Activity act)
    '''
def toStringProps():
    '''    public static String toStringProps(final Activity from, final String... props)
    '''
def encodeFields():
    '''    public static void encodeFields(final IMXActivity act, final String[] fields, final GWASchedule model, final ReplyBuilder builder, final TreeGridUtil.ITGSerializationHelper helper)
    '''
def isInterruptable():
    '''    public static boolean isInterruptable(final GWASchedule model, final Activity mxa)
    public static boolean isInterruptable(final IMXGanttModel model, final IMXActivity mxa)
    '''
def getTGNWParts():
    '''    public static String getTGNWParts(final GWASchedule model, final Activity mxa, final TreeGridUtil.ITGSerializationHelper helper)
    public static String getTGNWParts(final IMXGanttModel model, final IMXActivity mxa, final TreeGridUtil.ITGSerializationHelper helper)
    '''
def equals():
    '''    public static boolean equals(final Activity mx1, final Activity mx2, final String propName)
    '''
def resolveSelectedActivitiesById():
    '''    public static List<Activity> resolveSelectedActivitiesById(final GWASchedule model, final List<Object> arr)
    '''
def isHidden():
    '''    public static boolean isHidden(final IMXActivity mxa)
    '''
def isDummy():
    '''    public static boolean isDummy(final IMXActivity next)
    '''
def isAssignmentDummy():
    '''    public static boolean isAssignmentDummy(final IMXActivity node)
    '''
def encodeActivityColumnValues():
    '''    public static void encodeActivityColumnValues(final TGJsonWriter jsonWriter, final IMXGanttModel model, final IMXActivity mxa, final boolean isRunBar, final TreeGridUtil.ITGSerializationHelper helper, final CompareMaxModelTGEmitter.ModelNumIDGenerator idGen)
    '''
def writeIDFields():
    '''    public static void writeIDFields(final TGJsonWriter jsonWriter, final IMXActivity mxa, final CompareMaxModelTGEmitter.ModelNumIDGenerator idGen)
    public static void writeIDFields(final TGJsonWriter jsonWriter, final IMXResource mxa, final CompareMaxModelTGEmitter.ModelNumIDGenerator idGen)
    '''
def isLocked():
    '''    public static boolean isLocked(final IMXActivity activity)
    '''
def showRequirementIcon():
    '''    public static boolean showRequirementIcon(final IMXActivity mxa)
    '''
def showWorklogIcon():
    '''    public static boolean showWorklogIcon(final IMXActivity mxa)
    '''
def isCompleted():
    '''    public static boolean isCompleted(final IMXActivity mxa)
    '''
def buildGWAAssignmentID():
    '''    public static String buildGWAAssignmentID(final String woNum, final String siteID, final String orgID, final Long assignmentID)
    public static String buildGWAAssignmentID(final MboRemote wo, final MboRemote assignment)
    '''
def buildGWAResourceID():
    '''    public static String buildGWAResourceID(final MboRemote labor, final MboRemote crew)
    public static String buildGWAResourceID(final String resource, final IMXActivity activity)
    '''
def addCellIcon():
    '''    public static void addCellIcon(final DataRow row, final String colName, final String imageUrl, final int iconWidth, String align, final TMenuItem item)
    '''
def detectAllConflicts():
    '''    public static void detectAllConflicts(final Activity resv, final GWASchedule model, final String resourceID, final ReplyBuilder reply)
    '''
def detectScheduleWindowConflict():
    '''    public static void detectScheduleWindowConflict(final GWASchedule model, final Activity activity, final ReplyBuilder reply)
    '''
def detectSkillMappingConflict():
    '''    public static void detectSkillMappingConflict(final GWASchedule model, final Activity activity, final String resourceID, final ReplyBuilder reply)
    '''
def setResources():
    '''    public static void setResources(final GWASchedule schedule, final Activity activity)
    '''
def setDateColumns():
    '''    public static void setDateColumns(final List<Column> dateCols, final JSONObject activity, final TimeZone userTimeZone)
    '''
def mergeWork():
    '''    public static ReplyBuilder mergeWork(final GWASchedule schedule, final Activity activity, final MboRemote skdProject, final UserInfo userInfo, final boolean unassign)
    '''
