def getInstances():
    '''returns List<Entity>\n\n
    getInstances(@Context final HttpServletRequest httpServletRequest, @QueryParam("oslc.where") final String where)\n
    '''
def getInstance():
    '''returns Entity\n\n
    getInstance(@Context final HttpServletRequest httpServletRequest, @PathParam("instanceId") final String instanceId)\n
    '''
def getCompact():
    '''returns Compact\n\n
    getCompact(@Context final HttpServletRequest httpServletRequest, @PathParam("instanceId") final String instanceId)\n
    '''
def getSmallPreview():
    '''returns None\n\n
    getSmallPreview(@Context final HttpServletRequest httpServletRequest, @Context final HttpServletResponse httpServletResponse, @PathParam("resourceId") final String resourceId)\n
    '''
def getLargePreview():
    '''returns None\n\n
    getLargePreview(@Context final HttpServletRequest httpServletRequest, @Context final HttpServletResponse httpServletResponse, @PathParam("resourceId") final String resourceId)\n
    '''
def createInstance():
    '''returns Response\n\n
    createInstance(@Context final HttpServletRequest httpServletRequest, final Template instance)\n
    '''
def updateInstance():
    '''returns Response\n\n
    updateInstance(@Context final HttpServletRequest httpServletRequest, @PathParam("instanceId") final String instanceId, final Entity instance)\n
    '''
def deleteInstance():
    '''returns None\n\n
    deleteInstance(@Context final HttpServletRequest httpServletRequest, @PathParam("instanceId") final String instanceId)\n
    '''
