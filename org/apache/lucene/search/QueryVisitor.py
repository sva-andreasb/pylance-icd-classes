def consumeTerms():
    '''returns None\n\n
    consumeTerms(final Query query, final Term... terms)\n
    consumeTerms(final Query query, final Term... terms)\n
    '''
def consumeTermsMatching():
    '''returns None\n\n
    consumeTermsMatching(final Query query, final String field, final ByteRunAutomaton automaton)\n
    '''
def visitLeaf():
    '''returns None\n\n
    visitLeaf(final Query query)\n
    '''
def acceptField():
    '''returns boolean\n\n
    acceptField(final String field)\n
    '''
def getSubVisitor():
    '''returns QueryVisitor\n\n
    getSubVisitor(final BooleanClause.Occur occur, final Query parent)\n
    '''
