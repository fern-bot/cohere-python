# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from ...errors.too_many_requests_error import TooManyRequestsError
from ...types.compatible_endpoint import CompatibleEndpoint
from ...types.list_models_response import ListModelsResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class ModelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        page_size: typing.Optional[float] = None,
        page_token: typing.Optional[str] = None,
        endpoint: typing.Optional[CompatibleEndpoint] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListModelsResponse:
        """
        Returns a list of models available for use. The list contains models from Cohere as well as your fine-tuned models.

        Parameters:
            - page_size: typing.Optional[float]. Maximum number of models to include in a page
                                                 Defaults to `20`, min value of `1`, max value of `1000`.
            - page_token: typing.Optional[str]. Page token provided in the `next_page_token` field of a previous response.

            - endpoint: typing.Optional[CompatibleEndpoint]. When provided, filters the list of models to only those that are compatible with the specified endpoint.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from cohere.base_client import BaseCohere

        client = BaseCohere(
            client_name="YOUR_CLIENT_NAME",
            token="YOUR_TOKEN",
        )
        client.models.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "models"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                        "endpoint": endpoint.value if endpoint is not None else None,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListModelsResponse, _response.json())  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncModelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        page_size: typing.Optional[float] = None,
        page_token: typing.Optional[str] = None,
        endpoint: typing.Optional[CompatibleEndpoint] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListModelsResponse:
        """
        Returns a list of models available for use. The list contains models from Cohere as well as your fine-tuned models.

        Parameters:
            - page_size: typing.Optional[float]. Maximum number of models to include in a page
                                                 Defaults to `20`, min value of `1`, max value of `1000`.
            - page_token: typing.Optional[str]. Page token provided in the `next_page_token` field of a previous response.

            - endpoint: typing.Optional[CompatibleEndpoint]. When provided, filters the list of models to only those that are compatible with the specified endpoint.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from cohere.base_client import AsyncBaseCohere

        client = AsyncBaseCohere(
            client_name="YOUR_CLIENT_NAME",
            token="YOUR_TOKEN",
        )
        await client.models.list()
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "models"),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "page_size": page_size,
                        "page_token": page_token,
                        "endpoint": endpoint.value if endpoint is not None else None,
                        **(
                            request_options.get("additional_query_parameters", {})
                            if request_options is not None
                            else {}
                        ),
                    }
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else 60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListModelsResponse, _response.json())  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
