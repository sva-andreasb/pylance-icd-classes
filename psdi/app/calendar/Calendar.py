def ():
    '''returns Calendar\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def isAvailable():
    '''returns boolean\n\n
    isAvailable(final Date date)\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def canApplyShift():
    '''returns None\n\n
    canApplyShift(final ShiftRemote shift)\n
    canApplyShift(final String shiftname)\n
    '''
def applyShift():
    '''returns None\n\n
    applyShift(final Vector shiftSet)\n
    applyShift(final String shiftname)\n
    applyShift(final String shiftname, final Date startdate, final Date enddate)\n
    '''
def setWPIncrement():
    '''returns None\n\n
    setWPIncrement(final int i)\n
    '''
def applyNonWorkTime():
    '''returns None\n\n
    applyNonWorkTime(final MboSetRemote nonWorkTimeSet)\n
    applyNonWorkTime(final String nonWorkType, final String description, final Date startDate, final Date endDate)\n
    '''
def calculateAvailability():
    '''returns double\n\n
    calculateAvailability()\n
    calculateAvailability(final Date startDate, final Date endDate)\n
    '''
def calculateHours():
    '''returns double\n\n
    calculateHours(final Date date1, final Date date2)\n
    '''
def calculateDownTime():
    '''returns double\n\n
    calculateDownTime(final Date lastChangeDate, final Date currentChangeDate)\n
    '''
def getDownTime():
    '''returns double\n\n
    getDownTime(final Date currentChangeDate, final Date lastChangeDate)\n
    getDownTime(final Date currentChangeDate, final Date lastChangeDate, final TimeZone tz)\n
    '''
def getWorkPeriodData():
    '''returns double\n\n
    getWorkPeriodData(final WorkPeriodSet workPeriodSet, final Date lastChangeDate, final Date currentChangeDate)\n
    getWorkPeriodData(final WorkPeriodSet workPeriodSet, final Date lastChangeDate, final Date currentChangeDate, final TimeZone tz)\n
    '''
def addDates():
    '''returns Date\n\n
    addDates(final Date date, final int days)\n
    '''
def combineDateTime():
    '''returns Date\n\n
    combineDateTime(final Date date, final Date time)\n
    combineDateTime(final Date date, final Date time, final TimeZone tz)\n
    '''
def deleteWorkPeriod():
    '''returns None\n\n
    deleteWorkPeriod(final Date startDate, final Date endDate)\n
    '''
def calculateWorkHours():
    '''returns double\n\n
    calculateWorkHours(final Date workDate)\n
    '''
def getWorkPeriodSet():
    '''returns WorkPeriodSetRemote\n\n
    getWorkPeriodSet(final Date workDate)\n
    '''
def getMonthsAvailableHours():
    '''returns String[][]\n\n
    getMonthsAvailableHours(final com.ibm.icu.util.Calendar cal)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
