def SLRouteServiceCache():
    '''public SLRouteServiceCache(final String currentProjectId)
    '''
def verifyProject():
    '''public void verifyProject(final String id, final String calendar, final String shift, final Date startDate, final Date endDate, final String projectName, final String orgId)
    '''
def putShiftInfo():
    '''public void putShiftInfo(final String shift, final HashMap<Long, SLRouteService.ShiftInformation> baseModShifts)
    '''
def getShiftCalMap():
    '''public HashMap<String, SKDCalendarInfo> getShiftCalMap()
    '''
def getCalendarBreaks():
    '''public HashMap<String, ArrayList> getCalendarBreaks()
    '''
def getDaysInShiftPattern():
    '''public HashMap<String, Integer> getDaysInShiftPattern()
    '''
def getMergedWorkPeriods():
    '''public ArrayList<Date> getMergedWorkPeriods()
    '''
def setShiftGridInfo():
    '''public void setShiftGridInfo(final HashMap<String, SKDCalendarInfo> shiftCalMap, final HashMap<String, ArrayList> calendarBreaks, final HashMap<String, Integer> daysInShiftPattern, final ArrayList<Date> mergedWorkPeriods)
    '''
def hasShiftGridInfo():
    '''public boolean hasShiftGridInfo()
    '''
def addResourceRow():
    '''public void addResourceRow(final String name, final String id, final String parentid, final String objectname, final String refobjname, final String objectid)
    '''
def updateResourceMaps():
    '''public void updateResourceMaps()
    '''
def getResourceHier():
    '''public HashMap<String, SKDResource> getResourceHier()
    '''
def getObjKeyedResourceHier():
    '''public SKDResource getObjKeyedResourceHier(final String refobjname, final String objectid)
    '''
def clearResourceHier():
    '''public void clearResourceHier()
    '''
def isUIDebug():
    '''public boolean isUIDebug()
    '''
def setUIDebug():
    '''public void setUIDebug(final boolean isUIDebug)
    '''
def getWorkQuery():
    '''public String getWorkQuery()
    '''
def setWorkQuery():
    '''public void setWorkQuery(final String workQuery)
    '''
def getProjectName():
    '''public String getProjectName()
    '''
def getOrgId():
    '''public String getOrgId()
    '''
def getSKDResourceInstance():
    '''public SKDResource getSKDResourceInstance(final String name, final String id, final String parentid, final String objectname, final String refobjname, final String objectid)
    '''
def SKDResource():
    '''public SKDResource()
    public SKDResource(final String name, final String id, final String parentid, final String objectname, final String refobjname, final String objectid)
    '''
