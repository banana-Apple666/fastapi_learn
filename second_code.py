from fastapi import FastAPI

app = FastAPI()

# 用路径参数的形式设置路由，此时路由是个动态的，且里面的内容函数可以直接调用
@app.get("/items/{id}/{name}")
async def path_way(id : int,name):
    return {"items_id" : id,"名字" :name}

# 启动服务
import uvicorn
if __name__ == "__main__":
    uvicorn.run('second_code:app',host='127.0.0.1',port=8000,reload=True)
