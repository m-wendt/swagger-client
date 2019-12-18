# swagger_client.CredentialsPostApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credentials_reminder**](CredentialsPostApi.md#credentials_reminder) | **POST** /v3/credentials/reminder | Sends a reminder mail with the credentials for the account that matches the given email address.


# **credentials_reminder**
> credentials_reminder(credentials_reminder)

Sends a reminder mail with the credentials for the account that matches the given email address.

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
api_instance = swagger_client.CredentialsPostApi(swagger_client.ApiClient(configuration))
credentials_reminder = swagger_client.SaveTVWebApiRequestModelsCredentialsReminder() # SaveTVWebApiRequestModelsCredentialsReminder | The credentials reminder.

try:
    # Sends a reminder mail with the credentials for the account that matches the given email address.
    api_instance.credentials_reminder(credentials_reminder)
except ApiException as e:
    print("Exception when calling CredentialsPostApi->credentials_reminder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_reminder** | [**SaveTVWebApiRequestModelsCredentialsReminder**](SaveTVWebApiRequestModelsCredentialsReminder.md)| The credentials reminder. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

