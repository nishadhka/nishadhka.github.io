import subprocess

# run your program and collect the string output
#cmd = ["-p '/dev/ttyUSB0' -b 9600 --parity=N -D"]
p1 = subprocess.Popen(['python', 'miniterm.py', '-p','/dev/ttyUSB0', '-b','9600','--parity=N', '-D', 'S'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
#p1 = subprocess.Popen(['python', 'miniterm.py', '-p','/dev/ttyUSB0', '-b','9600','--parity=N', '-D'], stdin=PIPE,stdout=PIPE)
#p1.stdin.write("S\n")
#out_str = subprocess.check_output(cmd, shell=True)
#cmd = "S"
#out_str1 = subprocess.check_output(cmd, shell=True)
#p1.stdin.flush()
# See if it works.
#print(process)
#print(out_str1)
#while p1.poll() is None:
#    l = p1.stdout.readline()
#    print l
#p1.stdin.write('S')
#p1.stdin.flush()
#p2 = subprocess.Popen(['S'], stdin=p1.stdout) #send p1's output to p2
#p1.communicate('S\n')
#p1.stdout.close()
#print p2.stdout.read()
#p1.stdin.write('a line\n')
