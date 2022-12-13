def selectFirstString():
    '''public static String selectFirstString(final Connection dc, final String query)
    '''
def selectFirstStringPs():
    '''public static String selectFirstStringPs(final Connection dc, final String query, final String... params)
    '''
def listAllStrings():
    '''public static List<String> listAllStrings(final Connection dc, final String query)
    '''
def doSql():
    '''public static int doSql(final Connection con, final String sql, final boolean ignoreError)
    public static void doSql(final Connection con, final List<String> sqlList, final boolean ignoreError)
    public static void doSql(final Connection con, final List<String> sqlList)
    public static int doSql(final Connection con, final String sql)
    public static int doSql(final Connection con, final String sql, final String... params)
    public static int doSql(final Connection dc, final SQLSpecificTransform transform, final String sql)
    public static void doSql(final Connection dc, final SQLSpecificTransform sqlTransform, final String... sql)
    '''
def selectFirstInteger():
    '''public static Integer selectFirstInteger(final Connection con, final String query)
    '''
def exists():
    '''public static boolean exists(final Connection dc, final String query)
    '''
def existsPs():
    '''public static boolean existsPs(final Connection dc, final String query, final String... params)
    '''
def selectAll():
    '''public static List<AttributeStorage> selectAll(final Connection dc, final String query, final AttributeStorageDefinition retStoreDef)
    '''
def selectFirst():
    '''public static AttributeStorage selectFirst(final Connection con, final String query, final AttributeStorageDefinition asd)
    '''
def selectFirstBoolean():
    '''public static Boolean selectFirstBoolean(final Connection con, final String query)
    '''
def selectFirstLong():
    '''public static Long selectFirstLong(final Connection con, final String query)
    '''
def doCall():
    '''public static void doCall(final Connection con, final String call)
    '''
def selectFirstDouble():
    '''public static Double selectFirstDouble(final Connection con, final String query)
    '''
def printQuery():
    '''public static String printQuery(final Connection dc, final String query)
    '''
