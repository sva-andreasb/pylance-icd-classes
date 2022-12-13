ENABLED = "String  \"Enabled\""
DISABLED = "String  \"Disabled\""
def getRules():
    '''    public List<Rule> getRules()
    '''
def setRules():
    '''    public void setRules(final List<Rule> rules)
    '''
def withRules():
    '''    public BucketLifecycleConfiguration withRules(final List<Rule> rules)
    public BucketLifecycleConfiguration withRules(final Rule... rules)
    '''
def BucketLifecycleConfiguration():
    '''    public BucketLifecycleConfiguration(final List<Rule> rules)
    public BucketLifecycleConfiguration()
    '''
def Rule():
    '''    public Rule()
    '''
def setId():
    '''    public void setId(final String id)
    '''
def setPrefix():
    '''    public void setPrefix(final String prefix)
    '''
def setExpirationInDays():
    '''    public void setExpirationInDays(final int expirationInDays)
    '''
def setNoncurrentVersionExpirationInDays():
    '''    public void setNoncurrentVersionExpirationInDays(final int value)
    '''
def getId():
    '''    public String getId()
    '''
def withId():
    '''    public Rule withId(final String id)
    '''
def getPrefix():
    '''    public String getPrefix()
    '''
def withPrefix():
    '''    public Rule withPrefix(final String prefix)
    '''
def getExpirationInDays():
    '''    public int getExpirationInDays()
    '''
def withExpirationInDays():
    '''    public Rule withExpirationInDays(final int expirationInDays)
    '''
def getNoncurrentVersionExpirationInDays():
    '''    public int getNoncurrentVersionExpirationInDays()
    '''
def withNoncurrentVersionExpirationInDays():
    '''    public Rule withNoncurrentVersionExpirationInDays(final int value)
    '''
def getStatus():
    '''    public String getStatus()
    '''
def setStatus():
    '''    public void setStatus(final String status)
    '''
def withStatus():
    '''    public Rule withStatus(final String status)
    '''
def setExpirationDate():
    '''    public void setExpirationDate(final Date expirationDate)
    '''
def getExpirationDate():
    '''    public Date getExpirationDate()
    '''
def withExpirationDate():
    '''    public Rule withExpirationDate(final Date expirationDate)
    '''
def setTransition():
    '''    public void setTransition(final Transition transition)
    '''
def getTransition():
    '''    public Transition getTransition()
    '''
def withTransition():
    '''    public Rule withTransition(final Transition transition)
    '''
def setNoncurrentVersionTransition():
    '''    public void setNoncurrentVersionTransition(final NoncurrentVersionTransition nonCurrentVersionTransition)
    '''
def getNoncurrentVersionTransition():
    '''    public NoncurrentVersionTransition getNoncurrentVersionTransition()
    '''
def withNoncurrentVersionTransition():
    '''    public Rule withNoncurrentVersionTransition(final NoncurrentVersionTransition nonCurrentVersionTransition)
    '''
def getTransitions():
    '''    public List<Transition> getTransitions()
    '''
def setTransitions():
    '''    public void setTransitions(final List<Transition> transitions)
    '''
def withTransitions():
    '''    public Rule withTransitions(final List<Transition> transitions)
    '''
def addTransition():
    '''    public Rule addTransition(final Transition transition)
    '''
def getNoncurrentVersionTransitions():
    '''    public List<NoncurrentVersionTransition> getNoncurrentVersionTransitions()
    '''
def setNoncurrentVersionTransitions():
    '''    public void setNoncurrentVersionTransitions(final List<NoncurrentVersionTransition> noncurrentVersionTransitions)
    '''
def withNoncurrentVersionTransitions():
    '''    public Rule withNoncurrentVersionTransitions(final List<NoncurrentVersionTransition> noncurrentVersionTransitions)
    '''
def addNoncurrentVersionTransition():
    '''    public Rule addNoncurrentVersionTransition(final NoncurrentVersionTransition noncurrentVersionTransition)
    '''
def getAbortIncompleteMultipartUpload():
    '''    public AbortIncompleteMultipartUpload getAbortIncompleteMultipartUpload()
    '''
def setAbortIncompleteMultipartUpload():
    '''    public void setAbortIncompleteMultipartUpload(final AbortIncompleteMultipartUpload abortIncompleteMultipartUpload)
    '''
def withAbortIncompleteMultipartUpload():
    '''    public Rule withAbortIncompleteMultipartUpload(final AbortIncompleteMultipartUpload abortIncompleteMultipartUpload)
    '''
def isExpiredObjectDeleteMarker():
    '''    public boolean isExpiredObjectDeleteMarker()
    '''
def setExpiredObjectDeleteMarker():
    '''    public void setExpiredObjectDeleteMarker(final boolean expiredObjectDeleteMarker)
    '''
def withExpiredObjectDeleteMarker():
    '''    public Rule withExpiredObjectDeleteMarker(final boolean expiredObjectDeleteMarker)
    '''
def Transition():
    '''    public Transition()
    '''
def setDays():
    '''    public void setDays(final int expirationInDays)
    public void setDays(final int expirationInDays)
    '''
def getDays():
    '''    public int getDays()
    public int getDays()
    '''
def withDays():
    '''    public Transition withDays(final int expirationInDays)
    public NoncurrentVersionTransition withDays(final int expirationInDays)
    '''
def setStorageClass():
    '''    public void setStorageClass(final StorageClass storageClass)
    public void setStorageClass(final String storageClass)
    public void setStorageClass(final StorageClass storageClass)
    public void setStorageClass(final String storageClass)
    '''
def getStorageClass():
    '''    public StorageClass getStorageClass()
    public StorageClass getStorageClass()
    '''
def getStorageClassAsString():
    '''    public String getStorageClassAsString()
    public String getStorageClassAsString()
    '''
def withStorageClass():
    '''    public Transition withStorageClass(final StorageClass storageClass)
    public Transition withStorageClass(final String storageClass)
    public NoncurrentVersionTransition withStorageClass(final StorageClass storageClass)
    public NoncurrentVersionTransition withStorageClass(final String storageClass)
    '''
def setDate():
    '''    public void setDate(final Date expirationDate)
    '''
def getDate():
    '''    public Date getDate()
    '''
def withDate():
    '''    public Transition withDate(final Date expirationDate)
    '''
def NoncurrentVersionTransition():
    '''    public NoncurrentVersionTransition()
    '''
