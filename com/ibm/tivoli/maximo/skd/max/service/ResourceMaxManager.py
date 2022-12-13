def ResourceMaxManager():
    '''public ResourceMaxManager(final MXServer mxServer)
    '''
def getResources():
    '''public Collection<IMXResource> getResources(final Schedule schedule, final Range<Date> range, final List<String> objectNames, final boolean bucketBased)
    '''
def getReservations():
    '''public Collection<IMXReservation> getReservations(final Schedule schedule, final IMXResource resource)
    '''
def getResourceForId():
    '''public IMXResource getResourceForId(final String id)
    '''
def getAllReservations():
    '''public Collection<IMXReservation> getAllReservations(final Long projectId, final UserInfo userInfo)
    '''
def getResourcesAvailability():
    '''public Collection<IMXResource> getResourcesAvailability(final Set<String> resources, final UserInfo userInfo, final int resourceType, final Long projectId)
    '''
def getTotalWorkHours():
    '''public Double getTotalWorkHours(final Long projectId, final UserInfo userInfo)
    '''
def getModifiedAvailabilityHours():
    '''public Map<String, Double> getModifiedAvailabilityHours(final Long projectId, final String type, final UserInfo userInfo)
    '''
def getZoneAvailability():
    '''public Collection<IMXResource> getZoneAvailability(final Long projectId, final UserInfo userInfo)
    '''
def getAllZoneReservations():
    '''public Collection<IMXReservation> getAllZoneReservations(final Long projectId, final UserInfo userInfo)
    '''
