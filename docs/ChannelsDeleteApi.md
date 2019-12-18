# swagger_client.ChannelsDeleteApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channels_delete**](ChannelsDeleteApi.md#channels_delete) | **DELETE** /v3/channels/{id} | Deletes the channel with the given identifier.
[**channels_delete_all_catch_all_channels**](ChannelsDeleteApi.md#channels_delete_all_catch_all_channels) | **DELETE** /v3/channels/catchall | Deletes all catch all channels for the current user.


# **channels_delete**
> channels_delete(id, recordhandling=recordhandling)

Deletes the channel with the given identifier.

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
api_instance = swagger_client.ChannelsDeleteApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the channel that should be deleted.
recordhandling = 56 # int | Sets the handling of the records created by the channel.     Default value: 0    Values:     0 = Keep all records    1 = Deletes programmed records only (state Requested)    2 = Deletes ready records only (state Ok, Failed)    3 = Deletes all records (optional)

try:
    # Deletes the channel with the given identifier.
    api_instance.channels_delete(id, recordhandling=recordhandling)
except ApiException as e:
    print("Exception when calling ChannelsDeleteApi->channels_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the channel that should be deleted. | 
 **recordhandling** | **int**| Sets the handling of the records created by the channel.     Default value: 0    Values:     0 &#x3D; Keep all records    1 &#x3D; Deletes programmed records only (state Requested)    2 &#x3D; Deletes ready records only (state Ok, Failed)    3 &#x3D; Deletes all records | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_delete_all_catch_all_channels**
> channels_delete_all_catch_all_channels(recordhandling=recordhandling)

Deletes all catch all channels for the current user.

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
api_instance = swagger_client.ChannelsDeleteApi(swagger_client.ApiClient(configuration))
recordhandling = 56 # int | Sets the handling of the records created by the channel.     Default value: 0    Values:     0 = Keep all records    1 = Deletes programmed records only (state Requested)    2 = Deletes ready records only (state Ok, Failed)    3 = Deletes all records (optional)

try:
    # Deletes all catch all channels for the current user.
    api_instance.channels_delete_all_catch_all_channels(recordhandling=recordhandling)
except ApiException as e:
    print("Exception when calling ChannelsDeleteApi->channels_delete_all_catch_all_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recordhandling** | **int**| Sets the handling of the records created by the channel.     Default value: 0    Values:     0 &#x3D; Keep all records    1 &#x3D; Deletes programmed records only (state Requested)    2 &#x3D; Deletes ready records only (state Ok, Failed)    3 &#x3D; Deletes all records | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

