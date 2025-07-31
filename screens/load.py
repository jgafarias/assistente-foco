import flet as ft

class LoadingScreen(ft.Container):
    def __init__(self):
        super().__init__()
        self.visible = False
        self.alignment = ft.alignment.center
        self.bgcolor = ft.Colors.with_opacity(0.8, ft.Colors.BLACK)

        self.content = ft.Column(
            [
                ft.ProgressRing(width=40, height=40, stroke_width=4),
                ft.Container(height=10),
                ft.Text("Carregando...", size=16, color=ft.Colors.WHITE),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )

    def show(self):
        self.visible = True

    def hide(self):
        self.visible = False