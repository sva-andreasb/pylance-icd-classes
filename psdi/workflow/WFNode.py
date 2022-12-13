def WFNode():
    '''    public WFNode(final MboSet ms)
    '''
def init():
    '''    public void init()
    '''
def initRelationship():
    '''    public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
def add():
    '''    public void add()
    '''
def getWFCallStack():
    '''    public WFCallStack getWFCallStack()
    '''
def getWorkflowActions():
    '''    public WFActionSet getWorkflowActions()
    '''
def getWorkflowActionsIn():
    '''    public WFActionSet getWorkflowActionsIn()
    '''
def applyWorkflowAction():
    '''    public void applyWorkflowAction(final WFActionRemote action, final String memo)
    public final void applyWorkflowAction(final WFActionRemote action)
    '''
def makeNodeNotifications():
    '''    public void makeNodeNotifications()
    '''
def completeWorkflowAssignment():
    '''    public boolean completeWorkflowAssignment(final WFAssignment assignMbo, final WFAction actionMbo, final String memo)
    '''
def stopAtNode():
    '''    public void stopAtNode(final String memo)
    '''
def writeTransaction():
    '''    public void writeTransaction(final String transType, final String memo)
    '''
def hasOwnerNode():
    '''    public boolean hasOwnerNode()
    '''
def countPositiveAction():
    '''    public int countPositiveAction()
    '''
def countNegativeAction():
    '''    public int countNegativeAction()
    '''
def hasPositiveActionIn():
    '''    public boolean hasPositiveActionIn()
    '''
def hasNegativeActionIn():
    '''    public boolean hasNegativeActionIn()
    '''
def countPositiveActionIn():
    '''    public int countPositiveActionIn()
    '''
def countNegativeActionIn():
    '''    public int countNegativeActionIn()
    '''
def getCompanionSet():
    '''    public MboSetRemote getCompanionSet()
    '''
def canTakePositive():
    '''    public boolean canTakePositive()
    '''
def canTakeNegative():
    '''    public boolean canTakeNegative()
    '''
def addedAction():
    '''    public void addedAction(final boolean wasPositive)
    '''
def removedAction():
    '''    public void removedAction(final boolean wasPositive)
    '''
def delete():
    '''    public void delete(final long modifier)
    '''
def undelete():
    '''    public void undelete()
    '''
def hasNodeActions():
    '''    public boolean hasNodeActions(final boolean isPositive)
    '''
def getNodeDetail():
    '''    public NodeDetail getNodeDetail()
    '''
def canDelete():
    '''    public void canDelete()
    '''
def duplicateDetails():
    '''    public void duplicateDetails(final WFNode origNode)
    '''
def getValidateOrder():
    '''    public String[] getValidateOrder()
    '''
