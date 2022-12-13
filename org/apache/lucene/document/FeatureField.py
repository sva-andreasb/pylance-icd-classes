def FeatureField():
'''public FeatureField(final String fieldName, final String featureName, final float featureValue)
'''
pass
def setFeatureValue():
'''public void setFeatureValue(final float featureValue)
'''
pass
def tokenStream():
'''public TokenStream tokenStream(final Analyzer analyzer, final TokenStream reuse)
'''
pass
def newLogQuery():
'''public static Query newLogQuery(final String fieldName, final String featureName, final float weight, final float scalingFactor)
'''
pass
def newSaturationQuery():
'''public static Query newSaturationQuery(final String fieldName, final String featureName, final float weight, final float pivot)
public static Query newSaturationQuery(final String fieldName, final String featureName)
'''
pass
def newSigmoidQuery():
'''public static Query newSigmoidQuery(final String fieldName, final String featureName, final float weight, final float pivot, final float exp)
'''
pass
def newFeatureSort():
'''public static SortField newFeatureSort(final String field, final String featureName)
'''
pass
def newDoubleValues():
'''public static DoubleValuesSource newDoubleValues(final String field, final String featureName)
'''
pass
def incrementToken():
'''public boolean incrementToken()
'''
pass
def reset():
'''public void reset()
'''
pass
def close():
'''public void close()
'''
pass
def equals():
'''public boolean equals(final Object obj)
public boolean equals(final Object obj)
public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
public int hashCode()
'''
pass
def toString():
'''public String toString()
public String toString()
public String toString()
'''
pass
def score():
'''public float score(final float freq, final long norm)
public float score(final float freq, final long norm)
public float score(final float freq, final long norm)
'''
pass
def rewrite():
'''public FeatureFunction rewrite(final IndexReader reader)
'''
pass
