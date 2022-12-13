def getSKDPMUtility():
'''public static synchronized SKDPMUtility getSKDPMUtility()
'''
pass
def isPMPendingReforecast():
'''public boolean isPMPendingReforecast(final MXActivity pm)
'''
pass
def getEarlyPMStartDate():
'''public Date getEarlyPMStartDate(final MXActivity pm, final Date refDate)
'''
pass
def getEarlyPMEndDate():
'''public Date getEarlyPMEndDate(final MXActivity pm, final Date refDate)
'''
pass
def updatePMSummaryActivity():
'''public void updatePMSummaryActivity(final MXActivity pm)
'''
pass
def updatePMChildrenActivity():
'''public void updatePMChildrenActivity(final MXActivity parentpm)
'''
pass
def markAllPMChildrenForSegmentDeletion():
'''public void markAllPMChildrenForSegmentDeletion(final MXActivity parentActivity, final int deletedCount, final int newCount)
'''
pass
def getEarliestPMSegmentStartDate():
'''public Date getEarliestPMSegmentStartDate(final MXActivity pm)
'''
pass
def getLastestPMSegmentEndDate():
'''public Date getLastestPMSegmentEndDate(final MXActivity pm)
'''
pass
def updateAllLeafActivities():
'''public void updateAllLeafActivities(final MXActivity parentActivity, final IlvTimeInterval timeInterval)
'''
pass
def getLeafActivity():
'''public MXActivity getLeafActivity(final MXActivity parentActivity)
'''
pass
def getSegmentDates():
'''public Date[] getSegmentDates(final MXActivity pm, final int sequence)
'''
pass
def updatePMSegmentReservations():
'''public void updatePMSegmentReservations(final MXActivity pm, final int sequenceIndex)
'''
pass
def updateAllPMSegmentReservations():
'''public void updateAllPMSegmentReservations(final MXActivity pm)
'''
pass
def getSegmentClosestToToday():
'''public CustomActivitySegmentRenderer getSegmentClosestToToday(final MXActivity pm, final CustomPMActivityRenderer pmRenderer)
'''
pass
def setupInitialOverlapping():
'''public void setupInitialOverlapping(final CustomActivitySegmentRenderer movingSegment, final MXActivity pm, final CustomPMActivityRenderer pmGraphic)
'''
pass
