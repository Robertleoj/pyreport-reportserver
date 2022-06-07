from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from report_runner import run_report


class ReportReq(BaseModel):
    report_code: str

app = FastAPI()

class ReportResponse(BaseModel):
    html: str

@app.post('/run_report', response_class=JSONResponse)
async def report_getter(param: ReportReq):
    report_code = param.report_code
    html_text = run_report(report_code)
    # print("================= HTML TEXT ===================")
    # print(html_text)
    # print("================= HTML TEXT ===================")
    res = ReportResponse(html=html_text)
    return JSONResponse(content=jsonable_encoder(res))