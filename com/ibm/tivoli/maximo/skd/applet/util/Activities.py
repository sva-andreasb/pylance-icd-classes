WO_INTERNAL_STATUS_APPR = "String  APPR""
PROPERTY_READ_ONLY_MODEL = "String  __READ_ONLY_MODEL""
def isWorkorder():
'''public static boolean isWorkorder(final IlvActivity act)
'''
pass
def isAssignment():
'''public static boolean isAssignment(final IlvActivity act)
'''
pass
def isPM():
'''public static boolean isPM(final IlvActivity act)
'''
pass
def hasChildren():
'''public static boolean hasChildren(final IlvHierarchyNode item, final IlvHierarchyChart chart)
'''
pass
def hasAnyChildren():
'''public static boolean hasAnyChildren(final IlvHierarchyNode[] items, final IlvHierarchyChart chart)
'''
pass
def addCrafts():
'''public static void addCrafts(final HashSet crafts, final IlvActivity item, final IlvGanttChart ganttChart)
'''
pass
def visitResource():
'''public static <T> void visitResource(final IlvResource item, final IlvHierarchyChart chart, final IlvResourceVisitor<T> visitor, final T state)
'''
pass
def visitResources():
'''public static <T> void visitResources(final IlvResource[] items, final IlvHierarchyChart chart, final IlvResourceVisitor<T> visitor, final T state)
'''
pass
def visitActivity():
'''public static <T> void visitActivity(final IlvActivity item, final IlvGanttChart ganttChart, final IlvActivityVisitor<T> visitor, final T state)
'''
pass
def visitNodes():
'''public static <T> void visitNodes(final IlvHierarchyNode[] items, final IlvHierarchyChart ganttChart, final IlvNodeVisitor<T> visitor, final T state)
'''
pass
def visitNode():
'''public static <T> void visitNode(final IlvHierarchyNode item, final IlvHierarchyChart chart, final IlvNodeVisitor<T> visitor, final T state)
'''
pass
def visitActivities():
'''public static <T> void visitActivities(final IlvActivity[] items, final IlvGanttChart ganttChart, final IlvActivityVisitor<T> visitor, final T state)
'''
pass
def newAdjustTimeVisitor():
'''public static final IlvActivityVisitor<Set<String>> newAdjustTimeVisitor(final IlvDuration adjustment)
'''
pass
def visit():
'''public void visit(final IlvActivity item, final IlvGanttChart chart, final Set<String> state)
public void visit(final IlvActivity item, final IlvGanttChart chart, final Set<String> state)
public void visit(final IlvActivity item, final IlvGanttChart chart, final Void state)
public void visit(final IlvHierarchyNode item, final IlvHierarchyChart chart, final Void state)
public void visit(final IlvActivity item, final IlvGanttChart chart, final HasCancelled state)
public void visit(final IlvActivity item, final IlvGanttChart chart, final Void state)
public void visit(final IlvHierarchyNode item, final IlvHierarchyChart chart, final Void state)
public void visit(final IlvActivity item, final IlvGanttChart chart, final HasCancelled state)
public void visit(final IlvHierarchyNode type, final IlvHierarchyChart chart, final Void state)
'''
pass
def getActivityContextMenu():
'''public static JPopupMenu getActivityContextMenu(final IlvActivity item, final IlvGanttChart gchart)
'''
pass
def actionPerformed():
'''public void actionPerformed(final ActionEvent e)
public void actionPerformed(final ActionEvent e)
public void actionPerformed(final ActionEvent e)
public void actionPerformed(final ActionEvent e)
public void actionPerformed(final ActionEvent e)
public void actionPerformed(final ActionEvent e)
public void actionPerformed(final ActionEvent e)
public void actionPerformed(final ActionEvent e)
public void actionPerformed(final ActionEvent e)
'''
pass
def onDateSelected():
'''public void onDateSelected(final Calendar value)
public void onDateSelected(final Calendar value)
'''
pass
def moveToDay():
'''public static void moveToDay(final Calendar day, final IlvActivity[] selected, final IlvGanttChart gchart)
'''
pass
def setWorkToDay():
'''public static void setWorkToDay(final Calendar day, final IlvActivity[] selected, final IlvGanttChart gchart)
'''
pass
def dumpDebugInfoForItem():
'''public static void dumpDebugInfoForItem(final IlvGanttChart gchart, final IlvActivity item)
'''
pass
def dumpDebegInfoForContaints():
'''public static void dumpDebegInfoForContaints(final String msg, final Iterator<IlvConstraint> iter)
'''
pass
def dumpDebugInfoForContstraint():
'''public static void dumpDebugInfoForContstraint(final IlvConstraint c)
'''
pass
def dumpDebugCompareInfoForItems():
'''public static void dumpDebugCompareInfoForItems(final String msg, final IlvUserPropertyHolder item1, final IlvUserPropertyHolder item2)
'''
pass
def copyProperties():
'''public static void copyProperties(final IlvActivity src, final IlvActivity dest)
'''
pass
def showWorkForTimeInterval():
'''public static void showWorkForTimeInterval(final long startMillis, final long durMillis, final IlvHierarchyChart gchart)
'''
pass
def applyVisibleTime():
'''public static void applyVisibleTime(final IlvTimeScrollController timeScroller, final IlvHierarchyChart chart)
'''
pass
def showWorkForSelectedActivities():
'''public static void showWorkForSelectedActivities(final IlvActivity[] selected, final IlvHierarchyChart gchart)
'''
pass
def adjustChartForPadding():
'''public static void adjustChartForPadding(final IlvHierarchyChart gchart, Date start, IlvDuration duration)
'''
pass
def showWorkForSelectedResource():
'''public static void showWorkForSelectedResource(final IlvResource selected, final IlvHierarchyChart chart)
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
def getID():
'''public static String getID(final IlvHierarchyNode node)
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
'''public static IlvHierarchyNode[] getChildren(final IlvHierarchyNode item, final IlvHierarchyChart chart)
'''
pass
def dumpDebugInfoForResource():
'''public static void dumpDebugInfoForResource(final IlvResource selectedresource, final IlvGanttModel model)
'''
pass
def count():
'''public static long count(final Iterator<?> items)
'''
pass
def countActivities():
'''public static long countActivities(final IlvHierarchyChart chart)
'''
pass
def countResources():
'''public static long countResources(final IlvHierarchyChart chart)
'''
pass
def countReservations():
'''public static long countReservations(final IlvScheduleChart chart)
'''
pass
def hideDurationInTooltip():
'''public static boolean hideDurationInTooltip(final IlvActivity act)
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
public boolean canAccept(final IlvActivity act)
'''
pass
def ShowMoveToMenuVisitor():
'''public ShowMoveToMenuVisitor()
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
