COPY_ALWAYS = "boolean  true"
COPY_ONLY_ON_CHANGE = "boolean  false"
def ():
    '''returns SqlTransformCopy\n\n
    ()\n
    (final boolean alwaysDuplicate)\n
    '''
def transform():
    '''returns SqlNode\n\n
    transform(final SqlProject sqlProject, final SqlNode subNode)\n
    transform(final SqlDistinct sqlDistinct, final SqlNode subNode)\n
    transform(final SqlRestrict sqlRestrict, final SqlNode subNode)\n
    transform(final SqlSlice sqlSlice, final SqlNode subNode)\n
    transform(final SqlSelectBlock sqlSelectBlock, final SqlNode subNode)\n
    transform(final SqlJoinInner sqlJoinInner, final SqlNode left, final SqlNode right)\n
    transform(final SqlJoinLeftOuter sqlJoinLeftOuter, final SqlNode left, final SqlNode right)\n
    transform(final SqlUnion sqlUnion, final SqlNode left, final SqlNode right)\n
    transform(final SqlTable sqlTable)\n
    transform(final SqlRename sqlRename, final SqlNode subNode)\n
    transform(final SqlCoalesce sqlCoalesce, final SqlNode subNode)\n
    '''
