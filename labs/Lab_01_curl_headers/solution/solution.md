# HTTP HTTPS и их параметры
### Лабораторная работа №1

**Цель:** Познакомиться с протоколом HTTP и протоколом HTTPS, используя **curl**, а так же особенностями установления соединения между источником и получателем.

***Сurl*** будет использоваться для получения информации с таких источников как:

>* <https://www.rgups.ru/>
>* <https://github.com/>
>* <https://www.rzd.ru/>
>* <https://dzen.ru/?yredirect=true>
>* <https://www.python.org/>

## Значения ключей, которые будут использоваться

* **I** - Этот ключ указывает отправить только заголовки HTTP-ответа сервера, без тела ответа.

* **L** - Этот ключ указывает следовать перенаправлениям при запросе, если сервер возвращает код (301 или 302).

* **k** - Этот ключ отключает проверку SSL-сертификата.

## Начало работы с **curl**

### 1. РГУПС

**GET** запрос на сайт ***РГУПС:***

```
curl -kIL rgups.com
```

**HTTP** ответ с сайта ***РГУПС:***

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:--  0:00:01 --:--:--     0HTTP/1.1 301 Moved Permanently
Date: Sun, 17 Sep 2023 19:03:57 GMT
Server: Apache
X-Powered-By: PHP/7.3.33
X-Redirect-By: WordPress
Upgrade: h2,h2c
Connection: Upgrade
Location: https://rgups.com/
Content-Type: text/html; charset=UTF-8

HTTP/1.1 200 OK
Date: Sun, 17 Sep 2023 19:03:58 GMT
Server: Apache
X-Powered-By: PHP/7.3.33
Link: <https://rgups.com/wp-json/>; rel="https://api.w.org/", <https://rgups.com/wp-json/wp/v2/pages/1222>; rel="alternate"; type="application/json", <https://rgups.com/>; rel=shortlink
Upgrade: h2,h2c
Connection: Upgrade
Content-Type: text/html; charset=UTF-8
```

### Разбор ответа построчно

* ***Date: Sun, 17 Sep 2023 19:03:57 GMT*** - время, в которое мы совершили **GET** запрос.
* ***Server: Apache*** - имя сервера, выполняющего запрос.
* ***X-Powered-By: PHP/7.3.33*** - версия **PHP**, которая обрабатывает скрипты.
* ***X-Redirect-By: WordPress*** - указывает, что произошло переопределение на другую страницу с использованием WordPress.
* ***Upgrade: h2,h2c*** - указывает на протоколы, которые сервер поддерживает для обновления соединения.
* ***Connection: Upgrade*** - указывает, что сервер готов обновить соединение с клиентом.
* ***Location: https://rgups.com/*** - указывает новый URL-адрес, на который произошло перенаправление.
* ***Content-Type: text/html; charset=UTF-8*** - указывает тип содержимого ответа (HTML) и его кодировку (UTF-8).
* ***HTTP/1.1 200 OK*** - статус ответа от сервера.
* ***Link: <https://rgups.com/wp-json/>; rel="https://api.w.org/", <https://rgups.com/wp-json/wp/v2/pages/1222>; rel="alternate"; type="application/json", <https://rgups.com/>; rel=shortlink*** - ссылки на внешние источники.

### 2. GitHub

**GET** запрос на сайт ***GitHub:***

```
curl -kIL curl -kIL https://github.com/

