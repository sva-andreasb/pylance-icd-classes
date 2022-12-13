INFORMATION = "short  4096"
SUCCESS = "short  256"
WARNING = "short  16"
ERROR = "short  1"
NOINIT = "short  -1"
def Log():
    '''    public Log(Servlet servlet, final String s)
    '''
def findMessageString():
    '''    public static String findMessageString(final String s)
    public static String findMessageString(final String key, final Object[] obj)
    '''
def getLevel():
    '''    public static final short getLevel()
    '''
def getMessage():
    '''    public static String getMessage(final String str, final Object[] array)
    '''
def init():
    '''    public static void init()
    public static synchronized void init(final Servlet servlet)
    public void init(final Servlet servlet, final String s)
    '''
def logit():
    '''    public String logit(final int n, String x)
    public String logit(final int n, final String s, final Object[] array)
    '''
def msg():
    '''    public static final String msg(final int n, final String s)
    public static final String msg(final int n, final String s, final Object o)
    public static final String msg(final int n, final String s, final Object o, final Object o2)
    public static final String msg(final int n, final String s, final Object o, final Object o2, final Object o3)
    public static final String msg(final int n, final String s, final Object o, final Object o2, final Object o3, final Object o4)
    public static final String msg(final int n, final String s, final Object[] array)
    '''
def willLog():
    '''    public static final boolean willLog(final short n)
    '''
