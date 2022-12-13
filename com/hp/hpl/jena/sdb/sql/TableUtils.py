def dump():
'''public static void dump(final SDBConnection conn, final String tableName)
public static void dump(final Connection conn, final String tableName)
'''
pass
def hasTable():
'''public static boolean hasTable(final Connection connection, final String table, String... types)
public static boolean hasTable(final SDBConnectionHolder holder, final String table, final String... types)
'''
pass
def getTableNames():
'''public static List<String> getTableNames(final Connection connection)
public static List<String> getTableNames(final Connection connection, final String tableTypeName)
'''
pass
def getTableSize():
'''public static long getTableSize(final Connection connection, final String table)
'''
pass
def dropTable():
'''public static void dropTable(final SDBConnection connection, final String tableName)
'''
pass
def dropTableSilent():
'''public static void dropTableSilent(final SDBConnection connection, final String tableName)
'''
pass
