def ():
    '''returns SKDViewerAppletExtensionManager\n\n
    ()\n
    '''
def initialize():
    '''returns None\n\n
    initialize(final Set<SKDViewerAppletExtensionInfo> appletExtInfoSet)\n
    '''
def invokeInit():
    '''returns None\n\n
    invokeInit()\n
    '''
def invokeCreateToolBarButtons():
    '''returns None\n\n
    invokeCreateToolBarButtons(final JToolBar toolBar)\n
    '''
def invokeCPMInitialize():
    '''returns None\n\n
    invokeCPMInitialize(final IlvGanttModel model, final IlvActivity[] selectedActivities)\n
    '''
def invokeCPMRelease():
    '''returns None\n\n
    invokeCPMRelease(final IlvGanttModel model, final IlvActivity[] selectedActivities, final boolean success)\n
    '''
def invokeCPMComputeEarlyStartAndFinish():
    '''returns SKDCPMAdjustedActivityData\n\n
    invokeCPMComputeEarlyStartAndFinish(final IlvGanttModel model, final IlvActivity activity, final Date parentEarlyStart, final Date activityEarlyStart, final Date activityEarlyFinish)\n
    '''
def invokeCPMComputeLateStartAndFinish():
    '''returns SKDCPMAdjustedActivityData\n\n
    invokeCPMComputeLateStartAndFinish(final IlvGanttModel model, final IlvActivity activity, final Date parentLatestFinish, final Date activityLateStart, final Date activityLatefinish)\n
    '''
def getActivityBarRenderers():
    '''returns Iterator<SKDActivityBar>\n\n
    getActivityBarRenderers()\n
    '''
def getActivityMilestoneRenderers():
    '''returns Iterator<SKDActivityMilestone>\n\n
    getActivityMilestoneRenderers()\n
    '''
