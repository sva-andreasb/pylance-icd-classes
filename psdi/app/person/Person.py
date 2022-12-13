def Person():
    '''public Person(final MboSet ms)
    '''
def init():
    '''public void init()
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def getDefaultDisplayName():
    '''public String getDefaultDisplayName()
    '''
def add():
    '''public void add()
    '''
def appValidate():
    '''public void appValidate()
    '''
def canDelete():
    '''public void canDelete()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def isDelegateLoopCreated():
    '''public void isDelegateLoopCreated()
    '''
def getSupervisees():
    '''public String getSupervisees()
    '''
def setPrimaryPhone():
    '''public void setPrimaryPhone(final MboRemote inPhone)
    '''
def setPrimaryEmail():
    '''public void setPrimaryEmail(final MboRemote inEmail)
    '''
def getPrimaryPhone():
    '''public MboRemote getPrimaryPhone()
    '''
def getPrimaryEmail():
    '''public MboRemote getPrimaryEmail()
    '''
def getEndDateFromCalendar():
    '''public Date getEndDateFromCalendar(Date startDate, final String duration, final String orgid)
    '''
def getTodaysHours():
    '''public double getTodaysHours(final Date startDate, final String orgid)
    '''
def getAvailableHours():
    '''public double getAvailableHours(final Date startDate, final String orgid)
    public double getAvailableHours(final Date startDate, final String orgid, final AvailCalc availCalc)
    public double getAvailableHours(final Date startDate, final PersonCalRemote personCal, AvailCalc availCalc)
    '''
def getAvailableMbo():
    '''public MboRemote getAvailableMbo(final Date startDate, final String orgid)
    public MboRemote getAvailableMbo(final Date startDate, final String orgid, final AvailCalc availCalc)
    public MboRemote getAvailableMbo(final Date startDate, final PersonCalRemote personCal, AvailCalc availCalc)
    '''
def getAvailableMboList():
    '''public List<MboRemote> getAvailableMboList(final Date startDate, final String orgid)
    public List<MboRemote> getAvailableMboList(final Date startDate, final String orgid, final AvailCalc availCalc)
    public List<MboRemote> getAvailableMboList(final Date startDate, final PersonCalRemote personCal, AvailCalc availCalc)
    '''
def isActive():
    '''public boolean isActive()
    '''
def changeStatus():
    '''public void changeStatus(final String status, final Date date, final String memo)
    '''
def getDelegate():
    '''public PersonRemote getDelegate(final Date asof)
    '''
def getLastDelegate():
    '''public PersonRemote getLastDelegate(final PersonRemote person, final Date asof)
    '''
def getCalType():
    '''public String getCalType()
    '''
def getLocaleStr():
    '''public String getLocaleStr()
    '''
def getTimezoneStr():
    '''public String getTimezoneStr()
    '''
def updatePrimaryCalendar():
    '''public void updatePrimaryCalendar()
    '''
def deletePrimaryCalendar():
    '''public void deletePrimaryCalendar()
    '''
def getValidateOrder():
    '''public String[] getValidateOrder()
    '''
def getStartApp():
    '''public String getStartApp()
    '''
def toChangeStatusAfterInactive():
    '''public boolean toChangeStatusAfterInactive()
    '''
def setDateTo():
    '''public void setDateTo(final Date dateTo)
    '''
def getDateTo():
    '''public Date getDateTo()
    '''
def deletePersonData():
    '''public void deletePersonData()
    '''
