def ():
    '''returns PlusPSLAFinder\n\n
    (final Mbo mbo)\n
    ()\n
    '''
def applySLAs():
    '''returns String[]\n\n
    applySLAs()\n
    applySLAs(final MboSet set, final MboRemote mboRemote)\n
    '''
def calculateMeasurements():
    '''returns None\n\n
    calculateMeasurements()\n
    calculateMeasurements(final MboRemote mboRemote)\n
    '''
def clearTargetDates():
    '''returns None\n\n
    clearTargetDates()\n
    clearTargetDates(final MboRemote mboRemote)\n
    '''
def calculateSLARecordsTimes():
    '''returns MboRemote\n\n
    calculateSLARecordsTimes(final MboRemote mboRemote)\n
    calculateSLARecordsTimes(final MboRemote mboRemote, final Mbo mbo)\n
    '''
def getAppliableSLAs():
    '''returns List<MboRemote>\n\n
    getAppliableSLAs(final String s, final boolean b)\n
    '''
def getAppliableSLAsAsMboSet():
    '''returns MboSetRemote\n\n
    getAppliableSLAsAsMboSet(final String s, final boolean b)\n
    '''
def calculateDate():
    '''returns Date\n\n
    calculateDate(final Mbo mbo, final double time, final String uom)\n
    '''
def getCalendarToUse():
    '''returns String[]\n\n
    getCalendarToUse(final MboRemote mboRemote, final MboRemote mboRemote2)\n
    '''
def convertDaysInWorkHours():
    '''returns double\n\n
    convertDaysInWorkHours(final MboSetRemote mboSetRemote, final double n)\n
    '''
