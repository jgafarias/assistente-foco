import flet as ft
import time
import threading

def show_loading_then(page, next_view_fn, menu, *args, **kwargs):
    def worker():
        # Cria o loading
        load = ft.ProgressRing(
            value=0.0,
            stroke_width=7,
            color=ft.Colors.BLUE_300,
            scale=2,
            bgcolor=ft.Colors.with_opacity(0.1, ft.Colors.BLACK)
        )
        load_text = ft.Text(
            "Carregando aplicativos...",
            color=ft.Colors.WHITE,
            size=20
        )
        loading_col = ft.Column(
            controls=[
                load,
                ft.Container(height=20),
                load_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )

        page.controls.clear()
        page.add(loading_col)
        page.controls.append(ft.Container(height=10))
        page.controls.append(menu)
        page.update()

        # Simula carregamento
        for i in range(101):
            time.sleep(0.01)
            load.value = i / 100.0
            page.update()

        # Troca para a próxima tela
        page.controls.clear()
        next_view = next_view_fn(page, *args, **kwargs)
        if next_view is not None:
            page.add(next_view)
        page.controls.append(ft.Container(height=10))
        page.controls.append(menu)
        page.update()
    threading.Thread(target=worker, daemon=True).start()