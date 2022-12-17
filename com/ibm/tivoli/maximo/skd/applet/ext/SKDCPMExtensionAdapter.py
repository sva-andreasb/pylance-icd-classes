def initialize():
    '''returns None\n\n
    initialize(final IlvGanttModel model, final IlvActivity[] selectedActivities)\n
    '''
def computeEarlyStartAndFinish():
    '''returns SKDCPMAdjustedActivityData\n\n
    computeEarlyStartAndFinish(final IlvGanttModel model, final IlvActivity activity, final Date parentEarlyStart, final Date activityEarlyStart, final Date activityEarlyFinish)\n
    '''
def computeLateStartAndFinish():
    '''returns SKDCPMAdjustedActivityData\n\n
    computeLateStartAndFinish(final IlvGanttModel model, final IlvActivity activity, final Date parentLatestFinish, final Date activityLateStart, final Date activityLatefinish)\n
    '''
def isEarlyStartAndFinishAcceptable():
    '''returns boolean\n\n
    isEarlyStartAndFinishAcceptable(final IlvGanttModel model, final IlvActivity activity, final Date parentEarlyStart, final Date activityEarlyStart, final Date activityEarlyFinish)\n
    '''
def isLateStartAndFinishAcceptable():
    '''returns boolean\n\n
    isLateStartAndFinishAcceptable(final IlvGanttModel model, final IlvActivity activity, final Date parentLatestFinish, final Date activityLateStart, final Date activityLatefinish)\n
    '''
def release():
    '''returns None\n\n
    release(final IlvGanttModel model, final IlvActivity[] selectedActivities, final boolean success)\n
    '''