```

**HTTP** ответ с сайта ***GitHub:***

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 OK
Server: GitHub.com
Date: Sun, 17 Sep 2023 21:08:40 GMT
Content-Type: text/html; charset=utf-8
Vary: X-PJAX, X-PJAX-Container, Turbo-Visit, Turbo-Frame, Accept-Language, Accept-Encoding, Accept, X-Requested-With
content-language: en-US
ETag: W/"725535ba193e1ab9c104b6189b7aba19"
Cache-Control: max-age=0, private, must-revalidate
Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
X-Frame-Options: deny
X-Content-Type-Options: nosniff
X-XSS-Protection: 0
Referrer-Policy: origin-when-cross-origin, strict-origin-when-cross-origin
Content-Security-Policy: default-src 'none'; base-uri 'self'; child-src github.com/assets-cdn/worker/ gist.github.com/assets-cdn/worker/; connect-src 'self' uploads.github.com www.githubstatus.com collector.github.com raw.githubusercontent.com api.github.com github-cloud.s3.amazonaws.com github-production-repository-file-5c1aeb.s3.amazonaws.com github-production-upload-manifest-file-7fdce7.s3.amazonaws.com github-production-user-asset-6210df.s3.amazonaws.com cdn.optimizely.com logx.optimizely.com/v1/events objects-origin.githubusercontent.com *.actions.githubusercontent.com productionresultssa0.blob.core.windows.net/ productionresultssa1.blob.core.windows.net/ productionresultssa2.blob.core.windows.net/ productionresultssa3.blob.core.windows.net/ productionresultssa4.blob.core.windows.net/ productionresultssa5.blob.core.windows.net/ productionresultssa6.blob.core.windows.net/ productionresultssa7.blob.core.windows.net/ productionresultssa8.blob.core.windows.net/ productionresultssa9.blob.core.windows.net/ wss://*.actions.githubusercontent.com github-production-repository-image-32fea6.s3.amazonaws.com github-production-release-asset-2e65be.s3.amazonaws.com insights.github.com wss://alive.github.com github.githubassets.com; font-src github.githubassets.com; form-action 'self' github.com gist.github.com objects-origin.githubusercontent.com; frame-ancestors 'none'; frame-src viewscreen.githubusercontent.com notebooks.githubusercontent.com support.github.com; img-src 'self' data: github.githubassets.com media.githubusercontent.com camo.githubusercontent.com identicons.github.com avatars.githubusercontent.com github-cloud.s3.amazonaws.com objects.githubusercontent.com secured-user-images.githubusercontent.com/ user-images.githubusercontent.com/ private-user-images.githubusercontent.com opengraph.githubassets.com github-production-user-asset-6210df.s3.amazonaws.com customer-stories-feed.github.com spotlights-feed.github.com objects-origin.githubusercontent.com *.githubusercontent.com; manifest-src 'self'; media-src github.com user-images.githubusercontent.com/ secured-user-images.githubusercontent.com/ private-user-images.githubusercontent.com github.githubassets.com; script-src github.githubassets.com; style-src 'unsafe-inline' github.githubassets.com; upgrade-insecure-requests; worker-src github.com/assets-cdn/worker/ gist.github.com/assets-cdn/worker/
Set-Cookie: _gh_sess=K6F2pHceC2%2BxNGTUOEtv4RjITaJkKFZ8VHyVZHk5YdCcYlAysAfvXBLQ%2FQDNMImK0LP6V7MI1FzxdPJ5sX2yCt4b4nc8%2FjziZnH6BtQLfnl5Za4CYHEYAGwiGr0erfb9CByVHlJYr%2FDqfQC6engffByzUJXkZ8okzPrXtGmLfAEwrjcS6pPUjAmwyTkFcReJ3Vczo1yPxyi1owYCG6DrXwg%2F3EvD4MuZD3Wn%2F1LZk5WT5cfBYSoDwXfEqfQukcOGhxIHt7jgTxpj5H3iJAbOIA%3D%3D--1aHHeIDjBfx3GKuk--rVHhOoHxNO8xwKPbKELPcA%3D%3D; Path=/; HttpOnly; Secure; SameSite=Lax
Set-Cookie: _octo=GH1.1.1466902783.1694984923; Path=/; Domain=github.com; Expires=Tue, 17 Sep 2024 21:08:43 GMT; Secure; SameSite=Lax
Set-Cookie: logged_in=no; Path=/; Domain=github.com; Expires=Tue, 17 Sep 2024 21:08:43 GMT; HttpOnly; Secure; SameSite=Lax
Accept-Ranges: bytes
X-GitHub-Request-Id: 50FA:0F8B:1C9A4AC1:1CFE14A7:65076ADB

```

### Разбор ответа построчно

