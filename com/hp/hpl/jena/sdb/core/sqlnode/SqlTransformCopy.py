COPY_ALWAYS = "boolean  true"
COPY_ONLY_ON_CHANGE = "boolean  false"
def SqlTransformCopy():
    '''public SqlTransformCopy()
    public SqlTransformCopy(final boolean alwaysDuplicate)
    '''
def transform():
    '''public SqlNode transform(final SqlProject sqlProject, final SqlNode subNode)
    public SqlNode transform(final SqlDistinct sqlDistinct, final SqlNode subNode)
    public SqlNode transform(final SqlRestrict sqlRestrict, final SqlNode subNode)
    public SqlNode transform(final SqlSlice sqlSlice, final SqlNode subNode)
    public SqlNode transform(final SqlSelectBlock sqlSelectBlock, final SqlNode subNode)
    public SqlNode transform(final SqlJoinInner sqlJoinInner, final SqlNode left, final SqlNode right)
    public SqlNode transform(final SqlJoinLeftOuter sqlJoinLeftOuter, final SqlNode left, final SqlNode right)
    public SqlNode transform(final SqlUnion sqlUnion, final SqlNode left, final SqlNode right)
    public SqlNode transform(final SqlTable sqlTable)
    public SqlNode transform(final SqlRename sqlRename, final SqlNode subNode)
    public SqlNode transform(final SqlCoalesce sqlCoalesce, final SqlNode subNode)
    '''
