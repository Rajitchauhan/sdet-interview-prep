import pytest
import task_manager as tm

@pytest.mark.smoke
def test_valid_title():
    result = tm.add_task("SDET")
    assert 'id' in result
    assert result['title'] == 'SDET'
    assert result['completed'] is False

@pytest.mark.smoke
@pytest.mark.regression
def test_empty_title():
    with pytest.raises(ValueError) as exc:
        tm.add_task("")

    assert "Task title is required" in str(exc.value)

# @pytest.fixture
# def task():
#     return   {
#             "id": 1,
#             "title": "SDET",
#             "completed": False
#         }

@pytest.mark.smoke
@pytest.mark.regression
def test_complete_task(task):  
    rs = tm.complete_task(task)

    assert rs['completed'] is True 

@pytest.mark.smoke
@pytest.mark.regression
def test_is_task_completed(task):
    task['completed'] = True
    
    assert tm.is_task_completed(task) is True


def test_is_false_task_completed(task):
    
    assert tm.is_task_completed(task) is False

@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("title" , [("SDET"),
("Pytest") , ("Automation"),("Playwright")])
def test_title(title):
    result = tm.add_task(title)
    assert result['title'] == title 


@pytest.mark.regression
@pytest.mark.parametrize("title" , ["" , None  , False])
def test_falsy_title(title):
    with pytest.raises(ValueError , match="Task title is required"):
        tm.add_task(title)


@pytest.mark.regression
@pytest.mark.parametrize(
    "title",
    ["SDET", "Pytest", "Automation", "Playwright"]
)
def test_title_with_fixture(task, title):

    task["title"] = title

    result = tm.is_task_completed(task)

    assert result is False
    assert task["title"] == title 


@pytest.fixture(scope='module')
def database():
    print("DATABASE CONNECTED")

    db = {
        "connected": True,
        "tasks": []
    }

    yield db

    print("DATABASE CLOSED")


@pytest.mark.smoke
@pytest.mark.regression
def test_db(database):
    assert database['connected'] is True
    database["tasks"].append("SDET")


@pytest.mark.regression
def test_add_db(database):
    # database['tasks'].append('SDET')

    assert 'SDET' in database['tasks']


@pytest.mark.smoke
def test_task_fixture_is_available(task):
    assert task["id"] == 1
    assert task["title"] == "SDET"
    assert task["completed"] is False

import requests

def test_get_posts(api_base_url):
    res = requests.get(api_base_url)

    assert res.status_code == 200

    # data = res.json()

    # print(data)



