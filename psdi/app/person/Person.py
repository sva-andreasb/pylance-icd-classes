def ():
    '''returns Person\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def getDefaultDisplayName():
    '''returns String\n\n
    getDefaultDisplayName()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def isDelegateLoopCreated():
    '''returns None\n\n
    isDelegateLoopCreated()\n
    '''
def getSupervisees():
    '''returns String\n\n
    getSupervisees()\n
    '''
def setPrimaryPhone():
    '''returns None\n\n
    setPrimaryPhone(final MboRemote inPhone)\n
    '''
def setPrimaryEmail():
    '''returns None\n\n
    setPrimaryEmail(final MboRemote inEmail)\n
    '''
def getPrimaryPhone():
    '''returns MboRemote\n\n
    getPrimaryPhone()\n
    '''
def getPrimaryEmail():
    '''returns MboRemote\n\n
    getPrimaryEmail()\n
    '''
def getEndDateFromCalendar():
    '''returns Date\n\n
    getEndDateFromCalendar(Date startDate, final String duration, final String orgid)\n
    '''
def getTodaysHours():
    '''returns double\n\n
    getTodaysHours(final Date startDate, final String orgid)\n
    '''
def getAvailableHours():
    '''returns double\n\n
    getAvailableHours(final Date startDate, final String orgid)\n
    getAvailableHours(final Date startDate, final String orgid, final AvailCalc availCalc)\n
    getAvailableHours(final Date startDate, final PersonCalRemote personCal, AvailCalc availCalc)\n
    '''
def getAvailableMbo():
    '''returns MboRemote\n\n
    getAvailableMbo(final Date startDate, final String orgid)\n
    getAvailableMbo(final Date startDate, final String orgid, final AvailCalc availCalc)\n
    getAvailableMbo(final Date startDate, final PersonCalRemote personCal, AvailCalc availCalc)\n
    '''
def getAvailableMboList():
    '''returns List<MboRemote>\n\n
    getAvailableMboList(final Date startDate, final String orgid)\n
    getAvailableMboList(final Date startDate, final String orgid, final AvailCalc availCalc)\n
    getAvailableMboList(final Date startDate, final PersonCalRemote personCal, AvailCalc availCalc)\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo)\n
    '''
def getDelegate():
    '''returns PersonRemote\n\n
    getDelegate(final Date asof)\n
    '''
def getLastDelegate():
    '''returns PersonRemote\n\n
    getLastDelegate(final PersonRemote person, final Date asof)\n
    '''
def getCalType():
    '''returns String\n\n
    getCalType()\n
    '''
def getLocaleStr():
    '''returns String\n\n
    getLocaleStr()\n
    '''
def getTimezoneStr():
    '''returns String\n\n
    getTimezoneStr()\n
    '''
def updatePrimaryCalendar():
    '''returns None\n\n
    updatePrimaryCalendar()\n
    '''
def deletePrimaryCalendar():
    '''returns None\n\n
    deletePrimaryCalendar()\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
def getStartApp():
    '''returns String\n\n
    getStartApp()\n
    '''
def toChangeStatusAfterInactive():
    '''returns boolean\n\n
    toChangeStatusAfterInactive()\n
    '''
def setDateTo():
    '''returns None\n\n
    setDateTo(final Date dateTo)\n
    '''
def getDateTo():
    '''returns Date\n\n
    getDateTo()\n
    '''
def deletePersonData():
    '''returns None\n\n
    deletePersonData()\n
    '''
