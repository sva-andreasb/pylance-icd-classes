def ():
    '''returns ApiModel\n\n
    (final String xml)\n
    (final ModelObject[] model, final String title, final int depth, final int max_objs, final OIDExpander autofill, final HashMap suppressList)\n
    (final ModelObject[] model, final String title, int depth, final String[] attribs, final int max_objs, final OIDExpander autofill, final HashMap suppressList)\n
    (final ModelObject[] model, final String title, int depth)\n
    (final ModelObject[] model, final String title, int depth, final String[] attribs, final OIDExpander autofill)\n
    '''
def toXml():
    '''returns String\n\n
    toXml(final String query)\n
    '''
def toValue():
    '''returns String\n\n
    toValue(final String query)\n
    '''
def toModel():
    '''returns ModelObject[]\n\n
    toModel()\n
    toModel(final HashMap oidMap, final Class[] oidClasses)\n
    '''
def getExportMode():
    '''returns boolean\n\n
    getExportMode()\n
    '''
def setExportMode():
    '''returns None\n\n
    setExportMode(final boolean flag)\n
    '''
def getIndent():
    '''returns int\n\n
    getIndent()\n
    '''
def setIndent():
    '''returns None\n\n
    setIndent(final int indent)\n
    '''
def setDoDestroy():
    '''returns None\n\n
    setDoDestroy(final boolean destroy)\n
    '''
def getAutoFill():
    '''returns OIDExpander\n\n
    getAutoFill()\n
    '''
def setAutoFill():
    '''returns None\n\n
    setAutoFill(final OIDExpander autofill)\n
    '''
def getSourceName():
    '''returns String\n\n
    getSourceName()\n
    '''
def setSourceName():
    '''returns None\n\n
    setSourceName(final String sourceName)\n
    '''
