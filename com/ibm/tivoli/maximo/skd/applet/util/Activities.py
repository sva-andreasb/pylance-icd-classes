WO_INTERNAL_STATUS_APPR = "String  \"APPR\""
PROPERTY_READ_ONLY_MODEL = "String  \"__READ_ONLY_MODEL\""
def isWorkorder():
    '''    public static boolean isWorkorder(final IlvActivity act)
    '''
def isAssignment():
    '''    public static boolean isAssignment(final IlvActivity act)
    '''
def isPM():
    '''    public static boolean isPM(final IlvActivity act)
    '''
def hasChildren():
    '''    public static boolean hasChildren(final IlvHierarchyNode item, final IlvHierarchyChart chart)
    '''
def hasAnyChildren():
    '''    public static boolean hasAnyChildren(final IlvHierarchyNode[] items, final IlvHierarchyChart chart)
    '''
def addCrafts():
    '''    public static void addCrafts(final HashSet crafts, final IlvActivity item, final IlvGanttChart ganttChart)
    '''
def visitResource():
    '''    public static <T> void visitResource(final IlvResource item, final IlvHierarchyChart chart, final IlvResourceVisitor<T> visitor, final T state)
    '''
def visitResources():
    '''    public static <T> void visitResources(final IlvResource[] items, final IlvHierarchyChart chart, final IlvResourceVisitor<T> visitor, final T state)
    '''
def visitActivity():
    '''    public static <T> void visitActivity(final IlvActivity item, final IlvGanttChart ganttChart, final IlvActivityVisitor<T> visitor, final T state)
    '''
def visitNodes():
    '''    public static <T> void visitNodes(final IlvHierarchyNode[] items, final IlvHierarchyChart ganttChart, final IlvNodeVisitor<T> visitor, final T state)
    '''
def visitNode():
    '''    public static <T> void visitNode(final IlvHierarchyNode item, final IlvHierarchyChart chart, final IlvNodeVisitor<T> visitor, final T state)
    '''
def visitActivities():
    '''    public static <T> void visitActivities(final IlvActivity[] items, final IlvGanttChart ganttChart, final IlvActivityVisitor<T> visitor, final T state)
    '''
def newAdjustTimeVisitor():
    '''    public static final IlvActivityVisitor<Set<String>> newAdjustTimeVisitor(final IlvDuration adjustment)
    '''
def visit():
    '''    public void visit(final IlvActivity item, final IlvGanttChart chart, final Set<String> state)
    public void visit(final IlvActivity item, final IlvGanttChart chart, final Set<String> state)
    public void visit(final IlvActivity item, final IlvGanttChart chart, final Void state)
    public void visit(final IlvHierarchyNode item, final IlvHierarchyChart chart, final Void state)
    public void visit(final IlvActivity item, final IlvGanttChart chart, final HasCancelled state)
    public void visit(final IlvActivity item, final IlvGanttChart chart, final Void state)
    public void visit(final IlvHierarchyNode item, final IlvHierarchyChart chart, final Void state)
    public void visit(final IlvActivity item, final IlvGanttChart chart, final HasCancelled state)
    public void visit(final IlvHierarchyNode type, final IlvHierarchyChart chart, final Void state)
    '''
def getActivityContextMenu():
    '''    public static JPopupMenu getActivityContextMenu(final IlvActivity item, final IlvGanttChart gchart)
    '''
def actionPerformed():
    '''    public void actionPerformed(final ActionEvent e)
    public void actionPerformed(final ActionEvent e)
    public void actionPerformed(final ActionEvent e)
    public void actionPerformed(final ActionEvent e)
    public void actionPerformed(final ActionEvent e)
    public void actionPerformed(final ActionEvent e)
    public void actionPerformed(final ActionEvent e)
    public void actionPerformed(final ActionEvent e)
    public void actionPerformed(final ActionEvent e)
    '''
def onDateSelected():
    '''    public void onDateSelected(final Calendar value)
    public void onDateSelected(final Calendar value)
    '''
def moveToDay():
    '''    public static void moveToDay(final Calendar day, final IlvActivity[] selected, final IlvGanttChart gchart)
    '''
def setWorkToDay():
    '''    public static void setWorkToDay(final Calendar day, final IlvActivity[] selected, final IlvGanttChart gchart)
    '''
def dumpDebugInfoForItem():
    '''    public static void dumpDebugInfoForItem(final IlvGanttChart gchart, final IlvActivity item)
    '''
def dumpDebegInfoForContaints():
    '''    public static void dumpDebegInfoForContaints(final String msg, final Iterator<IlvConstraint> iter)
    '''
