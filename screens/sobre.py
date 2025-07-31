import flet as ft

def sobre_view(page: ft.Page):

    page.assets_dir = "assets"
    
    return ft.Column(
        [
            ft.Text("Assistente de Foco", style=ft.TextStyle(size=18, weight=ft.FontWeight.BOLD)),
            ft.Text("Versão: 1.0.0", style=ft.TextStyle(size=15)),
            ft.Text("Este aplicativo ajuda você a manter o foco bloqueando aplicativos distrativos.", style=ft.TextStyle(size=12)),
            ft.Divider(),
            ft.Text("Desenvolvido por Joao Gabriel", style=ft.TextStyle(size=11), italic=True),
            ft.Divider(tooltip='Contato'),
            ft.ElevatedButton(
                width=137,
                content=ft.Row(
                    [
                        ft.Image(src="linkedin.png", width=20, height=20),
                        ft.Text("Meu LinkedIn"),
                    ],
                    spacing=10,
                ),
                on_click=lambda e: page.launch_url("https://www.linkedin.com/in/jgafarias/"),
                color=ft.Colors.WHITE,
                bgcolor=ft.Colors.BLUE_700,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )