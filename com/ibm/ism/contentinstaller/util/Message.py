TYPE_ERROR = "int  0"
TYPE_WARNING = "int  1"
TYPE_ALERT = "int  2"
TYPE_REPLACEMENT_REQUIRED = "int  3"
def Message():
    '''    public Message(final int type, final String msgId, final Object[] msgArgs)
    '''
def getType():
    '''    public int getType()
    '''
def getMsgId():
    '''    public String getMsgId()
    '''
def getMsgArgs():
    '''    public Object[] getMsgArgs()
    '''
def newError():
    '''    public static Message newError(final String msgId, final Object[] msgArgs)
    '''
def newWarning():
    '''    public static Message newWarning(final String msgId, final Object[] msgArgs)
    '''
def newAlert():
    '''    public static Message newAlert(final String msgId, final Object[] msgArgs)
    '''
def newReplacementRequired():
    '''    public static Message newReplacementRequired(final String msgId, final Object[] msgArgs)
    '''
def isError():
    '''    public boolean isError()
    '''
def isWarning():
    '''    public boolean isWarning()
    '''
def isAlert():
    '''    public boolean isAlert()
    '''
def isReplacementRequired():
    '''    public boolean isReplacementRequired()
    '''
