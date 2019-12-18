# swagger_client.RecordsGetApi

All URIs are relative to *https://api.save.tv:443*

Method | HTTP request | Description
------------- | ------------- | -------------
[**records_count**](RecordsGetApi.md#records_count) | **GET** /v3/records/count | Retrieves the number of records for the current account that match the filter condition.
[**records_download**](RecordsGetApi.md#records_download) | **GET** /v3/records/{id}/downloads/{recordformat} | Requests the download URL for a record.
[**records_get**](RecordsGetApi.md#records_get) | **GET** /v3/records | Retrieves the record for the current account that match the filter condition.
[**records_get_0**](RecordsGetApi.md#records_get_0) | **GET** /v3/records/{id} | Retrieves a single record with the given identifier.
[**records_get_suggestions**](RecordsGetApi.md#records_get_suggestions) | **GET** /v3/records/suggestions | Provides suggestions for the telecast search text.
[**records_groups**](RecordsGetApi.md#records_groups) | **GET** /v3/records/groups/{key} | Groups the records of the current user by the given key.


# **records_count**
> SaveTVWebApiResponseModelsRecordCount records_count(adfreeavailable=adfreeavailable, channels=channels, dayofweeks=dayofweeks, exacttitle=exacttitle, exacttitles=exacttitles, excludedtelecastids=excludedtelecastids, excludedtvstations=excludedtvstations, excluderepeatedbroadcasts=excluderepeatedbroadcasts, fsk=fsk, ishighlight=ishighlight, lastupdatedate=lastupdatedate, maxenddate=maxenddate, maxstartdate=maxstartdate, maxstarttime=maxstarttime, minenddate=minenddate, minstartdate=minstartdate, minstarttime=minstarttime, q=q, recordformats=recordformats, recordstates=recordstates, removedeletedtelecasts=removedeletedtelecasts, searchtextscope=searchtextscope, starids=starids, tags=tags, telecastids=telecastids, timeblock=timeblock, timeblocks=timeblocks, tvcategories=tvcategories, tvstations=tvstations, tvsubcategories=tvsubcategories)

Retrieves the number of records for the current account that match the filter condition.

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
api_instance = swagger_client.RecordsGetApi(swagger_client.ApiClient(configuration))
adfreeavailable = true # bool | Determines wether the ad cut list is available. (optional)
channels = [56] # list[int] | A comma-separated list of TV channel identifiers. (optional)
dayofweeks = [56] # list[int] | Selects only telecast whose start date matches the given day of weeks. The start date comparison is based on local time.    Values:    0 = Sunday    1 = Monday    2 = Tuesday    3 = Wednesday    4 = Thursday    5 = Friday    6 = Saturday (optional)
exacttitle = 'exacttitle_example' # str | Selects only telecasts whose title matches exactly (but case insensitive) the given value. (optional)
exacttitles = ['exacttitles_example'] # list[str] | Selects only telecasts whose title matches exactly (but case insensitive) one of the given values.    When the parameter \"exactTitle\" is given too, the value of this parameter is ignored.    The titles are separated by a comma. Commas inside a title are escaped with \"\\,\" (1 back slash, 1 commma).    Example:    Title 1: Tatort    Title 2: Im Himmel, unter der Erde    Value: Tatort,Im Himmel\\, unter der Erde (optional)
excludedtelecastids = [56] # list[int] | A comma-separated list of telecast identifiers that will be ignored even if the other filter criterias would match these telecasts. (optional)
excludedtvstations = [56] # list[int] | A comma-separated list of TV station identifiers that must not match. (optional)
excluderepeatedbroadcasts = true # bool |  (optional)
fsk = [56] # list[int] | Selects only telecasts whose fsk matches the given value.    Values:    0 = Includes all ages from 0 to 5.    6 = Includes all ages from 6 to 11.    12 = Includes all ages from 12 to 15.    16 = Includes all ages from 16 to 17.    18 = Includes all ages from 18 and above. (optional)
ishighlight = true # bool | Determines whether the telecast must be an highlight or not. (optional)
lastupdatedate = '2013-10-20T19:20:30+01:00' # datetime | Selects only records that was updated (finished, ad free available, changed record dates, ...) / created after the given date.    Date format: 2015-03-20 17:45:00Z (optional)
maxenddate = '2013-10-20T19:20:30+01:00' # datetime | The maximum end date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
maxstartdate = '2013-10-20T19:20:30+01:00' # datetime | The maximum start date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
maxstarttime = 'maxstarttime_example' # str | The maximum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 (optional)
minenddate = '2013-10-20T19:20:30+01:00' # datetime | The minimum end date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
minstartdate = '2013-10-20T19:20:30+01:00' # datetime | The minimum start date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
minstarttime = 'minstarttime_example' # str | The minimum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 (optional)
q = 'q_example' # str | The search text used for a text search. (optional)
recordformats = [56] # list[int] | A comma-separated list of record formats. Selects only telecasts that are available in the given formats.    Values:    4 = Mobile    5 = SD    6 = HD (optional)
recordstates = [56] # list[int] | A comma-separated list of record states.    Values:    1 = The user has requested the format.    2 = The format was successfully recorded or the recording process failed.    3 = The format was recorded and encoded successful and the user can download the format.    4 = The recording or encoding process produced errors. The user cannot download the format.    5 = The user has deleted the format. (optional)
removedeletedtelecasts = true # bool | When set, deleted records are removed from result set.    The default value is true. (optional)
searchtextscope = 56 # int | The scope defines the kind of the text search.    The default value is: 1    Values:     1 = search in all texts    2 = search in title and subtitle (optional)
starids = [56] # list[int] | A comma-separated list of star identifiers. (optional)
tags = ['tags_example'] # list[str] | A comma-separated list of tag keys.    Values:    record:guard = The record was adjusted by the guard.    record:manual = The record was created manually.    record:resume:0 = The record was partially seen and can be resumed at the last position. The record was seen with ad.    record:resume:1 = The record was partially seen and can be resumed at the last position. The record was seen without ad.    record:seen = The record was seen / downloaded. (optional)
telecastids = [56] # list[int] | A comma-separated list of telecast identifiers. (optional)
timeblock = 56 # int | A time block selects telecasts of one time range.    Values    1 = telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 = telecasts that start between 06:00 and 12:00    3 = telecasts that start between 12:00 and 18:00    4 = telecasts that start between 18:00 and 00:00    5 = telecasts that start between 00:00 and 06:00    6 = telecasts that are running currently, one telecast per TV station    7 = telecasts that start after the currently running telecasts, one telecast per TV station    8 = telecasts that start between 20:15 and 20:30    9 = telecasts that start after 22:15 (optional)
timeblocks = [56] # list[int] | A list of time blocks that selects telecasts of one time range.    Values:    1 = telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 = telecasts that start between 06:00 and 12:00    3 = telecasts that start between 12:00 and 18:00    4 = telecasts that start between 18:00 and 00:00    5 = telecasts that start between 00:00 and 06:00    6 = telecasts that are running currently, one telecast per TV station    7 = telecasts that start after the currently running telecasts, one telecast per TV station    8 = telecasts that start between 20:15 and 20:30    9 = telecasts that start after 22:15    6 + 7 must be used exclusively, all others can be combined. (optional)
tvcategories = [56] # list[int] | A comma-separated list of TV category identifiers. (optional)
tvstations = [56] # list[int] | A comma-separated list of TV station identifiers. (optional)
tvsubcategories = [56] # list[int] | A comma-separated list of TV sub category identifiers. (optional)

try:
    # Retrieves the number of records for the current account that match the filter condition.
    api_response = api_instance.records_count(adfreeavailable=adfreeavailable, channels=channels, dayofweeks=dayofweeks, exacttitle=exacttitle, exacttitles=exacttitles, excludedtelecastids=excludedtelecastids, excludedtvstations=excludedtvstations, excluderepeatedbroadcasts=excluderepeatedbroadcasts, fsk=fsk, ishighlight=ishighlight, lastupdatedate=lastupdatedate, maxenddate=maxenddate, maxstartdate=maxstartdate, maxstarttime=maxstarttime, minenddate=minenddate, minstartdate=minstartdate, minstarttime=minstarttime, q=q, recordformats=recordformats, recordstates=recordstates, removedeletedtelecasts=removedeletedtelecasts, searchtextscope=searchtextscope, starids=starids, tags=tags, telecastids=telecastids, timeblock=timeblock, timeblocks=timeblocks, tvcategories=tvcategories, tvstations=tvstations, tvsubcategories=tvsubcategories)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsGetApi->records_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adfreeavailable** | **bool**| Determines wether the ad cut list is available. | [optional] 
 **channels** | [**list[int]**](int.md)| A comma-separated list of TV channel identifiers. | [optional] 
 **dayofweeks** | [**list[int]**](int.md)| Selects only telecast whose start date matches the given day of weeks. The start date comparison is based on local time.    Values:    0 &#x3D; Sunday    1 &#x3D; Monday    2 &#x3D; Tuesday    3 &#x3D; Wednesday    4 &#x3D; Thursday    5 &#x3D; Friday    6 &#x3D; Saturday | [optional] 
 **exacttitle** | **str**| Selects only telecasts whose title matches exactly (but case insensitive) the given value. | [optional] 
 **exacttitles** | [**list[str]**](str.md)| Selects only telecasts whose title matches exactly (but case insensitive) one of the given values.    When the parameter \&quot;exactTitle\&quot; is given too, the value of this parameter is ignored.    The titles are separated by a comma. Commas inside a title are escaped with \&quot;\\,\&quot; (1 back slash, 1 commma).    Example:    Title 1: Tatort    Title 2: Im Himmel, unter der Erde    Value: Tatort,Im Himmel\\, unter der Erde | [optional] 
 **excludedtelecastids** | [**list[int]**](int.md)| A comma-separated list of telecast identifiers that will be ignored even if the other filter criterias would match these telecasts. | [optional] 
 **excludedtvstations** | [**list[int]**](int.md)| A comma-separated list of TV station identifiers that must not match. | [optional] 
 **excluderepeatedbroadcasts** | **bool**|  | [optional] 
 **fsk** | [**list[int]**](int.md)| Selects only telecasts whose fsk matches the given value.    Values:    0 &#x3D; Includes all ages from 0 to 5.    6 &#x3D; Includes all ages from 6 to 11.    12 &#x3D; Includes all ages from 12 to 15.    16 &#x3D; Includes all ages from 16 to 17.    18 &#x3D; Includes all ages from 18 and above. | [optional] 
 **ishighlight** | **bool**| Determines whether the telecast must be an highlight or not. | [optional] 
 **lastupdatedate** | **datetime**| Selects only records that was updated (finished, ad free available, changed record dates, ...) / created after the given date.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **maxenddate** | **datetime**| The maximum end date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **maxstartdate** | **datetime**| The maximum start date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **maxstarttime** | **str**| The maximum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 | [optional] 
 **minenddate** | **datetime**| The minimum end date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **minstartdate** | **datetime**| The minimum start date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **minstarttime** | **str**| The minimum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 | [optional] 
 **q** | **str**| The search text used for a text search. | [optional] 
 **recordformats** | [**list[int]**](int.md)| A comma-separated list of record formats. Selects only telecasts that are available in the given formats.    Values:    4 &#x3D; Mobile    5 &#x3D; SD    6 &#x3D; HD | [optional] 
 **recordstates** | [**list[int]**](int.md)| A comma-separated list of record states.    Values:    1 &#x3D; The user has requested the format.    2 &#x3D; The format was successfully recorded or the recording process failed.    3 &#x3D; The format was recorded and encoded successful and the user can download the format.    4 &#x3D; The recording or encoding process produced errors. The user cannot download the format.    5 &#x3D; The user has deleted the format. | [optional] 
 **removedeletedtelecasts** | **bool**| When set, deleted records are removed from result set.    The default value is true. | [optional] 
 **searchtextscope** | **int**| The scope defines the kind of the text search.    The default value is: 1    Values:     1 &#x3D; search in all texts    2 &#x3D; search in title and subtitle | [optional] 
 **starids** | [**list[int]**](int.md)| A comma-separated list of star identifiers. | [optional] 
 **tags** | [**list[str]**](str.md)| A comma-separated list of tag keys.    Values:    record:guard &#x3D; The record was adjusted by the guard.    record:manual &#x3D; The record was created manually.    record:resume:0 &#x3D; The record was partially seen and can be resumed at the last position. The record was seen with ad.    record:resume:1 &#x3D; The record was partially seen and can be resumed at the last position. The record was seen without ad.    record:seen &#x3D; The record was seen / downloaded. | [optional] 
 **telecastids** | [**list[int]**](int.md)| A comma-separated list of telecast identifiers. | [optional] 
 **timeblock** | **int**| A time block selects telecasts of one time range.    Values    1 &#x3D; telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 &#x3D; telecasts that start between 06:00 and 12:00    3 &#x3D; telecasts that start between 12:00 and 18:00    4 &#x3D; telecasts that start between 18:00 and 00:00    5 &#x3D; telecasts that start between 00:00 and 06:00    6 &#x3D; telecasts that are running currently, one telecast per TV station    7 &#x3D; telecasts that start after the currently running telecasts, one telecast per TV station    8 &#x3D; telecasts that start between 20:15 and 20:30    9 &#x3D; telecasts that start after 22:15 | [optional] 
 **timeblocks** | [**list[int]**](int.md)| A list of time blocks that selects telecasts of one time range.    Values:    1 &#x3D; telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 &#x3D; telecasts that start between 06:00 and 12:00    3 &#x3D; telecasts that start between 12:00 and 18:00    4 &#x3D; telecasts that start between 18:00 and 00:00    5 &#x3D; telecasts that start between 00:00 and 06:00    6 &#x3D; telecasts that are running currently, one telecast per TV station    7 &#x3D; telecasts that start after the currently running telecasts, one telecast per TV station    8 &#x3D; telecasts that start between 20:15 and 20:30    9 &#x3D; telecasts that start after 22:15    6 + 7 must be used exclusively, all others can be combined. | [optional] 
 **tvcategories** | [**list[int]**](int.md)| A comma-separated list of TV category identifiers. | [optional] 
 **tvstations** | [**list[int]**](int.md)| A comma-separated list of TV station identifiers. | [optional] 
 **tvsubcategories** | [**list[int]**](int.md)| A comma-separated list of TV sub category identifiers. | [optional] 

### Return type

[**SaveTVWebApiResponseModelsRecordCount**](SaveTVWebApiResponseModelsRecordCount.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **records_download**
> SaveTVWebApiResponseModelsDownload records_download(id, record_format, adfree=adfree, endtime=endtime, isstreaming=isstreaming, starttime=starttime)

Requests the download URL for a record.

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
api_instance = swagger_client.RecordsGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the telecast.
record_format = 56 # int | The record format used for download.    Values:     4 = H.264 mobile    5 = H.264 SD    6 = H.264 HD
adfree = true # bool | Determines wether the ad cut list will be applied when available.    Default value is false. (optional)
endtime = 56 # int | The amount of seconds from the beginning until there, where the record should end, rest of it get's truncated. (optional)
isstreaming = true # bool |  (optional)
starttime = 56 # int | The amount of seconds from the beginning of the record which are skipped. (optional)

try:
    # Requests the download URL for a record.
    api_response = api_instance.records_download(id, record_format, adfree=adfree, endtime=endtime, isstreaming=isstreaming, starttime=starttime)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsGetApi->records_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the telecast. | 
 **record_format** | **int**| The record format used for download.    Values:     4 &#x3D; H.264 mobile    5 &#x3D; H.264 SD    6 &#x3D; H.264 HD | 
 **adfree** | **bool**| Determines wether the ad cut list will be applied when available.    Default value is false. | [optional] 
 **endtime** | **int**| The amount of seconds from the beginning until there, where the record should end, rest of it get&#39;s truncated. | [optional] 
 **isstreaming** | **bool**|  | [optional] 
 **starttime** | **int**| The amount of seconds from the beginning of the record which are skipped. | [optional] 

### Return type

[**SaveTVWebApiResponseModelsDownload**](SaveTVWebApiResponseModelsDownload.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **records_get**
> SaveTVWebApiResponseModelsPagedRecordList records_get(adfreeavailable=adfreeavailable, channels=channels, dayofweeks=dayofweeks, exacttitle=exacttitle, exacttitles=exacttitles, excludedtelecastids=excludedtelecastids, excludedtvstations=excludedtvstations, excluderepeatedbroadcasts=excluderepeatedbroadcasts, fields=fields, fsk=fsk, ishighlight=ishighlight, lastupdatedate=lastupdatedate, limit=limit, maxenddate=maxenddate, maxstartdate=maxstartdate, maxstarttime=maxstarttime, minenddate=minenddate, minstartdate=minstartdate, minstarttime=minstarttime, nopagingheader=nopagingheader, offset=offset, q=q, recordformats=recordformats, recordstates=recordstates, removedeletedtelecasts=removedeletedtelecasts, searchtextscope=searchtextscope, sort=sort, starids=starids, tags=tags, telecastids=telecastids, timeblock=timeblock, timeblocks=timeblocks, tvcategories=tvcategories, tvstations=tvstations, tvsubcategories=tvsubcategories)

Retrieves the record for the current account that match the filter condition.

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
api_instance = swagger_client.RecordsGetApi(swagger_client.ApiClient(configuration))
adfreeavailable = true # bool | Determines wether the ad cut list is available. (optional)
channels = [56] # list[int] | A comma-separated list of TV channel identifiers. (optional)
dayofweeks = [56] # list[int] | Selects only telecast whose start date matches the given day of weeks. The start date comparison is based on local time.    Values:    0 = Sunday    1 = Monday    2 = Tuesday    3 = Wednesday    4 = Thursday    5 = Friday    6 = Saturday (optional)
exacttitle = 'exacttitle_example' # str | Selects only telecasts whose title matches exactly (but case insensitive) the given value. (optional)
exacttitles = ['exacttitles_example'] # list[str] | Selects only telecasts whose title matches exactly (but case insensitive) one of the given values.    When the parameter \"exactTitle\" is given too, the value of this parameter is ignored.    The titles are separated by a comma. Commas inside a title are escaped with \"\\,\" (1 back slash, 1 commma).    Example:    Title 1: Tatort    Title 2: Im Himmel, unter der Erde    Value: Tatort,Im Himmel\\, unter der Erde (optional)
excludedtelecastids = [56] # list[int] | A comma-separated list of telecast identifiers that will be ignored even if the other filter criterias would match these telecasts. (optional)
excludedtvstations = [56] # list[int] | A comma-separated list of TV station identifiers that must not match. (optional)
excluderepeatedbroadcasts = true # bool |  (optional)
fields = ['adfreeavailable, adfreelength, channels, channels.id, channels.name, createdate, defect.adcut.availablelength, defect.adcut.expectedlength, defect.adcut.istelecastendset, defect.adcut.istelecaststartset, defect.encoding.followuptime.availablelength, defect.encoding.followuptime.expectedlength, defect.encoding.leadtime.availablelength, defect.encoding.leadtime.expectedlength, defect.encoding.telecast.availablelength, defect.encoding.telecast.expectedlength, enddate, formats, formats.cutvideosize, formats.recordformat.id, formats.recordformat.name, formats.recordstate.id, formats.recordstate.name, formats.recordstatemessage, formats.retentiondate, formats.uncutvideosize, isadcutenabled, playlists.id, playlists.name, resumepositions, resumepositions.adfree, resumepositions.default, startdate, tags.key, tags.value, telecast, telecast.commentator, telecast.country, telecast.description, telecast.director, telecast.enddate, telecast.episode, telecast.hasmoved, telecast.id, telecast.imageurl100, telecast.imageurl250, telecast.imageurl500, telecast.interpret, telecast.isblackwhite, telecast.ishighlight, telecast.isomitted, telecast.moderator, telecast.rating, telecast.roles, telecast.roles.rolename, telecast.roles.starid, telecast.roles.starname, telecast.slug, telecast.startdate, telecast.subject, telecast.subtitle, telecast.title, telecast.tvcategory.id, telecast.tvcategory.name, telecast.tvstation.id, telecast.tvstation.isrecordable, telecast.tvstation.largelogourl, telecast.tvstation.name, telecast.tvstation.smalllogourl, telecast.tvsubcategory.id, telecast.tvsubcategory.name, telecast.updatedate, telecast.voluntaryselfregulationofthemovieindustry, telecast.year, telecastid, updatedate'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"telecastid\" is always transmitted.    _The allowed field values:_    adfreeavailable,    adfreelength,    channels,    channels.id,    channels.name,    createdate,    defect.adcut.availablelength,    defect.adcut.expectedlength,    defect.adcut.istelecastendset,    defect.adcut.istelecaststartset,    defect.encoding.followuptime.availablelength,    defect.encoding.followuptime.expectedlength,    defect.encoding.leadtime.availablelength,    defect.encoding.leadtime.expectedlength,    defect.encoding.telecast.availablelength,    defect.encoding.telecast.expectedlength,    enddate,    formats,    formats.cutvideosize,    formats.recordformat.id,    formats.recordformat.name,    formats.recordstate.id,    formats.recordstate.name,    formats.recordstatemessage,    formats.retentiondate,    formats.uncutvideosize,    isadcutenabled,    playlists.id,    playlists.name,    resumepositions,    resumepositions.adfree,    resumepositions.default,    startdate,    tags.key,    tags.value,    telecast,    telecast.commentator,    telecast.country,    telecast.description,    telecast.director,    telecast.enddate,    telecast.episode,    telecast.hasmoved,    telecast.id,    telecast.imageurl100,    telecast.imageurl250,    telecast.imageurl500,    telecast.interpret,    telecast.isblackwhite,    telecast.ishighlight,    telecast.isomitted,    telecast.moderator,    telecast.rating,    telecast.roles,    telecast.roles.rolename,    telecast.roles.starid,    telecast.roles.starname,    telecast.slug,    telecast.startdate,    telecast.subject,    telecast.subtitle,    telecast.title,    telecast.tvcategory.id,    telecast.tvcategory.name,    telecast.tvstation.id,    telecast.tvstation.isrecordable,    telecast.tvstation.largelogourl,    telecast.tvstation.name,    telecast.tvstation.smalllogourl,    telecast.tvsubcategory.id,    telecast.tvsubcategory.name,    telecast.updatedate,    telecast.voluntaryselfregulationofthemovieindustry,    telecast.year,    telecastid,    updatedate (optional) (default to adfreeavailable, adfreelength, channels, channels.id, channels.name, createdate, defect.adcut.availablelength, defect.adcut.expectedlength, defect.adcut.istelecastendset, defect.adcut.istelecaststartset, defect.encoding.followuptime.availablelength, defect.encoding.followuptime.expectedlength, defect.encoding.leadtime.availablelength, defect.encoding.leadtime.expectedlength, defect.encoding.telecast.availablelength, defect.encoding.telecast.expectedlength, enddate, formats, formats.cutvideosize, formats.recordformat.id, formats.recordformat.name, formats.recordstate.id, formats.recordstate.name, formats.recordstatemessage, formats.retentiondate, formats.uncutvideosize, isadcutenabled, playlists.id, playlists.name, resumepositions, resumepositions.adfree, resumepositions.default, startdate, tags.key, tags.value, telecast, telecast.commentator, telecast.country, telecast.description, telecast.director, telecast.enddate, telecast.episode, telecast.hasmoved, telecast.id, telecast.imageurl100, telecast.imageurl250, telecast.imageurl500, telecast.interpret, telecast.isblackwhite, telecast.ishighlight, telecast.isomitted, telecast.moderator, telecast.rating, telecast.roles, telecast.roles.rolename, telecast.roles.starid, telecast.roles.starname, telecast.slug, telecast.startdate, telecast.subject, telecast.subtitle, telecast.title, telecast.tvcategory.id, telecast.tvcategory.name, telecast.tvstation.id, telecast.tvstation.isrecordable, telecast.tvstation.largelogourl, telecast.tvstation.name, telecast.tvstation.smalllogourl, telecast.tvsubcategory.id, telecast.tvsubcategory.name, telecast.updatedate, telecast.voluntaryselfregulationofthemovieindustry, telecast.year, telecastid, updatedate)
fsk = [56] # list[int] | Selects only telecasts whose fsk matches the given value.    Values:    0 = Includes all ages from 0 to 5.    6 = Includes all ages from 6 to 11.    12 = Includes all ages from 12 to 15.    16 = Includes all ages from 16 to 17.    18 = Includes all ages from 18 and above. (optional)
ishighlight = true # bool | Determines whether the telecast must be an highlight or not. (optional)
lastupdatedate = '2013-10-20T19:20:30+01:00' # datetime | Selects only records that was updated (finished, ad free available, changed record dates, ...) / created after the given date.    Date format: 2015-03-20 17:45:00Z (optional)
limit = 56 # int | Sets the maximum number of items in result set.    The default value: 50.    The maximum allowed value: 5000. (optional)
maxenddate = '2013-10-20T19:20:30+01:00' # datetime | The maximum end date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
maxstartdate = '2013-10-20T19:20:30+01:00' # datetime | The maximum start date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
maxstarttime = 'maxstarttime_example' # str | The maximum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 (optional)
minenddate = '2013-10-20T19:20:30+01:00' # datetime | The minimum end date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
minstartdate = '2013-10-20T19:20:30+01:00' # datetime | The minimum start date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
minstarttime = 'minstarttime_example' # str | The minimum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 (optional)
nopagingheader = true # bool | By default, the response object is a plain list of items and the paging metadata is put into the header.    Example header:     X-Total-Count: 403    X-Paging-Offset: 0    X-Paging-Limit: 20    When set to true, the response object is a complex object that contains the paging meta data and the items in 2 separate properties. The header does not contain additional values (optional)
offset = 56 # int | Sets the number of data items that are skipped in the result set.    The default value: 0. (optional)
q = 'q_example' # str | The search text used for a text search. (optional)
recordformats = [56] # list[int] | A comma-separated list of record formats. Selects only telecasts that are available in the given formats.    Values:    4 = Mobile    5 = SD    6 = HD (optional)
recordstates = [56] # list[int] | A comma-separated list of record states.    Values:    1 = The user has requested the format.    2 = The format was successfully recorded or the recording process failed.    3 = The format was recorded and encoded successful and the user can download the format.    4 = The recording or encoding process produced errors. The user cannot download the format.    5 = The user has deleted the format. (optional)
removedeletedtelecasts = true # bool | When set, deleted records are removed from result set.    The default value is true. (optional)
searchtextscope = 56 # int | The scope defines the kind of the text search.    The default value is: 1    Values:     1 = search in all texts    2 = search in title and subtitle (optional)
sort = NULL # list[object] | Sets the sort properties. The values are comma-separated. To sort ascending add a \"+\" before the sort property, to sort descending add a \"-\" before the sort property.    When omitted, a default sorting is used.    Example: sort=+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    category    episode    random    startdate    subcategory    subtitle    title    tvstationposition    year    Default sorting:    +startdate (optional)
starids = [56] # list[int] | A comma-separated list of star identifiers. (optional)
tags = ['tags_example'] # list[str] | A comma-separated list of tag keys.    Values:    record:guard = The record was adjusted by the guard.    record:manual = The record was created manually.    record:resume:0 = The record was partially seen and can be resumed at the last position. The record was seen with ad.    record:resume:1 = The record was partially seen and can be resumed at the last position. The record was seen without ad.    record:seen = The record was seen / downloaded. (optional)
telecastids = [56] # list[int] | A comma-separated list of telecast identifiers. (optional)
timeblock = 56 # int | A time block selects telecasts of one time range.    Values    1 = telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 = telecasts that start between 06:00 and 12:00    3 = telecasts that start between 12:00 and 18:00    4 = telecasts that start between 18:00 and 00:00    5 = telecasts that start between 00:00 and 06:00    6 = telecasts that are running currently, one telecast per TV station    7 = telecasts that start after the currently running telecasts, one telecast per TV station    8 = telecasts that start between 20:15 and 20:30    9 = telecasts that start after 22:15 (optional)
timeblocks = [56] # list[int] | A list of time blocks that selects telecasts of one time range.    Values:    1 = telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 = telecasts that start between 06:00 and 12:00    3 = telecasts that start between 12:00 and 18:00    4 = telecasts that start between 18:00 and 00:00    5 = telecasts that start between 00:00 and 06:00    6 = telecasts that are running currently, one telecast per TV station    7 = telecasts that start after the currently running telecasts, one telecast per TV station    8 = telecasts that start between 20:15 and 20:30    9 = telecasts that start after 22:15    6 + 7 must be used exclusively, all others can be combined. (optional)
tvcategories = [56] # list[int] | A comma-separated list of TV category identifiers. (optional)
tvstations = [56] # list[int] | A comma-separated list of TV station identifiers. (optional)
tvsubcategories = [56] # list[int] | A comma-separated list of TV sub category identifiers. (optional)

try:
    # Retrieves the record for the current account that match the filter condition.
    api_response = api_instance.records_get(adfreeavailable=adfreeavailable, channels=channels, dayofweeks=dayofweeks, exacttitle=exacttitle, exacttitles=exacttitles, excludedtelecastids=excludedtelecastids, excludedtvstations=excludedtvstations, excluderepeatedbroadcasts=excluderepeatedbroadcasts, fields=fields, fsk=fsk, ishighlight=ishighlight, lastupdatedate=lastupdatedate, limit=limit, maxenddate=maxenddate, maxstartdate=maxstartdate, maxstarttime=maxstarttime, minenddate=minenddate, minstartdate=minstartdate, minstarttime=minstarttime, nopagingheader=nopagingheader, offset=offset, q=q, recordformats=recordformats, recordstates=recordstates, removedeletedtelecasts=removedeletedtelecasts, searchtextscope=searchtextscope, sort=sort, starids=starids, tags=tags, telecastids=telecastids, timeblock=timeblock, timeblocks=timeblocks, tvcategories=tvcategories, tvstations=tvstations, tvsubcategories=tvsubcategories)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsGetApi->records_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **adfreeavailable** | **bool**| Determines wether the ad cut list is available. | [optional] 
 **channels** | [**list[int]**](int.md)| A comma-separated list of TV channel identifiers. | [optional] 
 **dayofweeks** | [**list[int]**](int.md)| Selects only telecast whose start date matches the given day of weeks. The start date comparison is based on local time.    Values:    0 &#x3D; Sunday    1 &#x3D; Monday    2 &#x3D; Tuesday    3 &#x3D; Wednesday    4 &#x3D; Thursday    5 &#x3D; Friday    6 &#x3D; Saturday | [optional] 
 **exacttitle** | **str**| Selects only telecasts whose title matches exactly (but case insensitive) the given value. | [optional] 
 **exacttitles** | [**list[str]**](str.md)| Selects only telecasts whose title matches exactly (but case insensitive) one of the given values.    When the parameter \&quot;exactTitle\&quot; is given too, the value of this parameter is ignored.    The titles are separated by a comma. Commas inside a title are escaped with \&quot;\\,\&quot; (1 back slash, 1 commma).    Example:    Title 1: Tatort    Title 2: Im Himmel, unter der Erde    Value: Tatort,Im Himmel\\, unter der Erde | [optional] 
 **excludedtelecastids** | [**list[int]**](int.md)| A comma-separated list of telecast identifiers that will be ignored even if the other filter criterias would match these telecasts. | [optional] 
 **excludedtvstations** | [**list[int]**](int.md)| A comma-separated list of TV station identifiers that must not match. | [optional] 
 **excluderepeatedbroadcasts** | **bool**|  | [optional] 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;telecastid\&quot; is always transmitted.    _The allowed field values:_    adfreeavailable,    adfreelength,    channels,    channels.id,    channels.name,    createdate,    defect.adcut.availablelength,    defect.adcut.expectedlength,    defect.adcut.istelecastendset,    defect.adcut.istelecaststartset,    defect.encoding.followuptime.availablelength,    defect.encoding.followuptime.expectedlength,    defect.encoding.leadtime.availablelength,    defect.encoding.leadtime.expectedlength,    defect.encoding.telecast.availablelength,    defect.encoding.telecast.expectedlength,    enddate,    formats,    formats.cutvideosize,    formats.recordformat.id,    formats.recordformat.name,    formats.recordstate.id,    formats.recordstate.name,    formats.recordstatemessage,    formats.retentiondate,    formats.uncutvideosize,    isadcutenabled,    playlists.id,    playlists.name,    resumepositions,    resumepositions.adfree,    resumepositions.default,    startdate,    tags.key,    tags.value,    telecast,    telecast.commentator,    telecast.country,    telecast.description,    telecast.director,    telecast.enddate,    telecast.episode,    telecast.hasmoved,    telecast.id,    telecast.imageurl100,    telecast.imageurl250,    telecast.imageurl500,    telecast.interpret,    telecast.isblackwhite,    telecast.ishighlight,    telecast.isomitted,    telecast.moderator,    telecast.rating,    telecast.roles,    telecast.roles.rolename,    telecast.roles.starid,    telecast.roles.starname,    telecast.slug,    telecast.startdate,    telecast.subject,    telecast.subtitle,    telecast.title,    telecast.tvcategory.id,    telecast.tvcategory.name,    telecast.tvstation.id,    telecast.tvstation.isrecordable,    telecast.tvstation.largelogourl,    telecast.tvstation.name,    telecast.tvstation.smalllogourl,    telecast.tvsubcategory.id,    telecast.tvsubcategory.name,    telecast.updatedate,    telecast.voluntaryselfregulationofthemovieindustry,    telecast.year,    telecastid,    updatedate | [optional] [default to adfreeavailable, adfreelength, channels, channels.id, channels.name, createdate, defect.adcut.availablelength, defect.adcut.expectedlength, defect.adcut.istelecastendset, defect.adcut.istelecaststartset, defect.encoding.followuptime.availablelength, defect.encoding.followuptime.expectedlength, defect.encoding.leadtime.availablelength, defect.encoding.leadtime.expectedlength, defect.encoding.telecast.availablelength, defect.encoding.telecast.expectedlength, enddate, formats, formats.cutvideosize, formats.recordformat.id, formats.recordformat.name, formats.recordstate.id, formats.recordstate.name, formats.recordstatemessage, formats.retentiondate, formats.uncutvideosize, isadcutenabled, playlists.id, playlists.name, resumepositions, resumepositions.adfree, resumepositions.default, startdate, tags.key, tags.value, telecast, telecast.commentator, telecast.country, telecast.description, telecast.director, telecast.enddate, telecast.episode, telecast.hasmoved, telecast.id, telecast.imageurl100, telecast.imageurl250, telecast.imageurl500, telecast.interpret, telecast.isblackwhite, telecast.ishighlight, telecast.isomitted, telecast.moderator, telecast.rating, telecast.roles, telecast.roles.rolename, telecast.roles.starid, telecast.roles.starname, telecast.slug, telecast.startdate, telecast.subject, telecast.subtitle, telecast.title, telecast.tvcategory.id, telecast.tvcategory.name, telecast.tvstation.id, telecast.tvstation.isrecordable, telecast.tvstation.largelogourl, telecast.tvstation.name, telecast.tvstation.smalllogourl, telecast.tvsubcategory.id, telecast.tvsubcategory.name, telecast.updatedate, telecast.voluntaryselfregulationofthemovieindustry, telecast.year, telecastid, updatedate]
 **fsk** | [**list[int]**](int.md)| Selects only telecasts whose fsk matches the given value.    Values:    0 &#x3D; Includes all ages from 0 to 5.    6 &#x3D; Includes all ages from 6 to 11.    12 &#x3D; Includes all ages from 12 to 15.    16 &#x3D; Includes all ages from 16 to 17.    18 &#x3D; Includes all ages from 18 and above. | [optional] 
 **ishighlight** | **bool**| Determines whether the telecast must be an highlight or not. | [optional] 
 **lastupdatedate** | **datetime**| Selects only records that was updated (finished, ad free available, changed record dates, ...) / created after the given date.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **limit** | **int**| Sets the maximum number of items in result set.    The default value: 50.    The maximum allowed value: 5000. | [optional] 
 **maxenddate** | **datetime**| The maximum end date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **maxstartdate** | **datetime**| The maximum start date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **maxstarttime** | **str**| The maximum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 | [optional] 
 **minenddate** | **datetime**| The minimum end date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **minstartdate** | **datetime**| The minimum start date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **minstarttime** | **str**| The minimum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 | [optional] 
 **nopagingheader** | **bool**| By default, the response object is a plain list of items and the paging metadata is put into the header.    Example header:     X-Total-Count: 403    X-Paging-Offset: 0    X-Paging-Limit: 20    When set to true, the response object is a complex object that contains the paging meta data and the items in 2 separate properties. The header does not contain additional values | [optional] 
 **offset** | **int**| Sets the number of data items that are skipped in the result set.    The default value: 0. | [optional] 
 **q** | **str**| The search text used for a text search. | [optional] 
 **recordformats** | [**list[int]**](int.md)| A comma-separated list of record formats. Selects only telecasts that are available in the given formats.    Values:    4 &#x3D; Mobile    5 &#x3D; SD    6 &#x3D; HD | [optional] 
 **recordstates** | [**list[int]**](int.md)| A comma-separated list of record states.    Values:    1 &#x3D; The user has requested the format.    2 &#x3D; The format was successfully recorded or the recording process failed.    3 &#x3D; The format was recorded and encoded successful and the user can download the format.    4 &#x3D; The recording or encoding process produced errors. The user cannot download the format.    5 &#x3D; The user has deleted the format. | [optional] 
 **removedeletedtelecasts** | **bool**| When set, deleted records are removed from result set.    The default value is true. | [optional] 
 **searchtextscope** | **int**| The scope defines the kind of the text search.    The default value is: 1    Values:     1 &#x3D; search in all texts    2 &#x3D; search in title and subtitle | [optional] 
 **sort** | [**list[object]**](object.md)| Sets the sort properties. The values are comma-separated. To sort ascending add a \&quot;+\&quot; before the sort property, to sort descending add a \&quot;-\&quot; before the sort property.    When omitted, a default sorting is used.    Example: sort&#x3D;+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    category    episode    random    startdate    subcategory    subtitle    title    tvstationposition    year    Default sorting:    +startdate | [optional] 
 **starids** | [**list[int]**](int.md)| A comma-separated list of star identifiers. | [optional] 
 **tags** | [**list[str]**](str.md)| A comma-separated list of tag keys.    Values:    record:guard &#x3D; The record was adjusted by the guard.    record:manual &#x3D; The record was created manually.    record:resume:0 &#x3D; The record was partially seen and can be resumed at the last position. The record was seen with ad.    record:resume:1 &#x3D; The record was partially seen and can be resumed at the last position. The record was seen without ad.    record:seen &#x3D; The record was seen / downloaded. | [optional] 
 **telecastids** | [**list[int]**](int.md)| A comma-separated list of telecast identifiers. | [optional] 
 **timeblock** | **int**| A time block selects telecasts of one time range.    Values    1 &#x3D; telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 &#x3D; telecasts that start between 06:00 and 12:00    3 &#x3D; telecasts that start between 12:00 and 18:00    4 &#x3D; telecasts that start between 18:00 and 00:00    5 &#x3D; telecasts that start between 00:00 and 06:00    6 &#x3D; telecasts that are running currently, one telecast per TV station    7 &#x3D; telecasts that start after the currently running telecasts, one telecast per TV station    8 &#x3D; telecasts that start between 20:15 and 20:30    9 &#x3D; telecasts that start after 22:15 | [optional] 
 **timeblocks** | [**list[int]**](int.md)| A list of time blocks that selects telecasts of one time range.    Values:    1 &#x3D; telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 &#x3D; telecasts that start between 06:00 and 12:00    3 &#x3D; telecasts that start between 12:00 and 18:00    4 &#x3D; telecasts that start between 18:00 and 00:00    5 &#x3D; telecasts that start between 00:00 and 06:00    6 &#x3D; telecasts that are running currently, one telecast per TV station    7 &#x3D; telecasts that start after the currently running telecasts, one telecast per TV station    8 &#x3D; telecasts that start between 20:15 and 20:30    9 &#x3D; telecasts that start after 22:15    6 + 7 must be used exclusively, all others can be combined. | [optional] 
 **tvcategories** | [**list[int]**](int.md)| A comma-separated list of TV category identifiers. | [optional] 
 **tvstations** | [**list[int]**](int.md)| A comma-separated list of TV station identifiers. | [optional] 
 **tvsubcategories** | [**list[int]**](int.md)| A comma-separated list of TV sub category identifiers. | [optional] 

### Return type

[**SaveTVWebApiResponseModelsPagedRecordList**](SaveTVWebApiResponseModelsPagedRecordList.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **records_get_0**
> SaveTVWebApiResponseModelsRecord records_get_0(id, fields=fields)

Retrieves a single record with the given identifier.

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
api_instance = swagger_client.RecordsGetApi(swagger_client.ApiClient(configuration))
id = 56 # int | The identifier of the telecast.
fields = ['adfreeavailable, adfreelength, channels, channels.id, channels.name, createdate, defect.adcut.availablelength, defect.adcut.expectedlength, defect.adcut.istelecastendset, defect.adcut.istelecaststartset, defect.encoding.followuptime.availablelength, defect.encoding.followuptime.expectedlength, defect.encoding.leadtime.availablelength, defect.encoding.leadtime.expectedlength, defect.encoding.telecast.availablelength, defect.encoding.telecast.expectedlength, enddate, formats, formats.cutvideosize, formats.recordformat.id, formats.recordformat.name, formats.recordstate.id, formats.recordstate.name, formats.recordstatemessage, formats.retentiondate, formats.uncutvideosize, isadcutenabled, playlists.id, playlists.name, resumepositions, resumepositions.adfree, resumepositions.default, startdate, tags.key, tags.value, telecast, telecast.commentator, telecast.country, telecast.description, telecast.director, telecast.enddate, telecast.episode, telecast.hasmoved, telecast.id, telecast.imageurl100, telecast.imageurl250, telecast.imageurl500, telecast.interpret, telecast.isblackwhite, telecast.ishighlight, telecast.isomitted, telecast.moderator, telecast.rating, telecast.roles, telecast.roles.rolename, telecast.roles.starid, telecast.roles.starname, telecast.slug, telecast.startdate, telecast.subject, telecast.subtitle, telecast.title, telecast.tvcategory.id, telecast.tvcategory.name, telecast.tvstation.id, telecast.tvstation.isrecordable, telecast.tvstation.largelogourl, telecast.tvstation.name, telecast.tvstation.smalllogourl, telecast.tvsubcategory.id, telecast.tvsubcategory.name, telecast.updatedate, telecast.voluntaryselfregulationofthemovieindustry, telecast.year, telecastid, updatedate'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \"telecastid\" is always transmitted.    _The allowed field values:_    adfreeavailable,    adfreelength,    channels,    channels.id,    channels.name,    createdate,    defect.adcut.availablelength,    defect.adcut.expectedlength,    defect.adcut.istelecastendset,    defect.adcut.istelecaststartset,    defect.encoding.followuptime.availablelength,    defect.encoding.followuptime.expectedlength,    defect.encoding.leadtime.availablelength,    defect.encoding.leadtime.expectedlength,    defect.encoding.telecast.availablelength,    defect.encoding.telecast.expectedlength,    enddate,    formats,    formats.cutvideosize,    formats.recordformat.id,    formats.recordformat.name,    formats.recordstate.id,    formats.recordstate.name,    formats.recordstatemessage,    formats.retentiondate,    formats.uncutvideosize,    isadcutenabled,    playlists.id,    playlists.name,    resumepositions,    resumepositions.adfree,    resumepositions.default,    startdate,    tags.key,    tags.value,    telecast,    telecast.commentator,    telecast.country,    telecast.description,    telecast.director,    telecast.enddate,    telecast.episode,    telecast.hasmoved,    telecast.id,    telecast.imageurl100,    telecast.imageurl250,    telecast.imageurl500,    telecast.interpret,    telecast.isblackwhite,    telecast.ishighlight,    telecast.isomitted,    telecast.moderator,    telecast.rating,    telecast.roles,    telecast.roles.rolename,    telecast.roles.starid,    telecast.roles.starname,    telecast.slug,    telecast.startdate,    telecast.subject,    telecast.subtitle,    telecast.title,    telecast.tvcategory.id,    telecast.tvcategory.name,    telecast.tvstation.id,    telecast.tvstation.isrecordable,    telecast.tvstation.largelogourl,    telecast.tvstation.name,    telecast.tvstation.smalllogourl,    telecast.tvsubcategory.id,    telecast.tvsubcategory.name,    telecast.updatedate,    telecast.voluntaryselfregulationofthemovieindustry,    telecast.year,    telecastid,    updatedate (optional) (default to adfreeavailable, adfreelength, channels, channels.id, channels.name, createdate, defect.adcut.availablelength, defect.adcut.expectedlength, defect.adcut.istelecastendset, defect.adcut.istelecaststartset, defect.encoding.followuptime.availablelength, defect.encoding.followuptime.expectedlength, defect.encoding.leadtime.availablelength, defect.encoding.leadtime.expectedlength, defect.encoding.telecast.availablelength, defect.encoding.telecast.expectedlength, enddate, formats, formats.cutvideosize, formats.recordformat.id, formats.recordformat.name, formats.recordstate.id, formats.recordstate.name, formats.recordstatemessage, formats.retentiondate, formats.uncutvideosize, isadcutenabled, playlists.id, playlists.name, resumepositions, resumepositions.adfree, resumepositions.default, startdate, tags.key, tags.value, telecast, telecast.commentator, telecast.country, telecast.description, telecast.director, telecast.enddate, telecast.episode, telecast.hasmoved, telecast.id, telecast.imageurl100, telecast.imageurl250, telecast.imageurl500, telecast.interpret, telecast.isblackwhite, telecast.ishighlight, telecast.isomitted, telecast.moderator, telecast.rating, telecast.roles, telecast.roles.rolename, telecast.roles.starid, telecast.roles.starname, telecast.slug, telecast.startdate, telecast.subject, telecast.subtitle, telecast.title, telecast.tvcategory.id, telecast.tvcategory.name, telecast.tvstation.id, telecast.tvstation.isrecordable, telecast.tvstation.largelogourl, telecast.tvstation.name, telecast.tvstation.smalllogourl, telecast.tvsubcategory.id, telecast.tvsubcategory.name, telecast.updatedate, telecast.voluntaryselfregulationofthemovieindustry, telecast.year, telecastid, updatedate)

try:
    # Retrieves a single record with the given identifier.
    api_response = api_instance.records_get_0(id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsGetApi->records_get_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The identifier of the telecast. | 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The field \&quot;telecastid\&quot; is always transmitted.    _The allowed field values:_    adfreeavailable,    adfreelength,    channels,    channels.id,    channels.name,    createdate,    defect.adcut.availablelength,    defect.adcut.expectedlength,    defect.adcut.istelecastendset,    defect.adcut.istelecaststartset,    defect.encoding.followuptime.availablelength,    defect.encoding.followuptime.expectedlength,    defect.encoding.leadtime.availablelength,    defect.encoding.leadtime.expectedlength,    defect.encoding.telecast.availablelength,    defect.encoding.telecast.expectedlength,    enddate,    formats,    formats.cutvideosize,    formats.recordformat.id,    formats.recordformat.name,    formats.recordstate.id,    formats.recordstate.name,    formats.recordstatemessage,    formats.retentiondate,    formats.uncutvideosize,    isadcutenabled,    playlists.id,    playlists.name,    resumepositions,    resumepositions.adfree,    resumepositions.default,    startdate,    tags.key,    tags.value,    telecast,    telecast.commentator,    telecast.country,    telecast.description,    telecast.director,    telecast.enddate,    telecast.episode,    telecast.hasmoved,    telecast.id,    telecast.imageurl100,    telecast.imageurl250,    telecast.imageurl500,    telecast.interpret,    telecast.isblackwhite,    telecast.ishighlight,    telecast.isomitted,    telecast.moderator,    telecast.rating,    telecast.roles,    telecast.roles.rolename,    telecast.roles.starid,    telecast.roles.starname,    telecast.slug,    telecast.startdate,    telecast.subject,    telecast.subtitle,    telecast.title,    telecast.tvcategory.id,    telecast.tvcategory.name,    telecast.tvstation.id,    telecast.tvstation.isrecordable,    telecast.tvstation.largelogourl,    telecast.tvstation.name,    telecast.tvstation.smalllogourl,    telecast.tvsubcategory.id,    telecast.tvsubcategory.name,    telecast.updatedate,    telecast.voluntaryselfregulationofthemovieindustry,    telecast.year,    telecastid,    updatedate | [optional] [default to adfreeavailable, adfreelength, channels, channels.id, channels.name, createdate, defect.adcut.availablelength, defect.adcut.expectedlength, defect.adcut.istelecastendset, defect.adcut.istelecaststartset, defect.encoding.followuptime.availablelength, defect.encoding.followuptime.expectedlength, defect.encoding.leadtime.availablelength, defect.encoding.leadtime.expectedlength, defect.encoding.telecast.availablelength, defect.encoding.telecast.expectedlength, enddate, formats, formats.cutvideosize, formats.recordformat.id, formats.recordformat.name, formats.recordstate.id, formats.recordstate.name, formats.recordstatemessage, formats.retentiondate, formats.uncutvideosize, isadcutenabled, playlists.id, playlists.name, resumepositions, resumepositions.adfree, resumepositions.default, startdate, tags.key, tags.value, telecast, telecast.commentator, telecast.country, telecast.description, telecast.director, telecast.enddate, telecast.episode, telecast.hasmoved, telecast.id, telecast.imageurl100, telecast.imageurl250, telecast.imageurl500, telecast.interpret, telecast.isblackwhite, telecast.ishighlight, telecast.isomitted, telecast.moderator, telecast.rating, telecast.roles, telecast.roles.rolename, telecast.roles.starid, telecast.roles.starname, telecast.slug, telecast.startdate, telecast.subject, telecast.subtitle, telecast.title, telecast.tvcategory.id, telecast.tvcategory.name, telecast.tvstation.id, telecast.tvstation.isrecordable, telecast.tvstation.largelogourl, telecast.tvstation.name, telecast.tvstation.smalllogourl, telecast.tvsubcategory.id, telecast.tvsubcategory.name, telecast.updatedate, telecast.voluntaryselfregulationofthemovieindustry, telecast.year, telecastid, updatedate]

### Return type

[**SaveTVWebApiResponseModelsRecord**](SaveTVWebApiResponseModelsRecord.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **records_get_suggestions**
> list[SaveTVWebApiResponseModelsSuggestion] records_get_suggestions(q=q)

Provides suggestions for the telecast search text.

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
api_instance = swagger_client.RecordsGetApi(swagger_client.ApiClient(configuration))
q = 'q_example' # str |  (optional)

try:
    # Provides suggestions for the telecast search text.
    api_response = api_instance.records_get_suggestions(q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsGetApi->records_get_suggestions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**|  | [optional] 

### Return type

[**list[SaveTVWebApiResponseModelsSuggestion]**](SaveTVWebApiResponseModelsSuggestion.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **records_groups**
> list[SaveTVWebApiResponseModelsRecordGroup] records_groups(key, adfreeavailable=adfreeavailable, channels=channels, dayofweeks=dayofweeks, exacttitle=exacttitle, exacttitles=exacttitles, excludedtelecastids=excludedtelecastids, excludedtvstations=excludedtvstations, excluderepeatedbroadcasts=excluderepeatedbroadcasts, fields=fields, fsk=fsk, includedrecordslimit=includedrecordslimit, ishighlight=ishighlight, lastupdatedate=lastupdatedate, limit=limit, maxenddate=maxenddate, maxstartdate=maxstartdate, maxstarttime=maxstarttime, minenddate=minenddate, minstartdate=minstartdate, minstarttime=minstarttime, nopagingheader=nopagingheader, offset=offset, q=q, recordformats=recordformats, recordstates=recordstates, removedeletedtelecasts=removedeletedtelecasts, searchtextscope=searchtextscope, sort=sort, starids=starids, tags=tags, telecastids=telecastids, timeblock=timeblock, timeblocks=timeblocks, tvcategories=tvcategories, tvstations=tvstations, tvsubcategories=tvsubcategories)

Groups the records of the current user by the given key.

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
api_instance = swagger_client.RecordsGetApi(swagger_client.ApiClient(configuration))
key = 'key_example' # str | The key defines the property that is used for grouping.    Allowed values:    channel = Group by channel    date = Group by record start date (ignore time part)    title = Group by title    tvstation = Group by TV station
adfreeavailable = true # bool | Determines wether the ad cut list is available. (optional)
channels = [56] # list[int] | A comma-separated list of TV channel identifiers. (optional)
dayofweeks = [56] # list[int] | Selects only telecast whose start date matches the given day of weeks. The start date comparison is based on local time.    Values:    0 = Sunday    1 = Monday    2 = Tuesday    3 = Wednesday    4 = Thursday    5 = Friday    6 = Saturday (optional)
exacttitle = 'exacttitle_example' # str | Selects only telecasts whose title matches exactly (but case insensitive) the given value. (optional)
exacttitles = ['exacttitles_example'] # list[str] | Selects only telecasts whose title matches exactly (but case insensitive) one of the given values.    When the parameter \"exactTitle\" is given too, the value of this parameter is ignored.    The titles are separated by a comma. Commas inside a title are escaped with \"\\,\" (1 back slash, 1 commma).    Example:    Title 1: Tatort    Title 2: Im Himmel, unter der Erde    Value: Tatort,Im Himmel\\, unter der Erde (optional)
excludedtelecastids = [56] # list[int] | A comma-separated list of telecast identifiers that will be ignored even if the other filter criterias would match these telecasts. (optional)
excludedtvstations = [56] # list[int] | A comma-separated list of TV station identifiers that must not match. (optional)
excluderepeatedbroadcasts = true # bool |  (optional)
fields = ['adfreeavailable, adfreelength, channels, channels.id, channels.name, count, createdate, defect.adcut.availablelength, defect.adcut.expectedlength, defect.adcut.istelecastendset, defect.adcut.istelecaststartset, defect.encoding.followuptime.availablelength, defect.encoding.followuptime.expectedlength, defect.encoding.leadtime.availablelength, defect.encoding.leadtime.expectedlength, defect.encoding.telecast.availablelength, defect.encoding.telecast.expectedlength, enddate, formats, formats.cutvideosize, formats.recordformat.id, formats.recordformat.name, formats.recordstate.id, formats.recordstate.name, formats.recordstatemessage, formats.retentiondate, formats.uncutvideosize, imageurl100, imageurl250, imageurl500, isadcutenabled, key, playlists.id, playlists.name, resumepositions, resumepositions.adfree, resumepositions.default, startdate, tags.key, tags.value, telecast, telecast.commentator, telecast.country, telecast.description, telecast.director, telecast.enddate, telecast.episode, telecast.hasmoved, telecast.id, telecast.imageurl100, telecast.imageurl250, telecast.imageurl500, telecast.interpret, telecast.isblackwhite, telecast.ishighlight, telecast.isomitted, telecast.moderator, telecast.rating, telecast.roles, telecast.roles.rolename, telecast.roles.starid, telecast.roles.starname, telecast.slug, telecast.startdate, telecast.subject, telecast.subtitle, telecast.title, telecast.tvcategory.id, telecast.tvcategory.name, telecast.tvstation.id, telecast.tvstation.isrecordable, telecast.tvstation.largelogourl, telecast.tvstation.name, telecast.tvstation.smalllogourl, telecast.tvsubcategory.id, telecast.tvsubcategory.name, telecast.updatedate, telecast.voluntaryselfregulationofthemovieindustry, telecast.year, telecastid, title, updatedate'] # list[str] | Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The fields \"key, telecastid\" are always transmitted.    _The allowed field values:_    adfreeavailable,    adfreelength,    channels,    channels.id,    channels.name,    count,    createdate,    defect.adcut.availablelength,    defect.adcut.expectedlength,    defect.adcut.istelecastendset,    defect.adcut.istelecaststartset,    defect.encoding.followuptime.availablelength,    defect.encoding.followuptime.expectedlength,    defect.encoding.leadtime.availablelength,    defect.encoding.leadtime.expectedlength,    defect.encoding.telecast.availablelength,    defect.encoding.telecast.expectedlength,    enddate,    formats,    formats.cutvideosize,    formats.recordformat.id,    formats.recordformat.name,    formats.recordstate.id,    formats.recordstate.name,    formats.recordstatemessage,    formats.retentiondate,    formats.uncutvideosize,    imageurl100,    imageurl250,    imageurl500,    isadcutenabled,    key,    playlists.id,    playlists.name,    resumepositions,    resumepositions.adfree,    resumepositions.default,    startdate,    tags.key,    tags.value,    telecast,    telecast.commentator,    telecast.country,    telecast.description,    telecast.director,    telecast.enddate,    telecast.episode,    telecast.hasmoved,    telecast.id,    telecast.imageurl100,    telecast.imageurl250,    telecast.imageurl500,    telecast.interpret,    telecast.isblackwhite,    telecast.ishighlight,    telecast.isomitted,    telecast.moderator,    telecast.rating,    telecast.roles,    telecast.roles.rolename,    telecast.roles.starid,    telecast.roles.starname,    telecast.slug,    telecast.startdate,    telecast.subject,    telecast.subtitle,    telecast.title,    telecast.tvcategory.id,    telecast.tvcategory.name,    telecast.tvstation.id,    telecast.tvstation.isrecordable,    telecast.tvstation.largelogourl,    telecast.tvstation.name,    telecast.tvstation.smalllogourl,    telecast.tvsubcategory.id,    telecast.tvsubcategory.name,    telecast.updatedate,    telecast.voluntaryselfregulationofthemovieindustry,    telecast.year,    telecastid,    title,    updatedate (optional) (default to adfreeavailable, adfreelength, channels, channels.id, channels.name, count, createdate, defect.adcut.availablelength, defect.adcut.expectedlength, defect.adcut.istelecastendset, defect.adcut.istelecaststartset, defect.encoding.followuptime.availablelength, defect.encoding.followuptime.expectedlength, defect.encoding.leadtime.availablelength, defect.encoding.leadtime.expectedlength, defect.encoding.telecast.availablelength, defect.encoding.telecast.expectedlength, enddate, formats, formats.cutvideosize, formats.recordformat.id, formats.recordformat.name, formats.recordstate.id, formats.recordstate.name, formats.recordstatemessage, formats.retentiondate, formats.uncutvideosize, imageurl100, imageurl250, imageurl500, isadcutenabled, key, playlists.id, playlists.name, resumepositions, resumepositions.adfree, resumepositions.default, startdate, tags.key, tags.value, telecast, telecast.commentator, telecast.country, telecast.description, telecast.director, telecast.enddate, telecast.episode, telecast.hasmoved, telecast.id, telecast.imageurl100, telecast.imageurl250, telecast.imageurl500, telecast.interpret, telecast.isblackwhite, telecast.ishighlight, telecast.isomitted, telecast.moderator, telecast.rating, telecast.roles, telecast.roles.rolename, telecast.roles.starid, telecast.roles.starname, telecast.slug, telecast.startdate, telecast.subject, telecast.subtitle, telecast.title, telecast.tvcategory.id, telecast.tvcategory.name, telecast.tvstation.id, telecast.tvstation.isrecordable, telecast.tvstation.largelogourl, telecast.tvstation.name, telecast.tvstation.smalllogourl, telecast.tvsubcategory.id, telecast.tvsubcategory.name, telecast.updatedate, telecast.voluntaryselfregulationofthemovieindustry, telecast.year, telecastid, title, updatedate)
fsk = [56] # list[int] | Selects only telecasts whose fsk matches the given value.    Values:    0 = Includes all ages from 0 to 5.    6 = Includes all ages from 6 to 11.    12 = Includes all ages from 12 to 15.    16 = Includes all ages from 16 to 17.    18 = Includes all ages from 18 and above. (optional)
includedrecordslimit = 56 # int | Gets the limit of records in one group until the records will be included into the response. When a group contains more records, no record is included in the response for this group.    Default value: 0 (optional)
ishighlight = true # bool | Determines whether the telecast must be an highlight or not. (optional)
lastupdatedate = '2013-10-20T19:20:30+01:00' # datetime | Selects only records that was updated (finished, ad free available, changed record dates, ...) / created after the given date.    Date format: 2015-03-20 17:45:00Z (optional)
limit = 56 # int | Sets the maximum number of items in result set.    The default value: 50.    The maximum allowed value: 2000. (optional)
maxenddate = '2013-10-20T19:20:30+01:00' # datetime | The maximum end date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
maxstartdate = '2013-10-20T19:20:30+01:00' # datetime | The maximum start date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
maxstarttime = 'maxstarttime_example' # str | The maximum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 (optional)
minenddate = '2013-10-20T19:20:30+01:00' # datetime | The minimum end date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
minstartdate = '2013-10-20T19:20:30+01:00' # datetime | The minimum start date of the telecast.    Date format: 2015-03-20 17:45:00Z (optional)
minstarttime = 'minstarttime_example' # str | The minimum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 (optional)
nopagingheader = true # bool | By default, the response object is a plain list of items and the paging metadata is put into the header.    Example header:     X-Total-Count: 403    X-Paging-Offset: 0    X-Paging-Limit: 20    When set to true, the response object is a complex object that contains the paging meta data and the items in 2 separate properties. The header does not contain additional values (optional)
offset = 56 # int | Sets the number of data items that are skipped in the result set.    The default value: 0. (optional)
q = 'q_example' # str | The search text used for a text search. (optional)
recordformats = [56] # list[int] | A comma-separated list of record formats. Selects only telecasts that are available in the given formats.    Values:    4 = Mobile    5 = SD    6 = HD (optional)
recordstates = [56] # list[int] | A comma-separated list of record states.    Values:    1 = The user has requested the format.    2 = The format was successfully recorded or the recording process failed.    3 = The format was recorded and encoded successful and the user can download the format.    4 = The recording or encoding process produced errors. The user cannot download the format.    5 = The user has deleted the format. (optional)
removedeletedtelecasts = true # bool | When set, deleted records are removed from result set.    The default value is true. (optional)
searchtextscope = 56 # int | The scope defines the kind of the text search.    The default value is: 1    Values:     1 = search in all texts    2 = search in title and subtitle (optional)
sort = NULL # list[object] | Sets the sort properties. The values are comma-separated. To sort ascending add a \"+\" before the sort property, to sort descending add a \"-\" before the sort property.    When omitted, a default sorting is used.    Example: sort=+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    startdate    title    Default sorting:    +startdate,+title (optional)
starids = [56] # list[int] | A comma-separated list of star identifiers. (optional)
tags = ['tags_example'] # list[str] | A comma-separated list of tag keys.    Values:    record:guard = The record was adjusted by the guard.    record:manual = The record was created manually.    record:resume:0 = The record was partially seen and can be resumed at the last position. The record was seen with ad.    record:resume:1 = The record was partially seen and can be resumed at the last position. The record was seen without ad.    record:seen = The record was seen / downloaded. (optional)
telecastids = [56] # list[int] | A comma-separated list of telecast identifiers. (optional)
timeblock = 56 # int | A time block selects telecasts of one time range.    Values    1 = telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 = telecasts that start between 06:00 and 12:00    3 = telecasts that start between 12:00 and 18:00    4 = telecasts that start between 18:00 and 00:00    5 = telecasts that start between 00:00 and 06:00    6 = telecasts that are running currently, one telecast per TV station    7 = telecasts that start after the currently running telecasts, one telecast per TV station    8 = telecasts that start between 20:15 and 20:30    9 = telecasts that start after 22:15 (optional)
timeblocks = [56] # list[int] | A list of time blocks that selects telecasts of one time range.    Values:    1 = telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 = telecasts that start between 06:00 and 12:00    3 = telecasts that start between 12:00 and 18:00    4 = telecasts that start between 18:00 and 00:00    5 = telecasts that start between 00:00 and 06:00    6 = telecasts that are running currently, one telecast per TV station    7 = telecasts that start after the currently running telecasts, one telecast per TV station    8 = telecasts that start between 20:15 and 20:30    9 = telecasts that start after 22:15    6 + 7 must be used exclusively, all others can be combined. (optional)
tvcategories = [56] # list[int] | A comma-separated list of TV category identifiers. (optional)
tvstations = [56] # list[int] | A comma-separated list of TV station identifiers. (optional)
tvsubcategories = [56] # list[int] | A comma-separated list of TV sub category identifiers. (optional)

try:
    # Groups the records of the current user by the given key.
    api_response = api_instance.records_groups(key, adfreeavailable=adfreeavailable, channels=channels, dayofweeks=dayofweeks, exacttitle=exacttitle, exacttitles=exacttitles, excludedtelecastids=excludedtelecastids, excludedtvstations=excludedtvstations, excluderepeatedbroadcasts=excluderepeatedbroadcasts, fields=fields, fsk=fsk, includedrecordslimit=includedrecordslimit, ishighlight=ishighlight, lastupdatedate=lastupdatedate, limit=limit, maxenddate=maxenddate, maxstartdate=maxstartdate, maxstarttime=maxstarttime, minenddate=minenddate, minstartdate=minstartdate, minstarttime=minstarttime, nopagingheader=nopagingheader, offset=offset, q=q, recordformats=recordformats, recordstates=recordstates, removedeletedtelecasts=removedeletedtelecasts, searchtextscope=searchtextscope, sort=sort, starids=starids, tags=tags, telecastids=telecastids, timeblock=timeblock, timeblocks=timeblocks, tvcategories=tvcategories, tvstations=tvstations, tvsubcategories=tvsubcategories)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsGetApi->records_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The key defines the property that is used for grouping.    Allowed values:    channel &#x3D; Group by channel    date &#x3D; Group by record start date (ignore time part)    title &#x3D; Group by title    tvstation &#x3D; Group by TV station | 
 **adfreeavailable** | **bool**| Determines wether the ad cut list is available. | [optional] 
 **channels** | [**list[int]**](int.md)| A comma-separated list of TV channel identifiers. | [optional] 
 **dayofweeks** | [**list[int]**](int.md)| Selects only telecast whose start date matches the given day of weeks. The start date comparison is based on local time.    Values:    0 &#x3D; Sunday    1 &#x3D; Monday    2 &#x3D; Tuesday    3 &#x3D; Wednesday    4 &#x3D; Thursday    5 &#x3D; Friday    6 &#x3D; Saturday | [optional] 
 **exacttitle** | **str**| Selects only telecasts whose title matches exactly (but case insensitive) the given value. | [optional] 
 **exacttitles** | [**list[str]**](str.md)| Selects only telecasts whose title matches exactly (but case insensitive) one of the given values.    When the parameter \&quot;exactTitle\&quot; is given too, the value of this parameter is ignored.    The titles are separated by a comma. Commas inside a title are escaped with \&quot;\\,\&quot; (1 back slash, 1 commma).    Example:    Title 1: Tatort    Title 2: Im Himmel, unter der Erde    Value: Tatort,Im Himmel\\, unter der Erde | [optional] 
 **excludedtelecastids** | [**list[int]**](int.md)| A comma-separated list of telecast identifiers that will be ignored even if the other filter criterias would match these telecasts. | [optional] 
 **excludedtvstations** | [**list[int]**](int.md)| A comma-separated list of TV station identifiers that must not match. | [optional] 
 **excluderepeatedbroadcasts** | **bool**|  | [optional] 
 **fields** | [**list[str]**](str.md)| Selects the fields that will be transmitted in the response. The field names are comma-separated, case-insensitive and will be trimmed.    The fields \&quot;key, telecastid\&quot; are always transmitted.    _The allowed field values:_    adfreeavailable,    adfreelength,    channels,    channels.id,    channels.name,    count,    createdate,    defect.adcut.availablelength,    defect.adcut.expectedlength,    defect.adcut.istelecastendset,    defect.adcut.istelecaststartset,    defect.encoding.followuptime.availablelength,    defect.encoding.followuptime.expectedlength,    defect.encoding.leadtime.availablelength,    defect.encoding.leadtime.expectedlength,    defect.encoding.telecast.availablelength,    defect.encoding.telecast.expectedlength,    enddate,    formats,    formats.cutvideosize,    formats.recordformat.id,    formats.recordformat.name,    formats.recordstate.id,    formats.recordstate.name,    formats.recordstatemessage,    formats.retentiondate,    formats.uncutvideosize,    imageurl100,    imageurl250,    imageurl500,    isadcutenabled,    key,    playlists.id,    playlists.name,    resumepositions,    resumepositions.adfree,    resumepositions.default,    startdate,    tags.key,    tags.value,    telecast,    telecast.commentator,    telecast.country,    telecast.description,    telecast.director,    telecast.enddate,    telecast.episode,    telecast.hasmoved,    telecast.id,    telecast.imageurl100,    telecast.imageurl250,    telecast.imageurl500,    telecast.interpret,    telecast.isblackwhite,    telecast.ishighlight,    telecast.isomitted,    telecast.moderator,    telecast.rating,    telecast.roles,    telecast.roles.rolename,    telecast.roles.starid,    telecast.roles.starname,    telecast.slug,    telecast.startdate,    telecast.subject,    telecast.subtitle,    telecast.title,    telecast.tvcategory.id,    telecast.tvcategory.name,    telecast.tvstation.id,    telecast.tvstation.isrecordable,    telecast.tvstation.largelogourl,    telecast.tvstation.name,    telecast.tvstation.smalllogourl,    telecast.tvsubcategory.id,    telecast.tvsubcategory.name,    telecast.updatedate,    telecast.voluntaryselfregulationofthemovieindustry,    telecast.year,    telecastid,    title,    updatedate | [optional] [default to adfreeavailable, adfreelength, channels, channels.id, channels.name, count, createdate, defect.adcut.availablelength, defect.adcut.expectedlength, defect.adcut.istelecastendset, defect.adcut.istelecaststartset, defect.encoding.followuptime.availablelength, defect.encoding.followuptime.expectedlength, defect.encoding.leadtime.availablelength, defect.encoding.leadtime.expectedlength, defect.encoding.telecast.availablelength, defect.encoding.telecast.expectedlength, enddate, formats, formats.cutvideosize, formats.recordformat.id, formats.recordformat.name, formats.recordstate.id, formats.recordstate.name, formats.recordstatemessage, formats.retentiondate, formats.uncutvideosize, imageurl100, imageurl250, imageurl500, isadcutenabled, key, playlists.id, playlists.name, resumepositions, resumepositions.adfree, resumepositions.default, startdate, tags.key, tags.value, telecast, telecast.commentator, telecast.country, telecast.description, telecast.director, telecast.enddate, telecast.episode, telecast.hasmoved, telecast.id, telecast.imageurl100, telecast.imageurl250, telecast.imageurl500, telecast.interpret, telecast.isblackwhite, telecast.ishighlight, telecast.isomitted, telecast.moderator, telecast.rating, telecast.roles, telecast.roles.rolename, telecast.roles.starid, telecast.roles.starname, telecast.slug, telecast.startdate, telecast.subject, telecast.subtitle, telecast.title, telecast.tvcategory.id, telecast.tvcategory.name, telecast.tvstation.id, telecast.tvstation.isrecordable, telecast.tvstation.largelogourl, telecast.tvstation.name, telecast.tvstation.smalllogourl, telecast.tvsubcategory.id, telecast.tvsubcategory.name, telecast.updatedate, telecast.voluntaryselfregulationofthemovieindustry, telecast.year, telecastid, title, updatedate]
 **fsk** | [**list[int]**](int.md)| Selects only telecasts whose fsk matches the given value.    Values:    0 &#x3D; Includes all ages from 0 to 5.    6 &#x3D; Includes all ages from 6 to 11.    12 &#x3D; Includes all ages from 12 to 15.    16 &#x3D; Includes all ages from 16 to 17.    18 &#x3D; Includes all ages from 18 and above. | [optional] 
 **includedrecordslimit** | **int**| Gets the limit of records in one group until the records will be included into the response. When a group contains more records, no record is included in the response for this group.    Default value: 0 | [optional] 
 **ishighlight** | **bool**| Determines whether the telecast must be an highlight or not. | [optional] 
 **lastupdatedate** | **datetime**| Selects only records that was updated (finished, ad free available, changed record dates, ...) / created after the given date.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **limit** | **int**| Sets the maximum number of items in result set.    The default value: 50.    The maximum allowed value: 2000. | [optional] 
 **maxenddate** | **datetime**| The maximum end date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **maxstartdate** | **datetime**| The maximum start date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **maxstarttime** | **str**| The maximum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 | [optional] 
 **minenddate** | **datetime**| The minimum end date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **minstartdate** | **datetime**| The minimum start date of the telecast.    Date format: 2015-03-20 17:45:00Z | [optional] 
 **minstarttime** | **str**| The minimum start time of the telecast. The time is interpreted as local time. The given value is inclusive.    Time format: 17:30 | [optional] 
 **nopagingheader** | **bool**| By default, the response object is a plain list of items and the paging metadata is put into the header.    Example header:     X-Total-Count: 403    X-Paging-Offset: 0    X-Paging-Limit: 20    When set to true, the response object is a complex object that contains the paging meta data and the items in 2 separate properties. The header does not contain additional values | [optional] 
 **offset** | **int**| Sets the number of data items that are skipped in the result set.    The default value: 0. | [optional] 
 **q** | **str**| The search text used for a text search. | [optional] 
 **recordformats** | [**list[int]**](int.md)| A comma-separated list of record formats. Selects only telecasts that are available in the given formats.    Values:    4 &#x3D; Mobile    5 &#x3D; SD    6 &#x3D; HD | [optional] 
 **recordstates** | [**list[int]**](int.md)| A comma-separated list of record states.    Values:    1 &#x3D; The user has requested the format.    2 &#x3D; The format was successfully recorded or the recording process failed.    3 &#x3D; The format was recorded and encoded successful and the user can download the format.    4 &#x3D; The recording or encoding process produced errors. The user cannot download the format.    5 &#x3D; The user has deleted the format. | [optional] 
 **removedeletedtelecasts** | **bool**| When set, deleted records are removed from result set.    The default value is true. | [optional] 
 **searchtextscope** | **int**| The scope defines the kind of the text search.    The default value is: 1    Values:     1 &#x3D; search in all texts    2 &#x3D; search in title and subtitle | [optional] 
 **sort** | [**list[object]**](object.md)| Sets the sort properties. The values are comma-separated. To sort ascending add a \&quot;+\&quot; before the sort property, to sort descending add a \&quot;-\&quot; before the sort property.    When omitted, a default sorting is used.    Example: sort&#x3D;+prop1,-prop2    Sorts first by prop1 ascending then by prop2 descending.    Allowed sort properties:    startdate    title    Default sorting:    +startdate,+title | [optional] 
 **starids** | [**list[int]**](int.md)| A comma-separated list of star identifiers. | [optional] 
 **tags** | [**list[str]**](str.md)| A comma-separated list of tag keys.    Values:    record:guard &#x3D; The record was adjusted by the guard.    record:manual &#x3D; The record was created manually.    record:resume:0 &#x3D; The record was partially seen and can be resumed at the last position. The record was seen with ad.    record:resume:1 &#x3D; The record was partially seen and can be resumed at the last position. The record was seen without ad.    record:seen &#x3D; The record was seen / downloaded. | [optional] 
 **telecastids** | [**list[int]**](int.md)| A comma-separated list of telecast identifiers. | [optional] 
 **timeblock** | **int**| A time block selects telecasts of one time range.    Values    1 &#x3D; telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 &#x3D; telecasts that start between 06:00 and 12:00    3 &#x3D; telecasts that start between 12:00 and 18:00    4 &#x3D; telecasts that start between 18:00 and 00:00    5 &#x3D; telecasts that start between 00:00 and 06:00    6 &#x3D; telecasts that are running currently, one telecast per TV station    7 &#x3D; telecasts that start after the currently running telecasts, one telecast per TV station    8 &#x3D; telecasts that start between 20:15 and 20:30    9 &#x3D; telecasts that start after 22:15 | [optional] 
 **timeblocks** | [**list[int]**](int.md)| A list of time blocks that selects telecasts of one time range.    Values:    1 &#x3D; telecasts that start between 06:00 and 12:00, contains also the telecast that runs at 06:00    2 &#x3D; telecasts that start between 06:00 and 12:00    3 &#x3D; telecasts that start between 12:00 and 18:00    4 &#x3D; telecasts that start between 18:00 and 00:00    5 &#x3D; telecasts that start between 00:00 and 06:00    6 &#x3D; telecasts that are running currently, one telecast per TV station    7 &#x3D; telecasts that start after the currently running telecasts, one telecast per TV station    8 &#x3D; telecasts that start between 20:15 and 20:30    9 &#x3D; telecasts that start after 22:15    6 + 7 must be used exclusively, all others can be combined. | [optional] 
 **tvcategories** | [**list[int]**](int.md)| A comma-separated list of TV category identifiers. | [optional] 
 **tvstations** | [**list[int]**](int.md)| A comma-separated list of TV station identifiers. | [optional] 
 **tvsubcategories** | [**list[int]**](int.md)| A comma-separated list of TV sub category identifiers. | [optional] 

### Return type

[**list[SaveTVWebApiResponseModelsRecordGroup]**](SaveTVWebApiResponseModelsRecordGroup.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

