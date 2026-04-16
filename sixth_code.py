from fastapi import FastAPI,HTTPException
from pydantic import BaseModel

app = FastAPI()

#用类去实现自定义,新闻接口：id，title，content
class News(BaseModel):
    id: int
    title: str
    content: str
    
# 自定义响应类型
@app.get("/items/{id}",response_model=News)
async def get_news(id : int):
    return {
        "id":id,
        "title":f"这是第{id}本书",
        "content":'这是一本好书'
    }

# 异常响应处理
# 接口：当id为1~6时正常输出
@app.get('/news/{id}')
async def get_news(id:int):
    id_list = [1,2,3,4,5,6]
    if id not in id_list:
        raise HTTPException(status_code=404,detail='所找的资源不存在')
    return {
        "id":id
    }

# 启动服务
import uvicorn
if __name__ == "__main__":
    uvicorn.run('sixth_code:app',host='127.0.0.1',port=8000,reload=True)
