from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.cors import CORSMiddleware
import uvicorn
import matlab
import matlab.engine
app = FastAPI()
# app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["Access-Control-Allow-Origin", "http://z4s7377775.qicp.vip", "*"],
)
@app.get("/")
async def GUI(request:Request):
    return templates.TemplateResponse(name='back_end.html', context={'request':request})
@app.get("/1/{a}/{b}/{c}/{e}")  # 设置路由
async def ditong(a: float, b: float, c: float, e: float):
    eng = matlab.engine.start_matlab()
    ret = eng.ditong(matlab.double([a]), matlab.double([b]), matlab.double([c]), matlab.double([e]))
    print('前端数据是:', a, b, c, e)
    return(a, b, c, e, ret)
@app.get("/2/{a}/{b}/{c}/{d}/{e}/{f}")
async def daizu(a: float, b: float, c: float, d: float, e: float, f: float):
    eng1 = matlab.engine.start_matlab()
    ret1 = eng1.daizu(matlab.double([a]), matlab.double([b]), matlab.double([c]), matlab.double([d]), matlab.double([e]), matlab.double([f]))
    print("前端数据是:", a, b, c, d, e, f, ret1)
    return(a, b, c, d, f, e, f, ret1)
if __name__ == "__main__":
    uvicorn.run(app, host="192.168.2.8", port=8000)