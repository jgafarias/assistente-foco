import flet as ft
from screens.sobre import sobre_view
from screens.timer import cronometro_view

def main(page: ft.Page):
    page.title = "Assistente de Foco"
    page.window.width = 700
    page.window.height = 600
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK
    page.window.resizable = False

    # Menu inferior (criado uma única vez)
    menu = ft.BottomAppBar(
        ft.Row(
            [
                ft.IconButton(
                    icon=ft.Icons.HOURGLASS_BOTTOM_ROUNDED,
                    tooltip="Início",
                    on_click=lambda e: page.go("/"),
                ),
                ft.IconButton(
                    icon=ft.Icons.APP_BLOCKING_ROUNDED,
                    tooltip="Apps Bloqueados",
                    on_click=lambda e: print("Navegando para Apps Bloqueados"),
                ),
                ft.IconButton(
                    icon=ft.Icons.INFO_OUTLINE_ROUNDED,
                    tooltip="Sobre o app",
                    on_click=lambda e: page.go("/sobre"),
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
    )

    def route_change(e):
        page.controls.clear()

        if page.route == "/sobre":
            page.title = "Sobre o Assistente de Foco"
            page.controls.append(sobre_view(page))
        else:
            page.title = "Assistente de Foco"
            page.controls.append(cronometro_view(page))

        # Adiciona o menu sempre ao final
        page.controls.append(menu)
        page.update()

    page.on_route_change = route_change
    route_change(None)  # Inicialização

ft.app(target=main)
