def WFInstance():
'''public WFInstance(final MboSet ms)
'''
pass
def init():
'''public void init()
'''
pass
def add():
'''public void add()
'''
pass
def getControlledMbo():
'''public MboRemote getControlledMbo()
'''
pass
def setControlledMbo():
'''public void setControlledMbo(final MboRemote mbo)
'''
pass
def initiateWorkflow():
'''public void initiateWorkflow(final String memo, final WFProcess wfProcess)
'''
pass
def getActions():
'''public WFActionSetRemote getActions()
'''
pass
def completeWorkflowAssignment():
'''public void completeWorkflowAssignment(final int assignment, final int action, final String memo)
public void completeWorkflowAssignment(final String assignment, final int action, final String memo)
'''
pass
def applyWorkflowAction():
'''public void applyWorkflowAction(final int actionID)
public void applyWorkflowAction(final int actionID, final String memo)
'''
pass
def getWFDiagramInfo():
'''public WFViewInfo getWFDiagramInfo(final int callSeq)
'''
pass
def cancelWorkflowAssignment():
'''public void cancelWorkflowAssignment(final WFAssignmentRemote assignment, final String actionMemo)
'''
pass
def stopWorkflow():
'''public void stopWorkflow(final String memo)
'''
pass
def getCurrentNode():
'''public WFNode getCurrentNode()
'''
pass
def interactionComplete():
'''public void interactionComplete()
'''
pass
def waitComplete():
'''public void waitComplete()
'''
pass
def atInteraction():
'''public boolean atInteraction()
'''
pass
def getInteraction():
'''public WFInteractionRemote getInteraction()
'''
pass
def escalateAssignment():
'''public void escalateAssignment(final int assignID, final String memo)
public void escalateAssignment(final String assignID, final String memo)
'''
pass
def atStoppingPoint():
'''public boolean atStoppingPoint()
'''
pass
def canAutoCompleteInteraction():
'''public boolean canAutoCompleteInteraction()
'''
pass
def delete():
'''public void delete(final long accessModifier)
'''
pass
