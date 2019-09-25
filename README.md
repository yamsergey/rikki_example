## Example Project for Rikki testing environment
This project is an example of how you can use `Rikki` testing environment.
Currently it has an example only for Android, but will be updated with iOS as well.


## Requirements

You will need to prepare android emulator with name `Pixel_API_28`. Or you can use any name but don't forget to change it in `rikki-talk/features/environment.py` 

Then you will need to install `mitmproxy certificate`. There are 2 ways to do that.

 - Trusted User Certificate (Allow to decrypt traffic only for your app)
    - Install user certificate  as described (there)[https://docs.mitmproxy.org/stable/concepts-certificates/]
    - Make your application trust user certificates (Android Docs)[https://developer.android.com/training/articles/security-config]
        >  Allow in only for debug version if it's your production app
        > warehouse.apk has the config already
 - Push needed certificate to system trusted certificates (Only for emulator or rooted devices). Described below
 - Configure the emulator to use Proxy
    - Wi-Fi settings
    - Proxy host 10.0.2.2 (Default ip to address host machine from emulator)
    - Proxy port 8080       

### Push certificate to system trusted

Android doesn’t allow to sniff traffic on Android because of pinned certificates rule. We can adjust own app to allow particular certificates. But it doesn’t works for ads, because all requests for Google Ads happens from Google Play services.

To overcome it we can push needed certificates to any Goole Android Emulators ( API images only ).

#### Steps

First lets start our emulator with writable system:

```bash
cd cd $ANDROID_HOME/emulator/
./emulator -avd EMULATOR_NAME -writable-system
```

Switch `adb` to root mode:

```bash
adb root
```

Disable security checks

```bash
adb disable-verity
```

Remount system, to make it writable

```bash
# -R will reboot emulator if needed
adb remount -R
```

Push certificates to system storage:

```bash
adb push c8750f0d.0 /system/etc/security/cacerts
```

#### Add your certificate 

You can add any certificate you want to Android as user certificate. In that case Android will store it in: `/data/misc/user/0/cacerts-added/` . Just move them fro there to `/system/etc/security/cacerts`
