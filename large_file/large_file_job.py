"""
<PYATS_JOBFILE>
"""
# To run the job:
# pyats run job basic_example_job.py
# Description: This example shows the basic functionality of pyats
#              with few passing tests

import os
from pyats.easypy import run


# All run() must be inside a main function
def main(runtime):
    # Find the location of the script in relation to the job file
    test_path = os.path.dirname(os.path.abspath(__file__))
    testscript = os.path.join(test_path, 'large_file_script.py')

    one_gb = 1024 * 1024 * 300  # 1GB
    one_gb = int(one_gb)
    with open(os.path.join(runtime.directory, 'large_file'), 'wb') as fout:
        fout.write(os.urandom(one_gb))

    # Execute the testscript
    run(testscript=testscript)
