# Mobile cross-platform tests (1 test covers ios + android ) with Python + Pytest + Selene + Appium

## Quick Start / Demo

1. Clone this repo
2. Do `poetry install`
3. Open project in your favorite code editor, setup interpreter
4. Download [wikipedia app apk](https://github.com/wikimedia/apps-android-wikipedia/releases/tag/latest), and store it inside project root with name `app-alpha-universal-release.apk`.
5. Go through [Appium Setup for Local Android Tutorial](https://autotest.how/appium-setup-for-local-android-tutorial-md) if you haven't set up your local infrastructure yet.
    a. This guides can be an alternative source of materials: [official guide](https://appium.io/docs/en/drivers/android-uiautomator2/) on complete driver setup for android devices. Setup [only one device](https://appium.io/docs/en/writing-running-appium/running-tests/#running-your-test-app-with-appium-android) – either an android emulator or a real android device (connected to your machine). One more real device checklist – [from Zebrunner](https://github.com/zebrunner/mcloud-agent#android-devices) and consider some other developer options like «Stay awake» from [this official android guide](https://developer.android.com/studio/debug/dev-options#general). If you want to set up more than one device at once, you have to decide which device to use for tests, get its id from the result of running `adb devices` command and add a `udid=<YOUR_DEVICE_ID>` either to the corresponding `.env.{context}.defaults` file, or custom `.env` file.
6. Run `pytest tests/` from your terminal to execute the test on Android platform, or run it through your IDE.

## What's next...

TBD...
