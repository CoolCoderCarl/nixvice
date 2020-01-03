import time
import logServ
import systemd.daemon


if __name__ == '__main__':

    # print msg into unit status stream
    print('Starting up ...')
    # log init
    logServ.log_init()
    time.sleep(5)
    print('Startup complete')
    # notify systemd
    systemd.daemon.notify('READY=1')

    while True:
        logServ.make_logs()
        time.sleep(30)