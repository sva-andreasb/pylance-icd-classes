def WorkFlowService():
    '''    public WorkFlowService()
    public WorkFlowService(final MXServer mxServer)
    '''
def init():
    '''    public void init()
    '''
def destroy():
    '''    public void destroy()
    '''
def getActiveInstances():
    '''    public WFInstanceSetRemote getActiveInstances(final MboRemote mbo)
    '''
def validateCondition():
    '''    public void validateCondition(final MboRemote onBehalfOf, final String customAttr, final String condAttr)
    '''
def evaluateCondition():
    '''    public boolean evaluateCondition(final Mbo onBehalfOf, final String customclass, final String condition, final MboRemote mbo)
    '''
def initiateWorkflow():
    '''    public void initiateWorkflow(final String processName, final MboRemote target)
    '''
def getWFLogger():
    '''    public MXLogger getWFLogger()
    public MXLogger getWFLogger(final Mbo mbo)
    '''
def completeAssignment():
    '''    public void completeAssignment(@WSMboKey("WFASSIGNMENT") final WFAssignmentRemote assign, final String memo, final boolean accepted)
    '''
def isActiveProcess():
    '''    public boolean isActiveProcess(final String processName, final String mboName, final UserInfo ui)
    '''
def getDefaultAppForObject():
    '''    public String getDefaultAppForObject(final UserInfo ui, final String objectName)
    '''
