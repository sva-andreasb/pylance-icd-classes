def isPMPendingReforecast():
    '''returns boolean\n\n
    isPMPendingReforecast(final MXActivity pm)\n
    '''
def getEarlyPMStartDate():
    '''returns Date\n\n
    getEarlyPMStartDate(final MXActivity pm, final Date refDate)\n
    '''
def getEarlyPMEndDate():
    '''returns Date\n\n
    getEarlyPMEndDate(final MXActivity pm, final Date refDate)\n
    '''
def updatePMSummaryActivity():
    '''returns None\n\n
    updatePMSummaryActivity(final MXActivity pm)\n
    '''
def updatePMChildrenActivity():
    '''returns None\n\n
    updatePMChildrenActivity(final MXActivity parentpm)\n
    '''
def markAllPMChildrenForSegmentDeletion():
    '''returns None\n\n
    markAllPMChildrenForSegmentDeletion(final MXActivity parentActivity, final int deletedCount, final int newCount)\n
    '''
def getEarliestPMSegmentStartDate():
    '''returns Date\n\n
    getEarliestPMSegmentStartDate(final MXActivity pm)\n
    '''
def getLastestPMSegmentEndDate():
    '''returns Date\n\n
    getLastestPMSegmentEndDate(final MXActivity pm)\n
    '''
def updateAllLeafActivities():
    '''returns None\n\n
    updateAllLeafActivities(final MXActivity parentActivity, final IlvTimeInterval timeInterval)\n
    '''
def getLeafActivity():
    '''returns MXActivity\n\n
    getLeafActivity(final MXActivity parentActivity)\n
    '''
def getSegmentDates():
    '''returns Date[]\n\n
    getSegmentDates(final MXActivity pm, final int sequence)\n
    '''
def updatePMSegmentReservations():
    '''returns None\n\n
    updatePMSegmentReservations(final MXActivity pm, final int sequenceIndex)\n
    '''
def updateAllPMSegmentReservations():
    '''returns None\n\n
    updateAllPMSegmentReservations(final MXActivity pm)\n
    '''
def getSegmentClosestToToday():
    '''returns CustomActivitySegmentRenderer\n\n
    getSegmentClosestToToday(final MXActivity pm, final CustomPMActivityRenderer pmRenderer)\n
    '''
def setupInitialOverlapping():
    '''returns None\n\n
    setupInitialOverlapping(final CustomActivitySegmentRenderer movingSegment, final MXActivity pm, final CustomPMActivityRenderer pmGraphic)\n
    '''
