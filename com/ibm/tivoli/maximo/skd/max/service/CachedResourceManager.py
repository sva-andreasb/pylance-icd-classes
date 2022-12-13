def CachedResourceManager():
'''public CachedResourceManager(final IResourceManager parent)
'''
pass
def getResources():
'''public Collection<IMXResource> getResources(final Schedule schedule, final Range<Date> range, final List<String> objectNames, final boolean bucketBased)
'''
pass
def getReservations():
'''public Collection<IMXReservation> getReservations(final Schedule schedule, final IMXResource resource)
'''
pass
def getResourceForId():
'''public IMXResource getResourceForId(final String id)
'''
pass
def clearCaches():
'''public void clearCaches()
'''
pass
def getAllReservations():
'''public Collection<IMXReservation> getAllReservations(final Long projectId, final UserInfo userInfo)
'''
pass
def getResourcesAvailability():
'''public Collection<IMXResource> getResourcesAvailability(final Set<String> resources, final UserInfo userInfo, final int resourceType, final Long projectId)
'''
pass
def getTotalWorkHours():
'''public Double getTotalWorkHours(final Long projectId, final UserInfo userInfo)
'''
pass
def getModifiedAvailabilityHours():
'''public Map<String, Double> getModifiedAvailabilityHours(final Long projectId, final String type, final UserInfo userInfo)
'''
pass
def getZoneAvailability():
'''public Collection<IMXResource> getZoneAvailability(final Long projectId, final UserInfo userInfo)
'''
pass
def getAllZoneReservations():
'''public Collection<IMXReservation> getAllZoneReservations(final Long projectId, final UserInfo userInfo)
'''
pass
