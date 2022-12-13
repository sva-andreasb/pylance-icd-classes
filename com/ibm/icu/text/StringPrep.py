DEFAULT = "int  0"
ALLOW_UNASSIGNED = "int  1"
RFC3491_NAMEPREP = "int  0"
RFC3530_NFS4_CS_PREP = "int  1"
RFC3530_NFS4_CS_PREP_CI = "int  2"
RFC3530_NFS4_CIS_PREP = "int  3"
RFC3530_NFS4_MIXED_PREP_PREFIX = "int  4"
RFC3530_NFS4_MIXED_PREP_SUFFIX = "int  5"
RFC3722_ISCSI = "int  6"
RFC3920_NODEPREP = "int  7"
RFC3920_RESOURCEPREP = "int  8"
RFC4011_MIB = "int  9"
RFC4013_SASLPREP = "int  10"
RFC4505_TRACE = "int  11"
RFC4518_LDAP = "int  12"
RFC4518_LDAP_CI = "int  13"
def StringPrep():
    '''    public StringPrep(final InputStream inputStream)
    '''
def getInstance():
    '''    public static StringPrep getInstance(final int profile)
    '''
def prepare():
    '''    public StringBuffer prepare(final UCharacterIterator src, final int options)
    public String prepare(final String src, final int options)
    '''
def reset():
    '''    public void reset()
    '''
