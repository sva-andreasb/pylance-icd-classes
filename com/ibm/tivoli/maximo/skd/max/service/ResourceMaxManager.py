def ():
    '''returns ResourceMaxManager\n\n
    (final MXServer mxServer)\n
    '''
def getResources():
    '''returns Collection<IMXResource>\n\n
    getResources(final Schedule schedule, final Range<Date> range, final List<String> objectNames, final boolean bucketBased)\n
    '''
def getReservations():
    '''returns Collection<IMXReservation>\n\n
    getReservations(final Schedule schedule, final IMXResource resource)\n
    '''
def getResourceForId():
    '''returns IMXResource\n\n
    getResourceForId(final String id)\n
    '''
def getAllReservations():
    '''returns Collection<IMXReservation>\n\n
    getAllReservations(final Long projectId, final UserInfo userInfo)\n
    '''
def getResourcesAvailability():
    '''returns Collection<IMXResource>\n\n
    getResourcesAvailability(final Set<String> resources, final UserInfo userInfo, final int resourceType, final Long projectId)\n
    '''
def getTotalWorkHours():
    '''returns Double\n\n
    getTotalWorkHours(final Long projectId, final UserInfo userInfo)\n
    '''
def getZoneAvailability():
    '''returns Collection<IMXResource>\n\n
    getZoneAvailability(final Long projectId, final UserInfo userInfo)\n
    '''
def getAllZoneReservations():
    '''returns Collection<IMXReservation>\n\n
    getAllZoneReservations(final Long projectId, final UserInfo userInfo)\n
    '''
