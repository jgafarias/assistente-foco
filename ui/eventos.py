import time
import threading
from state.controle import tempo_restante, stop_event

def temporizador(segundos, page, cron, pause_button, restart_button, restart_func):
    tempo_restante[0] = segundos
    while tempo_restante[0] > 0 and not stop_event.is_set():
        mins = tempo_restante[0] // 60
        secs = tempo_restante[0] % 60
        cron.value = f'{mins:02d}:{secs:02d}'
        page.update()
        time.sleep(1)
        tempo_restante[0] -= 1
    if not stop_event.is_set() and tempo_restante[0] == 0:
        cron.value = '00:00'
        # cron.size = 50
        restart_button.visible = True
        pause_button.visible = False
        page.update()

def start_timer(e, page, min_input, cron, start_button, pause_button, pause_icon, restart_button):
    stop_event.clear()
    pause_icon.visible = False
    cron.visible = True
    try:
        if tempo_restante[0] == 0:
            minutos = int(min_input.value)
            tempo_restante[0] = minutos * 60
        thread = threading.Thread(target=temporizador, args=(tempo_restante[0], page, cron, pause_button, restart_button, lambda e: restart_timer(e, page, min_input, cron, start_button, pause_button, restart_button, pause_icon)), daemon=True)
        min_input.visible = False
        start_button.visible = False
        pause_button.visible = True
        restart_button.visible = False
        thread.start()
    except:
        cron.value = "Digite um número válido!"
        page.update()

def pause_timer(e, page, cron, pause_icon, start_button, pause_button, restart_button):
    stop_event.set()
    cron.visible = False
    pause_icon.visible = True
    start_button.text = 'Continuar'
    start_button.visible = True
    pause_button.visible = False
    restart_button.visible = True
    page.update()

def restart_timer(e, page, min_input, cron, start_button, pause_button, restart_button, pause_icon):
    stop_event.set()
    tempo_restante[0] = 0
    min_input.value = ""
    cron.value = "00:00"
    start_button.text = "Iniciar"
    start_button.visible = True
    pause_button.visible = False
    restart_button.visible = False
    min_input.visible = True
    pause_icon.visible = False
    cron.visible = True
    page.update()
