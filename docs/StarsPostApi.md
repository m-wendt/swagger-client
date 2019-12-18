# swagger_client.StarsPostApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stars_post_notification**](StarsPostApi.md#stars_post_notification) | **POST** /v3/stars/{id}/notifications | Creates a subscription for a star notifications (alerts).


# **stars_post_notification**
> stars_post_notification(id)

Creates a subscription for a star notifications (alerts).

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
api_instance = swagger_client.StarsPostApi(swagger_client.ApiClient(configuration))
id = 56 # int | The star identifier.

try:
    # Creates a subscription for a star notifications (alerts).
    api_instance.stars_post_notification(id)
except ApiException as e:
    print("Exception when calling StarsPostApi->stars_post_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The star identifier. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

