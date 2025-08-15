import flet as ft  
from navbar import create_navbar  
from database_mgr import create_table  
from main_page import create_main_page  
from newresume_page import create_newresume_page  
from manage_page import create_manage_page  
from settings_page import create_settings_page  

def main(page: ft.Page):  
    create_table()  

    # Navbar on_change handler  
    def handle_navbar_change(e):  
        page.controls.clear()  
        if e.control.selected_index == 0:  
            page.go("/")  
        elif e.control.selected_index == 1:  
            page.go("/newresume")  
        elif e.control.selected_index == 2:  
            page.go("/manage")  
        elif e.control.selected_index == 3:  
            page.go("/settings")  
        page.update()  
    page.navigation_bar = create_navbar(handle_navbar_change)  

    # Define routes  
    def route_change(e: ft.RouteChangeEvent):  
        if e.route == "/":  
            page.add(create_main_page(page))  
        elif e.route == "/newresume":  
            page.add(create_newresume_page(page))  
        elif e.route == "/manage":  
            page.add(create_manage_page(page))  
        elif e.route == "/settings":  
            page.add(create_settings_page(page))  
        page.update()  
    page.on_route_change = route_change  
    page.go(page.route)  

if __name__ == "__main__":  

    ft.app(main)  