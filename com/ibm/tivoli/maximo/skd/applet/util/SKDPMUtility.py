def getSKDPMUtility():
    '''    public static synchronized SKDPMUtility getSKDPMUtility()
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
    '''    public void updatePMChildrenActivity(final MXActivity parentpm)
    '''
def markAllPMChildrenForSegmentDeletion():
    '''    public void markAllPMChildrenForSegmentDeletion(final MXActivity parentActivity, final int deletedCount, final int newCount)
    '''
def getEarliestPMSegmentStartDate():
    '''    public Date getEarliestPMSegmentStartDate(final MXActivity pm)
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
    '''    public void updateAllPMSegmentReservations(final MXActivity pm)
    '''
def getSegmentClosestToToday():
    '''    public CustomActivitySegmentRenderer getSegmentClosestToToday(final MXActivity pm, final CustomPMActivityRenderer pmRenderer)
    '''
def setupInitialOverlapping():
    '''    public void setupInitialOverlapping(final CustomActivitySegmentRenderer movingSegment, final MXActivity pm, final CustomPMActivityRenderer pmGraphic)
    '''
