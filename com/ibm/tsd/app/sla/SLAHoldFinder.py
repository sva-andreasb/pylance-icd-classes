def SLAHoldFinder():
    '''public SLAHoldFinder()
    public SLAHoldFinder(final Mbo mbo)
    '''
def applySLAs():
    '''public String[] applySLAs(final MboSet set, final MboRemote subject)
    '''
def calculateMeasurements():
    '''public void calculateMeasurements(final Date startDate, final Date endDate)
    public void calculateMeasurements(final MboRemote subject)
    public void calculateMeasurements(final double SLAHoldTimeInMinutes)
    public void calculateMeasurements(final double SLAHoldTimeInMinutes, final Date startDate, final Date endDate)
    '''
def getAccumlatedSLAHoldDateTime():
    '''public int getAccumlatedSLAHoldDateTime()
    '''
def calculateSLAHoldTimeAccumlation():
    '''public int calculateSLAHoldTimeAccumlation(final Mbo sla, final Date reportedHoldDate, final Date removedHoldDate)
    '''
def timeDiffInSeconds():
    '''public static int timeDiffInSeconds(final Date date1, final Date date2)
    '''
