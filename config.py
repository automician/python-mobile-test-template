import pydantic
from appium.options.android import UiAutomator2Options

from python_mobile_test_template import assist


class Settings(pydantic.BaseSettings):
    # --- Appium Capabilities ---
    app: str = '../android/app/build/outputs/apk/debug/app-debug.apk'
    full_reset: bool = True
    new_command_timeout: int = 1000

    app_id: str = 'com.reactnativedemo'

    # --- Remote Driver ---
    remote_url: str = 'http://127.0.0.1:4723/wd/hub'

    # --- Selene ---
    timeout: float = 6.0

    @property
    def driver_options(self):
        options = UiAutomator2Options()
        options.app = assist.file.abs_path_from_project(self.app)
        options.full_reset = self.full_reset
        options.new_command_timeout = self.new_command_timeout

        return options


settings = Settings()

if __name__ == '__main__':
    """
    for debugging purposes
    to check the actual config values on start
    when simply running `python config.py`
    """
    print(settings.__repr__())
