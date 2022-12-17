def ():
    '''returns AlphabeticIndex\n\n
    (final ULocale locale)\n
    (final Locale locale)\n
    (final RuleBasedCollator collator)\n
    '''
def compare():
    '''returns int\n\n
    compare(final Record<V> o1, final Record<V> o2)\n
    '''
def addLabels():
    '''returns AlphabeticIndex<V>\n\n
    addLabels(final UnicodeSet additions)\n
    addLabels(final ULocale... additions)\n
    addLabels(final Locale... additions)\n
    '''
def setOverflowLabel():
    '''returns AlphabeticIndex<V>\n\n
    setOverflowLabel(final String overflowLabel)\n
    '''
def getUnderflowLabel():
    '''returns String\n\n
    getUnderflowLabel()\n
    '''
def setUnderflowLabel():
    '''returns AlphabeticIndex<V>\n\n
    setUnderflowLabel(final String underflowLabel)\n
    '''
def getOverflowLabel():
    '''returns String\n\n
    getOverflowLabel()\n
    '''
def setInflowLabel():
    '''returns AlphabeticIndex<V>\n\n
    setInflowLabel(final String inflowLabel)\n
    '''
def getInflowLabel():
    '''returns String\n\n
    getInflowLabel()\n
    '''
def getMaxLabelCount():
    '''returns int\n\n
    getMaxLabelCount()\n
    '''
def setMaxLabelCount():
    '''returns AlphabeticIndex<V>\n\n
    setMaxLabelCount(final int maxLabelCount)\n
    '''
def buildImmutableIndex():
    '''returns ImmutableIndex<V>\n\n
    buildImmutableIndex()\n
    '''
def getBucketLabels():
    '''returns List<String>\n\n
    getBucketLabels()\n
    '''
def getCollator():
    '''returns RuleBasedCollator\n\n
    getCollator()\n
    '''
def addRecord():
    '''returns AlphabeticIndex<V>\n\n
    addRecord(final CharSequence name, final V data)\n
    '''
def getBucketIndex():
    '''returns int\n\n
    getBucketIndex(final CharSequence name)\n
    getBucketIndex(final CharSequence name)\n
    '''
def clearRecords():
    '''returns AlphabeticIndex<V>\n\n
    clearRecords()\n
    '''
def getBucketCount():
    '''returns int\n\n
    getBucketCount()\n
    getBucketCount()\n
    '''
def getRecordCount():
    '''returns int\n\n
    getRecordCount()\n
    '''
def iterator():
    '''returns Iterator<Bucket<V>>\n\n
    iterator()\n
    iterator()\n
    iterator()\n
    iterator()\n
    '''
def getFirstCharactersInScripts():
    '''returns List<String>\n\n
    getFirstCharactersInScripts()\n
    '''
def getBucket():
    '''returns Bucket<V>\n\n
    getBucket(final int index)\n
    '''
def getName():
    '''returns CharSequence\n\n
    getName()\n
    '''
def getData():
    '''returns V\n\n
    getData()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getLabel():
    '''returns String\n\n
    getLabel()\n
    '''
def getLabelType():
    '''returns LabelType\n\n
    getLabelType()\n
    '''
def size():
    '''returns int\n\n
    size()\n
    '''
