def discoverItems():
    '''    public DiscoverItems discoverItems()
    '''
def getItems():
    '''    public <T extends Item> List<T> getItems()
    public <T extends Item> List<T> getItems(final String subscriptionId)
    public <T extends Item> List<T> getItems(final Collection<String> ids)
    public <T extends Item> List<T> getItems(final int maxItems)
    public <T extends Item> List<T> getItems(final int maxItems, final String subscriptionId)
    public <T extends Item> List<T> getItems(final List<ExtensionElement> additionalExtensions, final List<ExtensionElement> returnedExtensions)
    '''
def send():
    '''    public void send()
    public <T extends Item> void send(final T item)
    public <T extends Item> void send(final Collection<T> items)
    '''
def publish():
    '''    public void publish()
    public <T extends Item> void publish(final T item)
    public <T extends Item> void publish(final Collection<T> items)
    '''
def deleteAllItems():
    '''    public void deleteAllItems()
    '''
def deleteItem():
    '''    public void deleteItem(final String itemId)
    public void deleteItem(final Collection<String> itemIds)
    '''
