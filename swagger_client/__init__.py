# coding: utf-8

# flake8: noqa

"""
    Save.TV API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import apis into sdk package
from swagger_client.api.channel_time_frames__get_api import ChannelTimeFramesGetApi
from swagger_client.api.channels__delete_api import ChannelsDeleteApi
from swagger_client.api.channels__get_api import ChannelsGetApi
from swagger_client.api.channels__post_api import ChannelsPostApi
from swagger_client.api.credentials__post_api import CredentialsPostApi
from swagger_client.api.erotic_videos__get_api import EroticVideosGetApi
from swagger_client.api.folx_tv_videos__get_api import FolxTvVideosGetApi
from swagger_client.api.internet_service_providers__get_api import InternetServiceProvidersGetApi
from swagger_client.api.playlist_types__get_api import PlaylistTypesGetApi
from swagger_client.api.playlists__delete_api import PlaylistsDeleteApi
from swagger_client.api.playlists__get_api import PlaylistsGetApi
from swagger_client.api.playlists__post_api import PlaylistsPostApi
from swagger_client.api.record_formats__get_api import RecordFormatsGetApi
from swagger_client.api.record_states__get_api import RecordStatesGetApi
from swagger_client.api.records__delete_api import RecordsDeleteApi
from swagger_client.api.records__get_api import RecordsGetApi
from swagger_client.api.records__post_api import RecordsPostApi
from swagger_client.api.stars__delete_api import StarsDeleteApi
from swagger_client.api.stars__get_api import StarsGetApi
from swagger_client.api.stars__post_api import StarsPostApi
from swagger_client.api.telecasts__get_api import TelecastsGetApi
from swagger_client.api.telecasts__post_api import TelecastsPostApi
from swagger_client.api.time_blocks__get_api import TimeBlocksGetApi
from swagger_client.api.tv_categories__get_api import TvCategoriesGetApi
from swagger_client.api.tv_station_groups__get_api import TvStationGroupsGetApi
from swagger_client.api.tv_stations__get_api import TvStationsGetApi
from swagger_client.api.user__get_api import UserGetApi
from swagger_client.api.user__post_api import UserPostApi
from swagger_client.api.version__get_api import VersionGetApi

# import ApiClient
from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
# import models into sdk package
from swagger_client.models.microsoft_win32_safe_handles_safe_wait_handle import MicrosoftWin32SafeHandlesSafeWaitHandle
from swagger_client.models.olymp_collections_sort_description import OlympCollectionsSortDescription
from swagger_client.models.olymp_net45_audit_i_audit_info_provider import OlympNet45AuditIAuditInfoProvider
from swagger_client.models.olymp_web_api_response_models_error import OlympWebApiResponseModelsError
from swagger_client.models.olymp_web_api_response_models_paging import OlympWebApiResponseModelsPaging
from swagger_client.models.save_tv_epg_data_context_channel import SaveTVEpgDataContextChannel
from swagger_client.models.save_tv_epg_live_streaming_live_stream_urls import SaveTVEpgLiveStreamingLiveStreamUrls
from swagger_client.models.save_tv_epg_telecasts_rating import SaveTVEpgTelecastsRating
from swagger_client.models.save_tv_erotic_videos_i_domain_video_list_cache import SaveTVEroticVideosIDomainVideoListCache
from swagger_client.models.save_tv_erotic_videos_i_video_download_service import SaveTVEroticVideosIVideoDownloadService
from swagger_client.models.save_tv_erotic_videos_i_video_list_service import SaveTVEroticVideosIVideoListService
from swagger_client.models.save_tv_sn_global_accounts_i_user_account_state_cache import SaveTVSnGlobalAccountsIUserAccountStateCache
from swagger_client.models.save_tv_video_on_demand_folx_tv_videos_i_domain_video_list_cache import SaveTVVideoOnDemandFolxTvVideosIDomainVideoListCache
from swagger_client.models.save_tv_video_on_demand_folx_tv_videos_i_video_download_service import SaveTVVideoOnDemandFolxTvVideosIVideoDownloadService
from swagger_client.models.save_tv_web_api_request_models_access_code_update import SaveTVWebApiRequestModelsAccessCodeUpdate
from swagger_client.models.save_tv_web_api_request_models_access_code_validation import SaveTVWebApiRequestModelsAccessCodeValidation
from swagger_client.models.save_tv_web_api_request_models_catch_all_channel import SaveTVWebApiRequestModelsCatchAllChannel
from swagger_client.models.save_tv_web_api_request_models_channel_delete_request import SaveTVWebApiRequestModelsChannelDeleteRequest
from swagger_client.models.save_tv_web_api_request_models_channel_fields_filter import SaveTVWebApiRequestModelsChannelFieldsFilter
from swagger_client.models.save_tv_web_api_request_models_channel_filter import SaveTVWebApiRequestModelsChannelFilter
from swagger_client.models.save_tv_web_api_request_models_channel_telecast_fields_filter import SaveTVWebApiRequestModelsChannelTelecastFieldsFilter
from swagger_client.models.save_tv_web_api_request_models_channel_time_frame_fields_filter import SaveTVWebApiRequestModelsChannelTimeFrameFieldsFilter
from swagger_client.models.save_tv_web_api_request_models_credentials_reminder import SaveTVWebApiRequestModelsCredentialsReminder
from swagger_client.models.save_tv_web_api_request_models_delete_record_resume import SaveTVWebApiRequestModelsDeleteRecordResume
from swagger_client.models.save_tv_web_api_request_models_download_order import SaveTVWebApiRequestModelsDownloadOrder
from swagger_client.models.save_tv_web_api_request_models_full_text_search_channel import SaveTVWebApiRequestModelsFullTextSearchChannel
from swagger_client.models.save_tv_web_api_request_models_guard import SaveTVWebApiRequestModelsGuard
from swagger_client.models.save_tv_web_api_request_models_playlist import SaveTVWebApiRequestModelsPlaylist
from swagger_client.models.save_tv_web_api_request_models_playlist_fields_filter import SaveTVWebApiRequestModelsPlaylistFieldsFilter
from swagger_client.models.save_tv_web_api_request_models_playlist_filter import SaveTVWebApiRequestModelsPlaylistFilter
from swagger_client.models.save_tv_web_api_request_models_playlist_id_list import SaveTVWebApiRequestModelsPlaylistIdList
from swagger_client.models.save_tv_web_api_request_models_playlist_items_fields_filter import SaveTVWebApiRequestModelsPlaylistItemsFieldsFilter
from swagger_client.models.save_tv_web_api_request_models_record_buffer import SaveTVWebApiRequestModelsRecordBuffer
from swagger_client.models.save_tv_web_api_request_models_record_count_filter import SaveTVWebApiRequestModelsRecordCountFilter
from swagger_client.models.save_tv_web_api_request_models_record_fields_filter import SaveTVWebApiRequestModelsRecordFieldsFilter
from swagger_client.models.save_tv_web_api_request_models_record_filter import SaveTVWebApiRequestModelsRecordFilter
from swagger_client.models.save_tv_web_api_request_models_record_format_filter import SaveTVWebApiRequestModelsRecordFormatFilter
from swagger_client.models.save_tv_web_api_request_models_record_group_filter import SaveTVWebApiRequestModelsRecordGroupFilter
from swagger_client.models.save_tv_web_api_request_models_record_order import SaveTVWebApiRequestModelsRecordOrder
from swagger_client.models.save_tv_web_api_request_models_record_suggestion_filter import SaveTVWebApiRequestModelsRecordSuggestionFilter
from swagger_client.models.save_tv_web_api_request_models_set_record_resume import SaveTVWebApiRequestModelsSetRecordResume
from swagger_client.models.save_tv_web_api_request_models_star_channel import SaveTVWebApiRequestModelsStarChannel
from swagger_client.models.save_tv_web_api_request_models_star_fields_filter import SaveTVWebApiRequestModelsStarFieldsFilter
from swagger_client.models.save_tv_web_api_request_models_star_filter import SaveTVWebApiRequestModelsStarFilter
from swagger_client.models.save_tv_web_api_request_models_star_notification_delete_request import SaveTVWebApiRequestModelsStarNotificationDeleteRequest
from swagger_client.models.save_tv_web_api_request_models_telecast_fields_filter import SaveTVWebApiRequestModelsTelecastFieldsFilter
from swagger_client.models.save_tv_web_api_request_models_telecast_filter import SaveTVWebApiRequestModelsTelecastFilter
from swagger_client.models.save_tv_web_api_request_models_telecast_id_list import SaveTVWebApiRequestModelsTelecastIdList
from swagger_client.models.save_tv_web_api_request_models_telecast_ids_channel import SaveTVWebApiRequestModelsTelecastIdsChannel
from swagger_client.models.save_tv_web_api_request_models_telecast_rating import SaveTVWebApiRequestModelsTelecastRating
from swagger_client.models.save_tv_web_api_request_models_telecast_suggestion_filter import SaveTVWebApiRequestModelsTelecastSuggestionFilter
from swagger_client.models.save_tv_web_api_request_models_title_channel import SaveTVWebApiRequestModelsTitleChannel
from swagger_client.models.save_tv_web_api_request_models_tv_category_fields_filter import SaveTVWebApiRequestModelsTvCategoryFieldsFilter
from swagger_client.models.save_tv_web_api_request_models_tv_station_channel import SaveTVWebApiRequestModelsTvStationChannel
from swagger_client.models.save_tv_web_api_request_models_tv_station_fields_filter import SaveTVWebApiRequestModelsTvStationFieldsFilter
from swagger_client.models.save_tv_web_api_request_models_tv_station_filter import SaveTVWebApiRequestModelsTvStationFilter
from swagger_client.models.save_tv_web_api_request_models_tv_station_group_fields_filter import SaveTVWebApiRequestModelsTvStationGroupFieldsFilter
from swagger_client.models.save_tv_web_api_request_models_user_fields_filter import SaveTVWebApiRequestModelsUserFieldsFilter
from swagger_client.models.save_tv_web_api_request_models_user_setting import SaveTVWebApiRequestModelsUserSetting
from swagger_client.models.save_tv_web_api_request_models_user_userlane_state import SaveTVWebApiRequestModelsUserUserlaneState
from swagger_client.models.save_tv_web_api_response_models_catch_all import SaveTVWebApiResponseModelsCatchAll
from swagger_client.models.save_tv_web_api_response_models_channel import SaveTVWebApiResponseModelsChannel
from swagger_client.models.save_tv_web_api_response_models_channel_base import SaveTVWebApiResponseModelsChannelBase
from swagger_client.models.save_tv_web_api_response_models_channel_count import SaveTVWebApiResponseModelsChannelCount
from swagger_client.models.save_tv_web_api_response_models_channel_time_frame import SaveTVWebApiResponseModelsChannelTimeFrame
from swagger_client.models.save_tv_web_api_response_models_contract import SaveTVWebApiResponseModelsContract
from swagger_client.models.save_tv_web_api_response_models_download import SaveTVWebApiResponseModelsDownload
from swagger_client.models.save_tv_web_api_response_models_erotic import SaveTVWebApiResponseModelsErotic
from swagger_client.models.save_tv_web_api_response_models_erotic_video import SaveTVWebApiResponseModelsEroticVideo
from swagger_client.models.save_tv_web_api_response_models_guard import SaveTVWebApiResponseModelsGuard
from swagger_client.models.save_tv_web_api_response_models_internet_service_provider import SaveTVWebApiResponseModelsInternetServiceProvider
from swagger_client.models.save_tv_web_api_response_models_live_streaming import SaveTVWebApiResponseModelsLiveStreaming
from swagger_client.models.save_tv_web_api_response_models_paged_record_list import SaveTVWebApiResponseModelsPagedRecordList
from swagger_client.models.save_tv_web_api_response_models_paged_star_list import SaveTVWebApiResponseModelsPagedStarList
from swagger_client.models.save_tv_web_api_response_models_paged_telecast_list import SaveTVWebApiResponseModelsPagedTelecastList
from swagger_client.models.save_tv_web_api_response_models_playlist import SaveTVWebApiResponseModelsPlaylist
from swagger_client.models.save_tv_web_api_response_models_playlist_account_state import SaveTVWebApiResponseModelsPlaylistAccountState
from swagger_client.models.save_tv_web_api_response_models_playlist_base import SaveTVWebApiResponseModelsPlaylistBase
from swagger_client.models.save_tv_web_api_response_models_playlist_count import SaveTVWebApiResponseModelsPlaylistCount
from swagger_client.models.save_tv_web_api_response_models_playlist_item import SaveTVWebApiResponseModelsPlaylistItem
from swagger_client.models.save_tv_web_api_response_models_playlist_item_operation import SaveTVWebApiResponseModelsPlaylistItemOperation
from swagger_client.models.save_tv_web_api_response_models_playlist_type import SaveTVWebApiResponseModelsPlaylistType
from swagger_client.models.save_tv_web_api_response_models_rating import SaveTVWebApiResponseModelsRating
from swagger_client.models.save_tv_web_api_response_models_record import SaveTVWebApiResponseModelsRecord
from swagger_client.models.save_tv_web_api_response_models_record_ad_cut import SaveTVWebApiResponseModelsRecordAdCut
from swagger_client.models.save_tv_web_api_response_models_record_buffer import SaveTVWebApiResponseModelsRecordBuffer
from swagger_client.models.save_tv_web_api_response_models_record_count import SaveTVWebApiResponseModelsRecordCount
from swagger_client.models.save_tv_web_api_response_models_record_defect import SaveTVWebApiResponseModelsRecordDefect
from swagger_client.models.save_tv_web_api_response_models_record_encoding import SaveTVWebApiResponseModelsRecordEncoding
from swagger_client.models.save_tv_web_api_response_models_record_format import SaveTVWebApiResponseModelsRecordFormat
from swagger_client.models.save_tv_web_api_response_models_record_group import SaveTVWebApiResponseModelsRecordGroup
from swagger_client.models.save_tv_web_api_response_models_record_operation import SaveTVWebApiResponseModelsRecordOperation
from swagger_client.models.save_tv_web_api_response_models_record_requested_format import SaveTVWebApiResponseModelsRecordRequestedFormat
from swagger_client.models.save_tv_web_api_response_models_record_segment import SaveTVWebApiResponseModelsRecordSegment
from swagger_client.models.save_tv_web_api_response_models_record_state import SaveTVWebApiResponseModelsRecordState
from swagger_client.models.save_tv_web_api_response_models_resume_positions import SaveTVWebApiResponseModelsResumePositions
from swagger_client.models.save_tv_web_api_response_models_retention_time import SaveTVWebApiResponseModelsRetentionTime
from swagger_client.models.save_tv_web_api_response_models_role import SaveTVWebApiResponseModelsRole
from swagger_client.models.save_tv_web_api_response_models_star import SaveTVWebApiResponseModelsStar
from swagger_client.models.save_tv_web_api_response_models_star_award import SaveTVWebApiResponseModelsStarAward
from swagger_client.models.save_tv_web_api_response_models_star_link import SaveTVWebApiResponseModelsStarLink
from swagger_client.models.save_tv_web_api_response_models_suggestion import SaveTVWebApiResponseModelsSuggestion
from swagger_client.models.save_tv_web_api_response_models_tag import SaveTVWebApiResponseModelsTag
from swagger_client.models.save_tv_web_api_response_models_telecast import SaveTVWebApiResponseModelsTelecast
from swagger_client.models.save_tv_web_api_response_models_time import SaveTVWebApiResponseModelsTime
from swagger_client.models.save_tv_web_api_response_models_time_block import SaveTVWebApiResponseModelsTimeBlock
from swagger_client.models.save_tv_web_api_response_models_tv_category import SaveTVWebApiResponseModelsTvCategory
from swagger_client.models.save_tv_web_api_response_models_tv_station import SaveTVWebApiResponseModelsTvStation
from swagger_client.models.save_tv_web_api_response_models_tv_station_group import SaveTVWebApiResponseModelsTvStationGroup
from swagger_client.models.save_tv_web_api_response_models_tv_station_live_stream import SaveTVWebApiResponseModelsTvStationLiveStream
from swagger_client.models.save_tv_web_api_response_models_tv_sub_category import SaveTVWebApiResponseModelsTvSubCategory
from swagger_client.models.save_tv_web_api_response_models_user import SaveTVWebApiResponseModelsUser
from swagger_client.models.save_tv_web_api_server_app_security_i_user_id_resolver import SaveTVWebApiServerAppSecurityIUserIdResolver
from swagger_client.models.system_object import SystemObject
from swagger_client.models.system_threading_cancellation_token import SystemThreadingCancellationToken
from swagger_client.models.system_threading_wait_handle import SystemThreadingWaitHandle