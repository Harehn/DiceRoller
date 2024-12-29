:: Thanks to this link
:: https://stackoverflow.com/a/28421514/28974846
:: https://stackoverflow.com/a/51870885/28974846
start cmd.exe /k .\.venv\Scripts\python.exe .\Backend\server.py
cd Frontend/diceroller
start cmd.exe /c npm run serve
cd ..
cd ..
timeout -t 10
start firefox -new-window http://127.0.0.1:5000
timeout -t 10
start firefox http://127.0.0.1:8080