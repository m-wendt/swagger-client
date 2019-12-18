# swagger_client.StarsDeleteApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stars_delete_notification**](StarsDeleteApi.md#stars_delete_notification) | **DELETE** /v3/stars/notifications/{uuid} | Removes the subscription for a star notifications (alerts).


# **stars_delete_notification**
> stars_delete_notification(uuid, mailcancellationreasonid=mailcancellationreasonid)

Removes the subscription for a star notifications (alerts).

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
api_instance = swagger_client.StarsDeleteApi(swagger_client.ApiClient(configuration))
uuid = 'uuid_example' # str | The UUID.
mailcancellationreasonid = 56 # int |  (optional)

try:
    # Removes the subscription for a star notifications (alerts).
    api_instance.stars_delete_notification(uuid, mailcancellationreasonid=mailcancellationreasonid)
except ApiException as e:
    print("Exception when calling StarsDeleteApi->stars_delete_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**| The UUID. | 
 **mailcancellationreasonid** | **int**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

