def WFInstance():
    '''public WFInstance(final MboSet ms)
    '''
def init():
    '''public void init()
    '''
def add():
    '''public void add()
    '''
def getControlledMbo():
    '''public MboRemote getControlledMbo()
    '''
def setControlledMbo():
    '''public void setControlledMbo(final MboRemote mbo)
    '''
def initiateWorkflow():
    '''public void initiateWorkflow(final String memo, final WFProcess wfProcess)
    '''
def getActions():
    '''public WFActionSetRemote getActions()
    '''
def completeWorkflowAssignment():
    '''public void completeWorkflowAssignment(final int assignment, final int action, final String memo)
    public void completeWorkflowAssignment(final String assignment, final int action, final String memo)
    '''
def applyWorkflowAction():
    '''public void applyWorkflowAction(final int actionID)
    public void applyWorkflowAction(final int actionID, final String memo)
    '''
def getWFDiagramInfo():
    '''public WFViewInfo getWFDiagramInfo(final int callSeq)
    '''
def cancelWorkflowAssignment():
    '''public void cancelWorkflowAssignment(final WFAssignmentRemote assignment, final String actionMemo)
    '''
def stopWorkflow():
    '''public void stopWorkflow(final String memo)
    '''
def getCurrentNode():
    '''public WFNode getCurrentNode()
    '''
def interactionComplete():
    '''public void interactionComplete()
    '''
def waitComplete():
    '''public void waitComplete()
    '''
def atInteraction():
    '''public boolean atInteraction()
    '''
def getInteraction():
    '''public WFInteractionRemote getInteraction()
    '''
def escalateAssignment():
    '''public void escalateAssignment(final int assignID, final String memo)
    public void escalateAssignment(final String assignID, final String memo)
    '''
def atStoppingPoint():
    '''public boolean atStoppingPoint()
    '''
def canAutoCompleteInteraction():
    '''public boolean canAutoCompleteInteraction()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
