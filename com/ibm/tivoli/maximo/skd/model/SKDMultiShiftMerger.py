def ():
    '''returns Interval\n\n
    (final Locale l, final TimeZone tz)\n
    (final Date s, final Date e)\n
    '''
def mergeShifts():
    '''returns ArrayList<Date>\n\n
    mergeShifts(final HashMap<String, SKDCalendarInfo> calInfoMap, final boolean forWorkingHours)\n
    '''
def mergeShiftsNew():
    '''returns ArrayList<Date>\n\n
    mergeShiftsNew(final HashMap<String, SKDCalendarInfo> calInfoMap, final boolean forWorkingHours)\n
    '''
def mergeShiftsOLD():
    '''returns ArrayList<Date>\n\n
    mergeShiftsOLD(final HashMap<String, SKDCalendarInfo> calInfoMap, final boolean forWorkingHours)\n
    '''
def getShiftWorkTime():
    '''returns Date[]\n\n
    getShiftWorkTime(final ArrayList<Date> workperiods, final int index)\n
    '''
def insertWorkTime():
    '''returns None\n\n
    insertWorkTime(final ArrayList<Date> workperiods, final int index, final Date[] workTime)\n
    '''
def updateWorkTime():
    '''returns None\n\n
    updateWorkTime(final ArrayList<Date> workperiods, final int index, final Date[] workTime)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Interval o)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
