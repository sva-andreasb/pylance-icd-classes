def Analyzer():
'''public Analyzer()
public Analyzer(final ReuseStrategy reuseStrategy)
'''
pass
def tokenStream():
'''public final TokenStream tokenStream(final String fieldName, final Reader reader)
public final TokenStream tokenStream(final String fieldName, final String text)
'''
pass
def normalize():
'''public final BytesRef normalize(final String fieldName, final String text)
'''
pass
def getPositionIncrementGap():
'''public int getPositionIncrementGap(final String fieldName)
'''
pass
def getOffsetGap():
'''public int getOffsetGap(final String fieldName)
'''
pass
def getReuseStrategy():
'''public final ReuseStrategy getReuseStrategy()
'''
pass
def setVersion():
'''public void setVersion(final Version v)
'''
pass
def getVersion():
'''public Version getVersion()
'''
pass
def close():
'''public void close()
'''
pass
def getReusableComponents():
'''public TokenStreamComponents getReusableComponents(final Analyzer analyzer, final String fieldName)
public TokenStreamComponents getReusableComponents(final Analyzer analyzer, final String fieldName)
'''
pass
def setReusableComponents():
'''public void setReusableComponents(final Analyzer analyzer, final String fieldName, final TokenStreamComponents components)
public void setReusableComponents(final Analyzer analyzer, final String fieldName, final TokenStreamComponents components)
'''
pass
def TokenStreamComponents():
'''public TokenStreamComponents(final Consumer<Reader> source, final TokenStream result)
public TokenStreamComponents(final Tokenizer tokenizer, final TokenStream result)
public TokenStreamComponents(final Tokenizer tokenizer)
'''
pass
def getTokenStream():
'''public TokenStream getTokenStream()
'''
pass
def getSource():
'''public Consumer<Reader> getSource()
'''
pass
def reset():
'''public void reset()
'''
pass
def incrementToken():
'''public boolean incrementToken()
'''
pass
def end():
'''public void end()
'''
pass
