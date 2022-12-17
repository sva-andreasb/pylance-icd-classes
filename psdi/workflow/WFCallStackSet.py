def ():
    '''returns WFCallStackSet\n\n
    (final MboServerInterface ms)\n
    '''
def pushWFCallStack():
    '''returns WFCallStackRemote\n\n
    pushWFCallStack(final WFProcessRemote wfProcess)\n
    '''
def popWFCallStack():
    '''returns WFCallStackRemote\n\n
    popWFCallStack()\n
    '''
def getWFCallStack():
    '''returns WFCallStack\n\n
    getWFCallStack()\n
    '''
def initiateWorkflow():
    '''returns WFActionSetRemote\n\n
    initiateWorkflow(final String memo, final WFProcess wfProcess)\n
    '''
def stopWorkflow():
    '''returns None\n\n
    stopWorkflow(final String memo)\n
    '''
def applyWorkflowAction():
    '''returns WFActionSetRemote\n\n
    applyWorkflowAction(WFAction action, final String memo)\n
    '''
def getWFDiagramInfo():
    '''returns WFViewInfo\n\n
    getWFDiagramInfo(int requestedCallSeq)\n
    '''
def canAdd():
    '''returns None\n\n
    canAdd()\n
    '''
