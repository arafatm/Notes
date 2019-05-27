# Installing Kodi

from https://samhobbs.co.uk/2017/08/kodi-server-part-1-installation-and-configuration

## Install Kodi

```
sudo usermod -aG audio,video kodi

sudo apt-get update
sudo apt-get install software-properties-common

sudo add-apt-repository ppa:team-xbmc/ppa
sudo apt-get update
sudo apt-get install kodi xorg xserver-xorg-legacy dbus-x11 alsa-utils
```

## Starting Kodi automatically


`sudo vi /etc/systemd/system/kodi.service`

```
[Unit]
Description = Kodi Media Center

After = systemd-user-sessions.service sound.target

[Service]
User = kodi
Group = kodi
Type = simple
PAMName = login
ExecStart = /usr/bin/xinit /usr/bin/dbus-launch --exit-with-session /usr/bin/kodi-standalone -- :0 -nolisten tcp vt7
Restart = on-abort
RestartSec = 5

[Install]
WantedBy = multi-user.target
```

`sudo systemctl enable kodi`

## Allow shutdown/reboot

`sudo vi /etc/polkit-1/localauthority/50-local.d/kodi.pkla`

```
[kodi user]
Identity=unix-user:kodi
Action=org.freedesktop.login1.*
ResultAny=yes
ResultInactive=no
ResultActive=yes
```

`sudo systemctl restart polkitd.service`

## Allowing auto updates to Kodi

```
sudo apt-get install unattended-upgrades
```

If it's already installed, you can re-run the configuration script using:
`sudo dpkg-reconfigure unattended-upgrades`

This will create a config file at /etc/apt/apt.conf.d/20auto-upgrades with the contents:

```
APT::Periodic::Update-Package-Lists "1";
APT::Periodic::Unattended-Upgrade "1";
```

By default, only packages in the ubuntu archive are auto updated, but since we installed 
Kodi from the developers' PPA we won't receive auto updates unless we make a change. 

`sudo vi /etc/apt/apt.conf.d/50unattended-upgrades`
and edit the Unattended-Upgrade::Allowed-Origins block at the top

```
// Automatically upgrade packages from these (origin:archive) pairs
Unattended-Upgrade::Allowed-Origins {
        "${distro_id}:${distro_codename}";
        "${distro_id}:${distro_codename}-security";
        // Extended Security Maintenance; doesn't necessarily exist for
        // every release and this system may not have it installed, but if
        // available, the policy for updates is such that unattended-upgrades
        // should also install from here by default.
        "${distro_id}ESM:${distro_codename}";
//      "${distro_id}:${distro_codename}-updates";
//      "${distro_id}:${distro_codename}-proposed";
//      "${distro_id}:${distro_codename}-backports";
        // manually added so that auto updates include updates to Kodi
        "LP-PPA-team-xbmc:${distro_codename}";
};
```
