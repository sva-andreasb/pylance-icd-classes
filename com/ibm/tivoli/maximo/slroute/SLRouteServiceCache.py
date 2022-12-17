def ():
    '''returns SKDResource\n\n
    (final String currentProjectId)\n
    ()\n
    (final String name, final String id, final String parentid, final String objectname, final String refobjname, final String objectid)\n
    '''
def verifyProject():
    '''returns None\n\n
    verifyProject(final String id, final String calendar, final String shift, final Date startDate, final Date endDate, final String projectName, final String orgId)\n
    '''
def putShiftInfo():
    '''returns None\n\n
    putShiftInfo(final String shift, final HashMap<Long, SLRouteService.ShiftInformation> baseModShifts)\n
    '''
def getMergedWorkPeriods():
    '''returns ArrayList<Date>\n\n
    getMergedWorkPeriods()\n
    '''
def setShiftGridInfo():
    '''returns None\n\n
    setShiftGridInfo(final HashMap<String, SKDCalendarInfo> shiftCalMap, final HashMap<String, ArrayList> calendarBreaks, final HashMap<String, Integer> daysInShiftPattern, final ArrayList<Date> mergedWorkPeriods)\n
    '''
def hasShiftGridInfo():
    '''returns boolean\n\n
    hasShiftGridInfo()\n
    '''
def addResourceRow():
    '''returns None\n\n
    addResourceRow(final String name, final String id, final String parentid, final String objectname, final String refobjname, final String objectid)\n
    '''
def updateResourceMaps():
    '''returns None\n\n
    updateResourceMaps()\n
    '''
def getObjKeyedResourceHier():
    '''returns SKDResource\n\n
    getObjKeyedResourceHier(final String refobjname, final String objectid)\n
    '''
def clearResourceHier():
    '''returns None\n\n
    clearResourceHier()\n
    '''
def isUIDebug():
    '''returns boolean\n\n
    isUIDebug()\n
    '''
def setUIDebug():
    '''returns None\n\n
    setUIDebug(final boolean isUIDebug)\n
    '''
def getWorkQuery():
    '''returns String\n\n
    getWorkQuery()\n
    '''
def setWorkQuery():
    '''returns None\n\n
    setWorkQuery(final String workQuery)\n
    '''
def getProjectName():
    '''returns String\n\n
    getProjectName()\n
    '''
def getOrgId():
    '''returns String\n\n
    getOrgId()\n
    '''
def getSKDResourceInstance():
    '''returns SKDResource\n\n
    getSKDResourceInstance(final String name, final String id, final String parentid, final String objectname, final String refobjname, final String objectid)\n
    '''
