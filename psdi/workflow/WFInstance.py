def ():
    '''returns WFInstance\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def getControlledMbo():
    '''returns MboRemote\n\n
    getControlledMbo()\n
    '''
def setControlledMbo():
    '''returns None\n\n
    setControlledMbo(final MboRemote mbo)\n
    '''
def initiateWorkflow():
    '''returns None\n\n
    initiateWorkflow(final String memo, final WFProcess wfProcess)\n
    '''
def getActions():
    '''returns WFActionSetRemote\n\n
    getActions()\n
    '''
def completeWorkflowAssignment():
    '''returns None\n\n
    completeWorkflowAssignment(final int assignment, final int action, final String memo)\n
    completeWorkflowAssignment(final String assignment, final int action, final String memo)\n
    '''
def applyWorkflowAction():
    '''returns None\n\n
    applyWorkflowAction(final int actionID)\n
    applyWorkflowAction(final int actionID, final String memo)\n
    '''
def getWFDiagramInfo():
    '''returns WFViewInfo\n\n
    getWFDiagramInfo(final int callSeq)\n
    '''
def cancelWorkflowAssignment():
    '''returns None\n\n
    cancelWorkflowAssignment(final WFAssignmentRemote assignment, final String actionMemo)\n
    '''
def stopWorkflow():
    '''returns None\n\n
    stopWorkflow(final String memo)\n
    '''
def getCurrentNode():
    '''returns WFNode\n\n
    getCurrentNode()\n
    '''
def interactionComplete():
    '''returns None\n\n
    interactionComplete()\n
    '''
def waitComplete():
    '''returns None\n\n
    waitComplete()\n
    '''
def atInteraction():
    '''returns boolean\n\n
    atInteraction()\n
    '''
def getInteraction():
    '''returns WFInteractionRemote\n\n
    getInteraction()\n
    '''
def escalateAssignment():
    '''returns None\n\n
    escalateAssignment(final int assignID, final String memo)\n
    escalateAssignment(final String assignID, final String memo)\n
    '''
def atStoppingPoint():
    '''returns boolean\n\n
    atStoppingPoint()\n
    '''
def canAutoCompleteInteraction():
    '''returns boolean\n\n
    canAutoCompleteInteraction()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
