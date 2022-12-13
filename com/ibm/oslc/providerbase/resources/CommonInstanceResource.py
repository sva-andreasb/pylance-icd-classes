def getInstances():
    '''    public List<Entity> getInstances(@Context final HttpServletRequest httpServletRequest, @QueryParam("oslc.where") final String where)
    '''
def getInstance():
    '''    public Entity getInstance(@Context final HttpServletRequest httpServletRequest, @PathParam("instanceId") final String instanceId)
    '''
def getCompact():
    '''    public Compact getCompact(@Context final HttpServletRequest httpServletRequest, @PathParam("instanceId") final String instanceId)
    '''
def getSmallPreview():
    '''    public void getSmallPreview(@Context final HttpServletRequest httpServletRequest, @Context final HttpServletResponse httpServletResponse, @PathParam("resourceId") final String resourceId)
    '''
def getLargePreview():
    '''    public void getLargePreview(@Context final HttpServletRequest httpServletRequest, @Context final HttpServletResponse httpServletResponse, @PathParam("resourceId") final String resourceId)
    '''
def createInstance():
    '''    public Response createInstance(@Context final HttpServletRequest httpServletRequest, final Template instance)
    '''
def updateInstance():
    '''    public Response updateInstance(@Context final HttpServletRequest httpServletRequest, @PathParam("instanceId") final String instanceId, final Entity instance)
    '''
def deleteInstance():
    '''    public void deleteInstance(@Context final HttpServletRequest httpServletRequest, @PathParam("instanceId") final String instanceId)
    '''
