#Python environment

Setup virtualenv
```
virtualenv env -p python3
```
Install python dependencies
```
source env/bin/activate
pip install -r requirements.txt
```

# Setup MPD

## Add music directory

Set the `music_directory` in /etc/mpd.conf to the music folder and grant mpd
the permission

```
gpasswd -a mpd <your login group>
chmod 710 /home/<your home dir>

```
login group is probably your username