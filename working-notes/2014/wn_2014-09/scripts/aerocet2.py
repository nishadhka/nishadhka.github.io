import subprocess

# run your program and collect the string output
cmd = "python miniterm.py -p '/dev/ttyUSB0' -b 9600 --parity=N -D"
out_str = subprocess.check_output(cmd, shell=True)
cmd = "S"
out_str1 = subprocess.check_output(cmd, shell=True)

# See if it works.
print(out_str)
print(out_str1)
