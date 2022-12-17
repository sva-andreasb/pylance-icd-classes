def equals():
    '''returns boolean\n\n
    equals(final Object other)\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    '''
def toString():
    '''returns String\n\n
    toString(final String field)\n
    '''
def visit():
    '''returns None\n\n
    visit(final QueryVisitor visitor)\n
    '''
def rewrite():
    '''returns Query\n\n
    rewrite(final Query[] subQueries)\n
    rewrite(final Query[] subQueries)\n
    '''
def ():
    '''returns DisjunctionMaxRewrite\n\n
    ()\n
    (final float tieBreakerMultiplier)\n
    '''
def setRewriteMethod():
    '''returns Builder\n\n
    setRewriteMethod(final RewriteMethod rewiteMethod)\n
    '''
def add():
    '''returns Builder\n\n
    add(final Term term)\n
    add(final Term term, final float boost)\n
    add(final Term term, final float boost, final TermStates context)\n
    '''
def build():
    '''returns BlendedTermQuery\n\n
    build()\n
    '''
