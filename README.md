# mvid_test
## Запуск
В директорию `/data/` необходимо добавить файл `recommends.csv`

**Запустить в контейнере**

 ```
$ boot.cmd
```
**Запустить локально**
```
$ python dataset2hd5.py
$ python main.py
```
Первый запуск займет некоторое время, это связано с преобразованием данных в объект DataFrame.
Последующие запуски будут игнорировать этот шаг, данные будут читаться из hd5 файла.
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
$ ab -n 15000 -c 50 -r http://127.0.0.1:5000/recommendations?sku=Sm3QYKG2uA

This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient)
Completed 1500 requests
Completed 3000 requests
Completed 4500 requests
Completed 6000 requests
Completed 7500 requests
Completed 9000 requests
Completed 10500 requests
Completed 12000 requests
Completed 13500 requests
Completed 15000 requests
Finished 15000 requests


Server Software:        Werkzeug/1.0.1
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /recommendations?sku=Sm3QYKG2uA
Document Length:        3618 bytes

Concurrency Level:      50
Time taken for tests:   616.441 seconds
Complete requests:      15000
Failed requests:        0
Total transferred:      56475000 bytes
HTML transferred:       54270000 bytes
Requests per second:    24.33 [#/sec] (mean)
Time per request:       2054.803 [ms] (mean)
Time per request:       41.096 [ms] (mean, across all concurrent requests)
Transfer rate:          89.47 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.8      1      84
Processing:   105 2051 262.6   2091    2955
Waiting:       92 2024 257.2   2054    2935
Total:        105 2052 262.5   2092    2955
WARNING: The median and mean for the initial connection time are not within a normal deviation
        These results are probably not that reliable.

Percentage of the requests served within a certain time (ms)
  50%   2092
  66%   2187
  75%   2239
  80%   2271
  90%   2358
  95%   2424
  98%   2491
  99%   2552
 100%   2955 (longest request)
```
