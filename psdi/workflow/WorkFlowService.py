def ():
    '''returns WorkFlowService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def getActiveInstances():
    '''returns WFInstanceSetRemote\n\n
    getActiveInstances(final MboRemote mbo)\n
    '''
def validateCondition():
    '''returns None\n\n
    validateCondition(final MboRemote onBehalfOf, final String customAttr, final String condAttr)\n
    '''
def evaluateCondition():
    '''returns boolean\n\n
    evaluateCondition(final Mbo onBehalfOf, final String customclass, final String condition, final MboRemote mbo)\n
    '''
def initiateWorkflow():
    '''returns None\n\n
    initiateWorkflow(final String processName, final MboRemote target)\n
    '''
def getWFLogger():
    '''returns MXLogger\n\n
    getWFLogger()\n
    getWFLogger(final Mbo mbo)\n
    '''
def completeAssignment():
    '''returns None\n\n
    completeAssignment(@WSMboKey("WFASSIGNMENT") final WFAssignmentRemote assign, final String memo, final boolean accepted)\n
    '''
def isActiveProcess():
    '''returns boolean\n\n
    isActiveProcess(final String processName, final String mboName, final UserInfo ui)\n
    '''
def getDefaultAppForObject():
    '''returns String\n\n
    getDefaultAppForObject(final UserInfo ui, final String objectName)\n
    '''
