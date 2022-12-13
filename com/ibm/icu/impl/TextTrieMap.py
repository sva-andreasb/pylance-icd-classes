def TextTrieMap():
    '''    public TextTrieMap(final boolean ignoreCase)
    '''
def put():
    '''    public synchronized void put(final String text, final V o)
    '''
def get():
    '''    public Iterator<V> get(final String text)
    public Iterator<V> get(final String text, final int start)
    '''
def find():
    '''    public void find(final String text, final ResultHandler<V> handler)
    public void find(final String text, final int start, final ResultHandler<V> handler)
    '''
def CharacterNode():
    '''    public CharacterNode(final int ch)
    '''
def getCharacter():
    '''    public int getCharacter()
    '''
def addObject():
    '''    public void addObject(final V obj)
    '''
def iterator():
    '''    public Iterator<V> iterator()
    '''
def addChildNode():
    '''    public CharacterNode addChildNode(final int ch)
    '''
def getChildNodes():
    '''    public List<CharacterNode> getChildNodes()
    '''
def handlePrefixMatch():
    '''    public boolean handlePrefixMatch(final int matchLength, final Iterator<V> values)
    '''
def getMatches():
    '''    public Iterator<V> getMatches()
    '''
