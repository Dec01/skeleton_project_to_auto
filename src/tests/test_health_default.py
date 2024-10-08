import json
import pytest

from src.models.paths.user_paths import PathsServices
from src.models.payloads.model_get_health_default import ValidateGetHealthDefault

service = PathsServices.services_paths.get('health_check')

@pytest.mark.dev
class TestGetHealthV1Req:

    def test_get_health_check(self, domain, req):
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        try:
            response = req.get_request(domain, endpoint, {}, {})
            assert response is not None
            assert response.status_code == 200
            data = response.json()
            assert ValidateGetHealthDefault.response_default(data)
        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)


@pytest.mark.dev
@pytest.mark.asyncio
class TestGetHealthV2HttpxAsync:

    async def test_get_health_check(self, domain, async_req):
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        try:
            response = await async_req.get_request(domain, endpoint, {}, {})
            assert response is not None
            assert response.status_code == 200
            data = response.json()
            assert ValidateGetHealthDefault.response_default(data)
        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)


@pytest.mark.dev
@pytest.mark.asyncio
class TestGetHealthV3MoreTestsToGodTests:

    data_get_health = None

    @pytest.mark.dependency(name="test_main")
    async def test_get_health_check(self, domain, async_req):
        endpoint = service.get('service_endpoints_path').get('general_path').get('url')
        try:
            response = await async_req.get_request(domain, endpoint, {}, {})

            assert response is not None
            assert response.status_code == 200

            data = response.json()
            self.__class__.data_get_health = data
        except json.decoder.JSONDecodeError as e:
            assert False, print("Error decoding JSON response:", e)
        except Exception as e:
            assert False, print("Request Exception:", e)


    async def test_get_health_check_validate_response(self):
        assert self.__class__.data_post_user_student_cache is not None, "Данные не должны быть None"
        assert ValidateGetHealthDefault.response_default(self.__class__.data_get_health), "Ответ не валиден"
