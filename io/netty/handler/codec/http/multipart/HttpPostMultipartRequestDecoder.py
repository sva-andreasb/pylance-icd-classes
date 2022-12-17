def ():
    '''returns HttpPostMultipartRequestDecoder\n\n
    (final HttpRequest request)\n
    (final HttpDataFactory factory, final HttpRequest request)\n
    (final HttpDataFactory factory, final HttpRequest request, final Charset charset)\n
    '''
def isMultipart():
    '''returns boolean\n\n
    isMultipart()\n
    '''
def setDiscardThreshold():
    '''returns None\n\n
    setDiscardThreshold(final int discardThreshold)\n
    '''
def getDiscardThreshold():
    '''returns int\n\n
    getDiscardThreshold()\n
    '''
def getBodyHttpDatas():
    '''returns List<InterfaceHttpData>\n\n
    getBodyHttpDatas()\n
    getBodyHttpDatas(final String name)\n
    '''
def getBodyHttpData():
    '''returns InterfaceHttpData\n\n
    getBodyHttpData(final String name)\n
    '''
def offer():
    '''returns HttpPostMultipartRequestDecoder\n\n
    offer(final HttpContent content)\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    '''
def next():
    '''returns InterfaceHttpData\n\n
    next()\n
    '''
def currentPartialHttpData():
    '''returns InterfaceHttpData\n\n
    currentPartialHttpData()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def cleanFiles():
    '''returns None\n\n
    cleanFiles()\n
    '''
def removeHttpDataFromClean():
    '''returns None\n\n
    removeHttpDataFromClean(final InterfaceHttpData data)\n
    '''
