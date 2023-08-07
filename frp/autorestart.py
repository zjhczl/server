import subprocess
import time
# 检测进程是否正在运行


def is_process_running(process_name):
    try:
        # 执行pgrep命令
        subprocess.check_output(['pgrep', process_name])
        return True
    except subprocess.CalledProcessError:
        return False


def start_process(process_name, command):
    subprocess.Popen(command, shell=True)


while True:
    if not is_process_running("frpc"):
        print("start")
        start_process(
            "my_program", "~/server/frp/frpc -c ~/server/frp/frpc.ini")

    print("sleep...")
    time.sleep(10)
