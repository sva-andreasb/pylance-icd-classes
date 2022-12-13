VERSION_1_0 = "String  1.0""
ENCODING = "String  UTF-8""
FORM_ENCODED = "String  application/x-www-form-urlencoded""
OAUTH_CONSUMER_KEY = "String  oauth_consumer_key""
OAUTH_TOKEN = "String  oauth_token""
OAUTH_TOKEN_SECRET = "String  oauth_token_secret""
OAUTH_SIGNATURE_METHOD = "String  oauth_signature_method""
OAUTH_SIGNATURE = "String  oauth_signature""
OAUTH_TIMESTAMP = "String  oauth_timestamp""
OAUTH_NONCE = "String  oauth_nonce""
OAUTH_VERSION = "String  oauth_version""
OAUTH_CALLBACK = "String  oauth_callback""
OAUTH_CALLBACK_CONFIRMED = "String  oauth_callback_confirmed""
OAUTH_VERIFIER = "String  oauth_verifier""
HMAC_SHA1 = "String  HMAC-SHA1""
RSA_SHA1 = "String  RSA-SHA1""
VERSION_REJECTED = "String  version_rejected""
PARAMETER_ABSENT = "String  parameter_absent""
PARAMETER_REJECTED = "String  parameter_rejected""
TIMESTAMP_REFUSED = "String  timestamp_refused""
NONCE_USED = "String  nonce_used""
SIGNATURE_METHOD_REJECTED = "String  signature_method_rejected""
SIGNATURE_INVALID = "String  signature_invalid""
CONSUMER_KEY_UNKNOWN = "String  consumer_key_unknown""
CONSUMER_KEY_REJECTED = "String  consumer_key_rejected""
CONSUMER_KEY_REFUSED = "String  consumer_key_refused""
TOKEN_USED = "String  token_used""
TOKEN_EXPIRED = "String  token_expired""
TOKEN_REVOKED = "String  token_revoked""
TOKEN_REJECTED = "String  token_rejected""
ADDITIONAL_AUTHORIZATION_REQUIRED = "String  additional_authorization_required""
PERMISSION_UNKNOWN = "String  permission_unknown""
PERMISSION_DENIED = "String  permission_denied""
USER_REFUSED = "String  user_refused""
OAUTH_ACCEPTABLE_VERSIONS = "String  oauth_acceptable_versions""
OAUTH_ACCEPTABLE_TIMESTAMPS = "String  oauth_acceptable_timestamps""
OAUTH_PARAMETERS_ABSENT = "String  oauth_parameters_absent""
OAUTH_PARAMETERS_REJECTED = "String  oauth_parameters_rejected""
OAUTH_PROBLEM_ADVICE = "String  oauth_problem_advice""
def setCharacterEncoding():
'''public static void setCharacterEncoding(final String encoding)
'''
pass
def decodeCharacters():
'''public static String decodeCharacters(final byte[] from)
'''
pass
def encodeCharacters():
'''public static byte[] encodeCharacters(final String from)
'''
pass
def isFormEncoded():
'''public static boolean isFormEncoded(String contentType)
'''
pass
def formEncode():
'''public static String formEncode(final Iterable<? extends Map.Entry> parameters)
public static void formEncode(final Iterable<? extends Map.Entry> parameters, final OutputStream into)
'''
pass
def decodeForm():
'''public static List<Parameter> decodeForm(final String form)
'''
pass
def percentEncode():
'''public static String percentEncode(final Iterable values)
public static String percentEncode(final String s)
'''
pass
def decodePercent():
'''public static String decodePercent(final String s)
'''
pass
def newMap():
'''public static Map<String, String> newMap(final Iterable<? extends Map.Entry> from)
'''
pass
def newList():
'''public static List<Parameter> newList(final String... parameters)
'''
pass
def addParameters():
'''public static String addParameters(final String url, final String... parameters)
public static String addParameters(final String url, final Iterable<? extends Map.Entry<String, String>> parameters)
'''
pass
def isEmpty():
'''public static boolean isEmpty(final String str)
'''
pass
def Parameter():
'''public Parameter(final String key, final String value)
'''
pass
def getKey():
'''public String getKey()
'''
pass
def getValue():
'''public String getValue()
'''
pass
def setValue():
'''public String setValue(final String value)
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
'''public boolean equals(final Object obj)
'''
pass
