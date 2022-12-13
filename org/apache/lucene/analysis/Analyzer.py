def Analyzer():
    '''public Analyzer()
    public Analyzer(final ReuseStrategy reuseStrategy)
    '''
def tokenStream():
    '''public final TokenStream tokenStream(final String fieldName, final Reader reader)
    public final TokenStream tokenStream(final String fieldName, final String text)
    '''
def normalize():
    '''public final BytesRef normalize(final String fieldName, final String text)
    '''
def getPositionIncrementGap():
    '''public int getPositionIncrementGap(final String fieldName)
    '''
def getOffsetGap():
    '''public int getOffsetGap(final String fieldName)
    '''
def getReuseStrategy():
    '''public final ReuseStrategy getReuseStrategy()
    '''
def setVersion():
    '''public void setVersion(final Version v)
    '''
def getVersion():
    '''public Version getVersion()
    '''
def close():
    '''public void close()
    '''
def getReusableComponents():
    '''public TokenStreamComponents getReusableComponents(final Analyzer analyzer, final String fieldName)
    public TokenStreamComponents getReusableComponents(final Analyzer analyzer, final String fieldName)
    '''
def setReusableComponents():
    '''public void setReusableComponents(final Analyzer analyzer, final String fieldName, final TokenStreamComponents components)
    public void setReusableComponents(final Analyzer analyzer, final String fieldName, final TokenStreamComponents components)
    '''
def TokenStreamComponents():
    '''public TokenStreamComponents(final Consumer<Reader> source, final TokenStream result)
    public TokenStreamComponents(final Tokenizer tokenizer, final TokenStream result)
    public TokenStreamComponents(final Tokenizer tokenizer)
    '''
def getTokenStream():
    '''public TokenStream getTokenStream()
    '''
def getSource():
    '''public Consumer<Reader> getSource()
    '''
def reset():
    '''public void reset()
    '''
def incrementToken():
    '''public boolean incrementToken()
    '''
def end():
    '''public void end()
    '''
