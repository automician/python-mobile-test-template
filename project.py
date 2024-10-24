from enum import Enum
from typing import Optional

import dotenv
import pydantic

from python_mobile_test_template.support import path


class EnvContext(Enum):
    android = 'android'
    ios = 'ios'
    # bstack_android = 'bstack_android'
    # bstack_ios = 'bstack_ios'
    # local_android = 'local_android'
    # local = 'local'
    # local_ios = 'local_ios'


class Config(pydantic.BaseSettings):
    context: EnvContext = EnvContext.android

    # --- Selene settings --- #
    driver_remote_url: str = 'http://127.0.0.1:4723'
    timeout: float = 6

    # --- General Capabilities --- #
    newCommandTimeout: Optional[int] = 60
    app_package: str = 'org.wikipedia.alpha'
    app: Optional[str] = './app-alpha-universal-release.apk'
    appWaitActivity = 'org.wikipedia.*'
    deviceName: Optional[str] = None
    udid: Optional[str] = None
    noReset: Optional[bool] = None
    platformVersion: Optional[str] = None
    browserName: Optional[str] = None
    bstack_userName: Optional[str] = None
    bstack_accessKey: Optional[str] = None
    # --- Android Capabilities --- #
    avd: Optional[str] = None
    # --- iOS Capabilities --- #
    bundleId: Optional[str] = None
    initialDeeplinkUrl: Optional[str] = None

    @property
    def bstack_creds(self):
        return {
            'userName': self.bstack_userName,
            'accessKey': self.bstack_accessKey,
        }

    @property
    def runs_on_bstack(self):
        return self.app.startswith('bs://')

    def to_driver_options(self):
        general_caps = {
            **(
                {'newCommandTimeout': self.newCommandTimeout}
                if self.newCommandTimeout
                else {}
            ),
            **(
                {'platformVersion': self.platformVersion}
                if self.platformVersion
                else {}
            ),
            **({'browserName': self.browserName} if self.browserName else {}),
            **({'deviceName': self.deviceName} if self.deviceName else {}),
            **({'udid': self.udid} if self.udid else {}),
            **({'noReset': self.noReset} if self.noReset is not None else {}),
            **(
                {
                    'app': (
                        self.app
                        if (self.app.startswith('/') or self.runs_on_bstack)
                        else path.relative_from_root(self.app)
                    )
                }
                if self.app
                else {}
            ),
            **(
                {
                    "bstack:options": {
                        'projectName': 'Wikipedia App Tests',
                        # TODO: use some unique value
                        'buildName': 'browserstack-build-1',
                        # TODO: use some unique value
                        'sessionName': 'BStack first_test',
                        **self.bstack_creds,
                    }
                }
                if self.runs_on_bstack
                else {}
            ),
        }
        if self.context is EnvContext.android:
            from appium.options.android import UiAutomator2Options

            android_caps = {
                **general_caps,
                **({'avd': self.avd} if self.avd else {}),
                **(
                    {'appWaitActivity': self.appWaitActivity}
                    if self.appWaitActivity
                    else {}
                ),
            }
            return UiAutomator2Options().load_capabilities(android_caps)

        elif self.context is EnvContext.ios:
            from appium.options.ios import XCUITestOptions

            ios_caps = {
                **general_caps,
                **({'bundleId': self.bundleId} if self.bundleId else {}),
                **(
                    {'initialDeeplinkUrl': self.initialDeeplinkUrl}
                    if self.initialDeeplinkUrl
                    else {}
                ),
            }

            return XCUITestOptions().load_capabilities(ios_caps)

        else:
            raise ValueError(f'Unsupported context: {self.context}')


# To load env variables from .env file
# (they will override .env.{context}.defaults files)
dotenv.load_dotenv(
    dotenv_path=dotenv.find_dotenv('.env', usecwd=True),
    # but will not override env vars set out of .env file
    override=False,
)

config = Config(dotenv.find_dotenv(f'.env.{Config().context}.defaults', usecwd=True))
