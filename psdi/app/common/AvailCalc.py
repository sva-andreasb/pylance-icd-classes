def AvailCalc():
    '''    public AvailCalc()
    '''
def checkAvailableCalendar():
    '''    public String checkAvailableCalendar(final Date fromDate, final Date toDate, final String shiftnum)
    '''
def getWPSQL():
    '''    public String getWPSQL(final Date fromDate, final Date toDate)
    '''
def checkAvailableWorkHrs():
    '''    public double checkAvailableWorkHrs(final Date fromDate, final Date toDate, final String shiftnum)
    '''
def getSqlString():
    '''    public String getSqlString(final boolean istodate, final String str1, final String str2, final String shiftnum)
    '''
def getCalDate():
    '''    public Date getCalDate(final Date actualDate)
    '''
def getCalTime():
    '''    public Date getCalTime(final Date actualDate, final String defDate)
    public Date getCalTime(final String defDate, final boolean isstart)
    '''
def getNextWorkDate():
    '''    public Date getNextWorkDate(final Date fromDate)
    '''
def getToDate():
    '''    public Date getToDate(final Date fromDate)
    '''
def getDateTime():
    '''    public Date getDateTime(final Date workdt, final Date sttime)
    '''
def checkAvailableHours():
    '''    public double checkAvailableHours(final Date workdate, final PersonCalRemote personCal)
    '''
def checkAvailableMboList():
    '''    public List<MboRemote> checkAvailableMboList(final Date workdate, final PersonCalRemote personCal)
    '''
def checkAvailableMbo():
    '''    public MboRemote checkAvailableMbo(final Date workdate, final PersonCalRemote personCal)
    '''
def checkWorkPeriodMbo():
    '''    public MboRemote checkWorkPeriodMbo(Date workdate, final PersonCalRemote personCal)
    '''
def getStartDateTime():
    '''    public Date getStartDateTime(final Date workdate, final PersonCalRemote personCal)
    '''
def getNextWorkDateForCal():
    '''    public Date getNextWorkDateForCal(Date workdate, final String person, final String calnum, final String shiftnum, final String orgid)
    '''
def getSqlSqfFormat():
    '''    public String getSqlSqfFormat(final String strValue, final Date AvailDate, final String orgid)
    '''
def getCompositeWP():
    '''    public MboRemote getCompositeWP(final List<MboRemote> modAvailList, final Date workDate, final PersonRemote person, final String orgid)
    public MboRemote getCompositeWP(final List<MboRemote> modAvailList, final Date workDate, final PersonRemote person, final String orgid, final boolean isCreateAMGrid)
    '''
def getPersonCal():
    '''    public PersonCalRemote getPersonCal(final PersonRemote person, final String orgid)
    '''
def getToDateOneYear():
    '''    public Date getToDateOneYear(final Date fromDate)
    '''
