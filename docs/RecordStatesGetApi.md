# swagger_client.RecordStatesGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**record_states_get**](RecordStatesGetApi.md#record_states_get) | **GET** /v3/recordstates | Retrieves all available record states.
[**record_states_get_0**](RecordStatesGetApi.md#record_states_get_0) | **GET** /v3/recordstates/{id} | Retrieves a single record state with the given identifier.


# **record_states_get**
> list[SaveTVWebApiResponseModelsRecordState] record_states_get()

Retrieves all available record states.

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
api_instance = swagger_client.RecordStatesGetApi(swagger_client.ApiClient(configuration))

try:
    # Retrieves all available record states.
    api_response = api_instance.record_states_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordStatesGetApi->record_states_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[SaveTVWebApiResponseModelsRecordState]**](SaveTVWebApiResponseModelsRecordState.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_states_get_0**
> SaveTVWebApiResponseModelsRecordState record_states_get_0(id)

Retrieves a single record state with the given identifier.

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
api_instance = swagger_client.RecordStatesGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The record state identifier.

try:
    # Retrieves a single record state with the given identifier.
    api_response = api_instance.record_states_get_0(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordStatesGetApi->record_states_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The record state identifier. | 

### Return type

[**SaveTVWebApiResponseModelsRecordState**](SaveTVWebApiResponseModelsRecordState.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

