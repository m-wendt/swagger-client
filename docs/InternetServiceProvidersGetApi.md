# swagger_client.InternetServiceProvidersGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**internet_service_providers_get**](InternetServiceProvidersGetApi.md#internet_service_providers_get) | **GET** /v3/internetserviceproviders/{ipaddress} | Gets the internet service provider that holds the given IP address.


# **internet_service_providers_get**
> SaveTVWebApiResponseModelsInternetServiceProvider internet_service_providers_get(ip_address)

Gets the internet service provider that holds the given IP address.

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
api_instance = swagger_client.InternetServiceProvidersGetApi(swagger_client.ApiClient(configuration))
ip_address = 'ip_address_example' # str | The ip address.

try:
    # Gets the internet service provider that holds the given IP address.
    api_response = api_instance.internet_service_providers_get(ip_address)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InternetServiceProvidersGetApi->internet_service_providers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| The ip address. | 

### Return type

[**SaveTVWebApiResponseModelsInternetServiceProvider**](SaveTVWebApiResponseModelsInternetServiceProvider.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

