def CapMatrix():
    '''    public CapMatrix(final String dataSpec)
    '''
def getAvailableLangs():
    '''    public synchronized String[] getAvailableLangs()
    '''
def getAvailableFuncs():
    '''    public Integer[] getAvailableFuncs(final Locale locale)
    public Integer[] getAvailableFuncs(final String s)
    '''
def getEntryByFilename():
    '''    public synchronized Entry getEntryByFilename(final String anotherString)
    '''
def getEntryByFile():
    '''    public synchronized Entry getEntryByFile(final File file)
    '''
def getAvailableEntries():
    '''    public Entry[] getAvailableEntries(final String s, final int n)
    public Entry[] getAvailableEntries(final String s, final int[] array)
    '''
def getEntries():
    '''    public Entry[] getEntries(final Locale locale, final int[] array)
    '''
def getAllEntries():
    '''    public synchronized Entry[] getAllEntries()
    '''
def getAvailableFiles():
    '''    public File[] getAvailableFiles(final Locale locale, final int n)
    public File[] getAvailableFiles(final String s, final int n)
    '''
def getActivatedDicts():
    '''    public synchronized Dictionary[] getActivatedDicts()
    '''
def activate():
    '''    public synchronized Entry[] activate(final Locale locale, final int n)
    public synchronized Entry[] activate(final String s, final int n)
    public synchronized Dictionary activate()
    public synchronized Dictionary activate(final boolean b)
    public synchronized Dictionary activate(final boolean b, final boolean b2)
    public synchronized Dictionary activate(final int n)
    '''
def deactivateAll():
    '''    public synchronized void deactivateAll()
    '''
def deactivateFuzzy():
    '''    public synchronized void deactivateFuzzy(final int n)
    '''
def registerDictionary():
    '''    public synchronized Entry registerDictionary(final File file, final Dictionary dictionary)
    '''
def registerEntry():
    '''    public synchronized void registerEntry(final Entry e)
    '''
def getDataSpec():
    '''    public synchronized String getDataSpec()
    '''
def setDataSpec():
    '''    public synchronized void setDataSpec(final String s)
    public synchronized void setDataSpec(String theDataSpec, final boolean b)
    '''
def setDictCacheSize():
    '''    public void setDictCacheSize(final int n)
    '''
def getDictCacheSize():
    '''    public int getDictCacheSize()
    '''
def compare():
    '''    public int compare(final Object o, final Object o2)
    public int compare(final Object o, final Object o2)
    '''
def getFile():
    '''    public File getFile()
    '''
def getDictInfo():
    '''    public synchronized DictionaryInfo getDictInfo()
    '''
def getDict():
    '''    public Dictionary getDict()
    '''
def deactivate():
    '''    public synchronized void deactivate()
    '''
def isActivated():
    '''    public synchronized boolean isActivated()
    '''
def getDescription():
    '''    public String getDescription()
    '''
def getActivatedTime():
    '''    public long getActivatedTime()
    '''
def isNoDeactivateFuzzy():
    '''    public boolean isNoDeactivateFuzzy()
    '''
def setNoDeactivateFuzzy():
    '''    public void setNoDeactivateFuzzy(final boolean noDeactivateFuzzy)
    '''
def toString():
    '''    public String toString()
    '''
def hashCode():
    '''    public int hashCode()
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
