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


def get_report_path(report_id):
    return f'{REPORT_DIR}.{report_id}'


def import_report(report_id):
    # rep_path = get_report_path(report_id)
    module = __import__(get_report_path(report_id), fromlist=['make_report'])
    print(f'{module=}')
    return getattr(module, 'make_report')()

    # module= import_module(REPORT_DIR, f'{report_id}.py')
    # return getattr(module, 'report')
    # spec.loader.exec_module(report)
    # print(f'{rep_path=}')

    # return importName(get_report_path(report_id), 'report')


def run_report(report_id):
    # try:
    report_obj: datapane.Report = import_report(report_id)
    # print(report_obj)
    tmp_id = str(uuid.uuid4())

    tmp_html_filename = f'{TMP_DIR}/{tmp_id}.html'

    report_obj.save(tmp_html_filename)

    with open(tmp_html_filename, 'r') as f:
        html_text = f.read()

    os.remove(tmp_html_filename)
    # print(html_text)
    return str(html_text)

    # except BaseException as err:
        # return FAIL_HTML.format(reason=str(err))


if __name__ == "__main__":
    print(run_report("629e4684d1a64a4879ba233b"))




