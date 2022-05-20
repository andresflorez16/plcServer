from firebaseAdmin import pushData
import sched
import time

def task(taskTime, msg):
    delay = sched.scheduler(time.time, time.sleep)
    delay.enterabs(taskTime, 1, print, argument=(msg))
    print('leyendo')
    pushData('/Users', { 'name': 'zapato' })
    delay.run()

while True:
    task(time.time() + 1, 'Ejecutando')

