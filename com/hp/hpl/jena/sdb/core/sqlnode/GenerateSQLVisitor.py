def GenerateSQLVisitor():
    '''    public GenerateSQLVisitor(final IndentedWriter out)
    '''
def visit():
    '''    public void visit(final SqlProject sqlNode)
    public void visit(final SqlDistinct sqlNode)
    public void visit(final SqlRestrict sqlNode)
    public void visit(final SqlSlice sqlNode)
    public void visit(final SqlRename sqlNode)
    public void visit(final SqlSelectBlock sqlSelectBlock)
    public void visit(final SqlTable table)
    public void visit(SqlJoinInner join)
    public void visit(final SqlJoinLeftOuter join)
    public void visit(final SqlCoalesce sqlNode)
    public void visit(final SqlUnion sqlUnion)
    '''
def rewrite():
    '''    public SqlJoinInner rewrite(final SqlJoinInner join)
    '''
def conditionList():
    '''    public void conditionList(final SqlExprList conditions)
    '''
def convert():
    '''    public SqlTable convert(final SqlColumn item)
    '''
