import pytest , requests


@pytest.mark.smoke
def test_get_all_posts(api_base_url):
    get_res = requests.get(f"{api_base_url}/posts")

    assert get_res.status_code == 200 , "success ok!"

    data = get_res.json()
 
    assert len(data) > 0  , "nust be len greater then 0"


@pytest.mark.smoke
@pytest.mark.regression
def test_create_post(api_base_url, sample_payload):
    post_res = requests.post(f"{api_base_url}/posts" , json=sample_payload)

    assert post_res.status_code == 201 , "post created"

    data = post_res.json()

    assert "id" in data 

    assert data['title'] == sample_payload["title"] , "kya match hua"


@pytest.mark.regression
def test_invalid_endpoint_404(api_base_url):
    res = requests.get(f"{api_base_url}/non_existing_route_123")

    assert res.status_code == 404 , "page not found"
