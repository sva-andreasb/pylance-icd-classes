def FeatureField():
    '''    public FeatureField(final String fieldName, final String featureName, final float featureValue)
    '''
def setFeatureValue():
    '''    public void setFeatureValue(final float featureValue)
    '''
def tokenStream():
    '''    public TokenStream tokenStream(final Analyzer analyzer, final TokenStream reuse)
    '''
def newLogQuery():
    '''    public static Query newLogQuery(final String fieldName, final String featureName, final float weight, final float scalingFactor)
    '''
def newSaturationQuery():
    '''    public static Query newSaturationQuery(final String fieldName, final String featureName, final float weight, final float pivot)
    public static Query newSaturationQuery(final String fieldName, final String featureName)
    '''
def newSigmoidQuery():
    '''    public static Query newSigmoidQuery(final String fieldName, final String featureName, final float weight, final float pivot, final float exp)
    '''
def newFeatureSort():
    '''    public static SortField newFeatureSort(final String field, final String featureName)
    '''
def newDoubleValues():
    '''    public static DoubleValuesSource newDoubleValues(final String field, final String featureName)
    '''
def incrementToken():
    '''    public boolean incrementToken()
    '''
def reset():
    '''    public void reset()
    '''
def close():
    '''    public void close()
    '''
def equals():
    '''    public boolean equals(final Object obj)
    public boolean equals(final Object obj)
    public boolean equals(final Object obj)
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    public int hashCode()
    '''
def toString():
    '''    public String toString()
    public String toString()
    public String toString()
    '''
def score():
    '''    public float score(final float freq, final long norm)
    public float score(final float freq, final long norm)
    public float score(final float freq, final long norm)
    '''
def rewrite():
    '''    public FeatureFunction rewrite(final IndexReader reader)
    '''
