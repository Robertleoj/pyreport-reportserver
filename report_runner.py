import asyncio
import json

FAIL_HTML = """
<div>
    <h1>RUN FAILED</h1>
    <p>{reason}</p>
<div>
"""

DOCKER_CMD = 'docker run --rm -i report-runner'

async def run_report_code(report_code: bytes):

    proc = await asyncio.create_subprocess_shell(
        DOCKER_CMD,
        stdin=asyncio.subprocess.PIPE,
        stdout= asyncio.subprocess.PIPE,
        stderr= asyncio.subprocess.PIPE
    )

    # stdout, stderr = await proc.communicate(report_code.encode('utf-8'))
    stdout, stderr = await proc.communicate(report_code)
    return stdout.decode(), stderr.decode(), proc.returncode


async def run_report(report_code: str):
    stdout, stderr, returncode = await run_report_code(report_code.encode('utf-8'))
    if returncode:
        return FAIL_HTML.format(reason=stderr)
    else:
        return json.loads(stdout)


if __name__ == "__main__":
    code = """
def get_report():
    import numpy as np
    import datapane as dp
    import pandas as pd
    
    data = pd.DataFrame(np.linspace(0, 100, 100))
    
    return dp.Report(data)
    
print(get_report().get_html('a'))
    """.encode('utf-8')

    async def main(code):
        res = await run_report(code)
        print(res)

    loop = asyncio.get_event_loop()
    asyncio.ensure_future(main(code))
    loop.run_forever()
    loop.close()

    




