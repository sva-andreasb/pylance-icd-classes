ROOT_NODE = "String  ROOT""
WO_INTERNAL_STATUS_APPR = "String  APPR""
PROPERTY_READ_ONLY_MODEL = "String  __READ_ONLY_MODEL""
def findActivityById():
'''public static IlvActivity findActivityById(final String id, final IlvHierarchyNode start, final IlvGanttModel model)
public static IMXActivity findActivityById(final String id, final MXGanttModel model)
'''
pass
def findResourceById():
'''public static IlvResource findResourceById(final String id, final IlvHierarchyNode start, final IlvGanttModel model)
'''
pass
def find():
'''public static IlvHierarchyNode find(final Predicate idp, final IlvHierarchyNode start, final IlvGanttModel model)
'''
pass
def isAssignment():
'''public static boolean isAssignment(final MXActivity mxa)
public static boolean isAssignment(final IlvActivity act)
'''
pass
def isOtherAssignment():
'''public static boolean isOtherAssignment(final MXActivity mxa)
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
public static boolean isHidden(final IlvHierarchyNode node)
'''
pass
def showWorklogIcon():
'''public static boolean showWorklogIcon(final MXActivity mxa)
'''
pass
def showRequirementIcon():
'''public static boolean showRequirementIcon(final MXActivity mxa)
'''
pass
def isDummy():
'''public static boolean isDummy(final IlvResource next)
public static boolean isDummy(final IMXActivity act)
'''
pass
def isCompleted():
'''public static boolean isCompleted(final MXActivity mxa)
'''
pass
def toStringArray():
'''public static Object toStringArray(final String[] items)
'''
pass
def getParentWorkorder():
'''public static MXActivity getParentWorkorder(final MXGanttModel model, final IlvActivity assignment)
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
def isWorkorder():
'''public static boolean isWorkorder(final IlvActivity act)
'''
pass
def isPM():
'''public static boolean isPM(final IlvActivity act)
public static boolean isPM(final IlvHierarchyNode act)
'''
pass
def hasChildren():
'''public static boolean hasChildren(final IlvHierarchyNode item, final IlvGanttModel model)
'''
pass
def hasAnyChildren():
'''public static boolean hasAnyChildren(final IlvHierarchyNode[] items, final IlvGanttModel model)
'''
pass
def addCrafts():
'''public static void addCrafts(final HashSet crafts, final IlvActivity item, final IlvGanttChart ganttChart)
'''
pass
def visitResource():
'''public static <T> void visitResource(final IlvResource item, final IlvGanttModel model, final IlvResourceVisitor<T> visitor, final T state)
'''
pass
def visitResources():
'''public static <T> void visitResources(final IlvResource[] items, final IlvGanttModel model, final IlvResourceVisitor<T> visitor, final T state)
'''
pass
def visitActivity():
'''public static <T> void visitActivity(final IlvActivity item, final IlvGanttModel model, final IlvActivityVisitor<T> visitor, final T state)
'''
pass
def visitNodes():
'''public static <T> void visitNodes(final IlvHierarchyNode[] items, final IlvGanttModel model, final IlvNodeVisitor<T> visitor, final T state)
'''
pass
def visitNode():
'''public static <T> void visitNode(final IlvHierarchyNode item, final IlvGanttModel model, final IlvNodeVisitor<T> visitor, final T state)
'''
pass
def visitActivities():
'''public static <T> void visitActivities(final IlvActivity[] items, final IlvGanttModel model, final IlvActivityVisitor<T> visitor, final T state)
'''
pass
def newAdjustTimeVisitor():
'''public static final IlvActivityVisitor<Set<String>> newAdjustTimeVisitor(final IlvDuration adjustment)
'''
pass
def visit():
'''public void visit(final IlvActivity item, final IlvGanttModel model, final Set<String> state)
public void visit(final IlvActivity item, final IlvGanttModel model, final HasCancelled state)
public void visit(final IlvActivity item, final IlvGanttModel model, final Void state)
public void visit(final IlvHierarchyNode item, final IlvGanttModel model, final Void state)
public void visit(final IlvActivity item, final IlvGanttModel model, final HasCancelled state)
public void visit(final IlvHierarchyNode type, final IlvGanttModel model, final Void state)
'''
pass
def moveToDay():
'''public static void moveToDay(final Calendar day, final IlvActivity[] selected, final IlvGanttModel model)
'''
pass
def dumpDebegInfoForContaints():
'''public static void dumpDebegInfoForContaints(final String msg, final Iterator<IlvConstraint> iter, final PrintStream out)
'''
pass
def dumpDebugInfoForContstraint():
'''public static void dumpDebugInfoForContstraint(final IlvConstraint c, final PrintStream out)
'''
pass
def dumpDebugCompareInfoForItems():
'''public static void dumpDebugCompareInfoForItems(final String msg, final IlvUserPropertyHolder item1, final IlvUserPropertyHolder item2, final PrintStream out)
'''
pass
def copyProperties():
'''public static void copyProperties(final IlvActivity src, final IlvActivity dest)
'''
pass
def getEarliestStartTime():
'''public static Date getEarliestStartTime(final IlvActivity[] selected)
'''
pass
def getLatestEndTime():
'''public static Date getLatestEndTime(final IlvActivity[] selected)
'''
pass
def getParent():
'''public static IlvActivity getParent(final IlvActivity act, final IlvGanttModel model)
'''
pass
def getParentSafely():
'''public static IlvActivity getParentSafely(final IlvActivity act, final IlvGanttModel model)
'''
pass
def getID():
'''public static String getID(final IMXActivity mxa)
public static String getID(String actid)
public static String getID(final IlvHierarchyNode node)
'''
pass
def setProperty():
'''public static boolean setProperty(final Object node, final String prop, final Object val)
'''
pass
def getProperty():
'''public static Object getProperty(final Object node, final String prop)
public static <T> T getProperty(final Object node, final String prop, final T defaultValue)
'''
pass
def createUnionTimeInterval():
'''public static IlvTimeInterval createUnionTimeInterval(final IlvHierarchyNode... nodes)
'''
pass
def isWorkorderApproved():
'''public static boolean isWorkorderApproved(final MXActivity source)
'''
pass
def getActivityById():
'''public static IlvActivity getActivityById(final IlvGanttModel model, final IlvActivity parent, final String id)
'''
pass
def getChildren():
'''public static IlvHierarchyNode[] getChildren(final IlvHierarchyNode item, final IlvGanttModel model)
'''
pass
def dumpDebugInfoForResource():
'''public static void dumpDebugInfoForResource(final IlvResource selectedresource, final IlvGanttModel model, final PrintStream out)
'''
pass
def count():
'''public static long count(final Iterator<?> items)
'''
pass
def countActivities():
'''public static long countActivities(final IlvGanttModel model)
'''
pass
def countResources():
'''public static long countResources(final IlvGanttModel model)
'''
pass
def countReservations():
'''public static long countReservations(final IlvGanttModel model)
'''
pass
def dumpModel():
'''public static void dumpModel(final String msg, final MXGanttModel model, final PrintStream out, final boolean simple)
'''
pass
def dumpActivity():
'''public static void dumpActivity(final MXGanttModel model, final IlvActivity rootActivity, final PrintStream out, final boolean simple, final int indent)
'''
pass
def isAssignmentDummy():
'''public static boolean isAssignmentDummy(final IlvHierarchyNode node)
'''
pass
def dumpReservationsForResource():
'''public static void dumpReservationsForResource(final MXResource mxr, final MXGanttModel model, final PrintStream out)
'''
pass
def updateProperty():
'''public static boolean updateProperty(final IMXActivity act, final String prop, final Object val)
'''
pass
def isTimeRollupEnabled():
'''public static boolean isTimeRollupEnabled()
'''
pass
def isAverageRollupEnabled():
'''public static boolean isAverageRollupEnabled()
'''
pass
def getRelatedActivity():
'''public static MXActivity getRelatedActivity(final MXGanttModel model, final MXActivity activity, final MXResource resource, final NodeLocation location)
'''
pass
def compare():
'''public int compare(final MXActivity o1, final MXActivity o2)
'''
pass
def calculateProjectMinMax():
'''public static DateRange calculateProjectMinMax(final IMXGanttModel model)
'''
pass
def isRootActivity():
'''public static boolean isRootActivity(final IMXActivity activity)
'''
pass
def getPecentCompleteFieldForType():
'''public static String getPecentCompleteFieldForType(final IMXGanttModel.PercentCompleteType pcType)
'''
pass
def getTravelTimeConstraintForToActivity():
'''public static MXTravelTimeConstraint getTravelTimeConstraintForToActivity(final MXGanttModel theModel, final IlvActivity activity)
'''
pass
def IlvDurationToDouble():
'''public static double IlvDurationToDouble(final IlvDuration lv, final UserInfo ui)
'''
pass
def encodeTreeGridActivityContraints():
'''public static String encodeTreeGridActivityContraints(final IMXGanttModel model, final IMXActivity mxa)
'''
pass
def getFormattedProjectID():
'''public static long getFormattedProjectID(final String projectId)
'''
pass
def removeIDPrefix():
'''public static String removeIDPrefix(String actid)
'''
pass
def convertTreeInFlatList():
'''public static JSONArray convertTreeInFlatList(final JSONArray tree)
'''
pass
def IDPredicate():
'''public IDPredicate(final String id)
'''
pass
def test():
'''public boolean test(final IlvActivity in)
public boolean test(final IlvResource in)
public boolean test(final IlvActivity in)
public boolean test(final IlvActivity in)
public boolean test(final IlvResource in)
'''
pass
def ResourceIDPredicate():
'''public ResourceIDPredicate(final String id)
'''
pass
def FieldPredicate():
'''public FieldPredicate(final String fld, final Object value)
'''
pass
def MultipleFieldsPredicate():
'''public MultipleFieldsPredicate(final List<String> flds, final List<Object> values)
'''
pass
def ResourceFieldPredicate():
'''public ResourceFieldPredicate(final String fld, final Object value)
'''
pass
def FindByIDActivityVisitor():
'''public FindByIDActivityVisitor(final String id)
'''
pass
def isCancelled():
'''public boolean isCancelled()
public boolean isCancelled()
'''
pass
def cancel():
'''public void cancel()
public void cancel()
'''
pass
def getActivity():
'''public IlvActivity getActivity()
'''
pass
def FilterActivityVisitor():
'''public FilterActivityVisitor(final IFilter<IlvActivity> filter)
'''
pass
def getActivities():
'''public List<IlvActivity> getActivities()
'''
pass
def FilterNodeVisitor():
'''public FilterNodeVisitor(final IFilter<IlvHierarchyNode> filter)
'''
pass
def getNodes():
'''public List<IlvHierarchyNode> getNodes()
'''
pass
def SameTypeVisitor():
'''public SameTypeVisitor(final List<String> objectNames)
'''
pass
def isValid():
'''public boolean isValid()
'''
pass
def canAccept():
'''public boolean canAccept(final IlvActivity act)
'''
pass
def CountingVisitor():
'''public CountingVisitor()
'''
pass
def getCount():
'''public long getCount()
'''
pass
