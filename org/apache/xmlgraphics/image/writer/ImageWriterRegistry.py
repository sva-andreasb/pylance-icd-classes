def ImageWriterRegistry():
    '''    public ImageWriterRegistry()
    public ImageWriterRegistry(final Properties preferredOrder)
    '''
def getInstance():
    '''    public static ImageWriterRegistry getInstance()
    '''
def register():
    '''    public void register(final ImageWriter writer, final int priority)
    public synchronized void register(final ImageWriter writer)
    '''
def getWriterFor():
    '''    public synchronized ImageWriter getWriterFor(final String mime)
    '''
