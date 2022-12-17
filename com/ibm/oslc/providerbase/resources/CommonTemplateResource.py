def getTemplates():
    '''returns List<Entity>\n\n
    getTemplates(@Context final HttpServletRequest httpServletRequest, @QueryParam("oslc.where") final String where)\n
    '''
def getTemplate():
    '''returns Template\n\n
    getTemplate(@Context final HttpServletRequest httpServletRequest, @PathParam("templateId") final String templateId)\n
    '''
def getCompact():
    '''returns Compact\n\n
    getCompact(@Context final HttpServletRequest httpServletRequest, @PathParam("templateId") final String templateId)\n
    '''
def getSmallPreview():
    '''returns None\n\n
    getSmallPreview(@Context final HttpServletRequest httpServletRequest, @Context final HttpServletResponse httpServletResponse, @PathParam("resourceId") final String resourceId)\n
    '''
def createTemplate():
    '''returns Response\n\n
    createTemplate(@Context final HttpServletRequest httpServletRequest, final Entity template)\n
    '''
def updateTemplate():
    '''returns Response\n\n
    updateTemplate(@Context final HttpServletRequest httpServletRequest, @PathParam("templateId") final String templateId, final Entity template)\n
    '''
def deleteTemplate():
    '''returns None\n\n
    deleteTemplate(@Context final HttpServletRequest httpServletRequest, @PathParam("templateId") final String templateId)\n
    '''
