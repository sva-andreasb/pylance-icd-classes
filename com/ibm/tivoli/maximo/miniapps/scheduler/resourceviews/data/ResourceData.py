def ():
    '''returns ResourceData\n\n
    ()\n
    '''
def getNow():
    '''returns Date\n\n
    getNow(final UserInfo userInfo)\n
    '''
def getAvailableHoursData():
    '''returns double\n\n
    getAvailableHoursData(final IMXGanttModel model, final IMXResource resource, final UserInfo info, final AlternateAvailHashMap alternateAvailHashMap)\n
    getAvailableHoursData(final IMXGanttModel model, final IMXResource res, final UserInfo userInfo, final Date clickdate, final AlternateAvailHashMap alternateAvailHashMap)\n
    '''
def useOverlappingLoads():
    '''returns boolean\n\n
    useOverlappingLoads()\n
    '''
def getLoadHoursData():
    '''returns double\n\n
    getLoadHoursData(final IMXGanttModel model, final IMXResource resource, final UserInfo userInfo)\n
    getLoadHoursData(final IMXGanttModel mxGanttModel, final IMXResource res, final UserInfo userInfo, final Date clickdate)\n
    '''
def getLaborCrewTotalhours():
    '''returns double\n\n
    getLaborCrewTotalhours(final double avail, final AbstractTreeGridMiniAppBean.ShiftInfo shiftInfo)\n
    '''
def getAdditionalCapacity():
    '''returns double\n\n
    getAdditionalCapacity(final double load, final double avail)\n
    '''
def getAdditionalCapacityQuantity():
    '''returns double\n\n
    getAdditionalCapacityQuantity(final double addCapacity, final AbstractTreeGridMiniAppBean.ShiftInfo shiftInfo)\n
    '''
def getLoadQuantityData():
    '''returns double\n\n
    getLoadQuantityData(final IMXGanttModel model, final IMXResource resource, final Date clickdate)\n
    '''
