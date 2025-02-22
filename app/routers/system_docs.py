get_hw_info_json = """
```JSON
{
  "cpu_overall_percent": 15.8,
  "cpu_per_cpu_percent": [
    11.8,
    6.1,
    12.5
  ],
  "vram_total_bytes": 25134919680,
  "vram_available_bytes": 17240051712,
  "vram_used_bytes": 6044856320,
  "vram_usage_percent": 31.4,
  "swap_ram_total_bytes": 2147479552,
  "swap_used_bytes": 0,
  "swap_usage_bytes": 0,
  "temperatures_celsius": {
    "coretemp": [
      [
        "Core 1",
        51,
        84,
        100
      ],
      [
        "Core 2",
        53,
        84,
        100
      ],
      [
        "Core 3",
        50,
        84,
        100
      ]
    ]
  },
  "boot_time_timestamp": 1623486468,
  "disk_io_read_count": 254574,
  "disk_io_write_count": 133353,
  "disk_io_read_bytes": 5306839040,
  "disk_io_write_bytes": 5593076736,
  "disks": [
    {
      "device": "/dev/sda1",
      "mountpoint": "/boot/efi",
      "filesystem_type": "vfat",
      "partition_total_bytes": 535805952,
      "partition_used_bytes": 8228864,
      "partition_free_bytes": 527577088,
      "partition_percent": 1.5
    },
    {
      "device": "/dev/sda2",
      "mountpoint": "/",
      "filesystem_type": "ext4",
      "partition_total_bytes": 250438021120,
      "partition_used_bytes": 177157742592,
      "partition_free_bytes": 60487389184,
      "partition_percent": 74.5
    }
  ],
  "networks": [
    {
      "interface_name": "lo",
      "address": "127.0.0.1",
      "mac_address": "00:00:00:00:00:00"
    },
    {
      "interface_name": "enp4s0",
      "address": "192.168.1.23",
      "mac_address": "35:a3:5c:6a:4a:f0"
    }
  ],
  "networks_bytes_sent": 137088249,
  "networks_bytes_received": 1603400654
}
```
"""

