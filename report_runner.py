import uuid
import datapane
import os


REPORT_DATA_DIR = 'report_data'
REPORT_DIR = f'{REPORT_DATA_DIR}.reports'
TMP_DIR = f'./report_data/tmp'


FAIL_HTML = """
<div>
    <h1>RUN FAILED</h1>
    <p>{reason}</p>
<div>
"""


def get_report_obj(report_code):
    # if "def make_report()" not in report_code:
        # raise ValueError("Must declare get_report() function")
    print(report_code)
    exec(report_code, None, locals())
    report = locals().get('make_report')()
    return report


def run_report(report_code):
    try:
        report_obj = get_report_obj(report_code)
        html_text = report_obj.get_html('rep')
        return str(html_text)

    except BaseException as err:
        return FAIL_HTML.format(reason=str(err))


if __name__ == "__main__":
    print(run_report("12f97cef71794a0f3f2c7bd4"))

    




