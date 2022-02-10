#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
                                                    __----~~~~~~~~~~~------___
                                   .  .   ~~//====......          __--~ ~~
                   -.            \_|//     |||\\  ~~~~~~::::... /~
               ___-==_       _-~o~  \/    |||  \\            _/~~-
        __---~~~.==~||\=_    -_--~/_-~|-   |\\   \\        _/~
    _-~~     .=~    |  \\-_    '-~7  /-   /  ||    \      /
  .~       .~       |   \\ -_    /  /-   /   ||      \   /
 /  ____  /         |     \\ ~-_/  /|- _/   .||       \ /
 |~~    ~~|--~~~~--_ \     ~==-/   | \~--===~~        .\
          '         ~-|      /|    |-~\~~       __--~~
                      |-~~-_/ |    |   ~\_   _-~            /\
                           /  \     \__   \/~                \__
                       _--~ _/ | .-~~____--~-/                  ~~==.
                      ((->/~   '.|||' -_|    ~~-/ ,              . _||
                                 -_     ~\      ~~---l__i__i__i--~~_/
                                 _-~-__   ~)  \--______________--~~
                               //.-~~~-~_--~- |-------~~~~~~~~
                                      //.-~~~--\
                               神兽保佑
                              代码无BUG!

"""
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

import matlab
import matlab.engine
import uvicorn

app_filter = FastAPI()

# from pathlib import Path
# BASE_DIR = Path(__file__).resolve().parent
# templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'eryuan/templates')))

# app_filter.mount('/static', StaticFiles(directory='templates'), name='static')  # mount挂载 第一个参数为应用的前缀，第二个为路径，第三个为别名

templates = Jinja2Templates(directory="templates")


# 后台api允许跨域
app_filter.add_middleware(
    CORSMiddleware,
    allow_headers=["Access-Control-Allow-Origin","*"], # 这里最好明确的写允许的域名
    # allow_origins=["http://127.0.0.1","http://127.0.0.1/5000"],
    allow_origins=[" http://k55ymk.natappfree.cc"," http://k55ymk.natappfree.cc:80","192.168.3.7","192.168.3.7:5000","*"],
    allow_credentials=True,
    allow_methods=["*"],
)


# @app_filter.get("/") 
# async def index(request:Request):
#     # 返回一个模板对象，同时使用上下文中的数据对模板进行渲染
#     return templates.TemplateResponse(name="filter.html",context={"request": request})


@app_filter.get("/highpasshanning/{b}/{c}")  
async def highpasshanning(b: float, c: float):
    eng = matlab.engine.start_matlab()
    eng.cd('tinydemo',nargout=0)
    ret = eng.HighpassHanning(matlab.double([b]),matlab.double([c]))
    print("前端数据是:", b, c, ret)
    return ret

if __name__ == "__main__":
    uvicorn.run(app_filter, host="192.168.3.7", port=5000)
