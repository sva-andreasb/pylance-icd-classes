AUTO_DETECT_MERGES_AND_THREADS = "int  -1"
DEFAULT_CPU_CORE_COUNT_PROPERTY = "String  \"lucene.cms.override_core_count\""
DEFAULT_SPINS_PROPERTY = "String  \"lucene.cms.override_spins\""
def ():
    '''returns MergeThread\n\n
    ()\n
    (final IndexWriter writer, final MergePolicy.OneMerge merge)\n
    '''
def wrapForMerge():
    '''returns Directory\n\n
    wrapForMerge(final MergePolicy.OneMerge merge, final Directory in)\n
    '''
def createOutput():
    '''returns IndexOutput\n\n
    createOutput(final String name, final IOContext context)\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def sync():
    '''returns None\n\n
    sync()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final MergeThread other)\n
    '''
def run():
    '''returns None\n\n
    run()\n
    '''
