def getTemplates():
'''public List<Entity> getTemplates(@Context final HttpServletRequest httpServletRequest, @QueryParam("oslc.where") final String where)
'''
pass
def getTemplate():
'''public Template getTemplate(@Context final HttpServletRequest httpServletRequest, @PathParam("templateId") final String templateId)
'''
pass
def getCompact():
'''public Compact getCompact(@Context final HttpServletRequest httpServletRequest, @PathParam("templateId") final String templateId)
'''
pass
def getSmallPreview():
'''public void getSmallPreview(@Context final HttpServletRequest httpServletRequest, @Context final HttpServletResponse httpServletResponse, @PathParam("resourceId") final String resourceId)
'''
pass
def createTemplate():
'''public Response createTemplate(@Context final HttpServletRequest httpServletRequest, final Entity template)
'''
pass
def updateTemplate():
'''public Response updateTemplate(@Context final HttpServletRequest httpServletRequest, @PathParam("templateId") final String templateId, final Entity template)
'''
pass
def deleteTemplate():
'''public void deleteTemplate(@Context final HttpServletRequest httpServletRequest, @PathParam("templateId") final String templateId)
'''
pass
