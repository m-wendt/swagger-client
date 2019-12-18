# swagger_client.UserPostApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_access_code_update_access_code**](UserPostApi.md#user_access_code_update_access_code) | **POST** /v3/user/accesscode | Updates the AccessCode.
[**user_cancel_reminder_create_cancel_reminder**](UserPostApi.md#user_cancel_reminder_create_cancel_reminder) | **POST** /v3/user/cancellation-reminder | Creates the contract cancel reminder entry.
[**user_post**](UserPostApi.md#user_post) | **POST** /v3/user | Endpoint for saving user settings.
[**user_userlane_state_create_userlane_state**](UserPostApi.md#user_userlane_state_create_userlane_state) | **POST** /v3/user/userlane-state | Creates the current state of the userlane for a specific user.


# **user_access_code_update_access_code**
> user_access_code_update_access_code(access_code_update)

Updates the AccessCode.

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
api_instance = swagger_client.UserPostApi(swagger_client.ApiClient(configuration))
access_code_update = swagger_client.SaveTVWebApiRequestModelsAccessCodeUpdate() # SaveTVWebApiRequestModelsAccessCodeUpdate | The allowed range for the new code is between 0000 and 9999. The access code must have 4 digits. The old access code can also be the user password.

try:
    # Updates the AccessCode.
    api_instance.user_access_code_update_access_code(access_code_update)
except ApiException as e:
    print("Exception when calling UserPostApi->user_access_code_update_access_code: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_code_update** | [**SaveTVWebApiRequestModelsAccessCodeUpdate**](SaveTVWebApiRequestModelsAccessCodeUpdate.md)| The allowed range for the new code is between 0000 and 9999. The access code must have 4 digits. The old access code can also be the user password. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_cancel_reminder_create_cancel_reminder**
> user_cancel_reminder_create_cancel_reminder()

Creates the contract cancel reminder entry.

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
api_instance = swagger_client.UserPostApi(swagger_client.ApiClient(configuration))

try:
    # Creates the contract cancel reminder entry.
    api_instance.user_cancel_reminder_create_cancel_reminder()
except ApiException as e:
    print("Exception when calling UserPostApi->user_cancel_reminder_create_cancel_reminder: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_post**
> user_post(user_setting)

Endpoint for saving user settings.

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
api_instance = swagger_client.UserPostApi(swagger_client.ApiClient(configuration))
user_setting = swagger_client.SaveTVWebApiRequestModelsUserSetting() # SaveTVWebApiRequestModelsUserSetting | The user settings to save.

try:
    # Endpoint for saving user settings.
    api_instance.user_post(user_setting)
except ApiException as e:
    print("Exception when calling UserPostApi->user_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_setting** | [**SaveTVWebApiRequestModelsUserSetting**](SaveTVWebApiRequestModelsUserSetting.md)| The user settings to save. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_userlane_state_create_userlane_state**
> user_userlane_state_create_userlane_state(userlane_state)

Creates the current state of the userlane for a specific user.

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
api_instance = swagger_client.UserPostApi(swagger_client.ApiClient(configuration))
userlane_state = swagger_client.SaveTVWebApiRequestModelsUserUserlaneState() # SaveTVWebApiRequestModelsUserUserlaneState | The allowed range for the state is between 1 and 3.

try:
    # Creates the current state of the userlane for a specific user.
    api_instance.user_userlane_state_create_userlane_state(userlane_state)
except ApiException as e:
    print("Exception when calling UserPostApi->user_userlane_state_create_userlane_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userlane_state** | [**SaveTVWebApiRequestModelsUserUserlaneState**](SaveTVWebApiRequestModelsUserUserlaneState.md)| The allowed range for the state is between 1 and 3. | 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

