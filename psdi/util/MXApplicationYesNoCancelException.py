OK = "int  2"
CANCEL = "int  4"
YES = "int  8"
NO = "int  16"
NULL = "int  -1"
def MXApplicationYesNoCancelException():
    '''    public MXApplicationYesNoCancelException(final String id, final String eg, final String ek)
    public MXApplicationYesNoCancelException(final String id, final String eg, final String ek, final Object[] params)
    public MXApplicationYesNoCancelException(final String id, final String eg, final String ek, final Throwable t)
    public MXApplicationYesNoCancelException(final String id, final String eg, final String ek, final Object[] p, final Throwable t)
    '''
def getId():
    '''    public String getId()
    '''
def postUserInput():
    '''    public void postUserInput(final MXServerRemote server, final int answer, final UserInfo ui)
    '''
def getUserInput():
    '''    public static int getUserInput(final String id, final MXServerRemote server, final UserInfo ui)
    '''
def setContinueEvents():
    '''    public void setContinueEvents(final int responses)
    '''
def getContinueEvents():
    '''    public int getContinueEvents()
    '''
def getUserClickedValue():
    '''    public int getUserClickedValue()
    '''
