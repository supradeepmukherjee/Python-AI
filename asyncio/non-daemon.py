import threading,time

def monitorTemperature():
    while True:
        print('Temp: ')
        time.sleep(2)

threading.Thread(target=monitorTemperature
                #  ,daemon=False
                 ).start()

print('Main program done')