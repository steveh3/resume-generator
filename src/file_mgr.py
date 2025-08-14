from os import path, getenv, getcwd  
from pathlib import Path  
import json  

def main():  
    pass  

class AppSettings:  

    def __init__(self, settings_file: str = "settings.json"):  

        # Initializes the AppSettings manager.  
        # Args:  
        #    settings_file: The name of the JSON file to store settings.  
        app_data_path = getenv("FLET_APP_STORAGE_DATA")  
        if not app_data_path:  
            app_data_path = getcwd()  

        self.settings_file = Path(path.join(app_data_path, settings_file))  
        self._settings = self._load_settings()  

    def _get_default_file(self) -> dict:  

        # Returns a dictionary of default application settings.  
        return {  
            "Author": "Steve",  
            "Version": "0.1.0",  
            "Setting1": "True",  
            "Setting2": "False",  
        }  

      

    def _load_settings(self) -> dict:  

        # Loads settings from the JSON file or returns default settings  
        output_file = Path(self.settings_file)  
        if output_file.exists():  
            try:  
                with open(output_file, "r", encoding="utf-8") as f:  
                    return json.load(f)  
            except json.JSONDecodeError:  
                print(f"Warning: Settings file '{output_file} is corrupt")  
        else:  
            return self._get_default_file()  

    def _save_settings(self):  

        # Saves the current settings to the JSON file.  
        output_file = Path(self.settings_file)  
        try:  
            with open(output_file, "w", encoding="utf-8") as f:  
                json.dump(self._settings, f, indent=4)  
        except IOError as e:  
            print(f"Error saving settings to '{output_file}': {e}")  

    def get_setting(self, key: str, default_value=None):  

        # Retrieves a specific setting by its key.  
        # Args:  
        #    key: The key of the setting to retrieve.  
        #    default_value: The value to return if the key is not found.  
        # Returns:  
        #    The value of the setting or the default_value if not found.  
        return self._settings.get(key, default_value)  
      

    def set_setting(self, key: str, value):  

        #Sets or updates a specific setting and saves the changes.  
        #Args:  
        #    key: The key of the setting to set.  
        #    value: The new value for the setting.  
        self._settings[key] = value  
        self._save_settings()  

    def get_all_settings(self) -> dict:  

        # Returns a copy of all current settings.  
        return self._settings.copy()  

if __name__ == "__main__":  

    main()  