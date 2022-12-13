def distinct():
    '''    public static SqlNode distinct(final SDBRequest request, final SqlNode sqlNode)
    '''
def project():
    '''    public static SqlNode project(final SDBRequest request, final SqlNode sqlNode)
    public static SqlNode project(final SDBRequest request, final SqlNode sqlNode, final Collection<ColAlias> cols)
    public static SqlNode project(final SDBRequest request, final SqlNode sqlNode, final ColAlias col)
    '''
def slice():
    '''    public static SqlNode slice(final SDBRequest request, final SqlNode sqlNode, long start, long length)
    '''
def view():
    '''    public static SqlNode view(final SDBRequest request, final SqlNode sqlNode)
    '''
def restrict():
    '''    public static SqlNode restrict(final SDBRequest request, final SqlNode sqlNode, final SqlExprList exprs)
    public static SqlNode restrict(final SDBRequest request, final SqlNode sqlNode, final SqlExpr expr)
    '''
def isSelectBlock():
    '''    public boolean isSelectBlock()
    '''
def asSelectBlock():
    '''    public SqlSelectBlock asSelectBlock()
    '''
def setBlockAlias():
    '''    public void setBlockAlias(final String alias)
    '''
def getCols():
    '''    public List<ColAlias> getCols()
    '''
def add():
    '''    public void add(final ColAlias c)
    '''
def addAll():
    '''    public void addAll(final Collection<ColAlias> vc)
    '''
def clearView():
    '''    public SqlNode clearView()
    '''
def getConditions():
    '''    public SqlExprList getConditions()
    '''
def hasSlice():
    '''    public boolean hasSlice()
    '''
def hasConditions():
    '''    public boolean hasConditions()
    '''
def getStart():
    '''    public long getStart()
    '''
def getLength():
    '''    public long getLength()
    '''
def getIdScope():
    '''    public Scope getIdScope()
    '''
def getNodeScope():
    '''    public Scope getNodeScope()
    '''
def apply():
    '''    public SqlNode apply(final SqlTransform transform, final SqlNode newSubNode)
    '''
def copy():
    '''    public SqlNode copy(final SqlNode subNode)
    '''
def visit():
    '''    public void visit(final SqlNodeVisitor visitor)
    '''
def getDistinct():
    '''    public boolean getDistinct()
    '''
