def ResourceFinder():
    '''public ResourceFinder(final long skdprojectid, final String emQuery)
    '''
def getAvailResoures():
    '''public List getAvailResoures(final UserInfo userInfo, final String type, final MboRemote wo, final MboRemote req)
    '''
def getProjectResoures():
    '''public List getProjectResoures()
    '''
def getProjectReassignResoures():
    '''public List getProjectReassignResoures()
    '''
def getResourceProjectAssignedSet():
    '''public HashMap<String, MboSetRemote> getResourceProjectAssignedSet()
    '''
def getClosestResoureList():
    '''public List getClosestResoureList(final List resoureSet, final String type, final MboRemote wo, final MboRemote req, final boolean assignedlist)
    '''
def getTravelTimeForResoureList():
    '''public HashMap<String, Double> getTravelTimeForResoureList(final List resoureSet, final String type, final MboRemote wo, final MboRemote req, final boolean assignedlist)
    '''
def getWOandTravelTimeForResoureList():
    '''public HashMap<String, HashMap<String, Double>> getWOandTravelTimeForResoureList(final List resoureSet, final String type, final MboRemote wo, final MboRemote req, final boolean assignedlist)
    '''
def getDateDBSqlString():
    '''public String getDateDBSqlString()
    '''
def isAvailableByCalendar():
    '''public boolean isAvailableByCalendar(final UserInfo userInfo, final MboRemote resourceRemote, final MboRemote personCal, Date dateVal, AvailCalc availCalc, final boolean considerBreaks, final int mins)
    '''
