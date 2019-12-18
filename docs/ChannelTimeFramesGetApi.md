# swagger_client.ChannelTimeFramesGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_time_frames_get**](ChannelTimeFramesGetApi.md#channel_time_frames_get) | **GET** /v3/channeltimeframes | Retrieves all available channel time frames.
[**channel_time_frames_get_0**](ChannelTimeFramesGetApi.md#channel_time_frames_get_0) | **GET** /v3/channeltimeframes/{id} | Retrieves a single channel time frame with the given identifier.


# **channel_time_frames_get**
> list[SaveTVWebApiResponseModelsChannelTimeFrame] channel_time_frames_get(fields=fields)

Retrieves all available channel time frames.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ChannelTimeFramesGetApi(swagger_client.ApiClient(configuration))
fields = ['endtime, id, name, starttime'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    endtime,    id,    name,    starttime (optional) (default to endtime, id, name, starttime)

try:
    # Retrieves all available channel time frames.
    api_response = api_instance.channel_time_frames_get(fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelTimeFramesGetApi->channel_time_frames_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    endtime,    id,    name,    starttime | [optional] [default to endtime, id, name, starttime]

### Return type

[**list[SaveTVWebApiResponseModelsChannelTimeFrame]**](SaveTVWebApiResponseModelsChannelTimeFrame.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channel_time_frames_get_0**
> SaveTVWebApiResponseModelsChannelTimeFrame channel_time_frames_get_0(id, fields=fields)

Retrieves a single channel time frame with the given identifier.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ChannelTimeFramesGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the channel time frame.
fields = ['endtime, id, name, starttime'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"id\" is always transmitted.    _The allowed field values:_    endtime,    id,    name,    starttime (optional) (default to endtime, id, name, starttime)

try:
    # Retrieves a single channel time frame with the given identifier.
    api_response = api_instance.channel_time_frames_get_0(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelTimeFramesGetApi->channel_time_frames_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the channel time frame. | 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;id\&quot; is always transmitted.    _The allowed field values:_    endtime,    id,    name,    starttime | [optional] [default to endtime, id, name, starttime]

### Return type

[**SaveTVWebApiResponseModelsChannelTimeFrame**](SaveTVWebApiResponseModelsChannelTimeFrame.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

