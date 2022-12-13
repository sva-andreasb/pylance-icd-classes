def selectFirstString():
'''public static String selectFirstString(final Connection dc, final String query)
'''
pass
def selectFirstStringPs():
'''public static String selectFirstStringPs(final Connection dc, final String query, final String... params)
'''
pass
def listAllStrings():
'''public static List<String> listAllStrings(final Connection dc, final String query)
'''
pass
def doSql():
'''public static int doSql(final Connection con, final String sql, final boolean ignoreError)
public static void doSql(final Connection con, final List<String> sqlList, final boolean ignoreError)
public static void doSql(final Connection con, final List<String> sqlList)
public static int doSql(final Connection con, final String sql)
public static int doSql(final Connection con, final String sql, final String... params)
public static int doSql(final Connection dc, final SQLSpecificTransform transform, final String sql)
public static void doSql(final Connection dc, final SQLSpecificTransform sqlTransform, final String... sql)
'''
pass
def selectFirstInteger():
'''public static Integer selectFirstInteger(final Connection con, final String query)
'''
pass
def exists():
'''public static boolean exists(final Connection dc, final String query)
'''
pass
def existsPs():
'''public static boolean existsPs(final Connection dc, final String query, final String... params)
'''
pass
def selectAll():
'''public static List<AttributeStorage> selectAll(final Connection dc, final String query, final AttributeStorageDefinition retStoreDef)
'''
pass
def selectFirst():
'''public static AttributeStorage selectFirst(final Connection con, final String query, final AttributeStorageDefinition asd)
'''
pass
def selectFirstBoolean():
'''public static Boolean selectFirstBoolean(final Connection con, final String query)
'''
pass
def selectFirstLong():
'''public static Long selectFirstLong(final Connection con, final String query)
'''
pass
def doCall():
'''public static void doCall(final Connection con, final String call)
'''
pass
def selectFirstDouble():
'''public static Double selectFirstDouble(final Connection con, final String query)
'''
pass
def printQuery():
'''public static String printQuery(final Connection dc, final String query)
'''
pass
