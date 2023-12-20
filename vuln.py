import sys
import subprocess

print(
    subprocess.check_output(
        sys.argv[1:],
        shell=True
    )
)
