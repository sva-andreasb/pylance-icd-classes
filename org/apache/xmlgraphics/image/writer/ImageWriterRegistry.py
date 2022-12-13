def ImageWriterRegistry():
'''public ImageWriterRegistry()
public ImageWriterRegistry(final Properties preferredOrder)
'''
pass
def getInstance():
'''public static ImageWriterRegistry getInstance()
'''
pass
def register():
'''public void register(final ImageWriter writer, final int priority)
public synchronized void register(final ImageWriter writer)
'''
pass
def getWriterFor():
'''public synchronized ImageWriter getWriterFor(final String mime)
'''
pass
