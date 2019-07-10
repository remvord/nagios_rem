import sh


for num in range(1, 250):
    ip = "172.30.2." + str(num)

    try:
        sh.ping(ip, "-c 1", _out="/dev/null")
        # print(sh.ls("-l", "/tmp", color="never"))
        print("PING ", ip, "OK")

    except sh.ErrorReturnCode_1:
        print("PING ", ip, "FAILED")