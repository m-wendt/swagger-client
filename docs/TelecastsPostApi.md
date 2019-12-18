# swagger_client.TelecastsPostApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**telecasts_rating**](TelecastsPostApi.md#telecasts_rating) | **POST** /v3/telecasts/{id}/rating | Ratings the specified identifier.


# **telecasts_rating**
> SaveTVEpgTelecastsRating telecasts_rating(id, telecast_rating)

Ratings the specified identifier.

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
api_instance = swagger_client.TelecastsPostApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier.
telecast_rating = swagger_client.SaveTVWebApiRequestModelsTelecastRating() # SaveTVWebApiRequestModelsTelecastRating | The rating for the telecast. The allowed range for the rating is between 1 and 5.

try:
    # Ratings the specified identifier.
    api_response = api_instance.telecasts_rating(id, telecast_rating)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TelecastsPostApi->telecasts_rating: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier. | 
 **telecast_rating** | [**SaveTVWebApiRequestModelsTelecastRating**](SaveTVWebApiRequestModelsTelecastRating.md)| The rating for the telecast. The allowed range for the rating is between 1 and 5. | 

### Return type

[**SaveTVEpgTelecastsRating**](SaveTVEpgTelecastsRating.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

