def acceptOrigin():
    '''    public static boolean acceptOrigin(final MXActivity fromActivity, final MXGanttModel mxGanttModel)
    '''
def acceptDestination():
    '''    public static boolean acceptDestination(final MXActivity fromActivity, final MXActivity toActivity, final MXGanttModel mxGanttModel, final IlvConstraintType constraintType)
    '''
def isCycleDetected():
    '''    public static boolean isCycleDetected(final MXGanttModel mxGanttModel, final IlvActivity fromActivity, final IlvActivity toActivityToCheck, final HashMap<String, IlvActivity> activityPathMap)
    '''
def getConstraintType():
    '''    public static IlvConstraintType getConstraintType(final Dependency dep)
    '''
def getDependenyTo():
    '''    public static Dependency getDependenyTo(final List<Dependency> deps, final String to)
    '''
def getDeletedDependencies():
    '''    public static List<Dependency> getDeletedDependencies(final List<Dependency> oldDeps, final List<Dependency> newDeps)
    '''
def getInsertedDependencies():
    '''    public static List<Dependency> getInsertedDependencies(final List<Dependency> oldDeps, final List<Dependency> newDeps)
    '''
def getModifiedDependencies():
    '''    public static List<Dependency> getModifiedDependencies(final List<Dependency> oldDeps, final List<Dependency> newDeps)
    '''
def parseLeadLagHrs():
    '''    public static Double parseLeadLagHrs(final String lag)
    '''
def performCPMALL():
    '''    public static boolean performCPMALL(final MXGanttModel model, final BaseTreeGridMiniAppBean bean, final DataBean appBean)
    public static boolean performCPMALL(final Schedule model, final BaseLargeGanttView bean, final DataBean appBean)
    '''
def performCPMSelected():
    '''    public static IMXActivity[] performCPMSelected(final MXGanttModel model, final BaseTreeGridMiniAppBean bean, final List<String> activityIds, final DataBean appBean)
    public static IMXActivity[] performCPMSelected(final Schedule model, final BaseLargeGanttView bean, final List<String> activityIds, final DataBean appBean)
    '''
def createLinkedConstraints():
    '''    public static void createLinkedConstraints(final MXGanttModel model, final BaseTreeGridMiniAppBean bean, final List<String> ids, final String projectId, final SKDAppServiceBeanRemote serviceBean)
    public static void createLinkedConstraints(final Schedule model, final AbstractTreeGridMiniAppBean bean, final List<String> ids, final String projectId)
    '''
def isValid():
    '''    public static boolean isValid(final MXActivity from, final MXActivity to, final MXGanttModel model, final UserInfo userInfo)
    '''
def isValidParent():
    '''    public static boolean isValidParent(String parent, String checkWonum, final UserInfo userInfo)
    '''
