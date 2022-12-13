ROOT_NODE = "String  \"ROOT\""
WO_INTERNAL_STATUS_APPR = "String  \"APPR\""
PROPERTY_READ_ONLY_MODEL = "String  \"__READ_ONLY_MODEL\""
def findActivityById():
    '''public static IlvActivity findActivityById(final String id, final IlvHierarchyNode start, final IlvGanttModel model)
    public static IMXActivity findActivityById(final String id, final MXGanttModel model)
    '''
def findResourceById():
    '''public static IlvResource findResourceById(final String id, final IlvHierarchyNode start, final IlvGanttModel model)
    '''
def find():
    '''public static IlvHierarchyNode find(final Predicate idp, final IlvHierarchyNode start, final IlvGanttModel model)
    '''
def isAssignment():
    '''public static boolean isAssignment(final MXActivity mxa)
    public static boolean isAssignment(final IlvActivity act)
    '''
def isOtherAssignment():
    '''public static boolean isOtherAssignment(final MXActivity mxa)
    '''
def isReadOnly():
    '''public static boolean isReadOnly(final MXActivity mxa)
    '''
def isLocked():
    '''public static boolean isLocked(final MXActivity activity)
    '''
def isSecondary():
    '''public static boolean isSecondary(final MXActivity mxa)
    '''
def isHidden():
    '''public static boolean isHidden(final MXActivity mxa)
    public static boolean isHidden(final IlvHierarchyNode node)
    '''
def showWorklogIcon():
    '''public static boolean showWorklogIcon(final MXActivity mxa)
    '''
def showRequirementIcon():
    '''public static boolean showRequirementIcon(final MXActivity mxa)
    '''
def isDummy():
    '''public static boolean isDummy(final IlvResource next)
    public static boolean isDummy(final IMXActivity act)
    '''
def isCompleted():
    '''public static boolean isCompleted(final MXActivity mxa)
    '''
def toStringArray():
    '''public static Object toStringArray(final String[] items)
    '''
def getParentWorkorder():
    '''public static MXActivity getParentWorkorder(final MXGanttModel model, final IlvActivity assignment)
    '''
def getResourceForActivity():
    '''public static MXResource getResourceForActivity(final MXGanttModel model, final MXActivity mxa)
    '''
def getSecondaryAssignmens():
    '''public static List<MXActivity> getSecondaryAssignmens(final MXGanttModel model, final MXActivity primary)
    '''
def isWorkorder():
    '''public static boolean isWorkorder(final IlvActivity act)
    '''
def isPM():
    '''public static boolean isPM(final IlvActivity act)
    public static boolean isPM(final IlvHierarchyNode act)
    '''
def hasChildren():
    '''public static boolean hasChildren(final IlvHierarchyNode item, final IlvGanttModel model)
    '''
def hasAnyChildren():
    '''public static boolean hasAnyChildren(final IlvHierarchyNode[] items, final IlvGanttModel model)
    '''
def addCrafts():
    '''public static void addCrafts(final HashSet crafts, final IlvActivity item, final IlvGanttChart ganttChart)
    '''
def visitResource():
    '''public static <T> void visitResource(final IlvResource item, final IlvGanttModel model, final IlvResourceVisitor<T> visitor, final T state)
    '''
def visitResources():
    '''public static <T> void visitResources(final IlvResource[] items, final IlvGanttModel model, final IlvResourceVisitor<T> visitor, final T state)
    '''
def visitActivity():
    '''public static <T> void visitActivity(final IlvActivity item, final IlvGanttModel model, final IlvActivityVisitor<T> visitor, final T state)
    '''
def visitNodes():
    '''public static <T> void visitNodes(final IlvHierarchyNode[] items, final IlvGanttModel model, final IlvNodeVisitor<T> visitor, final T state)
    '''
def visitNode():
    '''public static <T> void visitNode(final IlvHierarchyNode item, final IlvGanttModel model, final IlvNodeVisitor<T> visitor, final T state)
    '''
