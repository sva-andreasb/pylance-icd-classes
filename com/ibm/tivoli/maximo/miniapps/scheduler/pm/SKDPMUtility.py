def SKDPMUtility():
    '''    public SKDPMUtility(final MXGanttModel model)
    '''
def isPMPendingReforecast():
    '''    public boolean isPMPendingReforecast(final MXActivity pm)
    '''
def getEarlyPMStartDate():
    '''    public Date getEarlyPMStartDate(final MXActivity pm, final Date refDate)
    '''
def getEarlyPMEndDate():
    '''    public Date getEarlyPMEndDate(final MXActivity pm, final Date refDate)
    '''
def updatePMSummaryActivity():
    '''    public void updatePMSummaryActivity(final MXActivity pm)
    '''
def updatePMChildrenActivity():
    '''    public List<MXActivity> updatePMChildrenActivity(final MXActivity parentpm)
    '''
def markAllPMChildrenForSegmentDeletion():
    '''    public void markAllPMChildrenForSegmentDeletion(final MXActivity parentActivity, final int deletedCount, final int newCount)
    '''
def getEarliestPMSegmentStartDate():
    '''    public Date getEarliestPMSegmentStartDate(final MXActivity pm)
    '''
def dumpPMSegmentInfo():
    '''    public static void dumpPMSegmentInfo(final MXActivity pm, final int seqNo, final PrintStream ps)
    '''
def getLastestPMSegmentEndDate():
    '''    public Date getLastestPMSegmentEndDate(final MXActivity pm)
    '''
def updateAllLeafActivities():
    '''    public void updateAllLeafActivities(final MXActivity parentActivity, final IlvTimeInterval timeInterval)
    '''
def getLeafActivity():
    '''    public MXActivity getLeafActivity(final MXActivity parentActivity)
    '''
def getSegmentDates():
    '''    public Date[] getSegmentDates(final MXActivity pm, final int sequence)
    '''
def updatePMSegmentReservations():
    '''    public void updatePMSegmentReservations(final MXActivity pm, final int sequenceIndex)
    '''
def updateAllPMSegmentReservations():
    '''    public boolean updateAllPMSegmentReservations(final MXActivity pm)
    '''
def setEdited():
    '''    public void setEdited(final boolean edited, final MXActivity pm, final int sequenceNum)
    '''
def markOtherSegmentsImmovable():
    '''    public void markOtherSegmentsImmovable(final MXActivity pm, final int sequenceNum)
    '''
