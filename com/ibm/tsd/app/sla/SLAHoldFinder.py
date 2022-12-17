def ():
    '''returns SLAHoldFinder\n\n
    ()\n
    (final Mbo mbo)\n
    '''
def applySLAs():
    '''returns String[]\n\n
    applySLAs(final MboSet set, final MboRemote subject)\n
    '''
def calculateMeasurements():
    '''returns None\n\n
    calculateMeasurements(final Date startDate, final Date endDate)\n
    calculateMeasurements(final MboRemote subject)\n
    calculateMeasurements(final double SLAHoldTimeInMinutes)\n
    calculateMeasurements(final double SLAHoldTimeInMinutes, final Date startDate, final Date endDate)\n
    '''
def getAccumlatedSLAHoldDateTime():
    '''returns int\n\n
    getAccumlatedSLAHoldDateTime()\n
    '''
def calculateSLAHoldTimeAccumlation():
    '''returns int\n\n
    calculateSLAHoldTimeAccumlation(final Mbo sla, final Date reportedHoldDate, final Date removedHoldDate)\n
    '''
