import subprocess

def adbml(cmd):
    connect = subprocess.Popen(str(cmd),stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    stdout,stderr = connect.communicate()
    stdout=stdout.decode("utf-8")
    stderr=stderr.decode("utf-8")
    print stdout
    print stderr

if __name__ == '__main__':
    cmd1 = r"adb shell screencap -p /sdcard/demo.png"
    cmd2 = r"adb pull /sdcard/demo.png tmp/demo.png"
    adbml(cmd1)
    adbml(cmd2)