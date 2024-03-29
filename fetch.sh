#!/bin/bash

curl 'https://www.strava.com/clubs/1227058/leaderboard' \
  -H 'accept: text/javascript, application/javascript, application/ecmascript, application/x-ecmascript' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'dnt: 1' \
  -H 'referer: https://www.strava.com/clubs/1227058' \
  -H 'sec-ch-ua: "Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  -H 'sec-fetch-dest: empty' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-site: same-origin' \
  -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
  -H 'x-requested-with: XMLHttpRequest' \
  -o data/results.json
