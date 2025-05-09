import flet as ft
from pantallas.interfaz_usuarios import CrudUsuarios
from pantallas.interfaz_empleados import CrudEmpleados
from pantallas.interfaz_articulos import CrudArticulos
from pantallas.interfaz_eventos import CrudEventos

#Botones para la barra de navegacion
class BotonNavegacion(ft.IconButton):
    def __init__(self, icon, tooltip, shape, bgcolor, side, on_click=None, selected=False):
        super().__init__(
            icon=icon,
            icon_size=30,
            tooltip=tooltip,
            icon_color="white",
            style=ft.ButtonStyle(
                shape=shape,
                padding=10,
                bgcolor=bgcolor if not selected else "#7289da",
                overlay_color="#7289da",
                side=side
            ),
            on_click=self.on_click_handler
        )
        self.on_click_callback = on_click
        self.selected = selected

    def on_click_handler(self, e):
        if self.on_click_callback:
            self.on_click_callback(e)

    def select(self):
        self.selected = True
        self.style.bgcolor = "#7289da"
        self.update()

    def deselect(self):
        self.selected = False
        self.style.bgcolor = self.style.bgcolor if self.style.bgcolor != "#7289da" else "#2f3136" # Mantener el bg original si no es el seleccionado
        self.update()

#Pantalla de inicio
def pantalla_inicio():
    return ft.Row([
        ft.Container(
            bgcolor="#2f3136",
            border_radius=ft.border_radius.all(8),
            padding=20,
            margin=ft.Margin(left=0, right=0, top=10, bottom=10),
            width=350,
            content = ft.Column(
                controls=[
                    ft.Image(
                        src = "assets/frifayer.jpg",
                        expand=True,
                        #width=350,
                        fit=ft.ImageFit.CONTAIN,
                    ),
                    ft.Image(
                        src = "assets/gato.jpeg",
                        expand=True,
                        #width=350,
                        fit=ft.ImageFit.CONTAIN,
                    )
                ]
            )
        ),

        ft.Container(
            ft.Column(
                controls=[
                    ft.Container(
                        ft.Image(
                            src="assets/diamante.png",
                            height=50
                        ),
                    ),
                    ft.Text(
                        "Diamantes pal Free",
                        size=50,
                        text_align="center",
                        font_family="28 Days Later",
                    ),
                    ft.Text(
                        "Bienvenido al POS de la BD Diamantes pal Free. \nPara manejar los CRUDS, seleccione una de las opciones de la izquierda.",
                        size=10,
                        text_align="center",
                        font_family="Minecraft",
                    )
                ],
                spacing=0,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            expand=True,
            bgcolor="#2f3136",
            border_radius=ft.border_radius.all(8),
            padding=20,
            margin=ft.Margin(left=5, right=10, top=10, bottom=10),
        )
    ], expand=True, spacing=0)

def main(page:ft.Page):
    page.title = "POS Casa de Apuestas"
    page.bgcolor = '#1c1c1d'
    page.window_min_width = 100
    page.window_min_height = 500

    cont_principal = ft.Column(expand=True)
    botones_cruds = []

    def cambiar_pantalla(pantalla_func, boton_seleccionado):
        cont_principal.controls.clear()
        if isinstance(pantalla_func, ft.Control):
            pantalla_func.expand = True
            cont_principal.controls.append(pantalla_func)
        elif hasattr(pantalla_func, '__call__'):
            control = pantalla_func()
            control.expand = True
            cont_principal.controls.append(control)
        page.update()

        # Deseleccionar todos los botones y seleccionar el actual
        for boton in botones_cruds:
            if isinstance(boton, BotonNavegacion):
                boton.deselect()
        boton_seleccionado.select()

    def salir(e):
        page.window.close()

    # Botones de navegación
    boton_inicio = BotonNavegacion(
        icon=ft.Icons.HOME, tooltip="Inicio", shape=ft.RoundedRectangleBorder(radius=10),
        bgcolor="#28282d", side=ft.BorderSide(1, "#28282d"),
        on_click=lambda e: cambiar_pantalla(pantalla_inicio(), boton_inicio),
        selected=True
    )
    botones_cruds.append(boton_inicio)
    
    botones_cruds.append(ft.Divider(thickness=1, color="WHITE"))

    boton_usuarios = BotonNavegacion(
        icon=ft.Icons.PERSON, tooltip="Usuarios", shape=ft.RoundedRectangleBorder(radius=30),
        bgcolor="#2f3136", side=ft.BorderSide(1, "#7289da"),
        on_click=lambda e: cambiar_pantalla(CrudUsuarios(page), boton_usuarios)
    )
    botones_cruds.append(boton_usuarios)

    boton_empleados = BotonNavegacion(
        icon=ft.Icons.BADGE, tooltip="Empleados", shape=ft.RoundedRectangleBorder(radius=30),
        bgcolor="#2f3136", side=ft.BorderSide(1, "#7289da"),
        on_click=lambda e: cambiar_pantalla(CrudEmpleados(page), boton_empleados)
    )
    botones_cruds.append(boton_empleados)

    boton_articulos = BotonNavegacion(
        icon=ft.Icons.STORE, tooltip="Artículos", shape=ft.RoundedRectangleBorder(radius=30),
        bgcolor="#2f3136", side=ft.BorderSide(1, "#7289da"),
        on_click=lambda e: cambiar_pantalla(CrudArticulos(page), boton_articulos)
    )
    botones_cruds.append(boton_articulos)

    boton_eventos = BotonNavegacion(
        icon=ft.Icons.EVENT, tooltip="Eventos", shape=ft.RoundedRectangleBorder(radius=30),
        bgcolor="#2f3136", side=ft.BorderSide(1, "#7289da"),
        on_click=lambda e: cambiar_pantalla(CrudEventos(page), boton_eventos)
    )
    botones_cruds.append(boton_eventos)

    navegacion = ft.Container(
        content=ft.Column(
            controls=[
                ft.Column(botones_cruds, spacing=10),
                ft.Container(expand=True),
                BotonNavegacion(
                    icon=ft.Icons.LOGOUT, tooltip="Salir", shape=ft.RoundedRectangleBorder(radius=30),
                    bgcolor="#2f3136", side=ft.BorderSide(1, "#7289da"), on_click=salir
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            spacing=10
        ),
        width=70,
        bgcolor="#2f3136",
        padding=10,
        border_radius=ft.border_radius.all(8),
        margin=ft.Margin(left=10, right=5, top=10, bottom=10),
    )

    page.add(
        ft.Row(
            controls=[
                navegacion,
                cont_principal
            ],
            expand=True,
            spacing=0
        )
    )

    cambiar_pantalla(pantalla_inicio(), boton_inicio)

ft.app(target=main)