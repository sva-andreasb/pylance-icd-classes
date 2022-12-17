def ():
    '''returns AvailCalc\n\n
    ()\n
    '''
def checkAvailableCalendar():
    '''returns String\n\n
    checkAvailableCalendar(final Date fromDate, final Date toDate, final String shiftnum)\n
    '''
def getWPSQL():
    '''returns String\n\n
    getWPSQL(final Date fromDate, final Date toDate)\n
    '''
def checkAvailableWorkHrs():
    '''returns double\n\n
    checkAvailableWorkHrs(final Date fromDate, final Date toDate, final String shiftnum)\n
    '''
def getSqlString():
    '''returns String\n\n
    getSqlString(final boolean istodate, final String str1, final String str2, final String shiftnum)\n
    '''
def getCalDate():
    '''returns Date\n\n
    getCalDate(final Date actualDate)\n
    '''
def getCalTime():
    '''returns Date\n\n
    getCalTime(final Date actualDate, final String defDate)\n
    getCalTime(final String defDate, final boolean isstart)\n
    '''
def getNextWorkDate():
    '''returns Date\n\n
    getNextWorkDate(final Date fromDate)\n
    '''
def getToDate():
    '''returns Date\n\n
    getToDate(final Date fromDate)\n
    '''
def getDateTime():
    '''returns Date\n\n
    getDateTime(final Date workdt, final Date sttime)\n
    '''
def checkAvailableHours():
    '''returns double\n\n
    checkAvailableHours(final Date workdate, final PersonCalRemote personCal)\n
    '''
def checkAvailableMboList():
    '''returns List<MboRemote>\n\n
    checkAvailableMboList(final Date workdate, final PersonCalRemote personCal)\n
    '''
def checkAvailableMbo():
    '''returns MboRemote\n\n
    checkAvailableMbo(final Date workdate, final PersonCalRemote personCal)\n
    '''
def checkWorkPeriodMbo():
    '''returns MboRemote\n\n
    checkWorkPeriodMbo(Date workdate, final PersonCalRemote personCal)\n
    '''
def getStartDateTime():
    '''returns Date\n\n
    getStartDateTime(final Date workdate, final PersonCalRemote personCal)\n
    '''
def getNextWorkDateForCal():
    '''returns Date\n\n
    getNextWorkDateForCal(Date workdate, final String person, final String calnum, final String shiftnum, final String orgid)\n
    '''
def getSqlSqfFormat():
    '''returns String\n\n
    getSqlSqfFormat(final String strValue, final Date AvailDate, final String orgid)\n
    '''
def getCompositeWP():
    '''returns MboRemote\n\n
    getCompositeWP(final List<MboRemote> modAvailList, final Date workDate, final PersonRemote person, final String orgid)\n
    getCompositeWP(final List<MboRemote> modAvailList, final Date workDate, final PersonRemote person, final String orgid, final boolean isCreateAMGrid)\n
    '''
def getPersonCal():
    '''returns PersonCalRemote\n\n
    getPersonCal(final PersonRemote person, final String orgid)\n
    '''
def getToDateOneYear():
    '''returns Date\n\n
    getToDateOneYear(final Date fromDate)\n
    '''
