def parseAndClose():
    '''public final <T> T parseAndClose(final Class<T> destinationClass)
    public final <T> T parseAndClose(final Class<T> destinationClass, final CustomizeJsonParser customizeParser)
    public final void parseAndClose(final Object destination)
    public final void parseAndClose(final Object destination, final CustomizeJsonParser customizeParser)
    '''
def skipToKey():
    '''public final void skipToKey(final String keyToFind)
    public final String skipToKey(final Set<String> keysToFind)
    '''
def parse():
    '''public final <T> T parse(final Class<T> destinationClass)
    public final <T> T parse(final Class<T> destinationClass, final CustomizeJsonParser customizeParser)
    public Object parse(final Type dataType, final boolean close)
    public Object parse(final Type dataType, final boolean close, final CustomizeJsonParser customizeParser)
    public final void parse(final Object destination)
    public final void parse(final Object destination, final CustomizeJsonParser customizeParser)
    '''
def parseArrayAndClose():
    '''public final <T> Collection<T> parseArrayAndClose(final Class<?> destinationCollectionClass, final Class<T> destinationItemClass)
    public final <T> Collection<T> parseArrayAndClose(final Class<?> destinationCollectionClass, final Class<T> destinationItemClass, final CustomizeJsonParser customizeParser)
    public final <T> void parseArrayAndClose(final Collection<? super T> destinationCollection, final Class<T> destinationItemClass)
    public final <T> void parseArrayAndClose(final Collection<? super T> destinationCollection, final Class<T> destinationItemClass, final CustomizeJsonParser customizeParser)
    '''
def parseArray():
    '''public final <T> Collection<T> parseArray(final Class<?> destinationCollectionClass, final Class<T> destinationItemClass)
    public final <T> Collection<T> parseArray(final Class<?> destinationCollectionClass, final Class<T> destinationItemClass, final CustomizeJsonParser customizeParser)
    public final <T> void parseArray(final Collection<? super T> destinationCollection, final Class<T> destinationItemClass)
    public final <T> void parseArray(final Collection<? super T> destinationCollection, final Class<T> destinationItemClass, final CustomizeJsonParser customizeParser)
    '''
