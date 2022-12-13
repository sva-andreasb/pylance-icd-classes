def getInfrastructureResources():
    '''public List<Entity> getInfrastructureResources(@Context final HttpServletRequest httpServletRequest)
    '''
def getInfrastructureResource():
    '''public Entity getInfrastructureResource(@Context final HttpServletRequest httpServletRequest, @PathParam("resourceId") final String resourceId)
    '''
def getCompact():
    '''public Compact getCompact(@Context final HttpServletRequest httpServletRequest, @PathParam("resourceId") final String resourceId)
    '''
def getSmallPreview():
    '''public void getSmallPreview(@Context final HttpServletRequest httpServletRequest, @Context final HttpServletResponse httpServletResponse, @PathParam("resourceId") final String resourceId)
    '''
def createInfrastructureResource():
    '''public Response createInfrastructureResource(@Context final HttpServletRequest httpServletRequest, final Entity resource)
    '''
def updateInfrastructureResource():
    '''public Entity updateInfrastructureResource(@Context final HttpServletRequest httpServletRequest, @PathParam("resourceId") final String resourceId, final Entity resource)
    '''
def deleteInfrastructureResource():
    '''public void deleteInfrastructureResource(@Context final HttpServletRequest httpServletRequest, @PathParam("resourceId") final String resourceId)
    '''
