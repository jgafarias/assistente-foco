import flet as ft
from ui.eventos import start_timer, pause_timer, restart_timer

def interface(page: ft.Page):
    page.title = 'Assistente de foco'
    page.window.height = 500
    page.window.width = 700
    page.window.resizable = False
    page.window.alignment = ft.alignment.center
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Componentes
    pause_icon = ft.Icon(name=ft.Icons.PAUSE, size=100, color=ft.Colors.WHITE, visible=False)
    cron = ft.Text(value='00:00', size=110, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD)
    min_input = ft.TextField(label='Minutos', hint_text='Ex: 3 (3 minutos)', width=250, keyboard_type=ft.KeyboardType.NUMBER)

    start_button = ft.ElevatedButton('Iniciar', width=200, bgcolor=ft.Colors.GREEN, color=ft.Colors.BLACK)
    pause_button = ft.ElevatedButton('Pausar', width=200, bgcolor=ft.Colors.GREEN, color=ft.Colors.BLACK, icon= ft.Icons.PAUSE, visible=False)
    restart_button = ft.ElevatedButton('Reiniciar', width=200, bgcolor=ft.Colors.RED, color=ft.Colors.WHITE, visible=False)

    # Eventos (passando referências)
    start_button.on_click = lambda e: start_timer(e, page, min_input, cron, start_button, pause_button, pause_icon, restart_button)
    pause_button.on_click = lambda e: pause_timer(e, page, cron, pause_icon, start_button, pause_button, restart_button)
    restart_button.on_click = lambda e: restart_timer(e, page, min_input, cron, start_button, pause_button, restart_button, pause_icon)

    # Adiciona ao layout
    page.add(
        pause_icon,
        cron,
        min_input,
        start_button,
        pause_button,
        restart_button
    )
