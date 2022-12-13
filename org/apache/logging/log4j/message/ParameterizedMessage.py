RECURSION_PREFIX = "String  \"[...\""
RECURSION_SUFFIX = "String  \"...]\""
ERROR_PREFIX = "String  \"[!!!\""
ERROR_SEPARATOR = "String  \"=>\""
ERROR_MSG_SEPARATOR = "String  \":\""
ERROR_SUFFIX = "String  \"!!!]\""
def ParameterizedMessage():
    '''public ParameterizedMessage(final String messagePattern, final String[] arguments, final Throwable throwable)
    public ParameterizedMessage(final String messagePattern, final Object[] arguments, final Throwable throwable)
    public ParameterizedMessage(final String messagePattern, final Object... arguments)
    public ParameterizedMessage(final String messagePattern, final Object arg)
    public ParameterizedMessage(final String messagePattern, final Object arg0, final Object arg1)
    '''
def getFormat():
    '''public String getFormat()
    '''
def getParameters():
    '''public Object[] getParameters()
    '''
def getThrowable():
    '''public Throwable getThrowable()
    '''
def getFormattedMessage():
    '''public String getFormattedMessage()
    '''
def formatTo():
    '''public void formatTo(final StringBuilder buffer)
    '''
def format():
    '''public static String format(final String messagePattern, final Object[] arguments)
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def countArgumentPlaceholders():
    '''public static int countArgumentPlaceholders(final String messagePattern)
    '''
def deepToString():
    '''public static String deepToString(final Object o)
    '''
def identityToString():
    '''public static String identityToString(final Object obj)
    '''
def toString():
    '''public String toString()
    '''