def dumpDebugInfoForContstraint():
    '''    public static void dumpDebugInfoForContstraint(final IlvConstraint c)
    '''
def dumpDebugCompareInfoForItems():
    '''    public static void dumpDebugCompareInfoForItems(final String msg, final IlvUserPropertyHolder item1, final IlvUserPropertyHolder item2)
    '''
def copyProperties():
    '''    public static void copyProperties(final IlvActivity src, final IlvActivity dest)
    '''
def showWorkForTimeInterval():
    '''    public static void showWorkForTimeInterval(final long startMillis, final long durMillis, final IlvHierarchyChart gchart)
    '''
def applyVisibleTime():
    '''    public static void applyVisibleTime(final IlvTimeScrollController timeScroller, final IlvHierarchyChart chart)
    '''
def showWorkForSelectedActivities():
    '''    public static void showWorkForSelectedActivities(final IlvActivity[] selected, final IlvHierarchyChart gchart)
    '''
def adjustChartForPadding():
    '''    public static void adjustChartForPadding(final IlvHierarchyChart gchart, Date start, IlvDuration duration)
    '''
def showWorkForSelectedResource():
    '''    public static void showWorkForSelectedResource(final IlvResource selected, final IlvHierarchyChart chart)
    '''
def getEarliestStartTime():
    '''    public static Date getEarliestStartTime(final IlvActivity[] selected)
    '''
def getLatestEndTime():
    '''    public static Date getLatestEndTime(final IlvActivity[] selected)
    '''
def getParent():
    '''    public static IlvActivity getParent(final IlvActivity act, final IlvGanttModel model)
    '''
def getID():
    '''    public static String getID(final IlvHierarchyNode node)
    '''
def setProperty():
    '''    public static boolean setProperty(final Object node, final String prop, final Object val)
    '''
def getProperty():
    '''    public static Object getProperty(final Object node, final String prop)
    public static <T> T getProperty(final Object node, final String prop, final T defaultValue)
    '''
def createUnionTimeInterval():
    '''    public static IlvTimeInterval createUnionTimeInterval(final IlvHierarchyNode... nodes)
    '''
def isWorkorderApproved():
    '''    public static boolean isWorkorderApproved(final MXActivity source)
    '''
def getActivityById():
    '''    public static IlvActivity getActivityById(final IlvGanttModel model, final IlvActivity parent, final String id)
    '''
def getChildren():
    '''    public static IlvHierarchyNode[] getChildren(final IlvHierarchyNode item, final IlvHierarchyChart chart)
    '''
def dumpDebugInfoForResource():
    '''    public static void dumpDebugInfoForResource(final IlvResource selectedresource, final IlvGanttModel model)
    '''
def count():
    '''    public static long count(final Iterator<?> items)
    '''
def countActivities():
    '''    public static long countActivities(final IlvHierarchyChart chart)
    '''
def countResources():
    '''    public static long countResources(final IlvHierarchyChart chart)
    '''
def countReservations():
    '''    public static long countReservations(final IlvScheduleChart chart)
    '''
def hideDurationInTooltip():
    '''    public static boolean hideDurationInTooltip(final IlvActivity act)
    '''
def FindByIDActivityVisitor():
    '''    public FindByIDActivityVisitor(final String id)
    '''
def isCancelled():
    '''    public boolean isCancelled()
    public boolean isCancelled()
    '''
def cancel():
    '''    public void cancel()
    public void cancel()
    '''
def getActivity():
    '''    public IlvActivity getActivity()
    '''
def FilterActivityVisitor():
    '''    public FilterActivityVisitor(final IFilter<IlvActivity> filter)
    '''
def getActivities():
    '''    public List<IlvActivity> getActivities()
    '''
def FilterNodeVisitor():
    '''    public FilterNodeVisitor(final IFilter<IlvHierarchyNode> filter)
    '''
def getNodes():
    '''    public List<IlvHierarchyNode> getNodes()
    '''
def SameTypeVisitor():
    '''    public SameTypeVisitor(final List<String> objectNames)
    '''
def isValid():
    '''    public boolean isValid()
    '''
def canAccept():
    '''    public boolean canAccept(final IlvActivity act)
    public boolean canAccept(final IlvActivity act)
    '''
def ShowMoveToMenuVisitor():
    '''    public ShowMoveToMenuVisitor()
    '''
def CountingVisitor():
    '''    public CountingVisitor()
    '''
def getCount():
    '''    public long getCount()
    '''
