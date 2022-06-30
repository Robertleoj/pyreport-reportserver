

import sys
from io import StringIO
import traceback
from datapane import Report
import json
from base64 import b64encode
import mimetypes
from pathlib import Path

_double_ext_map = {
    ".vl.json": "application/vnd.vegalite.v4+json",
    ".vl2.json": "application/vnd.vegalite.v2+json",
    ".vl3.json": "application/vnd.vegalite.v3+json",
    ".vl4.json": "application/vnd.vegalite.v4+json",
    ".bokeh.json": "application/vnd.bokeh.show+json",
    ".pl.json": "application/vnd.plotly.v1+json",
    ".fl.html": "application/vnd.folium+html",
    ".tbl.html": "application/vnd.datapane.table+html",
    ".tar.gz": "application/x-tgz",
}

double_ext_map = {k: str(v) for k, v in _double_ext_map.items()}



def guess_type(filename: Path):
    ext = "".join(filename.suffixes)
    if ext in double_ext_map.keys():
        return double_ext_map[ext]
    mtype: str
    mtype, _ = mimetypes.guess_type(str(filename))
    return str(mtype or "application/octet-stream")


input_file = sys.stdin.read()

old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()

err = None

report_doc, attachments =None, None

report = None


try:
    loc = {}

    exec(input_file, None, loc)

    make_report = loc['make_report']

    report = make_report()
    assert isinstance(report, Report)

    report_doc, attachments = report.get_report()

except Exception as e:
    err = traceback.format_exc()

sys.stdout = old_stdout

# print("After running all")

stdout = mystdout.getvalue()

att_items = []

if(attachments):
    for i, a in enumerate(attachments):
        # print(f'================= ATTACHMENT {i} ==============')
        # print(a)
        # print(f'{guess_type(a)=}')
        with open(a, 'rb') as f:
            mimetype = guess_type(a)
            content = b64encode(f.read()).decode('utf-8')
            att_items.append({
                'mimetype': mimetype,
                'file': content
            })

        # print('===================================')

ret_obj = {
    'stdout': stdout,
    'err': err,
    'report_doc': report_doc,
    'attachments': att_items
}


# print(report_doc)
# print(err)
# print(report_doc)

# print(type(stdout))
# print(type(err))
# print(type(report_doc))


print(json.dumps(ret_obj))

# sys.stdout.
