def ():
    '''returns GenerateSQLVisitor\n\n
    (final IndentedWriter out)\n
    '''
def visit():
    '''returns None\n\n
    visit(final SqlProject sqlNode)\n
    visit(final SqlDistinct sqlNode)\n
    visit(final SqlRestrict sqlNode)\n
    visit(final SqlSlice sqlNode)\n
    visit(final SqlRename sqlNode)\n
    visit(final SqlSelectBlock sqlSelectBlock)\n
    visit(final SqlTable table)\n
    visit(SqlJoinInner join)\n
    visit(final SqlJoinLeftOuter join)\n
    visit(final SqlCoalesce sqlNode)\n
    visit(final SqlUnion sqlUnion)\n
    '''
def rewrite():
    '''returns SqlJoinInner\n\n
    rewrite(final SqlJoinInner join)\n
    '''
def conditionList():
    '''returns None\n\n
    conditionList(final SqlExprList conditions)\n
    '''
def convert():
    '''returns SqlTable\n\n
    convert(final SqlColumn item)\n
    '''
