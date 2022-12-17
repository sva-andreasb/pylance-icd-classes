def ():
    '''returns PruneByAge\n\n
    ()\n
    (final IndexSearcher searcher)\n
    (final double maxAgeSec)\n
    '''
def record():
    '''returns long\n\n
    record(final IndexSearcher searcher)\n
    '''
def acquire():
    '''returns IndexSearcher\n\n
    acquire(final long version)\n
    '''
def release():
    '''returns None\n\n
    release(final IndexSearcher s)\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final SearcherTracker other)\n
    '''
def doPrune():
    '''returns boolean\n\n
    doPrune(final double ageSec, final IndexSearcher searcher)\n
    '''
