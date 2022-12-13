def SKDPMUtility():
'''public SKDPMUtility(final MXGanttModel model)
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
'''public List<MXActivity> updatePMChildrenActivity(final MXActivity parentpm)
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
def dumpPMSegmentInfo():
'''public static void dumpPMSegmentInfo(final MXActivity pm, final int seqNo, final PrintStream ps)
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
'''public boolean updateAllPMSegmentReservations(final MXActivity pm)
'''
pass
def setEdited():
'''public void setEdited(final boolean edited, final MXActivity pm, final int sequenceNum)
'''
pass
def markOtherSegmentsImmovable():
'''public void markOtherSegmentsImmovable(final MXActivity pm, final int sequenceNum)
'''
pass
