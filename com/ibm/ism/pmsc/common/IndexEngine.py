COPYRIGHT = "String IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.""
MAX_COUNT = "String GlobalSearch.maxCount""
DEFAULT_COUNT = "String 500""
def getInstance():
'''public static IndexEngine getInstance(final MboRemote mbo)
'''
pass
def clean():
'''public synchronized void clean()
'''
pass
def create():
'''public synchronized void create(final Map<String, String> toStores, final Map<String, String> toIndexes)
'''
pass
def search():
'''public List<Map> search(final String[] attributes, final String searchValue)
'''
pass
def createForMbo():
'''public long createForMbo(final MXSession session, final String mboName, final String[] fieldsToIndex, final String[] fieldsToStore)
public void createForMbo(final MboRemote mbo, final String[] fieldsToIndex, final String[] fieldsToStore, final Map<String, String> otherIndex, final Map<String, String> otherStore)
'''
pass
def createForMboSet():
'''public long createForMboSet(final MboSetRemote mboSet, final String[] fieldsToIndex, final String[] fieldsToStore, final Map<String, String> otherIndex, final Map<String, String> otherStore)
'''
pass
def createFile():
'''public synchronized void createFile(final File file, final Map<String, String> attributes)
'''
pass
