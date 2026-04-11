from fastapi import FastAPI,Path,Query

app = FastAPI()

# 给路径参数做类型注解
@app.get("/items/{id}/{name}")
async def path_way(name :str,id : int = Path(...,ge = 0,le = 100)):
    return {"items_id" : id,"名字" :name}

# 查询参数+类型注解
@app.get("/library/book")
async def search_book(price: int = Query(10,ge = 5,le = 225),
                      classify: int = Query(55,ge = 50,le = 100) ):
    return{"price": price,"classify" :classify}

# 启动服务
import uvicorn
if __name__ == "__main__":
    uvicorn.run('third_code:app',host='127.0.0.1',port=8000,reload=True)
