# 1. 导入 FastAPI 类
from fastapi import FastAPI

# 2. 创建应用实例
app = FastAPI()

# 生成一个装饰器，使app变成网页接口
@app.get("/")
# 加了get后，read_root函数将变成网页函数
def read_root():
    return {"message": "我的第一个FastAPI项目成功啦！"}

# 启动服务
# 1、通过命令：uvicorn filename:app_name --reload
# 2、通过调试：fastapi dev first_code
# 3、通过py文件：python filename。py（但是需要在代码中补充这几行代码）

# py文件运行项目的代码，host显示的是绑定的主机地址，port显示的是服务端端口，reload表示热加载
import uvicorn
# 这是手动运行服务，避免自动打开，只有当运行这个项目时才能别运行
if __name__ == "__main__":
    uvicorn.run('first_code:app',host='127.0.0.1',port=8000,reload=True)