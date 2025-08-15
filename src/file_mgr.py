from os import path, getenv, getcwd  
from pathlib import Path  
import json  

def main():  
    pass  

class ResumeFile:  

    def __init__(self, resume_name):  

        # Initializes the AppSettings manager.  
        # Args:  
        #    resume_name: The name of the JSON file.  
        app_data_path = getenv("FLET_APP_STORAGE_DATA")  
        if not app_data_path:  
            app_data_path = getcwd()  
        if not resume_name.lower().endswith(".json"):
            resume_name += ".json"

        self.resume_file = Path(path.join(app_data_path, resume_name))  
        self._resume = self._load_resume()  

    def _get_default_file(self) -> dict:  

        # Returns a dictionary of default resume
        return {  
            "Status": "Incomplete",  
            "Tags": [],  
            "Description": None,
            "Theme": None,
            "Contact Info": {
                "Name": None,
                "Phone": None,
                "eMail": None,
                "URL": None
            },
            "Summary": None,
            "Job History": [],
            "Education": [],
            "Skills": []
        }  

      

    def _load_resume(self) -> dict:  

        # Loads resume from the JSON file or returns default .JSON  
        output_file = Path(self.resume_file)  
        if output_file.exists():  
            try:  
                with open(output_file, "r", encoding="utf-8") as f:  
                    return json.load(f)  
            except json.JSONDecodeError:  
                print(f"Warning: Settings file '{output_file} is corrupt")  
        else:  
            return self._get_default_file()  

    def _save_resume(self):  

        # Saves the current settings to the JSON file.  
        output_file = Path(self.resume_file)  
        try:  
            with open(output_file, "w", encoding="utf-8") as f:  
                json.dump(self._resume, f, indent=4)  
        except IOError as e:  
            print(f"Error saving settings to '{output_file}': {e}")  

    def get_setting(self, key: str, default_value=None):  

        # Retrieves a specific setting by its key.  
        # Args:  
        #    key: The key of the setting to retrieve.  
        #    default_value: The value to return if the key is not found.  
        # Returns:  
        #    The value of the setting or the default_value if not found.  
        return self._resume.get(key, default_value)  
      

    def set_setting(self, key: str, value):  

        #Sets or updates a specific setting and saves the changes.  
        #Args:  
        #    key: The key of the setting to set.  
        #    value: The new value for the setting.  
        self._resume[key] = value  
        self._save_resume()  

    def get_all_settings(self) -> dict:  

        # Returns a copy of all current settings.  
        return self._resume.copy()  

if __name__ == "__main__":  
    main()  