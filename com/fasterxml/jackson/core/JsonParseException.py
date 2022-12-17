def ():
    '''returns JsonParseException\n\n
    (final String msg, final JsonLocation loc)\n
    (final String msg, final JsonLocation loc, final Throwable root)\n
    (final JsonParser p, final String msg)\n
    (final JsonParser p, final String msg, final Throwable root)\n
    (final JsonParser p, final String msg, final JsonLocation loc)\n
    (final JsonParser p, final String msg, final JsonLocation loc, final Throwable root)\n
    '''
def withParser():
    '''returns JsonParseException\n\n
    withParser(final JsonParser p)\n
    '''
def withRequestPayload():
    '''returns JsonParseException\n\n
    withRequestPayload(final RequestPayload p)\n
    '''
def getProcessor():
    '''returns JsonParser\n\n
    getProcessor()\n
    '''
def getRequestPayload():
    '''returns RequestPayload\n\n
    getRequestPayload()\n
    '''
def getRequestPayloadAsString():
    '''returns String\n\n
    getRequestPayloadAsString()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    '''
