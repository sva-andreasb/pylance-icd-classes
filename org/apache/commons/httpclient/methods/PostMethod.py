FORM_URL_ENCODED_CONTENT_TYPE = "String  \"application/x-www-form-urlencoded\""
def ():
    '''returns PostMethod\n\n
    ()\n
    (final String uri)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def setParameter():
    '''returns None\n\n
    setParameter(final String parameterName, final String parameterValue)\n
    '''
def getParameter():
    '''returns NameValuePair\n\n
    getParameter(final String paramName)\n
    '''
def getParameters():
    '''returns NameValuePair[]\n\n
    getParameters()\n
    '''
def addParameter():
    '''returns None\n\n
    addParameter(final String paramName, final String paramValue)\n
    addParameter(final NameValuePair param)\n
    '''
def addParameters():
    '''returns None\n\n
    addParameters(final NameValuePair[] parameters)\n
    '''
def removeParameter():
    '''returns boolean\n\n
    removeParameter(final String paramName)\n
    removeParameter(final String paramName, final String paramValue)\n
    '''
def setRequestBody():
    '''returns None\n\n
    setRequestBody(final NameValuePair[] parametersBody)\n
    '''
