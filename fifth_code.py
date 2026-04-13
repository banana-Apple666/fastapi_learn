from fastapi import FastAPI
from fastapi.responses import HTMLResponse,FileResponse

app = FastAPI()

# HTML响应类型
@app.get("/",response_class=HTMLResponse)
async def get_html():
    return "<h1>lemon出版社<h1>"

# 文件响应类型
@app.get('/')
async def get_file():
    path = "./1.jpg"
    return FileResponse(path)

# 启动服务
import uvicorn
if __name__ == "__main__":
    uvicorn.run('fifth_code:app',host='127.0.0.1',port=8000,reload=True)
