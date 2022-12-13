def TextTrieMap():
'''public TextTrieMap(final boolean ignoreCase)
'''
pass
def put():
'''public synchronized void put(final String text, final V o)
'''
pass
def get():
'''public Iterator<V> get(final String text)
public Iterator<V> get(final String text, final int start)
'''
pass
def find():
'''public void find(final String text, final ResultHandler<V> handler)
public void find(final String text, final int start, final ResultHandler<V> handler)
'''
pass
def CharacterNode():
'''public CharacterNode(final int ch)
'''
pass
def getCharacter():
'''public int getCharacter()
'''
pass
def addObject():
'''public void addObject(final V obj)
'''
pass
def iterator():
'''public Iterator<V> iterator()
'''
pass
def addChildNode():
'''public CharacterNode addChildNode(final int ch)
'''
pass
def getChildNodes():
'''public List<CharacterNode> getChildNodes()
'''
pass
def handlePrefixMatch():
'''public boolean handlePrefixMatch(final int matchLength, final Iterator<V> values)
'''
pass
def getMatches():
'''public Iterator<V> getMatches()
'''
pass
