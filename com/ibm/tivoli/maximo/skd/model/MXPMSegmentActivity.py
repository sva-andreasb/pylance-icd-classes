def MXPMSegmentActivity():
    '''    public MXPMSegmentActivity(final String id, final String name, final Date start, final Date end, final MXActivity parent, final int seq)
    '''
def getParent():
    '''    public MXActivity getParent()
    '''
def getSequence():
    '''    public int getSequence()
    '''
def setEndTime():
    '''    public void setEndTime(final Date endTime)
    '''
def setStartTime():
    '''    public void setStartTime(final Date startTime)
    '''
def setTimeInterval():
    '''    public void setTimeInterval(final Date arg0, final Date arg1)
    public void setTimeInterval(final IlvTimeInterval arg0)
    '''
def setProperty():
    '''    public Object setProperty(final String property, final Object value)
    public Object setProperty(final String property, final Object value, final boolean ignoreChangeTracking)
    '''
def getProperty():
    '''    public Object getProperty(final String arg0)
    '''
def isPMActivityID():
    '''    public static boolean isPMActivityID(final String id)
    '''
def getPMActivity():
    '''    public static MXPMSegmentActivity getPMActivity(final MXGanttModel model, final String id)
    public static MXPMSegmentActivity getPMActivity(final MXActivity pmParentRow, final int seqId)
    '''
