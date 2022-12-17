def ():
    '''returns WFNode\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def getWFCallStack():
    '''returns WFCallStack\n\n
    getWFCallStack()\n
    '''
def getWorkflowActions():
    '''returns WFActionSet\n\n
    getWorkflowActions()\n
    '''
def getWorkflowActionsIn():
    '''returns WFActionSet\n\n
    getWorkflowActionsIn()\n
    '''
def applyWorkflowAction():
    '''returns None\n\n
    applyWorkflowAction(final WFActionRemote action, final String memo)\n
    '''
def makeNodeNotifications():
    '''returns None\n\n
    makeNodeNotifications()\n
    '''
def completeWorkflowAssignment():
    '''returns boolean\n\n
    completeWorkflowAssignment(final WFAssignment assignMbo, final WFAction actionMbo, final String memo)\n
    '''
def stopAtNode():
    '''returns None\n\n
    stopAtNode(final String memo)\n
    '''
def writeTransaction():
    '''returns None\n\n
    writeTransaction(final String transType, final String memo)\n
    '''
def hasOwnerNode():
    '''returns boolean\n\n
    hasOwnerNode()\n
    '''
def countPositiveAction():
    '''returns int\n\n
    countPositiveAction()\n
    '''
def countNegativeAction():
    '''returns int\n\n
    countNegativeAction()\n
    '''
def hasPositiveActionIn():
    '''returns boolean\n\n
    hasPositiveActionIn()\n
    '''
def hasNegativeActionIn():
    '''returns boolean\n\n
    hasNegativeActionIn()\n
    '''
def countPositiveActionIn():
    '''returns int\n\n
    countPositiveActionIn()\n
    '''
def countNegativeActionIn():
    '''returns int\n\n
    countNegativeActionIn()\n
    '''
def getCompanionSet():
    '''returns MboSetRemote\n\n
    getCompanionSet()\n
    '''
def canTakePositive():
    '''returns boolean\n\n
    canTakePositive()\n
    '''
def canTakeNegative():
    '''returns boolean\n\n
    canTakeNegative()\n
    '''
def addedAction():
    '''returns None\n\n
    addedAction(final boolean wasPositive)\n
    '''
def removedAction():
    '''returns None\n\n
    removedAction(final boolean wasPositive)\n
    '''
def delete():
    '''returns None\n\n
    delete(final long modifier)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def hasNodeActions():
    '''returns boolean\n\n
    hasNodeActions(final boolean isPositive)\n
    '''
def getNodeDetail():
    '''returns NodeDetail\n\n
    getNodeDetail()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def duplicateDetails():
    '''returns None\n\n
    duplicateDetails(final WFNode origNode)\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
