def WFCallStackSet():
    '''public WFCallStackSet(final MboServerInterface ms)
    '''
def pushWFCallStack():
    '''public WFCallStackRemote pushWFCallStack(final WFProcessRemote wfProcess)
    '''
def popWFCallStack():
    '''public WFCallStackRemote popWFCallStack()
    '''
def getWFCallStack():
    '''public WFCallStack getWFCallStack()
    '''
def initiateWorkflow():
    '''public WFActionSetRemote initiateWorkflow(final String memo, final WFProcess wfProcess)
    '''
def stopWorkflow():
    '''public void stopWorkflow(final String memo)
    '''
def applyWorkflowAction():
    '''public final WFActionSetRemote applyWorkflowAction(final WFAction action)
    public WFActionSetRemote applyWorkflowAction(WFAction action, final String memo)
    '''
def getWFDiagramInfo():
    '''public WFViewInfo getWFDiagramInfo(int requestedCallSeq)
    '''
def canAdd():
    '''public void canAdd()
    '''
