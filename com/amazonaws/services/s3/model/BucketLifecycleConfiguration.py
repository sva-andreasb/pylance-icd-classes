ENABLED = "String  \"Enabled\""
DISABLED = "String  \"Disabled\""
def getRules():
    '''returns List<Rule>\n\n
    getRules()\n
    '''
def setRules():
    '''returns None\n\n
    setRules(final List<Rule> rules)\n
    '''
def withRules():
    '''returns BucketLifecycleConfiguration\n\n
    withRules(final List<Rule> rules)\n
    withRules(final Rule... rules)\n
    '''
def ():
    '''returns NoncurrentVersionTransition\n\n
    (final List<Rule> rules)\n
    ()\n
    ()\n
    ()\n
    ()\n
    '''
def setId():
    '''returns None\n\n
    setId(final String id)\n
    '''
def setPrefix():
    '''returns None\n\n
    setPrefix(final String prefix)\n
    '''
def setExpirationInDays():
    '''returns None\n\n
    setExpirationInDays(final int expirationInDays)\n
    '''
def setNoncurrentVersionExpirationInDays():
    '''returns None\n\n
    setNoncurrentVersionExpirationInDays(final int value)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def withId():
    '''returns Rule\n\n
    withId(final String id)\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix()\n
    '''
def withPrefix():
    '''returns Rule\n\n
    withPrefix(final String prefix)\n
    '''
def getExpirationInDays():
    '''returns int\n\n
    getExpirationInDays()\n
    '''
def withExpirationInDays():
    '''returns Rule\n\n
    withExpirationInDays(final int expirationInDays)\n
    '''
def getNoncurrentVersionExpirationInDays():
    '''returns int\n\n
    getNoncurrentVersionExpirationInDays()\n
    '''
def withNoncurrentVersionExpirationInDays():
    '''returns Rule\n\n
    withNoncurrentVersionExpirationInDays(final int value)\n
    '''
def getStatus():
    '''returns String\n\n
    getStatus()\n
    '''
def setStatus():
    '''returns None\n\n
    setStatus(final String status)\n
    '''
def withStatus():
    '''returns Rule\n\n
    withStatus(final String status)\n
    '''
def setExpirationDate():
    '''returns None\n\n
    setExpirationDate(final Date expirationDate)\n
    '''
def getExpirationDate():
    '''returns Date\n\n
    getExpirationDate()\n
    '''
def withExpirationDate():
    '''returns Rule\n\n
    withExpirationDate(final Date expirationDate)\n
    '''
def setTransition():
    '''returns None\n\n
    setTransition(final Transition transition)\n
    '''
def getTransition():
    '''returns Transition\n\n
    getTransition()\n
    '''
def withTransition():
    '''returns Rule\n\n
    withTransition(final Transition transition)\n
    '''
def setNoncurrentVersionTransition():
    '''returns None\n\n
    setNoncurrentVersionTransition(final NoncurrentVersionTransition nonCurrentVersionTransition)\n
    '''
def getNoncurrentVersionTransition():
    '''returns NoncurrentVersionTransition\n\n
    getNoncurrentVersionTransition()\n
    '''
def withNoncurrentVersionTransition():
    '''returns Rule\n\n
    withNoncurrentVersionTransition(final NoncurrentVersionTransition nonCurrentVersionTransition)\n
    '''
def getTransitions():
    '''returns List<Transition>\n\n
    getTransitions()\n
    '''
def setTransitions():
    '''returns None\n\n
    setTransitions(final List<Transition> transitions)\n
    '''
def withTransitions():
    '''returns Rule\n\n
    withTransitions(final List<Transition> transitions)\n
    '''
def addTransition():
    '''returns Rule\n\n
    addTransition(final Transition transition)\n
    '''
def getNoncurrentVersionTransitions():
    '''returns List<NoncurrentVersionTransition>\n\n
    getNoncurrentVersionTransitions()\n
    '''
def setNoncurrentVersionTransitions():
    '''returns None\n\n
    setNoncurrentVersionTransitions(final List<NoncurrentVersionTransition> noncurrentVersionTransitions)\n
    '''
def withNoncurrentVersionTransitions():
    '''returns Rule\n\n
    withNoncurrentVersionTransitions(final List<NoncurrentVersionTransition> noncurrentVersionTransitions)\n
    '''
def addNoncurrentVersionTransition():
    '''returns Rule\n\n
    addNoncurrentVersionTransition(final NoncurrentVersionTransition noncurrentVersionTransition)\n
    '''
def getAbortIncompleteMultipartUpload():
    '''returns AbortIncompleteMultipartUpload\n\n
    getAbortIncompleteMultipartUpload()\n
    '''
def setAbortIncompleteMultipartUpload():
    '''returns None\n\n
    setAbortIncompleteMultipartUpload(final AbortIncompleteMultipartUpload abortIncompleteMultipartUpload)\n
    '''
def withAbortIncompleteMultipartUpload():
    '''returns Rule\n\n
    withAbortIncompleteMultipartUpload(final AbortIncompleteMultipartUpload abortIncompleteMultipartUpload)\n
    '''
def isExpiredObjectDeleteMarker():
    '''returns boolean\n\n
    isExpiredObjectDeleteMarker()\n
    '''
def setExpiredObjectDeleteMarker():
    '''returns None\n\n
    setExpiredObjectDeleteMarker(final boolean expiredObjectDeleteMarker)\n
    '''
def withExpiredObjectDeleteMarker():
    '''returns Rule\n\n
    withExpiredObjectDeleteMarker(final boolean expiredObjectDeleteMarker)\n
    '''
def setDays():
    '''returns None\n\n
    setDays(final int expirationInDays)\n
    setDays(final int expirationInDays)\n
    '''
def getDays():
    '''returns int\n\n
    getDays()\n
    getDays()\n
    '''
def withDays():
    '''returns NoncurrentVersionTransition\n\n
    withDays(final int expirationInDays)\n
    withDays(final int expirationInDays)\n
    '''
def setStorageClass():
    '''returns None\n\n
    setStorageClass(final StorageClass storageClass)\n
    setStorageClass(final String storageClass)\n
    setStorageClass(final StorageClass storageClass)\n
    setStorageClass(final String storageClass)\n
    '''
def getStorageClass():
    '''returns StorageClass\n\n
    getStorageClass()\n
    getStorageClass()\n
    '''
def getStorageClassAsString():
    '''returns String\n\n
    getStorageClassAsString()\n
    getStorageClassAsString()\n
    '''
def withStorageClass():
    '''returns NoncurrentVersionTransition\n\n
    withStorageClass(final StorageClass storageClass)\n
    withStorageClass(final String storageClass)\n
    withStorageClass(final StorageClass storageClass)\n
    withStorageClass(final String storageClass)\n
    '''
def setDate():
    '''returns None\n\n
    setDate(final Date expirationDate)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate()\n
    '''
def withDate():
    '''returns Transition\n\n
    withDate(final Date expirationDate)\n
    '''
