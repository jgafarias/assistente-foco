import flet as ft
import asyncio
# Paginas
from screens.cronometro import cronometro_view
from screens.sobre import sobre_view
from screens.apps import apps_view
# loading view
from screens.load import LoadingScreen

def main(page: ft.Page):
    # Dados da página inicial
    page.title = "Assistente Foco"
    page.window.width = 800
    page.window.resizable = False
    page.window.center()
    page.theme_mode = ft.ThemeMode.DARK
    page.padding = 0

    # Controles principais da aplicação
    loading_screen = LoadingScreen()
    
    # Instanciamos as views uma única vez
    cronometro_page = cronometro_view(page)
    sobre_page = sobre_view(page)
    apps_page = apps_view(page)

    # Layout com Stack para sobrepor o loading e as views
    main_stack = ft.Stack(
        [
            cronometro_page,
            sobre_page,
            apps_page,
            loading_screen,
        ],
        expand=True
    )
    
    # Todos os controles são invisíveis no início, exceto o cronometro_page
    cronometro_page.visible = True
    sobre_page.visible = False
    apps_page.visible = False
    loading_screen.visible = False

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
        
    async def route_change(e):
        # Esconde todas as páginas e o loading para começar
        cronometro_page.visible = False
        sobre_page.visible = False
        apps_page.visible = False
        loading_screen.visible = False

        if page.route == "/apps":
            page.title = "Gerenciar Apps Bloqueados"
            # 1. Exibe o loading
            loading_screen.show()
            page.update()
            
            await asyncio.sleep(2) # Substitua por sua função assíncrona real

            # 3. Esconde o loading e mostra a página
            loading_screen.hide()
            apps_page.visible = True
            page.update()
            
        elif page.route == "/sobre":
            page.title = "Sobre o Assistente de Foco"
            sobre_page.visible = True
            page.update()
            
        else: # Rota "/"
            page.title = "Assistente de Foco"
            cronometro_page.visible = True
            page.update()

        # Atualiza o menu e a página
        page.bottom_appbar = build_menu()
        page.update()

    page.add(main_stack, build_menu())
    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)