* ***Server: GitHub.com*** - имя сервера, на который был отправлен запрос.
* ***Content-Type: text/html; charset=utf-8*** - указывает тип контента ответа, в данном случае это текстовый HTML документ с кодировкой UTF-8.
* ***Vary: X-PJAX, X-PJAX-Container, Turbo-Visit, Turbo-Frame, Accept-Language, Accept-Encoding, Accept, X-Requested-With*** - указывает на заголовки запроса, на основании которых сервер определяет, должен ли он возвращать кэшированный ответ или генерировать новый.
* ***content-language: en-US*** - указывает на язык содержимого ответа.
* ***ETag: W/"725535ba193e1ab9c104b6189b7aba19"*** - указывает на уникальный идентификатор версии ответа, который используется для кэширования.
* ***Cache-Control: max-age=0, private, must-revalidate*** - указывает на правила кэширования для клиента и прокси-серверов.
* ***Strict-Transport-Security: max-age=31536000; includeSubdomains; preload*** - указывает на политику безопасности для защищенного соединения.
* ***X-Frame-Options: deny*** - указывает на ограничения для встраивания страницы во фреймы.
* ***X-Content-Type-Options: nosniff*** - указывает на запрет преобразования типа контента сервером.
* ***X-XSS-Protection: 0*** - указывает на отключение защиты от межсайтового скриптинга.
* ***Referrer-Policy: origin-when-cross-origin, strict-origin-when-cross-origin*** - указывает на политику отправки заголовка Referer при переходе с других источников.
* ***Content-Security-Policy*** - указывает на политику безопасности контента, ограничивающую источники данных и ресурсов.
* ***Set-Cookie: _gh_sess=...*** - указывает на установку куки сессии для сохранения состояния пользователя.
* *** Accept-Ranges: bytes*** - указывает на то, что сервер поддерживает диапазоны байтов при загрузке файла.
* ***X-GitHub-Request-Id: 50FA:0F8B:1C9A4AC1:1CFE14A7:65076ADB*** - указывает на уникальный идентификатор запроса на сервере GitHub.

**GET** запрос на сайт ***РЖД:***

```
curl -kIL https://www.rzd.ru/

```

**HTTP** ответ с сайта ***РЖД:***

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0   109    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 403 Forbidden
Connection: close
Content-Length: 109
Content-Type: text/html

```

### Разбор ответа построчно

* ***Connection: close*** - указывает, что после завершения ответа сервер закрывает соединение с клиентом. Это означает, что клиент должен установить новое соединение для последующих запросов.
* ***Content-Length: 109*** - указывает размер тела ответа в байтах. Это позволяет клиенту знать, сколько данных он должен ожидать по сети.
* ***Content-Type: text/html*** - указывает тип контента ответа, в данном случае это HTML-документ. Это позволяет клиенту правильно интерпретировать данные и отобразить их для пользователя.

**GET** запрос на сайт ***Яндекс:***

```
curl -kIL https://dzen.ru/?yredirect=true

