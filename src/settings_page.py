import flet as ft  
from settings import AppSettings  
from database_mgr import delete_row, get_all_rows  

def main():  
    pass       

def create_settings_page(page):  
    settings = AppSettings()  
    def change_setting(e):  
        settings.set_setting(e.control.label,e.control.value)  

    return ft.Column([  
        ft.Text(f"Author: {settings.get_setting("Author")}"),  
        ft.Text(f"Version: {settings.get_setting("Version")}"),  
        ft.Divider(),  
        ft.Switch(  
            label="Setting1",  
            value=settings.get_setting("Setting1"),  
            on_change=change_setting,  
        ),  
        ft.Switch(  
            label="Setting2",  
            value=settings.get_setting("Setting2"),  
            on_change=change_setting,  
        ),  
    ])  


if __name__ == "__main__":  
    main()  