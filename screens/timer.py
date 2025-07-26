import flet as ft

def cronometro_view(page: ft.Page):
    
    # Exemplo simples:
    cron = ft.Text("00:00", size=150)
    
    start_button = ft.ElevatedButton(
        icon=ft.Icons.PLAY_ARROW,
        text="Iniciar",
        width=200,
        height=50,
        on_click=lambda e: start_timer(minutos=min_input.value),
        bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.GREEN),
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            overlay_color=ft.Colors.GREEN,
        )
    )
    
    min_input = ft.TextField(
        label="Minutos",
        width=150,
        border_radius=10,
        text_align=ft.TextAlign.CENTER,
        keyboard_type=ft.KeyboardType.NUMBER
    )

    stop_button = ft.ElevatedButton("Parar", visible=False)

    def start_timer(minutos):
        minutos = segundos * 60
        segundos = minutos % 60
        minutos = minutos // 60
        cron.value = f"{minutos:02}:{segundos:02}"
        cron.update()
        start_button.visible = False
        stop_button.visible = True
        # stop_button.on_click = lambda e: stop_timer(e)
        
        

    start_button.on_click = start_timer

    return ft.Column(
        [
            cron,
            min_input,
            ft.Row(
                [start_button, stop_button],
                alignment=ft.MainAxisAlignment.CENTER  # Centraliza os botões
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )
