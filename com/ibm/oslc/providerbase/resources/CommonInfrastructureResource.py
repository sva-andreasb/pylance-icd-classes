def getInfrastructureResources():
'''public List<Entity> getInfrastructureResources(@Context final HttpServletRequest httpServletRequest)
'''
pass
def getInfrastructureResource():
'''public Entity getInfrastructureResource(@Context final HttpServletRequest httpServletRequest, @PathParam("resourceId") final String resourceId)
'''
pass
def getCompact():
'''public Compact getCompact(@Context final HttpServletRequest httpServletRequest, @PathParam("resourceId") final String resourceId)
'''
pass
def getSmallPreview():
'''public void getSmallPreview(@Context final HttpServletRequest httpServletRequest, @Context final HttpServletResponse httpServletResponse, @PathParam("resourceId") final String resourceId)
'''
pass
def createInfrastructureResource():
'''public Response createInfrastructureResource(@Context final HttpServletRequest httpServletRequest, final Entity resource)
'''
pass
def updateInfrastructureResource():
'''public Entity updateInfrastructureResource(@Context final HttpServletRequest httpServletRequest, @PathParam("resourceId") final String resourceId, final Entity resource)
'''
pass
def deleteInfrastructureResource():
'''public void deleteInfrastructureResource(@Context final HttpServletRequest httpServletRequest, @PathParam("resourceId") final String resourceId)
'''
pass