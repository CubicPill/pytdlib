from ctypes.util import find_library
from ctypes import *
import json

# copy-paste from tdlib's python example
tdjson_path = find_library("tdjson") or "tdjson.dll"
if tdjson_path is None:
    raise RuntimeError('No valid libtdjson found, please build the lib first.')
tdjson = CDLL(tdjson_path)

td_json_client_create = tdjson.td_json_client_create
td_json_client_create.restype = c_void_p
td_json_client_create.argtypes = []

td_json_client_receive = tdjson.td_json_client_receive
td_json_client_receive.restype = c_char_p
td_json_client_receive.argtypes = [c_void_p, c_double]

td_json_client_send = tdjson.td_json_client_send
td_json_client_send.restype = None
td_json_client_send.argtypes = [c_void_p, c_char_p]

td_json_client_execute = tdjson.td_json_client_execute
td_json_client_execute.restype = c_char_p
td_json_client_execute.argtypes = [c_void_p, c_char_p]

td_json_client_destroy = tdjson.td_json_client_destroy
td_json_client_destroy.restype = None
td_json_client_destroy.argtypes = [c_void_p]

td_set_log_file_path = tdjson.td_set_log_file_path
td_set_log_file_path.restype = c_int
td_set_log_file_path.argtypes = [c_char_p]

td_set_log_max_file_size = tdjson.td_set_log_max_file_size
td_set_log_max_file_size.restype = None
td_set_log_max_file_size.argtypes = [c_longlong]

td_set_log_verbosity_level = tdjson.td_set_log_verbosity_level
td_set_log_verbosity_level.restype = None
td_set_log_verbosity_level.argtypes = [c_int]

fatal_error_callback_type = CFUNCTYPE(None, c_char_p)

td_set_log_fatal_error_callback = tdjson.td_set_log_fatal_error_callback
td_set_log_fatal_error_callback.restype = None
td_set_log_fatal_error_callback.argtypes = [fatal_error_callback_type]


def on_fatal_error_callback(error_message):
    raise RuntimeError("TDLib fatal error: " + error_message)


td_set_log_verbosity_level(2)
c_on_fatal_error_callback = fatal_error_callback_type(on_fatal_error_callback)
td_set_log_fatal_error_callback(c_on_fatal_error_callback)


class TDJSONClient:
    def __init__(self):
        """
        Creates a new instance of TDLib.
        """
        self.client = td_json_client_create()

    def td_send(self, query: dict):
        """
        Sends request to the TDLib client. May be called from any thread.
        :param query:
        :return:
        """
        query = json.dumps(query).encode("utf-8")
        td_json_client_send(self.client, query)

    def td_receive(self, timeout: c_double = 1.0) -> dict:
        """
        Receives incoming updates and request responses from the TDLib client. May be called from any thread,
        but shouldn't be called simultaneously from two different threads.
        :param timeout: Maximum number of seconds allowed for this function to wait for new data.
        :return: parsed dict or None if the timeout expires.
        """
        result = td_json_client_receive(self.client, timeout)
        if result:
            result = json.loads(result.decode("utf-8"))
        return result

    def td_execute(self, query: dict) -> dict:
        """
        Synchronously executes TDLib request. May be called from any thread.
        Only a few requests can be executed synchronously.
        :param query:
        :return: parsed dict or None if the request can't be parsed
        """
        query = json.dumps(query).encode("utf-8")
        result = td_json_client_execute(self.client, query)
        if result:
            result = json.loads(result.decode("utf-8"))
        return result

    def destroy(self):
        """
        Destroys the TDLib client instance. After this is called the client instance shouldn't be used anymore.
        :return: None
        """
        td_json_client_destroy(self.client)

    def __del__(self):
        self.destroy()