```

**HTTP** ответ с сайта ***Яндекс:***

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 Ok
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
Content-Security-Policy-Report-Only: default-src 'none'; connect-src 'self' an.yandex.ru strm.yandex.ru *.strm.yandex.net mc.yandex.ru yandex.st yastatic.net matchid.adfox.yandex.ru adfox.yandex.ru ads.adfox.ru ads6.adfox.ru jstracer.yandex.ru yastat.net yandex.ru awaps.yandex.net awaps.yandex.ru verify.yandex.ru *.verify.yandex.ru favicon.yandex.net pixel.adsafeprotected.com tps.doubleverify.com ad.adriver.ru amc.yandex.ru *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru mc.yandex.az mc.yandex.by mc.yandex.co.il mc.yandex.com mc.yandex.com.am mc.yandex.com.ge mc.yandex.com.tr mc.yandex.ee mc.yandex.fr mc.yandex.kg mc.yandex.kz mc.yandex.lt mc.yandex.lv mc.yandex.md mc.yandex.tj mc.yandex.tm mc.yandex.ua mc.yandex.uz mc.admetrica.ru yandexmetrica.com yandexmetrica.com:29009 yandexmetrica.com:30102 forms-ext-api.yandex.ru strm.yandex.net *.strm.yandex.ru *.cdn.ngenix.net zen-rc3.yandex.ru frontend.vh.yandex.ru https://vh.test.yandex.ru/live/ wss://push.yandex.ru api.passport.yandex.ru api.passport-test.yandex.ru suggest-maps.yandex.ru/suggest-geo vk.ru static.dzeninfra.ru avatars.dzeninfra.ru cdn.dzen.ru video.dzen.ru log.dzen.ru playlog.dzen.ru cdn.dzeninfra.ru *.cdn.dzeninfra.ru *.extcdn.dzeninfra.ru *.hot-video.dzeninfra.ru cold-video.dzeninfra.ru *.cold-video.dzeninfra.ru s3.dzeninfra.ru *.s3.dzeninfra.ru *.ms.dzen.ru notify.dzen.ru clck.dzen.ru static-mon.yandex.net cloud-api.yandex.ru yandex.ru dzen.ru *.adlooxtracking.com *.adlooxtracking.ru *.adsafeprotected.com *.doubleverify.com *.moatads.com *.serving-sys.com *.serving-sys.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net *.mycdn.me *.vkuser.net; frame-src awaps.yandex.net yandexadexchange.net *.yandexadexchange.net yastatic.net *.yandex.ru banners.adfox.ru yastat.net yandex.ru storage.mds.yandex.net *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru blob: mc.yandex.ru mc.yandex.md zenadservices.net sso.passport.yandex.ru id.vk.com *.dzen.ru sso.dzen.ru static.dzeninfra.ru suggest.dzen.ru 'self' yandex.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net *.mycdn.me *.vkuser.net *.doubleverify.com *.doubleclick.net; img-src 'self' data: avatars-fast.yandex.net favicon.yandex.net an.yandex.ru banners.adfox.ru content.adfox.ru ads6.adfox.ru tns-counter.ru *.tns-counter.ru s3.mds.yandex.net ads.adfox.ru amc.yandex.ru mc.admetrica.ru wcm-ru.frontend.weborama.fr wcm.solution.weborama.fr ad.adriver.ru bs.serving-sys.com ad.doubleclick.net counter.yadro.ru gdeby.hit.gemius.pl mc.yandex.ru verify.yandex.ru *.verify.yandex.ru yastatic.net yastat.net avatars.mds.yandex.net yandex.ru px.moatads.com awaps.yandex.net awaps.yandex.ru gdero.hit.gemius.pl pixel.adlooxtracking.com tps.doubleverify.com impression.appsflyer.com rgi.io track.rutarget.ru ssl.hurra.com pixel.adsafeprotected.com storage.mds.yandex.net *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru mc.yandex.az mc.yandex.by mc.yandex.co.il mc.yandex.com mc.yandex.com.am mc.yandex.com.ge mc.yandex.com.tr mc.yandex.ee mc.yandex.fr mc.yandex.kg mc.yandex.kz mc.yandex.lt mc.yandex.lv mc.yandex.md mc.yandex.tj mc.yandex.tm mc.yandex.ua mc.yandex.uz mc.webvisor.org *.mediascope.mc.yandex.ru avatars.mdst.yandex.net zen.s3.yandex.net strm.yandex.ru strm.yandex.net sso.passport.yandex.ru dzen.ru avatars.dzeninfra.ru static.dzeninfra.ru cdn.dzen.ru video.dzen.ru log.dzen.ru playlog.dzen.ru s3.dzeninfra.ru *.ms.dzen.ru *.s3.dzeninfra.ru *.zen.yandex.com *.m-counter.ru www.m-counter.ru www.tns-counter.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net *.mycdn.me *.vkuser.net *.doubleverify.com *.adsafeprotected.com *.serving-sys.com *.serving-sys.ru *.weborama.fr *.weborama-tech.ru *.hit.gemius.pl consentmanager.mgr.consensu.org cdn.consentmanager.mgr.consensu.org *.adlooxtracking.com *.adlooxtracking.ru vk.com vk.ru *.userapi.c  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0ent.adfox.ru data: yastat.net *.mycdn.me *.vkuser.net *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru blob: *.strm.yandex.net *.cdn.ngenix.net cdn.dzen.ru video.dzen.ru *.cdn.dzeninfra.ru *.extcdn.dzeninfra.ru *.hot-video.dzeninfra.ru cold-video.dzeninfra.ru *.cold-video.dzeninfra.ru *.s3.dzeninfra.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net; script-src 'unsafe-inline' 'unsafe-eval' an.yandex.ru yandex.st yastatic.net mc.yandex.ru banners.adfox.ru ads.adfox.ru ads6.adfox.ru yastat.net yandex.ru z.moatads.com storage.mds.yandex.net *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru mc.yandex.az mc.yandex.by mc.yandex.co.il mc.yandex.com mc.yandex.com.am mc.yandex.com.ge mc.yandex.com.tr mc.yandex.ee mc.yandex.fr mc.yandex.kg mc.yandex.kz mc.yandex.lt mc.yandex.lv mc.yandex.md mc.yandex.tj mc.yandex.tm mc.yandex.ua mc.yandex.uz chat.s3.yandex.net sso.dzen.ru sso.passport.yandex.ru static.dzeninfra.ru 'self' *.zen.yandex.com dzen.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net *.mycdn.me *.vkuser.net *.adlooxtracking.com *.adlooxtracking.ru *.adsafeprotected.com *.doubleverify.com *.moatads.com *.dvtps.com *.doubleclick.net *.serving-sys.ru *.userapi.com vk.com vk.ru *.vk.com *.vk.ru; style-src 'unsafe-inline' 'unsafe-eval' yandex.st yastatic.net banners.adfox.ru content.adfox.ru yastat.net *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru yandex.ru static.dzeninfra.ru 'self' *.zen.yandex.com dzen.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net *.mycdn.me *.vkuser.net; font-src 'self' data: an.yandex.ru yastatic.net yastat.net *.tunneler-si.dzen.ru *.tun.si.dzen.ru http-check-headers.yandex.ru static.dzeninfra.ru *.mail.ru *.mradx.net *.imgsmail.ru *.criteo.com *.criteo.net *.mycdn.me *.vkuser.net fonts.gstatic.com; child-src blob: mc.yandex.ru; manifest-src *.dzen.ru/manifest.webmanifest 'self'; report-uri https://csp.yandex.net/csp?from=zen_old&project=zen&yandex_login=&yandexuid=1357229281694985913&requestid=2879467022.211.1694985913289.81266&page=site_desktop;
Content-Type: text/html; charset=utf-8
Set-Cookie: _yasc=u6BgD/mIAEVilonOfnehF0rVCkjpqz/sBxm7deKnbFKgUbrdUIfom3QeZB9txxDS; domain=.dzen.ru; path=/; expires=Wed, 14 Sep 2033 21:25:13 GMT; secure
X-Content-Type-Options: nosniff
X-Frame-Options: deny
X-Requestid: 2879467022.211.1694985913289.81266
X-XSS-Protection: 1; mode=block
X-Yandex-Req-Id: 1694985913272908-592968595020974714500115-production-app-host-vlx-zen-264

```

**GET** запрос на сайт ***Python:***

```
curl -kIL https://www.python.org/

```

**HTTP** ответ с сайта ***Python:***

```
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0 50144    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0HTTP/1.1 200 OK
Connection: keep-alive
Content-Length: 50144
Server: nginx
Content-Type: text/html; charset=utf-8
X-Frame-Options: SAMEORIGIN
Via: 1.1 vegur, 1.1 varnish, 1.1 varnish
Accept-Ranges: bytes
Date: Sun, 17 Sep 2023 21:28:33 GMT
Age: 3429
X-Served-By: cache-iad-kiad7000025-IAD, cache-fra-eddf8230102-FRA
X-Cache: HIT, HIT
X-Cache-Hits: 315, 14
X-Timer: S1694986114.831538,VS0,VE0
Vary: Cookie
Strict-Transport-Security: max-age=63072000; includeSubDomains; preload
```