def getTemplates():
    '''public List<Entity> getTemplates(@Context final HttpServletRequest httpServletRequest, @QueryParam("oslc.where") final String where)
    '''
def getTemplate():
    '''public Template getTemplate(@Context final HttpServletRequest httpServletRequest, @PathParam("templateId") final String templateId)
    '''
def getCompact():
    '''public Compact getCompact(@Context final HttpServletRequest httpServletRequest, @PathParam("templateId") final String templateId)
    '''
def getSmallPreview():
    '''public void getSmallPreview(@Context final HttpServletRequest httpServletRequest, @Context final HttpServletResponse httpServletResponse, @PathParam("resourceId") final String resourceId)
    '''
def createTemplate():
    '''public Response createTemplate(@Context final HttpServletRequest httpServletRequest, final Entity template)
    '''
def updateTemplate():
    '''public Response updateTemplate(@Context final HttpServletRequest httpServletRequest, @PathParam("templateId") final String templateId, final Entity template)
    '''
def deleteTemplate():
    '''public void deleteTemplate(@Context final HttpServletRequest httpServletRequest, @PathParam("templateId") final String templateId)
    '''