def visitActivities():
    '''public static <T> void visitActivities(final IlvActivity[] items, final IlvGanttModel model, final IlvActivityVisitor<T> visitor, final T state)
    '''
def newAdjustTimeVisitor():
    '''public static final IlvActivityVisitor<Set<String>> newAdjustTimeVisitor(final IlvDuration adjustment)
    '''
def visit():
    '''public void visit(final IlvActivity item, final IlvGanttModel model, final Set<String> state)
    public void visit(final IlvActivity item, final IlvGanttModel model, final HasCancelled state)
    public void visit(final IlvActivity item, final IlvGanttModel model, final Void state)
    public void visit(final IlvHierarchyNode item, final IlvGanttModel model, final Void state)
    public void visit(final IlvActivity item, final IlvGanttModel model, final HasCancelled state)
    public void visit(final IlvHierarchyNode type, final IlvGanttModel model, final Void state)
    '''
def moveToDay():
    '''public static void moveToDay(final Calendar day, final IlvActivity[] selected, final IlvGanttModel model)
    '''
def dumpDebegInfoForContaints():
    '''public static void dumpDebegInfoForContaints(final String msg, final Iterator<IlvConstraint> iter, final PrintStream out)
    '''
def dumpDebugInfoForContstraint():
    '''public static void dumpDebugInfoForContstraint(final IlvConstraint c, final PrintStream out)
    '''
def dumpDebugCompareInfoForItems():
    '''public static void dumpDebugCompareInfoForItems(final String msg, final IlvUserPropertyHolder item1, final IlvUserPropertyHolder item2, final PrintStream out)
    '''
def copyProperties():
    '''public static void copyProperties(final IlvActivity src, final IlvActivity dest)
    '''
def getEarliestStartTime():
    '''public static Date getEarliestStartTime(final IlvActivity[] selected)
    '''
def getLatestEndTime():
    '''public static Date getLatestEndTime(final IlvActivity[] selected)
    '''
def getParent():
    '''public static IlvActivity getParent(final IlvActivity act, final IlvGanttModel model)
    '''
def getParentSafely():
    '''public static IlvActivity getParentSafely(final IlvActivity act, final IlvGanttModel model)
    '''
def getID():
    '''public static String getID(final IMXActivity mxa)
    public static String getID(String actid)
    public static String getID(final IlvHierarchyNode node)
    '''
def setProperty():
    '''public static boolean setProperty(final Object node, final String prop, final Object val)
    '''
def getProperty():
    '''public static Object getProperty(final Object node, final String prop)
    public static <T> T getProperty(final Object node, final String prop, final T defaultValue)
    '''
def createUnionTimeInterval():
    '''public static IlvTimeInterval createUnionTimeInterval(final IlvHierarchyNode... nodes)
    '''
def isWorkorderApproved():
    '''public static boolean isWorkorderApproved(final MXActivity source)
    '''
def getActivityById():
    '''public static IlvActivity getActivityById(final IlvGanttModel model, final IlvActivity parent, final String id)
    '''
def getChildren():
    '''public static IlvHierarchyNode[] getChildren(final IlvHierarchyNode item, final IlvGanttModel model)
    '''
def dumpDebugInfoForResource():
    '''public static void dumpDebugInfoForResource(final IlvResource selectedresource, final IlvGanttModel model, final PrintStream out)
    '''
def count():
    '''public static long count(final Iterator<?> items)
    '''
def countActivities():
    '''public static long countActivities(final IlvGanttModel model)
    '''
def countResources():
    '''public static long countResources(final IlvGanttModel model)
    '''
def countReservations():
    '''public static long countReservations(final IlvGanttModel model)
    '''
def dumpModel():
    '''public static void dumpModel(final String msg, final MXGanttModel model, final PrintStream out, final boolean simple)
    '''
def dumpActivity():
    '''public static void dumpActivity(final MXGanttModel model, final IlvActivity rootActivity, final PrintStream out, final boolean simple, final int indent)
    '''
