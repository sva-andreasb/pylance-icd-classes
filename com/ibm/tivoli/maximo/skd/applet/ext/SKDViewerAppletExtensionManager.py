def SKDViewerAppletExtensionManager():
    '''    public SKDViewerAppletExtensionManager()
    '''
def getSKDViewerAppletExtensionManager():
    '''    public static SKDViewerAppletExtensionManager getSKDViewerAppletExtensionManager()
    '''
def initialize():
    '''    public void initialize(final Set<SKDViewerAppletExtensionInfo> appletExtInfoSet)
    '''
def invokeInit():
    '''    public void invokeInit()
    '''
def invokeCreateToolBarButtons():
    '''    public void invokeCreateToolBarButtons(final JToolBar toolBar)
    '''
def getValidCPMExtensions():
    '''    public HashMap<String, SKDCPMExtension> getValidCPMExtensions()
    '''
def invokeCPMInitialize():
    '''    public void invokeCPMInitialize(final IlvGanttModel model, final IlvActivity[] selectedActivities)
    '''
def invokeCPMRelease():
    '''    public void invokeCPMRelease(final IlvGanttModel model, final IlvActivity[] selectedActivities, final boolean success)
    '''
def invokeCPMComputeEarlyStartAndFinish():
    '''    public SKDCPMAdjustedActivityData invokeCPMComputeEarlyStartAndFinish(final IlvGanttModel model, final IlvActivity activity, final Date parentEarlyStart, final Date activityEarlyStart, final Date activityEarlyFinish)
    '''
def invokeCPMComputeLateStartAndFinish():
    '''    public SKDCPMAdjustedActivityData invokeCPMComputeLateStartAndFinish(final IlvGanttModel model, final IlvActivity activity, final Date parentLatestFinish, final Date activityLateStart, final Date activityLatefinish)
    '''
def getActivityBarRenderers():
    '''    public Iterator<SKDActivityBar> getActivityBarRenderers()
    '''
def getActivityMilestoneRenderers():
    '''    public Iterator<SKDActivityMilestone> getActivityMilestoneRenderers()
    '''
