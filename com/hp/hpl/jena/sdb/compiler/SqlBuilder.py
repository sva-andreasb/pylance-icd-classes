def distinct():
'''public static SqlNode distinct(final SDBRequest request, final SqlNode sqlNode)
'''
pass
def slice():
'''public static SqlNode slice(final SDBRequest request, final SqlNode sqlNode, final long start, final long length)
'''
pass
def project():
'''public static SqlNode project(final SDBRequest request, final SqlNode sqlNode, final Collection<ColAlias> cols)
public static SqlNode project(final SDBRequest request, final SqlNode sqlNode, final ColAlias col)
'''
pass
def view():
'''public static SqlNode view(final SDBRequest request, final SqlNode sqlNode)
'''
pass
def restrict():
'''public static SqlNode restrict(final SDBRequest request, SqlNode sqlNode, final SqlExprList conditions)
public static SqlNode restrict(final SDBRequest request, final SqlNode sqlNode, final SqlExpr expr)
'''
pass
def innerJoin():
'''public static SqlNode innerJoin(final SDBRequest request, final SqlNode left, final SqlNode right)
'''
pass
def leftJoin():
'''public static SqlNode leftJoin(final SDBRequest request, final SqlNode left, final SqlNode right, final SqlExpr expr)
'''
pass
def leftJoinCoalesce():
'''public static SqlNode leftJoinCoalesce(final SDBRequest request, final String alias, final SqlNode left, final SqlNode right, final Set<Var> coalesceVars)
'''
pass