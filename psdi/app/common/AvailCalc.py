def AvailCalc():
'''public AvailCalc()
'''
pass
def checkAvailableCalendar():
'''public String checkAvailableCalendar(final Date fromDate, final Date toDate, final String shiftnum)
'''
pass
def getWPSQL():
'''public String getWPSQL(final Date fromDate, final Date toDate)
'''
pass
def checkAvailableWorkHrs():
'''public double checkAvailableWorkHrs(final Date fromDate, final Date toDate, final String shiftnum)
'''
pass
def getSqlString():
'''public String getSqlString(final boolean istodate, final String str1, final String str2, final String shiftnum)
'''
pass
def getCalDate():
'''public Date getCalDate(final Date actualDate)
'''
pass
def getCalTime():
'''public Date getCalTime(final Date actualDate, final String defDate)
public Date getCalTime(final String defDate, final boolean isstart)
'''
pass
def getNextWorkDate():
'''public Date getNextWorkDate(final Date fromDate)
'''
pass
def getToDate():
'''public Date getToDate(final Date fromDate)
'''
pass
def getDateTime():
'''public Date getDateTime(final Date workdt, final Date sttime)
'''
pass
def checkAvailableHours():
'''public double checkAvailableHours(final Date workdate, final PersonCalRemote personCal)
'''
pass
def checkAvailableMboList():
'''public List<MboRemote> checkAvailableMboList(final Date workdate, final PersonCalRemote personCal)
'''
pass
def checkAvailableMbo():
'''public MboRemote checkAvailableMbo(final Date workdate, final PersonCalRemote personCal)
'''
pass
def checkWorkPeriodMbo():
'''public MboRemote checkWorkPeriodMbo(Date workdate, final PersonCalRemote personCal)
'''
pass
def getStartDateTime():
'''public Date getStartDateTime(final Date workdate, final PersonCalRemote personCal)
'''
pass
def getNextWorkDateForCal():
'''public Date getNextWorkDateForCal(Date workdate, final String person, final String calnum, final String shiftnum, final String orgid)
'''
pass
def getSqlSqfFormat():
'''public String getSqlSqfFormat(final String strValue, final Date AvailDate, final String orgid)
'''
pass
def getCompositeWP():
'''public MboRemote getCompositeWP(final List<MboRemote> modAvailList, final Date workDate, final PersonRemote person, final String orgid)
public MboRemote getCompositeWP(final List<MboRemote> modAvailList, final Date workDate, final PersonRemote person, final String orgid, final boolean isCreateAMGrid)
'''
pass
def getPersonCal():
'''public PersonCalRemote getPersonCal(final PersonRemote person, final String orgid)
'''
pass
def getToDateOneYear():
'''public Date getToDateOneYear(final Date fromDate)
'''
pass
