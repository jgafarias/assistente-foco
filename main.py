import flet as ft
# Paginas
from screens.cronometro import cronometro_view
from screens.sobre import sobre_view
from screens.apps import apps_view
# Load
from screens.load import show_loading_then

def main(page: ft.Page):
    # Dados da página inicial
    page.title = "Assistente Foco"
    page.window.width = 800
    page.window.resizable = False
    page.window.center()
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    
    # Definir o tema da página
    page.theme_mode = ft.ThemeMode.DARK

    # Função para construir o menu com destaque no selecionado
    def build_menu():
        return ft.BottomAppBar(
            ft.Row(
                [
                    ft.IconButton(
                        icon=ft.Icons.HOURGLASS_BOTTOM_ROUNDED,
                        tooltip="Início",
                        on_click=lambda e: page.go("/"),
                        icon_color=ft.Colors.BLUE_400 if page.route == "/" else ft.Colors.WHITE,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.APP_BLOCKING_ROUNDED,
                        tooltip="Apps Bloqueados",
                        on_click=lambda e: page.go("/apps"),
                        icon_color=ft.Colors.BLUE_400 if page.route == "/apps" else ft.Colors.WHITE,
                    ),
                    ft.IconButton(
                        icon=ft.Icons.INFO_OUTLINE_ROUNDED,
                        tooltip="Sobre o app",
                        on_click=lambda e: page.go("/sobre"),
                        icon_color=ft.Colors.BLUE_400 if page.route == "/sobre" else ft.Colors.WHITE,
                    ),
                ],
                alignment=ft.MainAxisAlignment.SPACE_EVENLY,
            )
        )

    def route_change(e):
        page.controls.clear()
        menu = build_menu()  # Atualiza as cores do menu conforme a rota

        if page.route == "/sobre":
            page.title = "Sobre o Assistente de Foco"
            page.controls.append(sobre_view(page))
            page.controls.append(menu)
        elif page.route == "/apps":
            page.title = "Gerenciar Apps Bloqueados"
            show_loading_then(page, apps_view, menu)
        else:
            page.title = "Assistente de Foco"
            page.controls.append(cronometro_view(page))
            page.controls.append(menu)


        page.controls.append(ft.Container(height=10))
        page.update()

    page.on_route_change = route_change
    route_change(None)  # Inicialização

ft.app(target=main)