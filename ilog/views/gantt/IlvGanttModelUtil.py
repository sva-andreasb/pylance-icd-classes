def hasChildren():
'''public static boolean hasChildren(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def getFirstChild():
'''public static IlvHierarchyNode getFirstChild(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def getLastChild():
'''public static IlvHierarchyNode getLastChild(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def childIterator():
'''public static Iterator childIterator(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def activityPreorderIterator():
'''public static Iterator<IlvActivity> activityPreorderIterator(final IlvGanttModel ilvGanttModel)
'''
pass
def resourcePreorderIterator():
'''public static Iterator<IlvResource> resourcePreorderIterator(final IlvGanttModel ilvGanttModel)
'''
pass
def preorderIterator():
'''public static Iterator preorderIterator(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def activityPostorderIterator():
'''public static Iterator<IlvActivity> activityPostorderIterator(final IlvGanttModel ilvGanttModel, final IlvActivity ilvActivity)
public static Iterator<IlvActivity> activityPostorderIterator(final IlvGanttModel ilvGanttModel)
'''
pass
def resourcePostorderIterator():
'''public static Iterator<IlvResource> resourcePostorderIterator(final IlvGanttModel ilvGanttModel, final IlvResource ilvResource)
public static Iterator<IlvResource> resourcePostorderIterator(final IlvGanttModel ilvGanttModel)
'''
pass
def postorderIterator():
'''public static Iterator postorderIterator(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def activityBreadthFirstIterator():
'''public static Iterator<IlvActivity> activityBreadthFirstIterator(final IlvGanttModel ilvGanttModel, final IlvActivity ilvActivity)
public static Iterator<IlvActivity> activityBreadthFirstIterator(final IlvGanttModel ilvGanttModel)
'''
pass
def resourceBreadthFirstIterator():
'''public static Iterator<IlvResource> resourceBreadthFirstIterator(final IlvGanttModel ilvGanttModel, final IlvResource ilvResource)
public static Iterator<IlvResource> resourceBreadthFirstIterator(final IlvGanttModel ilvGanttModel)
'''
pass
def breadthFirstIterator():
'''public static Iterator breadthFirstIterator(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode)
'''
pass
def promote():
'''public static void promote(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode obj)
'''
pass
def demote():
'''public static void demote(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode obj)
'''
pass
def getDepth():
'''public static int getDepth(final IlvGanttModel ilvGanttModel, IlvHierarchyNode parent)
'''
pass
def isDescendant():
'''public static boolean isDescendant(final IlvGanttModel ilvGanttModel, final IlvHierarchyNode ilvHierarchyNode, final IlvHierarchyNode ilvHierarchyNode2)
'''
pass
def checkValidNonNullActivity():
'''public static void checkValidNonNullActivity(final IlvActivity ilvActivity)
'''
pass
def checkValidMemberActivity():
'''public static void checkValidMemberActivity(final IlvActivity obj, final IlvGanttModel obj2)
'''
pass
def checkValidNonRootMemberActivity():
'''public static void checkValidNonRootMemberActivity(final IlvActivity obj, final IlvGanttModel ilvGanttModel)
'''
pass
def checkValidNonNullResource():
'''public static void checkValidNonNullResource(final IlvResource ilvResource)
'''
pass
def checkValidMemberResource():
'''public static void checkValidMemberResource(final IlvResource obj, final IlvGanttModel obj2)
'''
pass
def checkValidNonRootMemberResource():
'''public static void checkValidNonRootMemberResource(final IlvResource obj, final IlvGanttModel ilvGanttModel)
'''
pass
def checkValidNonNullConstraint():
'''public static void checkValidNonNullConstraint(final IlvConstraint ilvConstraint)
'''
pass
def checkValidMemberConstraint():
'''public static void checkValidMemberConstraint(final IlvConstraint obj, final IlvGanttModel obj2)
'''
pass
def checkValidNewConstraint():
'''public static void checkValidNewConstraint(final IlvConstraint obj, final IlvGanttModel obj2)
'''
pass
def checkValidNonNullReservation():
'''public static void checkValidNonNullReservation(final IlvReservation ilvReservation)
'''
pass
def checkValidMemberReservation():
'''public static void checkValidMemberReservation(final IlvReservation obj, final IlvGanttModel obj2)
'''
pass
def checkValidNewReservation():
'''public static void checkValidNewReservation(final IlvReservation obj, final IlvGanttModel obj2)
'''
pass
def ResourceBreadthFirstIterator():
'''public ResourceBreadthFirstIterator(final IlvGanttModel a, final IlvResource ilvResource)
'''
pass
def getChildren():
'''public Iterator<IlvResource> getChildren(final IlvResource ilvResource)
public Iterator<IlvActivity> getChildren(final IlvActivity ilvActivity)
public Iterator<IlvResource> getChildren(final IlvResource ilvResource)
public Iterator<IlvActivity> getChildren(final IlvActivity ilvActivity)
'''
pass
def ActivityBreadthFirstIterator():
'''public ActivityBreadthFirstIterator(final IlvGanttModel a, final IlvActivity ilvActivity)
'''
pass
def ResourcePostorderIterator():
'''public ResourcePostorderIterator(final IlvGanttModel a, final IlvResource ilvResource)
'''
pass
def ActivityPostorderIterator():
'''public ActivityPostorderIterator(final IlvGanttModel a, final IlvActivity ilvActivity)
'''
pass
