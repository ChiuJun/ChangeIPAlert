# Change IP Alert

A simple but useful python script, that alert you via ServerChan when the IP of your device changes.

## Instalation

- Requests
```bash
pip install public-ip
```
- [ServerChan](https://sct.ftqq.com/)(https://sct.ftqq.com/)
> Server酱是什么
「Server酱」，英文名「ServerChan」，是一款「手机」和「服务器」、「智能设备」之间的通信软件。
说人话？就是从服务器、路由器等设备上推消息到手机的工具。

## Configuration

Just update the file config.json with your own api key from ServerChan then run the script:
```
python ChangeIPAlert.py
```

If you are on linux, you can use cron to schedule the task. See [crontab guru](https://crontab.guru/examples.html) to more details.
Thanks to vterron for the [public-ip](https://github.com/vterron/public-ip) module, that's a great job.