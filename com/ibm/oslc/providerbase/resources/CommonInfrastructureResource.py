def getInfrastructureResources():
    '''returns List<Entity>\n\n
    getInfrastructureResources(@Context final HttpServletRequest httpServletRequest)\n
    '''
def getInfrastructureResource():
    '''returns Entity\n\n
    getInfrastructureResource(@Context final HttpServletRequest httpServletRequest, @PathParam("resourceId") final String resourceId)\n
    '''
def getCompact():
    '''returns Compact\n\n
    getCompact(@Context final HttpServletRequest httpServletRequest, @PathParam("resourceId") final String resourceId)\n
    '''
def getSmallPreview():
    '''returns None\n\n
    getSmallPreview(@Context final HttpServletRequest httpServletRequest, @Context final HttpServletResponse httpServletResponse, @PathParam("resourceId") final String resourceId)\n
    '''
def createInfrastructureResource():
    '''returns Response\n\n
    createInfrastructureResource(@Context final HttpServletRequest httpServletRequest, final Entity resource)\n
    '''
def updateInfrastructureResource():
    '''returns Entity\n\n
    updateInfrastructureResource(@Context final HttpServletRequest httpServletRequest, @PathParam("resourceId") final String resourceId, final Entity resource)\n
    '''
def deleteInfrastructureResource():
    '''returns None\n\n
    deleteInfrastructureResource(@Context final HttpServletRequest httpServletRequest, @PathParam("resourceId") final String resourceId)\n
    '''
