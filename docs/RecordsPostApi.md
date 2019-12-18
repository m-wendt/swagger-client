# swagger_client.RecordsPostApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**records_post**](RecordsPostApi.md#records_post) | **POST** /v3/records | Creates new records or updates existing records with the given record buffer times.
[**records_post_0**](RecordsPostApi.md#records_post_0) | **POST** /v3/records/{id} | Creates a new record or updates an existing record with the given record buffer times.
[**records_post_resume**](RecordsPostApi.md#records_post_resume) | **POST** /v3/records/{id}/resume | Stores the current stream position for later resume.
[**records_post_tag_download_completed**](RecordsPostApi.md#records_post_tag_download_completed) | **POST** /v3/records/{id}/tags/download-completed | Creates a tag to mark the record as downloaded.


# **records_post**
> records_post(record_order)

Creates new records or updates existing records with the given record buffer times.

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
api_instance = swagger_client.RecordsPostApi(swagger_client.ApiClient(configuration))
record_order = swagger_client.SaveTVWebApiRequestModelsRecordOrder() # SaveTVWebApiRequestModelsRecordOrder | The record order.

try:
    # Creates new records or updates existing records with the given record buffer times.
    api_instance.records_post(record_order)
except ApiException as e:
    print("Exception when calling RecordsPostApi->records_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **record_order** | [**SaveTVWebApiRequestModelsRecordOrder**](SaveTVWebApiRequestModelsRecordOrder.md)| The record order. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **records_post_0**
> records_post_0(id, record_buffer)

Creates a new record or updates an existing record with the given record buffer times.

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
api_instance = swagger_client.RecordsPostApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the telecast.
record_buffer = swagger_client.SaveTVWebApiRequestModelsRecordBuffer() # SaveTVWebApiRequestModelsRecordBuffer | The record buffer times.

try:
    # Creates a new record or updates an existing record with the given record buffer times.
    api_instance.records_post_0(id, record_buffer)
except ApiException as e:
    print("Exception when calling RecordsPostApi->records_post_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the telecast. | 
 **record_buffer** | [**SaveTVWebApiRequestModelsRecordBuffer**](SaveTVWebApiRequestModelsRecordBuffer.md)| The record buffer times. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **records_post_resume**
> records_post_resume(id, set_record_resume)

Stores the current stream position for later resume.

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
api_instance = swagger_client.RecordsPostApi(swagger_client.ApiClient(configuration))
id = 56 # int | The record identifier.
set_record_resume = swagger_client.SaveTVWebApiRequestModelsSetRecordResume() # SaveTVWebApiRequestModelsSetRecordResume | The record resume.

try:
    # Stores the current stream position for later resume.
    api_instance.records_post_resume(id, set_record_resume)
except ApiException as e:
    print("Exception when calling RecordsPostApi->records_post_resume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The record identifier. | 
 **set_record_resume** | [**SaveTVWebApiRequestModelsSetRecordResume**](SaveTVWebApiRequestModelsSetRecordResume.md)| The record resume. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **records_post_tag_download_completed**
> records_post_tag_download_completed(id)

Creates a tag to mark the record as downloaded.

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
api_instance = swagger_client.RecordsPostApi(swagger_client.ApiClient(configuration))
id = 56 # int | The telecast identifier.

try:
    # Creates a tag to mark the record as downloaded.
    api_instance.records_post_tag_download_completed(id)
except ApiException as e:
    print("Exception when calling RecordsPostApi->records_post_tag_download_completed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The telecast identifier. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

