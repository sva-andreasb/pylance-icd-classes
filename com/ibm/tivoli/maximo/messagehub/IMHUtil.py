NO_RECORDS = "String  \"No Data Found.\""
STATUS = "String  \"Status\""
GIVE_UPs = "int  10"
NO_RECORDS_COUNT = "int  0"
KAFKA_BROKER_SASL = "String  \"kafka_broker_sasl\""
API_KEY = "String  \"api_key\""
FAIL_SAFE = "String  \"skip_on_error\""
TOPIC_NAME = "String  \"topic\""
ZERO = "int  0"
PAYLOAD = "String  \"payload\""
def compressData():
    '''public static byte[] compressData(final byte[] data)
    '''
def uncompressData():
    '''public static byte[] uncompressData(final byte[] cdata)
    '''
def createPayload():
    '''public static byte[] createPayload(final Map<String, String> props, byte[] reqBytes, final boolean compress)
    '''
def createPayloadAsJSON():
    '''public static byte[] createPayloadAsJSON(final Map<String, String> props, byte[] reqBytes, final boolean compress)
    '''
def serializePayloadToBytes():
    '''public static byte[] serializePayloadToBytes(final HashMap<String, Object> req)
    '''
def resurrectJSONPayload():
    '''public static JSONObject resurrectJSONPayload(final byte[] reqBytes)
    '''
def resurrectPayload():
    '''public static Map<String, Object> resurrectPayload(final byte[] reqBytes)
    '''
