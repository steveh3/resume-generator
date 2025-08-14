import flet as ft  

def main():  
    pass  

def create_navbar(page_on_change_handler):  
    return ft.NavigationBar(  
        destinations=[  
            ft.NavigationBarDestination(  
                icon=ft.Icons.HOME,  
                selected_icon=ft.Icons.HOME_OUTLINED,  
                label="Home",  
            ),  
            ft.NavigationBarDestination(  
                icon=ft.Icons.NOTE_ADD,   
                selected_icon=ft.Icons.NOTE_ADD_OUTLINED,   
                label="Generate",  
            ),  
            ft.NavigationBarDestination(  
                icon=ft.Icons.MANAGE_ACCOUNTS,   
                selected_icon=ft.Icons.MANAGE_ACCOUNTS_OUTLINED,  
                label="Manage"  
            ),              
            ft.NavigationBarDestination(  
                icon=ft.Icons.SETTINGS_APPLICATIONS,   
                selected_icon=ft.Icons.SETTINGS_APPLICATIONS_OUTLINED,  
                label="Settings"  
            ),    
        ],  
        on_change=page_on_change_handler,  
    )  

if __name__ == "__main__":  
    main()  