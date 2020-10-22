# mvid_test
## Запуск
В директорию `/data/` добавить файл `recommends.csv`

**Запустить в контейнере**
- На linux 
```
$ boot.sh
```
- На Windows 
 ```
$ boot.cmd
```

**Запустить локально** 
```
$ python main.py
```

## Пример использования
**Доступные параметры запроса**

* _sku_ - id товара
* _min_threshold_ - опциональный параметр минимального порога близости для рекомендаций

**Запрос**
```.shell script
$ curl --location --request GET 'http://127.0.0.1:5000/recommendations?sku=Sm3QYKG2uA&min_threshold=1'
```
**Ответ**
```
{
    "recommendations": [
        {
            "proba": 1.0,
            "recom": "VHGOYYaZiX"
        },
        {
            "proba": 1.099609375,
            "recom": "eDQZa9Y2Gn"
        }
    ],
    "sku": "Sm3QYKG2uA"
}
```
## ApacheBench
```
$ ab -n 50000 -c 50 -r http://127.0.0.1:8080/recommendations?sku=Sm3QYKG2uA

This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 5000 requests
Completed 10000 requests
Completed 15000 requests
Completed 20000 requests
Completed 25000 requests
Completed 30000 requests
Completed 35000 requests
Completed 40000 requests
Completed 45000 requests
Completed 50000 requests
Finished 50000 requests


Server Software:        Werkzeug/1.0.1
Server Hostname:        127.0.0.1
Server Port:            8080

Document Path:          /recommendations?sku=Sm3QYKG2uA
Document Length:        2206 bytes

Concurrency Level:      50
Time taken for tests:   2107.620 seconds
Complete requests:      50000
Failed requests:        0
Total transferred:      117650000 bytes
HTML transferred:       110300000 bytes
Requests per second:    23.72 [#/sec] (mean)
Time per request:       2107.620 [ms] (mean)
Time per request:       42.152 [ms] (mean, across all concurrent requests)
Transfer rate:          54.51 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.5      0      28
Processing:   106 2106 243.2   2138    3173
Waiting:       94 2078 237.8   2101    3171
Total:        106 2107 243.1   2138    3173

Percentage of the requests served within a certain time (ms)
  50%   2138
  66%   2228
  75%   2280
  80%   2311
  90%   2392
  95%   2459
  98%   2537
  99%   2594
 100%   3173 (longest request)
```
