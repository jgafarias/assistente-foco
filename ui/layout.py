import flet as ft

def interface(page: ft.Page):
    page.title = 'Assistente de foco'
    page.window.height = 500
    page.window.width = 700
    page.window.resizable = False
    page.window.alignment = ft.alignment.center
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    page.appbar = ft.AppBar(
        bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.CYAN_200),
        leading=None,
        toolbar_height=40,
        title=ft.Row(
            controls=[
                ft.TextButton(
                    "Apps", 
                    icon=ft.Icons.APP_BLOCKING_OUTLINED, 
                    tooltip='Aplicativos Bloqueados',
                    on_click=lambda e: print("Config clicado")),
                ft.TextButton(
                    "Sobre", 
                    icon=ft.Icons.INFO_OUTLINE, 
                    tooltip='Sobre o app',
                    on_click=lambda e: print("Config clicado")),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=30,
        ),
        center_title=False,
        actions=[],
    )

    # Componentes
    pause_icon = ft.Icon(name=ft.Icons.PAUSE, size=100, color=ft.Colors.WHITE, visible=False)
    
    cron = ft.Text(value='00:00', size=115, color=ft.Colors.BLUE_200, text_align=ft.TextAlign.CENTER, weight=ft.FontWeight.BOLD)

    min_input = ft.TextField(
        label="Minutos de Foco",
        width=170,
        text_align=ft.TextAlign.CENTER,
        keyboard_type=ft.KeyboardType.NUMBER,
        border_radius=10,
        color=ft.Colors.BLUE_200,
        border_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
        bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.CYAN_ACCENT_700),
    )

    start_button = ft.ElevatedButton(
        'Iniciar',
        bgcolor=ft.Colors.CYAN,
        width=100,
        height=40,
        color=ft.Colors.BLACK,
        icon=ft.Icons.ACCESS_TIME,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10)
        )
    )

    pause_button = ft.ElevatedButton(
        'Pausar',
        width=200,
        height=45,
        bgcolor=ft.Colors.GREEN,
        color=ft.Colors.BLACK,
        icon=ft.Icons.PAUSE,
        visible=False
    )

    restart_button = ft.ElevatedButton(
        'Reiniciar',
        width=200,
        height=45,
        bgcolor=ft.Colors.RED,
        color=ft.Colors.WHITE,
        icon=ft.Icons.REFRESH,
        visible=False
    )

    # Layout com espaçamentos
    page.add(
        ft.Column(
            controls=[
                pause_icon,
                cron,
                min_input,
                ft.Container(height=10),
                start_button,
                pause_button,
                ft.Container(height=20),
                restart_button,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
