def create():
    '''public static SqlCoalesce create(final SDBRequest request, final String alias, final SqlJoin join, final Set<Var> coalesceVars)
    '''
def getCoalesceVars():
    '''public Set<Var> getCoalesceVars()
    '''
def getNonCoalesceVars():
    '''public Set<Var> getNonCoalesceVars()
    '''
def isCoalesce():
    '''public boolean isCoalesce()
    '''
def asCoalesce():
    '''public SqlCoalesce asCoalesce()
    '''
def getIdScope():
    '''public Scope getIdScope()
    '''
def getNodeScope():
    '''public Scope getNodeScope()
    '''
def getJoinNode():
    '''public SqlJoin getJoinNode()
    '''
def visit():
    '''public void visit(final SqlNodeVisitor visitor)
    '''
def apply():
    '''public SqlNode apply(final SqlTransform transform, final SqlNode newSubNode)
    '''
def copy():
    '''public SqlNode copy(final SqlNode subNode)
    '''
