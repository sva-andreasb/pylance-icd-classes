LOCAL_STD = "int  1"
LOCAL_DST = "int  3"
LOCAL_FORMER = "int  4"
LOCAL_LATTER = "int  12"
def hasEquivalentTransitions():
    '''returns boolean\n\n
    hasEquivalentTransitions(final TimeZone tz, final long start, final long end)\n
    hasEquivalentTransitions(final TimeZone tz, final long start, final long end, final boolean ignoreDstAmount)\n
    '''
def getTimeZoneRules():
    '''returns TimeZoneRule[]\n\n
    getTimeZoneRules(final long start)\n
    '''
def getSimpleTimeZoneRulesNear():
    '''returns TimeZoneRule[]\n\n
    getSimpleTimeZoneRulesNear(final long date)\n
    '''
def getOffsetFromLocal():
    '''returns None\n\n
    getOffsetFromLocal(final long date, final int nonExistingTimeOpt, final int duplicatedTimeOpt, final int[] offsets)\n
    '''
