def ():
    '''returns ThrowableProxy\n\n
    (final Throwable throwable)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def formatWrapper():
    '''returns None\n\n
    formatWrapper(final StringBuilder sb, final ThrowableProxy cause, final String suffix)\n
    formatWrapper(final StringBuilder sb, final ThrowableProxy cause, final List<String> ignorePackages, final String suffix)\n
    formatWrapper(final StringBuilder sb, final ThrowableProxy cause, final List<String> ignorePackages, final TextRenderer textRenderer, final String suffix)\n
    formatWrapper(final StringBuilder sb, final ThrowableProxy cause, final List<String> ignorePackages, final TextRenderer textRenderer, final String suffix, final String lineSeparator)\n
    '''
def getCauseProxy():
    '''returns ThrowableProxy\n\n
    getCauseProxy()\n
    '''
def getCauseStackTraceAsString():
    '''returns String\n\n
    getCauseStackTraceAsString(final String suffix)\n
    getCauseStackTraceAsString(final List<String> packages, final String suffix)\n
    getCauseStackTraceAsString(final List<String> ignorePackages, final TextRenderer textRenderer, final String suffix)\n
    getCauseStackTraceAsString(final List<String> ignorePackages, final TextRenderer textRenderer, final String suffix, final String lineSeparator)\n
    '''
def getCommonElementCount():
    '''returns int\n\n
    getCommonElementCount()\n
    '''
def getExtendedStackTrace():
    '''returns ExtendedStackTraceElement[]\n\n
    getExtendedStackTrace()\n
    '''
def getExtendedStackTraceAsString():
    '''returns String\n\n
    getExtendedStackTraceAsString()\n
    getExtendedStackTraceAsString(final String suffix)\n
    getExtendedStackTraceAsString(final List<String> ignorePackages, final String suffix)\n
    getExtendedStackTraceAsString(final List<String> ignorePackages, final TextRenderer textRenderer, final String suffix)\n
    getExtendedStackTraceAsString(final List<String> ignorePackages, final TextRenderer textRenderer, final String suffix, final String lineSeparator)\n
    '''
def formatExtendedStackTraceTo():
    '''returns None\n\n
    formatExtendedStackTraceTo(final StringBuilder sb, final List<String> ignorePackages, final TextRenderer textRenderer, final String suffix, final String lineSeparator)\n
    '''
def getLocalizedMessage():
    '''returns String\n\n
    getLocalizedMessage()\n
    '''
def getMessage():
    '''returns String\n\n
    getMessage()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getStackTrace():
    '''returns StackTraceElement[]\n\n
    getStackTrace()\n
    '''
def getSuppressedProxies():
    '''returns ThrowableProxy[]\n\n
    getSuppressedProxies()\n
    '''
def getSuppressedStackTrace():
    '''returns String\n\n
    getSuppressedStackTrace(final String suffix)\n
    '''
def getThrowable():
    '''returns Throwable\n\n
    getThrowable()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
