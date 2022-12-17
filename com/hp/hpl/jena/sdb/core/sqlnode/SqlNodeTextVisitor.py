def ():
    '''returns SqlNodeTextVisitor\n\n
    (final IndentedWriter out)\n
    (final IndentedWriter out, final boolean withAnnotations)\n
    '''
def visit():
    '''returns None\n\n
    visit(final SqlProject sqlNode)\n
    visit(final SqlDistinct sqlNode)\n
    visit(final SqlRestrict sqlNode)\n
    visit(final SqlRename sqlRename)\n
    visit(final SqlTable sqlNode)\n
    visit(final SqlJoinInner sqlJoin)\n
    visit(final SqlJoinLeftOuter sqlJoin)\n
    visit(final SqlUnion sqlUnion)\n
    visit(final SqlCoalesce sqlNode)\n
    visit(final SqlSlice sqlNode)\n
    visit(final SqlSelectBlock sqlNode)\n
    '''
