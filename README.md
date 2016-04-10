# phantomscanner

scan HTTP hosts and grab screenshots

## Install

```
$ sudo apt-get install phantomjs
$ sudo apt-get install fonts-migmix  # Japanese fonts
```

```
$ virtualenv ENV
$ . ENV/bin/activate
(ENV)$ pip install -r requirements.txt
```

## Run

```
(ENV)$ python scanner.py 192.168.0.0/24
```

grabbed screenshots are stored in `images/`.
