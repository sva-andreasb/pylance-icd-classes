def ():
    '''returns QueryRescorer\n\n
    (final Query query)\n
    '''
def rescore():
    '''returns TopDocs\n\n
    rescore(final IndexSearcher searcher, final TopDocs firstPassTopDocs, final int topN)\n
    '''
def compare():
    '''returns int\n\n
    compare(final ScoreDoc a, final ScoreDoc b)\n
    compare(final ScoreDoc a, final ScoreDoc b)\n
    '''
def explain():
    '''returns Explanation\n\n
    explain(final IndexSearcher searcher, final Explanation firstPassExplanation, final int docID)\n
    '''
