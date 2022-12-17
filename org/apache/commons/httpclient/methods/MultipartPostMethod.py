MULTIPART_FORM_CONTENT_TYPE = "String  \"multipart/form-data\""
def ():
    '''returns MultipartPostMethod\n\n
    ()\n
    (final String uri)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def addParameter():
    '''returns None\n\n
    addParameter(final String parameterName, final String parameterValue)\n
    addParameter(final String parameterName, final File parameterFile)\n
    addParameter(final String parameterName, final String fileName, final File parameterFile)\n
    '''
def addPart():
    '''returns None\n\n
    addPart(final Part part)\n
    '''
def getParts():
    '''returns Part[]\n\n
    getParts()\n
    '''
def recycle():
    '''returns None\n\n
    recycle()\n
    '''
