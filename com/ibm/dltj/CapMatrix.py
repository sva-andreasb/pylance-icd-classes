def CapMatrix():
'''public CapMatrix(final String dataSpec)
'''
pass
def getAvailableLangs():
'''public synchronized String[] getAvailableLangs()
'''
pass
def getAvailableFuncs():
'''public Integer[] getAvailableFuncs(final Locale locale)
public Integer[] getAvailableFuncs(final String s)
'''
pass
def getEntryByFilename():
'''public synchronized Entry getEntryByFilename(final String anotherString)
'''
pass
def getEntryByFile():
'''public synchronized Entry getEntryByFile(final File file)
'''
pass
def getAvailableEntries():
'''public Entry[] getAvailableEntries(final String s, final int n)
public Entry[] getAvailableEntries(final String s, final int[] array)
'''
pass
def getEntries():
'''public Entry[] getEntries(final Locale locale, final int[] array)
'''
pass
def getAllEntries():
'''public synchronized Entry[] getAllEntries()
'''
pass
def getAvailableFiles():
'''public File[] getAvailableFiles(final Locale locale, final int n)
public File[] getAvailableFiles(final String s, final int n)
'''
pass
def getActivatedDicts():
'''public synchronized Dictionary[] getActivatedDicts()
'''
pass
def activate():
'''public synchronized Entry[] activate(final Locale locale, final int n)
public synchronized Entry[] activate(final String s, final int n)
public synchronized Dictionary activate()
public synchronized Dictionary activate(final boolean b)
public synchronized Dictionary activate(final boolean b, final boolean b2)
public synchronized Dictionary activate(final int n)
'''
pass
def deactivateAll():
'''public synchronized void deactivateAll()
'''
pass
def deactivateFuzzy():
'''public synchronized void deactivateFuzzy(final int n)
'''
pass
def registerDictionary():
'''public synchronized Entry registerDictionary(final File file, final Dictionary dictionary)
'''
pass
def registerEntry():
'''public synchronized void registerEntry(final Entry e)
'''
pass
def getDataSpec():
'''public synchronized String getDataSpec()
'''
pass
def setDataSpec():
'''public synchronized void setDataSpec(final String s)
public synchronized void setDataSpec(String theDataSpec, final boolean b)
'''
pass
def setDictCacheSize():
'''public void setDictCacheSize(final int n)
'''
pass
def getDictCacheSize():
'''public int getDictCacheSize()
'''
pass
def compare():
'''public int compare(final Object o, final Object o2)
public int compare(final Object o, final Object o2)
'''
pass
def getFile():
'''public File getFile()
'''
pass
def getDictInfo():
'''public synchronized DictionaryInfo getDictInfo()
'''
pass
def getDict():
'''public Dictionary getDict()
'''
pass
def deactivate():
'''public synchronized void deactivate()
'''
pass
def isActivated():
'''public synchronized boolean isActivated()
'''
pass
def getDescription():
'''public String getDescription()
'''
pass
def getActivatedTime():
'''public long getActivatedTime()
'''
pass
def isNoDeactivateFuzzy():
'''public boolean isNoDeactivateFuzzy()
'''
pass
def setNoDeactivateFuzzy():
'''public void setNoDeactivateFuzzy(final boolean noDeactivateFuzzy)
'''
pass
def toString():
'''public String toString()
'''
pass
def hashCode():
'''public int hashCode()
'''
pass
def equals():
'''public boolean equals(final Object o)
'''
pass
