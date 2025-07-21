import threading

stop_event = threading.Event()
tempo_restante = [0]  # lista para permitir mutabilidade entre arquivos
