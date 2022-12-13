def hasChildren():
    '''    public static boolean hasChildren(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
    '''
def getFirstChild():
    '''    public static IlvHierarchyNode getFirstChild(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
    '''
def getLastChild():
    '''    public static IlvHierarchyNode getLastChild(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
    '''
def childIterator():
    '''    public static Iterator childIterator(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
    '''
def activityPreorderIterator():
    '''    public static Iterator<IlvActivity> activityPreorderIterator(final IlvGanttModel ilvGanttModel)
    '''
def resourcePreorderIterator():
    '''    public static Iterator<IlvResource> resourcePreorderIterator(final IlvGanttModel ilvGanttModel)
    '''
def preorderIterator():
    '''    public static Iterator preorderIterator(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
    '''
def activityPostorderIterator():
    '''    public static Iterator<IlvActivity> activityPostorderIterator(final IlvGanttModel ilvGanttModel, final IlvActivity ilvActivity)
    public static Iterator<IlvActivity> activityPostorderIterator(final IlvGanttModel ilvGanttModel)
    '''
def resourcePostorderIterator():
    '''    public static Iterator<IlvResource> resourcePostorderIterator(final IlvGanttModel ilvGanttModel, final IlvResource ilvResource)
    public static Iterator<IlvResource> resourcePostorderIterator(final IlvGanttModel ilvGanttModel)
    '''
def postorderIterator():
    '''    public static Iterator postorderIterator(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
    '''
def activityBreadthFirstIterator():
    '''    public static Iterator<IlvActivity> activityBreadthFirstIterator(final IlvGanttModel ilvGanttModel, final IlvActivity ilvActivity)
    public static Iterator<IlvActivity> activityBreadthFirstIterator(final IlvGanttModel ilvGanttModel)
    '''
def resourceBreadthFirstIterator():
    '''    public static Iterator<IlvResource> resourceBreadthFirstIterator(final IlvGanttModel ilvGanttModel, final IlvResource ilvResource)
    public static Iterator<IlvResource> resourceBreadthFirstIterator(final IlvGanttModel ilvGanttModel)
    '''
def breadthFirstIterator():
    '''    public static Iterator breadthFirstIterator(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
    '''
def promote():
    '''    public static void promote(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode obj)
    '''
def demote():
    '''    public static void demote(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode obj)
    '''
def getDepth():
    '''    public static int getDepth(final IlvGanttModel ilvGanttModel, IlvHierarchyNode parent)
    '''
def isDescendant():
    '''    public static boolean isDescendant(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode, final IlvHierarchyNode ilvHierarchyNode2)
    '''
def checkValidNonNullActivity():
    '''    public static void checkValidNonNullActivity(final IlvActivity ilvActivity)
    '''
def checkValidMemberActivity():
    '''    public static void checkValidMemberActivity(final IlvActivity obj, final IlvGanttModel obj2)
    '''
def checkValidNonRootMemberActivity():
    '''    public static void checkValidNonRootMemberActivity(final IlvActivity obj, final IlvGanttModel ilvGanttModel)
    '''
def checkValidNonNullResource():
    '''    public static void checkValidNonNullResource(final IlvResource ilvResource)
    '''
def checkValidMemberResource():
    '''    public static void checkValidMemberResource(final IlvResource obj, final IlvGanttModel obj2)
    '''
def checkValidNonRootMemberResource():
    '''    public static void checkValidNonRootMemberResource(final IlvResource obj, final IlvGanttModel ilvGanttModel)
    '''
def checkValidNonNullConstraint():
    '''    public static void checkValidNonNullConstraint(final IlvConstraint ilvConstraint)
    '''
def checkValidMemberConstraint():
    '''    public static void checkValidMemberConstraint(final IlvConstraint obj, final IlvGanttModel obj2)
    '''
def checkValidNewConstraint():
    '''    public static void checkValidNewConstraint(final IlvConstraint obj, final IlvGanttModel obj2)
    '''
def checkValidNonNullReservation():
    '''    public static void checkValidNonNullReservation(final IlvReservation ilvReservation)
    '''
def checkValidMemberReservation():
    '''    public static void checkValidMemberReservation(final IlvReservation obj, final IlvGanttModel obj2)
    '''
def checkValidNewReservation():
    '''    public static void checkValidNewReservation(final IlvReservation obj, final IlvGanttModel obj2)
    '''
def ResourceBreadthFirstIterator():
    '''    public ResourceBreadthFirstIterator(final IlvGanttModel a, final IlvResource ilvResource)
    '''
def getChildren():
    '''    public Iterator<IlvResource> getChildren(final IlvResource ilvResource)
    public Iterator<IlvActivity> getChildren(final IlvActivity ilvActivity)
    public Iterator<IlvResource> getChildren(final IlvResource ilvResource)
    public Iterator<IlvActivity> getChildren(final IlvActivity ilvActivity)
    '''
def ActivityBreadthFirstIterator():
    '''    public ActivityBreadthFirstIterator(final IlvGanttModel a, final IlvActivity ilvActivity)
    '''
def ResourcePostorderIterator():
    '''    public ResourcePostorderIterator(final IlvGanttModel a, final IlvResource ilvResource)
    '''
def ActivityPostorderIterator():
    '''    public ActivityPostorderIterator(final IlvGanttModel a, final IlvActivity ilvActivity)
    '''
