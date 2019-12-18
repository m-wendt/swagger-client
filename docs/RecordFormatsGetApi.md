# swagger_client.RecordFormatsGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**record_formats_get**](RecordFormatsGetApi.md#record_formats_get) | **GET** /v3/recordformats | Retrieves all available record formats.
[**record_formats_get_0**](RecordFormatsGetApi.md#record_formats_get_0) | **GET** /v3/recordformats/{id} | Retrieves a single record format with the given identifier.


# **record_formats_get**
> list[SaveTVWebApiResponseModelsRecordFormat] record_formats_get(sort=sort)

Retrieves all available record formats.

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
api_instance = swagger_client.RecordFormatsGetApi(swagger_client.ApiClient(configuration))
sort = NULL # list[object] | Sets the sort properties. The values are comma-separated. To sort ascending add a \"+\" before the sort property, to sort descending add a \"-\" before the sort property.    When omitted, a default sorting is used.    Example: sort=+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    name    priority    Default sorting:    +priority (optional)

try:
    # Retrieves all available record formats.
    api_response = api_instance.record_formats_get(sort=sort)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordFormatsGetApi->record_formats_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | [**list[object]**](object.md)| Sets the sort properties. The values are comma-separated. To sort ascending add a \&quot;+\&quot; before the sort property, to sort descending add a \&quot;-\&quot; before the sort property.    When omitted, a default sorting is used.    Example: sort&#x3D;+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    name    priority    Default sorting:    +priority | [optional] 

### Return type

[**list[SaveTVWebApiResponseModelsRecordFormat]**](SaveTVWebApiResponseModelsRecordFormat.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **record_formats_get_0**
> SaveTVWebApiResponseModelsRecordFormat record_formats_get_0(id)

Retrieves a single record format with the given identifier.

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
api_instance = swagger_client.RecordFormatsGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the record format.

try:
    # Retrieves a single record format with the given identifier.
    api_response = api_instance.record_formats_get_0(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordFormatsGetApi->record_formats_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the record format. | 

### Return type

[**SaveTVWebApiResponseModelsRecordFormat**](SaveTVWebApiResponseModelsRecordFormat.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

