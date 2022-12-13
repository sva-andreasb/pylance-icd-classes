ERROR_CONNECT_TO_SELF = "String  \"message.linetoself\""
ERROR_CONNECTED = "String  \"message.lineexists\""
ERROR_ACTION_NOT_ALLOWED = "String  \"message.actionnotallowed\""
ERROR_NODE_NOT_ALLOWED = "String  \"message.nodenotallowed\""
MESSAGE_ADD = "String  \"message.add\""
MESSAGE_DELETE = "String  \"message.delete\""
MESSAGE_MOVE = "String  \"message.move\""
ERROR_NEED_JAVASCRIPT = "String  \"message.needjavascript\""
WARNING_LOSE_CHANGES = "String  \"message.losechanges\""
WARNING_WF_DELETE = "String  \"message.deleteworkflow\""
def showException():
    '''    public static void showException(final JApplet appletObject, final Exception ex)
    public static void showException(final JApplet appletObject, final Exception ex, final String message, final boolean asWarning)
    '''
def showError():
    '''    public static void showError(final JApplet appletObject, final Exception ex, String message)
    '''
def showWarning():
    '''    public static void showWarning(final JApplet appletObject, final Exception ex, String message)
    '''
def showMessage():
    '''    public static void showMessage(final JApplet appletObject, final Hashtable dialogInfo, final Object message)
    public static boolean showMessage(final String key)
    public static boolean showMessage(final String key, final Object arg)
    public static boolean showMessage(final String key, final Object[] args)
    public static boolean showMessage(final String key, final String message)
    public static boolean showMessage(final String key, String message, final Object[] args)
    '''
