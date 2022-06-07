import codejail.jail_code
codejail.jail_code.configure('python', '/home/king_rob/Desktop/Projects/PythonReporting/pyreport-reportserver/reportvenv-sandbox/bin/python', 'sandbox')
import codejail.safe_exec

codejail.safe_exec.safe_exec("1 + 1", {})
# codejail.safe_exec.safe_exec("import os\nos.system('ls /etc')", {})

