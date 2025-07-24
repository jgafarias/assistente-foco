import flet as ft

def cronometro_view(page: ft.Page):
    
    # Exemplo simples:
    cron = ft.Text("00:00", size=120)
    
    start_button = ft.ElevatedButton(
        icon=ft.Icons.PLAY_ARROW,
        text="Iniciar",
        width=200,
        height=50,
        bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.GREEN),
        color=ft.Colors.WHITE,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            overlay_color=ft.Colors.with_opacity(0.2, ft.Colors.GREEN),  # cor no hover
        )
    )

    stop_button = ft.ElevatedButton("Parar", visible=False)

    def start_timer(e):
        # Lógica para iniciar o timer
        cron.value = "00:00"  # Exemplo de atualização
        page.update()

    start_button.on_click = start_timer

    return ft.Column(
        [
            cron,
            ft.Row(
                [start_button, stop_button],
                alignment=ft.MainAxisAlignment.CENTER  # Centraliza os botões
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )
