def ():
    '''returns RBAWFService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def WFLaunchOnDemand():
    '''returns long\n\n
    WFLaunchOnDemand(final String userid, final String password, final String processName)\n
    '''
def WFRouteToWorkflow():
    '''returns long\n\n
    WFRouteToWorkflow(final String userid, final String password, final String processName, final String objectName, final long objectId)\n
    '''
def WFRouteToNextNode():
    '''returns long\n\n
    WFRouteToNextNode(final String userid, final String password, final long wfid, final boolean accepted)\n
    '''
def getDefaultAppForObject():
    '''returns String\n\n
    getDefaultAppForObject(final UserInfo ui, final String objectName)\n
    '''
