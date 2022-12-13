def WorkFlowService():
'''public WorkFlowService()
public WorkFlowService(final MXServer mxServer)
'''
pass
def init():
'''public void init()
'''
pass
def destroy():
'''public void destroy()
'''
pass
def getActiveInstances():
'''public WFInstanceSetRemote getActiveInstances(final MboRemote mbo)
'''
pass
def validateCondition():
'''public void validateCondition(final MboRemote onBehalfOf, final String customAttr, final String condAttr)
'''
pass
def evaluateCondition():
'''public boolean evaluateCondition(final Mbo onBehalfOf, final String customclass, final String condition, final MboRemote mbo)
'''
pass
def initiateWorkflow():
'''public void initiateWorkflow(final String processName, final MboRemote target)
'''
pass
def getWFLogger():
'''public MXLogger getWFLogger()
public MXLogger getWFLogger(final Mbo mbo)
'''
pass
def completeAssignment():
'''public void completeAssignment(@WSMboKey("WFASSIGNMENT") final WFAssignmentRemote assign, final String memo, final boolean accepted)
'''
pass
def isActiveProcess():
'''public boolean isActiveProcess(final String processName, final String mboName, final UserInfo ui)
'''
pass
def getDefaultAppForObject():
'''public String getDefaultAppForObject(final UserInfo ui, final String objectName)
'''
pass