def isAssignmentDummy():
    '''public static boolean isAssignmentDummy(final IlvHierarchyNode node)
    '''
def dumpReservationsForResource():
    '''public static void dumpReservationsForResource(final MXResource mxr, final MXGanttModel model, final PrintStream out)
    '''
def updateProperty():
    '''public static boolean updateProperty(final IMXActivity act, final String prop, final Object val)
    '''
def isTimeRollupEnabled():
    '''public static boolean isTimeRollupEnabled()
    '''
def isAverageRollupEnabled():
    '''public static boolean isAverageRollupEnabled()
    '''
def getRelatedActivity():
    '''public static MXActivity getRelatedActivity(final MXGanttModel model, final MXActivity activity, final MXResource resource, final NodeLocation location)
    '''
def compare():
    '''public int compare(final MXActivity o1, final MXActivity o2)
    '''
def calculateProjectMinMax():
    '''public static DateRange calculateProjectMinMax(final IMXGanttModel model)
    '''
def isRootActivity():
    '''public static boolean isRootActivity(final IMXActivity activity)
    '''
def getPecentCompleteFieldForType():
    '''public static String getPecentCompleteFieldForType(final IMXGanttModel.PercentCompleteType pcType)
    '''
def getTravelTimeConstraintForToActivity():
    '''public static MXTravelTimeConstraint getTravelTimeConstraintForToActivity(final MXGanttModel theModel, final IlvActivity activity)
    '''
def IlvDurationToDouble():
    '''public static double IlvDurationToDouble(final IlvDuration lv, final UserInfo ui)
    '''
def encodeTreeGridActivityContraints():
    '''public static String encodeTreeGridActivityContraints(final IMXGanttModel model, final IMXActivity mxa)
    '''
def getFormattedProjectID():
    '''public static long getFormattedProjectID(final String projectId)
    '''
def removeIDPrefix():
    '''public static String removeIDPrefix(String actid)
    '''
def convertTreeInFlatList():
    '''public static JSONArray convertTreeInFlatList(final JSONArray tree)
    '''
def IDPredicate():
    '''public IDPredicate(final String id)
    '''
def test():
    '''public boolean test(final IlvActivity in)
    public boolean test(final IlvResource in)
    public boolean test(final IlvActivity in)
    public boolean test(final IlvActivity in)
    public boolean test(final IlvResource in)
    '''
def ResourceIDPredicate():
    '''public ResourceIDPredicate(final String id)
    '''
def FieldPredicate():
    '''public FieldPredicate(final String fld, final Object value)
    '''
def MultipleFieldsPredicate():
    '''public MultipleFieldsPredicate(final List<String> flds, final List<Object> values)
    '''
def ResourceFieldPredicate():
    '''public ResourceFieldPredicate(final String fld, final Object value)
    '''
def FindByIDActivityVisitor():
    '''public FindByIDActivityVisitor(final String id)
    '''
def isCancelled():
    '''public boolean isCancelled()
    public boolean isCancelled()
    '''
def cancel():
    '''public void cancel()
    public void cancel()
    '''
def getActivity():
    '''public IlvActivity getActivity()
    '''
def FilterActivityVisitor():
    '''public FilterActivityVisitor(final IFilter<IlvActivity> filter)
    '''
def getActivities():
    '''public List<IlvActivity> getActivities()
    '''
def FilterNodeVisitor():
    '''public FilterNodeVisitor(final IFilter<IlvHierarchyNode> filter)
    '''
def getNodes():
    '''public List<IlvHierarchyNode> getNodes()
    '''
def SameTypeVisitor():
    '''public SameTypeVisitor(final List<String> objectNames)
    '''
def isValid():
    '''public boolean isValid()
    '''
def canAccept():
    '''public boolean canAccept(final IlvActivity act)
    '''
def CountingVisitor():
    '''public CountingVisitor()
    '''
def getCount():
    '''public long getCount()
    '''
