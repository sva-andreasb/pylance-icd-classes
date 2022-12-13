def getInstances():
'''public List<Entity> getInstances(@Context final HttpServletRequest httpServletRequest, @QueryParam("oslc.where") final String where)
'''
pass
def getInstance():
'''public Entity getInstance(@Context final HttpServletRequest httpServletRequest, @PathParam("instanceId") final String instanceId)
'''
pass
def getCompact():
'''public Compact getCompact(@Context final HttpServletRequest httpServletRequest, @PathParam("instanceId") final String instanceId)
'''
pass
def getSmallPreview():
'''public void getSmallPreview(@Context final HttpServletRequest httpServletRequest, @Context final HttpServletResponse httpServletResponse, @PathParam("resourceId") final String resourceId)
'''
pass
def getLargePreview():
'''public void getLargePreview(@Context final HttpServletRequest httpServletRequest, @Context final HttpServletResponse httpServletResponse, @PathParam("resourceId") final String resourceId)
'''
pass
def createInstance():
'''public Response createInstance(@Context final HttpServletRequest httpServletRequest, final Template instance)
'''
pass
def updateInstance():
'''public Response updateInstance(@Context final HttpServletRequest httpServletRequest, @PathParam("instanceId") final String instanceId, final Entity instance)
'''
pass
def deleteInstance():
'''public void deleteInstance(@Context final HttpServletRequest httpServletRequest, @PathParam("instanceId") final String instanceId)
'''
pass
