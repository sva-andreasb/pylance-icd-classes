def ():
    '''returns FldAssignScheduleDate\n\n
    (final MboValue mbv)\n
    '''
def action():
    '''returns None\n\n
    action()\n
    '''
def setAssignWorkDate():
    '''returns None\n\n
    setAssignWorkDate(final Assignment assignMbo)\n
    '''
def isWPMidnightSpanning():
    '''returns boolean\n\n
    isWPMidnightSpanning(final MboRemote workTimeMbo)\n
    '''
def isAssignMidnightSpanning():
    '''returns boolean\n\n
    isAssignMidnightSpanning(final Assignment assignMbo)\n
    '''
def assignAndWPOverlap():
    '''returns boolean\n\n
    assignAndWPOverlap(final Assignment assignMbo, final MboRemote workTimeMbo, final GregorianCalendar scratchCal, final AvailCalc availCalc)\n
    '''
def getWorkDatePlusDifference():
    '''returns Date\n\n
    getWorkDatePlusDifference(final Date wpWorkDate, final GregorianCalendar scratchCal, final int offset)\n
    '''
def getAvailableMbo():
    '''returns MboRemote\n\n
    getAvailableMbo(final MboRemote resMbo, final Date wpWorkDate, final String orgID, final AvailCalc availCalc)\n
    '''
def getResourceMbo():
    '''returns MboRemote\n\n
    getResourceMbo(final MboRemote mbo, final Resource resourceName)\n
    '''
