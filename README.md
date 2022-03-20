# Scanner
The purpose of the code is to support journalists by listening to the scanner 24/7 so they don't have to.

---
## Set Up

1. Log into your Gmail account
2. Click on your account
3. Click on "Manage your Google Account"
4. Under Security -> Signing in to Google click on "App passwords"
5. Generate a password by filling out the form
6. Copy the password (you won't be able to see it again)
7. In the alert_check function of scanner.py enter your email, the app password you just received, and your number followed by your carrier

Carrier information will be one of the following:
- **Att:** @mms.att.net
- **Tmobile:** @tmomail.net
- **Verizon:** @vtext.com
- **Sprint:** @messaging.sprintpcs.com
- **Virgin:** @vmobl.com
- **Boost:** @smsmyboostmobile.com
- **Cricket:** @sms.cricketwireless.net
- **Metro:** @mymetropcs.com
- **US Cellular:** @email.uscc.net
- **Xfinity:** @vtext.com

*Consider using environment variables if you don't want to hard code this information*

8. In alert_words.txt enter in the words that when said you get alerted

---
## Usage

With the script set up, we are ready to listen to the scanner. Place your device's microphone near the audio source. Run the script and await future alerts!

*The original intent was to run the script on a raspberry pi with a usb mic but other devices with a microphone can work as well.*

---
## Todo

- [ ] Send the audio when alert triggered