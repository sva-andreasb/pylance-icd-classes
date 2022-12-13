def distinct():
'''public static SqlNode distinct(final SDBRequest request, final SqlNode sqlNode)
'''
pass
def project():
'''public static SqlNode project(final SDBRequest request, final SqlNode sqlNode)
public static SqlNode project(final SDBRequest request, final SqlNode sqlNode, final Collection<ColAlias> cols)
public static SqlNode project(final SDBRequest request, final SqlNode sqlNode, final ColAlias col)
'''
pass
def slice():
'''public static SqlNode slice(final SDBRequest request, final SqlNode sqlNode, long start, long length)
'''
pass
def view():
'''public static SqlNode view(final SDBRequest request, final SqlNode sqlNode)
'''
pass
def restrict():
'''public static SqlNode restrict(final SDBRequest request, final SqlNode sqlNode, final SqlExprList exprs)
public static SqlNode restrict(final SDBRequest request, final SqlNode sqlNode, final SqlExpr expr)
'''
pass
def isSelectBlock():
'''public boolean isSelectBlock()
'''
pass
def asSelectBlock():
'''public SqlSelectBlock asSelectBlock()
'''
pass
def setBlockAlias():
'''public void setBlockAlias(final String alias)
'''
pass
def getCols():
'''public List<ColAlias> getCols()
'''
pass
def add():
'''public void add(final ColAlias c)
'''
pass
def addAll():
'''public void addAll(final Collection<ColAlias> vc)
'''
pass
def clearView():
'''public SqlNode clearView()
'''
pass
def getConditions():
'''public SqlExprList getConditions()
'''
pass
def hasSlice():
'''public boolean hasSlice()
'''
pass
def hasConditions():
'''public boolean hasConditions()
'''
pass
def getStart():
'''public long getStart()
'''
pass
def getLength():
'''public long getLength()
'''
pass
def getIdScope():
'''public Scope getIdScope()
'''
pass
def getNodeScope():
'''public Scope getNodeScope()
'''
pass
def apply():
'''public SqlNode apply(final SqlTransform transform, final SqlNode newSubNode)
'''
pass
def copy():
'''public SqlNode copy(final SqlNode subNode)
'''
pass
def visit():
'''public void visit(final SqlNodeVisitor visitor)
'''
pass
def getDistinct():
'''public boolean getDistinct()
'''
pass
