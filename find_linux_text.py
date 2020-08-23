import paramiko, getpass


class DoSomeThing(object):
    def __init__(self, host, port, name, passwd):
        self._host_ip = host
        self._host_port = port
        self._name = name
        self._passwd = passwd
        self._client = paramiko.SSHClient()

    def conn(self):
        self._client.set_missing_host_key_policy(
            paramiko.AutoAddPolicy())  # 指定当对方主机没有本机公钥的情况时应该怎么办，AutoAddPolicy表示自动在对方主机保存下本机的秘钥
        self._client.connect(self._host_ip, self._host_port, self._name, self._passwd)

    def close(self):
        self._client.close()

    def cmd_exec(self):
        cmd = "cat /home/ginny/foundme | grep \"di\""  # linux
        # cmd = "reg query HKEY_CURRENT_USER\AppEvents\Schemes\Apps\sapisvr /v DispFileName"  # windows
        # cmd = "xxx /home/ginny/foundme | grep \"di\""  命令错误示范，结果走标准错误
        stdin, stdout, stderr = self._client.exec_command(cmd)
        r = stdout.readlines()
        print(r)  # 列表
        if len(r) > 0:
            print(r[0].strip())  # 去除字符串前后的空格
        print(stderr.readlines())


if __name__ == '__main__':
    inst = DoSomeThing("192.168.1.105", "22", "ginny", "1992")
    try:
        inst.conn()
        inst.cmd_exec()
    except Exception as e:
        print(e)
    finally:
        inst.close()