get_debug_data_sample_str = """
***************************************************************
* RASPIBLITZ DEBUG LOGS 
***************************************************************
blitzversion: 1.7.0
chainnetwork: bitcoin / main
 15:27:34 up  4:10,  3 users,  load average: 1.23, 1.36, 1.38

*** BLOCKCHAIN SYSTEMD STATUS ***
● bitcoind.service - Bitcoin daemon
   Loaded: loaded (/etc/systemd/system/bitcoind.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2021-09-14 11:16:51 BST; 4h 10min ago
  Process: 1718 ExecStartPre=/home/admin/config.scripts/blitz.systemd.sh log blockchain STARTED (code=exited, status=0/SUCCESS)
  Process: 1724 ExecStart=/usr/local/bin/bitcoind -daemon -conf=/home/bitcoin/.bitcoin/bitcoin.conf -pid=/mnt/hdd/bitcoin/bitcoind.pid (code=exited, status=0/SUCCESS)
 Main PID: 1765 (bitcoind)
    Tasks: 12 (limit: 4533)
   CGroup: /system.slice/bitcoind.service
           └─1765 /usr/local/bin/bitcoind -daemon -conf=/home/bitcoin/.bitcoin/bitcoin.conf -pid=/mnt/hdd/bitcoin/bitcoind.pid

Sep 14 11:16:50 raspberrypi systemd[1]: Starting Bitcoin daemon...
Sep 14 11:16:51 raspberrypi systemd[1]: Started Bitcoin daemon.

*** LAST BLOCKCHAIN ERROR LOGS ***
sudo journalctl -u bitcoind -b --no-pager -n8
-- Logs begin at Tue 2021-09-14 11:15:58 BST, end at Tue 2021-09-14 15:27:35 BST. --
Sep 14 11:16:50 raspberrypi systemd[1]: Starting Bitcoin daemon...
Sep 14 11:16:51 raspberrypi systemd[1]: Started Bitcoin daemon.

*** LAST BLOCKCHAIN 20 INFO LOGS ***
sudo tail -n 20 /mnt/hdd/bitcoin/debug.log
2021-09-14T14:26:27Z Rolling forward 00000000000000000082dcdfb99c8b663828fd40fd68f343a17f766e1dee9bdc (499641)
2021-09-14T14:26:30Z Rolling forward 0000000000000000003c2cc296d753717135a38cfea6bc3ddba640aac063fb3b (499642)
2021-09-14T14:26:34Z Rolling forward 00000000000000000005869d321a8f2046d1e47f55b97920c9e4bb8a971db40b (499643)
2021-09-14T14:26:37Z Rolling forward 0000000000000000002d429f39afec70c938e888c3417d690bbc85e83529991c (499644)
2021-09-14T14:26:40Z Rolling forward 00000000000000000024c0bdbec66a889778c00bc69be0a96cbbd98b75c3ce09 (499645)
2021-09-14T14:26:43Z Rolling forward 00000000000000000082756af6724e3200ea9089cb4244cb2d94c83c3cd137d7 (499646)
2021-09-14T14:26:47Z Rolling forward 0000000000000000007f3bf2c37dc14630153b93bc2c34542deadb34a5eb201f (499647)
2021-09-14T14:26:51Z Rolling forward 0000000000000000003b9296ea38abd68e97beb0c5ed56a8255e6b379a02032b (499648)
2021-09-14T14:26:54Z Rolling forward 000000000000000000146931cda4713b5ded152c9ae57effe37f216d5a5f31b6 (499649)
2021-09-14T14:26:57Z Rolling forward 000000000000000000684318d6fc7266f8eb5dc349a170413a0c0ce2334da08f (499650)
2021-09-14T14:27:00Z Rolling forward 000000000000000000846d905295c15c98f9dc8c8f3ab44bbb997cca9a8e4c83 (499651)
2021-09-14T14:27:04Z Rolling forward 00000000000000000082bfa88de1c4e6501462e231f0aa54f552f36bdf34fdd3 (499652)
2021-09-14T14:27:08Z Rolling forward 000000000000000000acce35f2b4ba5256f016da6024abb09ad60b6dcbd0ed83 (499653)
2021-09-14T14:27:11Z Rolling forward 000000000000000000ae0edf99df2db7e05a0f18e3e5a3e0dfc67013dadc526f (499654)
2021-09-14T14:27:14Z Rolling forward 00000000000000000087cec98103a704a4594831e8173fa3c916b3c537456ab7 (499655)
2021-09-14T14:27:17Z Rolling forward 000000000000000000102d751e4c7e2de8f12e04cd4b44fe8179d492b29ea0e2 (499656)
2021-09-14T14:27:21Z Rolling forward 0000000000000000001a98320ee19986cfb19f30bb1d1deb0cfc21ed9fa3c7ae (499657)
2021-09-14T14:27:24Z Rolling forward 0000000000000000005ad979367405af6ad75465a8900089cb3bd7b53ff4dc9d (499658)
2021-09-14T14:27:28Z Rolling forward 0000000000000000005bd3de0386b9c24f92e363a04da33b6b6ac7450997f4aa (499659)
2021-09-14T14:27:32Z Rolling forward 0000000000000000009fd25eaf6245cd8a0a8869bbe28145f39e4de14dd62825 (499660)

*** LND SYSTEMD STATUS ***
● lnd.service - LND Lightning Daemon
   Loaded: loaded (/etc/systemd/system/lnd.service; enabled; vendor preset: enabled)
   Active: active (running) since Tue 2021-09-14 11:20:13 BST; 4h 7min ago
  Process: 7000 ExecStartPre=/home/admin/config.scripts/blitz.systemd.sh log lightning STARTED (code=exited, status=0/SUCCESS)
 Main PID: 7002 (lnd)
    Tasks: 10 (limit: 4533)
   CGroup: /system.slice/lnd.service
           └─7002 /usr/local/bin/lnd --tor.active --tor.streamisolation --tor.v3 --tor.socks=9070 --tor.control=9071 --listen=127.0.0.1:9735

Sep 14 11:20:13 raspberrypi systemd[1]: Starting LND Lightning Daemon...
Sep 14 11:20:13 raspberrypi systemd[1]: Started LND Lightning Daemon.

*** LAST LND ERROR LOGS ***
sudo journalctl -u lnd -b --no-pager -n12
-- Logs begin at Tue 2021-09-14 11:15:58 BST, end at Tue 2021-09-14 15:27:35 BST. --
Sep 14 11:16:51 raspberrypi systemd[1]: Starting LND Lightning Daemon...
Sep 14 11:16:51 raspberrypi systemd[1]: Started LND Lightning Daemon.
Sep 14 11:19:13 raspberrypi lnd[1772]: unable to create chain control: unable to connect to bitcoind: -28: Loading block index...
Sep 14 11:19:13 raspberrypi systemd[1]: lnd.service: Main process exited, code=exited, status=1/FAILURE
Sep 14 11:19:13 raspberrypi systemd[1]: lnd.service: Failed with result 'exit-code'.
Sep 14 11:20:13 raspberrypi systemd[1]: lnd.service: Service RestartSec=1min expired, scheduling restart.
Sep 14 11:20:13 raspberrypi systemd[1]: lnd.service: Scheduled restart job, restart counter is at 1.
Sep 14 11:20:13 raspberrypi systemd[1]: Stopped LND Lightning Daemon.
Sep 14 11:20:13 raspberrypi systemd[1]: Starting LND Lightning Daemon...
Sep 14 11:20:13 raspberrypi systemd[1]: Started LND Lightning Daemon.

*** LAST 30 LND INFO LOGS ***
sudo tail -n 30 /mnt/hdd/lnd/logs/bitcoin/mainnet/lnd.log
2021-09-14 11:16:51.708 [INF] LTND: Version: 0.12.1-beta commit=v0.12.1-beta, build=production, logging=default, debuglevel=debug
2021-09-14 11:16:51.709 [INF] LTND: Active chain: Bitcoin (network=mainnet)
2021-09-14 11:16:51.709 [INF] LTND: Opening the main database, this might take a few minutes...
2021-09-14 11:16:51.709 [INF] LTND: Opening bbolt database, sync_freelist=true, auto_compact=false
2021-09-14 11:16:51.724 [INF] CHDB: Checking for schema update: latest_version=20, db_version=20
2021-09-14 11:16:51.724 [INF] LTND: Database now open (time_to_open=15.109685ms)!
2021-09-14 11:16:51.763 [INF] RPCS: Password RPC server listening on 0.0.0.0:10009
2021-09-14 11:16:51.769 [INF] RPCS: Password gRPC proxy started at 0.0.0.0:8080
2021-09-14 11:16:51.769 [INF] LTND: Waiting for wallet encryption password. Use `lncli create` to create a wallet, `lncli unlock` to unlock an existing wallet, or `lncli changepassword` to change the password of an existing wallet and unlock it.
2021-09-14 11:19:12.895 [INF] LNWL: Opened wallet
2021-09-14 11:19:13.126 [INF] CHRE: Primary chain is set to: bitcoin
2021-09-14 11:19:13.257 [ERR] LTND: unable to create chain control: unable to connect to bitcoind: -28: Loading block index...
2021-09-14 11:19:13.257 [INF] LTND: Shutdown complete2021-09-14 11:20:14.120 [INF] LTND: Version: 0.12.1-beta commit=v0.12.1-beta, build=production, logging=default, debuglevel=debug
2021-09-14 11:20:14.121 [INF] LTND: Active chain: Bitcoin (network=mainnet)
2021-09-14 11:20:14.121 [INF] LTND: Opening the main database, this might take a few minutes...
2021-09-14 11:20:14.121 [INF] LTND: Opening bbolt database, sync_freelist=true, auto_compact=false
2021-09-14 11:20:14.133 [INF] CHDB: Checking for schema update: latest_version=20, db_version=20
2021-09-14 11:20:14.133 [INF] LTND: Database now open (time_to_open=11.654861ms)!
2021-09-14 11:20:14.172 [INF] RPCS: Password RPC server listening on 0.0.0.0:10009
2021-09-14 11:20:14.177 [INF] RPCS: Password gRPC proxy started at 0.0.0.0:8080
2021-09-14 11:20:14.177 [INF] LTND: Waiting for wallet encryption password. Use `lncli create` to create a wallet, `lncli unlock` to unlock an existing wallet, or `lncli changepassword` to change the password of an existing wallet and unlock it.

*** NGINX SYSTEMD STATUS ***
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
  Drop-In: /etc/systemd/system/nginx.service.d
           └─raspiblitz.conf
   Active: active (running) since Tue 2021-09-14 11:16:37 BST; 4h 10min ago
     Docs: man:nginx(8)
 Main PID: 905 (nginx)
    Tasks: 5 (limit: 4533)
   CGroup: /system.slice/nginx.service
           ├─905 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
           ├─911 nginx: worker process
           ├─913 nginx: worker process
           ├─914 nginx: worker process
           └─915 nginx: worker process

Sep 14 11:16:36 raspberrypi systemd[1]: Starting A high performance web server and a reverse proxy server...
Sep 14 11:16:37 raspberrypi systemd[1]: Started A high performance web server and a reverse proxy server.

*** LAST NGINX LOGS ***
sudo journalctl -u nginx -b --no-pager -n20
-- Logs begin at Tue 2021-09-14 11:15:58 BST, end at Tue 2021-09-14 15:27:35 BST. --
Sep 14 11:16:36 raspberrypi systemd[1]: Starting A high performance web server and a reverse proxy server...
Sep 14 11:16:37 raspberrypi systemd[1]: Started A high performance web server and a reverse proxy server.
--> CHECK CONFIG: sudo nginx -t


*** LAST 20 TOUCHSCREEN LOGS ***
sudo tail -n 20 /home/pi/.cache/lxsession/LXDE-pi/run.log
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
** Message: 01:44:02.973: wlan0: Received scan results
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
** Message: 01:45:03.021: wlan0: Received scan results
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
** Message: 01:46:02.982: wlan0: Received scan results
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
** Message: 01:47:02.989: wlan0: Received scan results
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono
Playing WAVE '/usr/share/piwiz/srprompt.wav' : Signed 16 bit Little Endian, Rate 22050 Hz, Mono


*** LAST 20 LOOP LOGS ***
sudo journalctl -u loopd -b --no-pager -n20
-- Logs begin at Tue 2021-09-14 11:15:58 BST, end at Tue 2021-09-14 15:27:35 BST. --
-- No entries --

- RTL is OFF by config

*** LAST 20 ElectRS LOGS ***
sudo journalctl -u electrs -b --no-pager -n20
-- Logs begin at Tue 2021-09-14 11:15:58 BST, end at Tue 2021-09-14 15:27:35 BST. --
-- No entries --

*** ElectRS Status ***
##### STATUS ELECTRS SERVICE
configured=0
serviceInstalled=0
infoSync='Service not installed'
serviceRunning=0
tipSynced=0
initialSynced=0
electrumResponding=0
infoSync='Not running - check: sudo journalctl -u electrs'


*** LAST 20 LIT LOGS ***
sudo journalctl -u litd -b --no-pager -n20
-- Logs begin at Tue 2021-09-14 11:15:58 BST, end at Tue 2021-09-14 15:27:36 BST. --
-- No entries --


*** LAST 20 BTCPayServer LOGS ***
sudo journalctl -u btcpayserver -b --no-pager -n20
-- Logs begin at Tue 2021-09-14 11:15:58 BST, end at Tue 2021-09-14 15:27:36 BST. --
-- No entries --


*** LAST 20 LNbits LOGS ***
sudo journalctl -u lnbits -b --no-pager -n20
-- Logs begin at Tue 2021-09-14 11:15:58 BST, end at Tue 2021-09-14 15:27:36 BST. --
-- No entries --


*** LAST 20 Thunderhub LOGS ***
sudo journalctl -u thunderhub -b --no-pager -n20
-- Logs begin at Tue 2021-09-14 11:15:58 BST, end at Tue 2021-09-14 15:27:36 BST. --
-- No entries --


*** LAST 20 SPECTER LOGS ***
sudo journalctl -u cryptoadvance-specter -b --no-pager -n20
-- Logs begin at Tue 2021-09-14 11:15:58 BST, end at Tue 2021-09-14 15:27:36 BST. --
-- No entries --


*** LAST 20 SPHINX LOGS ***
sudo journalctl -u sphinxrelay -b --no-pager -n20
-- Logs begin at Tue 2021-09-14 11:15:58 BST, end at Tue 2021-09-14 15:27:36 BST. --
-- No entries --


*** MOUNTED DRIVES ***
Filesystem     Type      Size  Used Avail Use% Mounted on
/dev/root      ext4       29G  3.8G   25G  14% /
devtmpfs       devtmpfs  1.9G     0  1.9G   0% /dev
tmpfs          tmpfs     1.9G     0  1.9G   0% /dev/shm
tmpfs          tmpfs     1.9G   33M  1.9G   2% /run
tmpfs          tmpfs     5.0M     0  5.0M   0% /run/lock
tmpfs          tmpfs     1.9G     0  1.9G   0% /sys/fs/cgroup
tmpfs          tmpfs      32M     0   32M   0% /var/cache/raspiblitz
/dev/mmcblk0p1 vfat      253M   30M  223M  12% /boot
/dev/sda1      ext4      916G  170G  700G  20% /mnt/hdd
tmpfs          tmpfs     385M     0  385M   0% /run/user/1000
tmpfs          tmpfs     385M     0  385M   0% /run/user/1001


*** DATADRIVE ***
# RASPIBLITZ DATA DRIVE Status

# BASICS
isMounted=1
isBTRFS=0
hddRaspiData=1
isSSD=1
datadisk='sda'
datapartition='sda1'
hddBlocksBitcoin=1
hddBlocksLitecoin=0
hddBytes=1000141693440
hddGigaBytes=931
hddUsedInfo='170G (20%)'
hddDataFreeKB=733759240
hddAdapterUSB=''
hddAdapterUSAP=0

# RAID
isRaid=0
raidCandidates=0

# SWAP
isSwapExternal=1
SwapExternalPath='/mnt/hdd/swapfile'


*** NETWORK ***
localip=192.168.0.103
dhcp=1
network_device=eth0

*** HARDWARE TEST RESULTS ***
UndervoltageReports in Logs: 0

*** SYSTEM STATUS (can take some seconds to gather) ***
localIP='192.168.0.102'
tempCelsius='63.2'
uptime=15042
upsStatus='OFF'
startcountBlockchain=1
bitcoinActive=1
bitcoinErrorShort='Loading block index'
bitcoinErrorFull='error code: -28 error message: Loading block index...'
startcountLightning=2
lndActive=1
lndRPCReady=0
walletOpened=0
walletReady=0
walletLocked=1
lndRPCReady=0
blitzTUIActive=0
blitzTUIRestarts=0
scriptRuntime=0

*** OPTION: SHARE THIS DEBUG OUTPUT ***
An easy way to share this debug output on GitHub or on a support chat
use the following command and share the resulting link:
/home/admin/XXdebugLogs.sh | nc termbin.com 9999
"""

get_debug_logs_raw_summary = "Get raw system logs as a text string."
get_debug_logs_raw_desc = """
This endpoint will gather latest system logs and return it in a 
raw string. This endpoint will **not** return immediately because 
it gathers all data on time of the request.
"""

get_debug_logs_raw_resp_desc = f"""
The latest system log as a string of text.

Returns a `HTTP_INTERNAL_SERVER_ERROR` with status code 500 if script execution fails on server.

Example output in `raw_data`:

```{get_debug_data_sample_str}```
"""
