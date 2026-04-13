from fastapi import FastAPI,Path,Query
from pydantic import BaseModel,Field

app = FastAPI()

# 请求体，定义
# 新增资源：书名，出版社，售价，作者
class Book(BaseModel):
  book:str = Field(...,min_length=2,max_length=20)
  writer:str = Field(min_length=2,max_length=10)
  publisher:str = Field(default="lemon出版社")
  price:int = Field(...,gt=0)

# 请求体，类型注解
@app.post("/add")
async def add(book:Book,writer:Book,publisher:Book,price:Book):
  return book

# 查询参数+类型注解
@app.get("/library/book")
async def search_book(price: int = Query(10,ge = 5,le = 225),
                      classify: int = Query(55,ge = 50,le = 100) ):
    return{"price": price,"classify" :classify}

# 启动服务
import uvicorn
if __name__ == "__main__":
    uvicorn.run('fourth_code:app',host='127.0.0.1',port=8000,reload=True)
