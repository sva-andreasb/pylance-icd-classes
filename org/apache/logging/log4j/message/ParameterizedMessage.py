RECURSION_PREFIX = "String  \"[...\""
RECURSION_SUFFIX = "String  \"...]\""
ERROR_PREFIX = "String  \"[!!!\""
ERROR_SEPARATOR = "String  \"=>\""
ERROR_MSG_SEPARATOR = "String  \":\""
ERROR_SUFFIX = "String  \"!!!]\""
def ():
    '''returns ParameterizedMessage\n\n
    (final String messagePattern, final String[] arguments, final Throwable throwable)\n
    (final String messagePattern, final Object[] arguments, final Throwable throwable)\n
    (final String messagePattern, final Object... arguments)\n
    (final String messagePattern, final Object arg)\n
    (final String messagePattern, final Object arg0, final Object arg1)\n
    '''
def getFormat():
    '''returns String\n\n
    getFormat()\n
    '''
def getParameters():
    '''returns Object[]\n\n
    getParameters()\n
    '''
def getThrowable():
    '''returns Throwable\n\n
    getThrowable()\n
    '''
def getFormattedMessage():
    '''returns String\n\n
    getFormattedMessage()\n
    '''
def formatTo():
    '''returns None\n\n
    formatTo(final StringBuilder buffer)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
