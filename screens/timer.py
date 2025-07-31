import flet as ft
import threading
import time

def cronometro_view(page: ft.Page):
    cron = ft.Text("00:00", size=150)

    min_input = ft.TextField(
        label="Minutos",
        width=150,
        border_radius=10,
        text_align=ft.TextAlign.CENTER,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    stop_button = ft.ElevatedButton(
        "Parar", 
        icon=ft.Icons.STOP,
        visible=False, 
        width=200,
        height=50,
        bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.RED),
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            overlay_color=ft.Colors.RED,
        )
    )
    start_button = ft.ElevatedButton(
        icon=ft.Icons.PLAY_ARROW,
        text="Iniciar",
        width=200,
        height=50,
        bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.GREEN),
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            overlay_color=ft.Colors.GREEN,
        )
    )

    timer_running = False
    tempo_restante = [0]  # Usando lista para mutabilidade em closures

    def countdown():
        nonlocal timer_running
        while tempo_restante[0] >= 0 and timer_running:
            minutos = tempo_restante[0] // 60
            segundos = tempo_restante[0] % 60
            cron.value = f"{minutos:02}:{segundos:02}"
            page.update()
            time.sleep(1)
            tempo_restante[0] -= 1
        start_button.visible = True
        stop_button.visible = False
        # Se acabou o tempo, volta o texto para "Iniciar"
        if tempo_restante[0] < 0:
            start_button.text = "Iniciar"
        page.update()
        timer_running = False

    def start_timer(e):
        nonlocal timer_running
        if not timer_running:
            # Se for um novo timer, volta o texto para "Iniciar"
            if tempo_restante[0] <= 0:
                try:
                    tempo_restante[0] = int(min_input.value) * 60
                except (ValueError, TypeError):
                    tempo_restante[0] = 0
                start_button.text = "Iniciar"
            timer_running = True
            start_button.visible = False
            stop_button.visible = True
            page.update()
            threading.Thread(target=countdown, daemon=True).start()

    def stop_timer(e):
        nonlocal timer_running
        timer_running = False
        start_button.text = "Continuar"  # Troca o texto para "Continuar"
        start_button.visible = True
        stop_button.visible = False
        page.update()

    start_button.on_click = start_timer
    stop_button.on_click = stop_timer

    return ft.Column(
        [
            cron,
            min_input,
            ft.Row(
                [start_button, stop_button],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )
