COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
ILOG_ODM_SERVICE_LOGGER = "String  \"ilog.odm.service\""
RC_OK = "int  0"
RC_NONE = "int  -1"
CIVDM1003E_application_already_deployed_RC = "int  8"
CIVDM1008E_wrong_file_name_RC = "int  4"
CIVDM1009E_cannot_find_settings_file_RC = "int  6"
CIVDM1011E_directory_not_specified_RC = "int  3"
CIVDM1018E_IloDeployODMAppTask_fileisdirectory_RC = "int  10"
CIVDM1019E_IloDeployODMAppTask_cantcreatedirectories_RC = "int  11"
CIVDM1029E_InvalidCmdLineArg_RC = "int  1"
CIVDM1039E_CannotCreateTempDir_RC = "int  5"
CIVDM1048E_ServerNotEnabled_RC = "int  9"
CIVDM1061E_PrereqOptionMustBeSetBefore_RC = "int  12"
CIVDM1063E_MissingArgsForOption_RC = "int  7"
CIVDM1112E_specified_file_does_not_exist_RC = "int  14"
CIVDM1113E_file_should_be_dir_RC = "int  15"
CIVDM1114E_file_should_be_file_RC = "int  16"
CIVDM1117E_Unspecified_Deployment_Exception_RC = "int  99"
CIVDM1119W_Solve_Status_No_Solution_RC = "int  20"
CIVDM1120W_Solve_Status_Aborted_RC = "int  21"
def getRC():
    '''    public int getRC()
    public int getRC()
    '''
def getSeverity():
    '''    public final Severity getSeverity()
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def callerMethod():
    '''    public static Object[] callerMethod(final Object... parameters)
    public static String callerMethod(final int callerLevel)
    '''
def getRCOrRethrow():
    '''    public <E extends Exception> IloServiceMessageCodesWithRC getRCOrRethrow(final E exception)
    public <E extends Exception> IloServiceMessageCodesWithRC getRCOrRethrow(final E exception)
    public IloServiceMessageCodesWithRC getRCOrRethrow()
    '''
def handleRTE():
    '''    public DeploymentException handleRTE(final RuntimeException rtExc, final Object... parameters)
    '''
def IloServiceMessageCodesWithRC():
    '''    public IloServiceMessageCodesWithRC()
    '''
def logRC():
    '''    public int logRC(final Object... parameters)
    '''
def compareTo():
    '''    public int compareTo(final IloServiceMessageCodesWithRC o)
    '''
def help():
    '''    public static void help(final boolean extended)
    '''
def logExc():
    '''    public int logExc(final Exception exc)
    '''
def IllegalArgumentException():
    '''    public IllegalArgumentException(final Object... parameters)
    public IllegalArgumentException(final java.lang.IllegalArgumentException cause, final Object... parameters)
    '''
def getMessageCode():
    '''    public IloServiceMessageCodes getMessageCode()
    public IloServiceMessageCodes getMessageCode()
    '''
def DeploymentException():
    '''    public DeploymentException(final Object... parameters)
    public DeploymentException(final Throwable cause, final Object... parameters)
    '''
def DeploymentExceptionWithCallerMethod():
    '''    public DeploymentExceptionWithCallerMethod(final Object... parameters)
    public DeploymentExceptionWithCallerMethod(final Throwable cause, final Object... parameters)
    '''
def DeploymentIOException():
    '''    public DeploymentIOException(final IOException cause, final Object... parameters)
    '''
def DeploymentSecurityException():
    '''    public DeploymentSecurityException(final GeneralSecurityException cause)
    '''
