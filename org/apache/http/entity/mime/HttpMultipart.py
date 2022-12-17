def ():
    '''returns HttpMultipart\n\n
    (final String subType, final Charset charset, final String boundary, final HttpMultipartMode mode)\n
    (final String subType, final Charset charset, final String boundary)\n
    (final String subType, final String boundary)\n
    '''
def getSubType():
    '''returns String\n\n
    getSubType()\n
    '''
def getCharset():
    '''returns Charset\n\n
    getCharset()\n
    '''
def getMode():
    '''returns HttpMultipartMode\n\n
    getMode()\n
    '''
def getBodyParts():
    '''returns List<FormBodyPart>\n\n
    getBodyParts()\n
    '''
def addBodyPart():
    '''returns None\n\n
    addBodyPart(final FormBodyPart part)\n
    '''
def getBoundary():
    '''returns String\n\n
    getBoundary()\n
    '''
def writeTo():
    '''returns None\n\n
    writeTo(final OutputStream out)\n
    '''
def getTotalLength():
    '''returns long\n\n
    getTotalLength()\n
    '''
