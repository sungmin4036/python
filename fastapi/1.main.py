from enum import Enum # python 3.4 이후 사용가능, 경로 매개변수를 받는 경로동작이 있지만, 유효하고 미리 정의할수 있는 경로 매개변수값을 원할시 사용
from fastapi import FastAPI # FastAPI는 API에 대한 모든 기능을 제공하는 파이썬 클래스입니다.
from typing import Optional

# Starlette를 직접 상속하는 클래스입니다.

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI() #app 변수는 FastAPI 클래스의 "인스턴스"가 됩니다
#uvicorn main:app --reload 개발서버 실행 <<-- 변수이름이 abc면 abc넣으면됨

# "경로"는 첫 번째 /에서 시작하는 URL의 마지막 부분을 나타냅니다. "경로"는 일반적으로 "앤드포인트" 또는 "라우트"라고도 불립니다.

# http 메소드==동작
# POST: 데이터를 생성하기 위해.
# GET: 데이터를 읽기 위해.
# PUT: 데이터를 업데이트하기 위해.
# DELETE: 데이터를 삭제하기 위해.

# @something 문법은 파이썬에서 "데코레이터"라 부릅니다.  데코레이터는 FastAPI에게 아래 함수가 경로 /에 해당하는 get 동작하라고 알려줍니다. 이것이 "경로 동작 데코레이터"입니다.


# 여러 경로/쿼리 매개변수
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
#FastAPI는 item_id가 경로 매개변수이고 q는 경로 매개변수가 아닌 쿼리 매개변수

# 필수 쿼리 매개변수
# @app.get("/items/{item_id}")
# async def read_user_item(item_id: str, needy: str):
#     item = {"item_id": item_id, "needy": needy}
#     return item   
# http://127.0.0.1:8000/items/foo-item할시 오류 발생
#  => http://127.0.0.1:8000/items/foo-item?needy=sooooneedy 해야 정상작동


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

@app.get("/files/{file_path:path}") # 경로 변환기 매개변수의 이름은 file_path이고 마지막 부분 :path는 매개변수가 경로와 일치해야함을 알려줍니다.
async def read_file(file_path: str):
    return {"file_path": file_path}

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}") # fastapi에게 바로 아래에 있는 함수가 다음으로 이동하는 요청을 처리하는것을 알려줌
async def read_item(item_id: int): #즉, 파이썬 타입 선언을 하면 FastAPI는 데이터 검증을 합니다. 오류는 검증을 통과하지 못한 지점도 정확하게 명시합니다. 이는 API와 상호 작용하는 코드를 개발하고 디버깅하는 데 매우 유용합니다.
    return {"item_id": item_id} 

# "asynchronous" because the computer / program doesn't have to be "synchronized" with the slow task, waiting for the exact moment that the task finishes, while doing nothing, to be able to take the task result and continue the work.
# Instead of that, by being an "asynchronous" system, once finished, the task can wait in line a little bit (some microseconds) for the computer / program to finish whatever it went to do, and then come back to take the results and continue working with them.
# For "synchronous" (contrary to "asynchronous") they commonly also use the term "sequential", because the computer / program follows all the steps in sequence before switching to a different task, even if those steps involve waiting.