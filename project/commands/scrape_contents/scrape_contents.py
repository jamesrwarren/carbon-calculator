import requests
import re
from bs4 import BeautifulSoup

URL = "https://www.tesco.com/groceries/en-GB/shop/frozen-food/all"

headers = {
    'authority': 'www.tesco.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'null; null; consumer=default; trkid=bb94ee93-6831-44fa-bf29-d34481fc531b; atrc=892c8e6c-e5f6-4af9-ab85-11a551f62274; DCO=sdc; _csrf=bKPtpu5YNY3jsdz2LIBg11FY; ighs-sess=eyJwYXNzcG9ydCI6eyJ1c2VyIjp7ImlkIjpudWxsfX0sImFuYWx5dGljc1Nlc3Npb25JZCI6IjVkMTk3NWQzN2Y0MTg2ZTY2Y2MwOGQ2ZTBlNWM1M2E4Iiwic3RvcmVJZCI6IjMwNjAifQ==; ighs-sess.sig=aWVfmsdDjnJaC9VkD0RY_Ftv2XQ; null; atrc=892c8e6c-e5f6-4af9-ab85-11a551f62274; AKA_A2=A; bm_sz=7DFD8BC1DE98D91261D9D40D77D2A2D1~YAAQd6cQAgZ9EVSEAQAAnd6nZhHXnMv/kaIe63ms+udljU7PfvKmSWO3YYfbhH9Rc3MfGU5wcjduTbcb4dqryE/M0pqachs0qPlIQqS2RHHn36nOO0GNGrrBBHRIfogSy1BJH2+zhdt9vI38C9Rq7lZf+/Ra2kMQGL7WjWicft0zq+/EgmnNV38K19Xp+u4nDgE3OR7z1a1wCn9BwlKFVzay2e+M4PwzjDY6uAjbe/f4FW6nYewel1Mbb8R5u903z3UsRCdmx9SumNK2qMPBl7ntiO+A+StYrOTDPN/LMbYkBg==~3359794~3617080; bm_mi=A174217C1337CFE8D9C33D416CF04AB8~YAAQd6cQAjx+EVSEAQAAgu+nZhF6ehOXyBnW/PCzMeUg1f+dXtEkgUiIOhXEXuZ31ZWMWjRucMAM0bX8nYcO7CvPWXcxbn3E90RaxVS79pA6QHTtQ/ANAafDh8e/55kMOI/xZCJnNF9FSqiljMP5xSA9cA431blsjS+cR/wyLOvSxmc+NNAHCBHcamuDsCKS8rQ/OtwtZHhXhPKYZl8es0dCNfTVqs3yJ7qiUxAjc7RaIxvMTVie+5HunL6SkxtKc0xgzff9embxBhVyxpPq67heq8R2OlKjkHwu+dlPncij897i8nFbHMtV4CcxdPhRUYZHvN3Kjg==~1; ak_bmsc=8F0BBB2061C62158643BA9C0DDF9C75A~000000000000000000000000000000~YAAQd6cQApWDEVSEAQAArjuoZhESMJlRcQ/dq4FhtTj+lj21IgYugpfOyBVkI4d3VgJyxn3Muzs+BT3kOb3Vtm/fWVzhw8qQa7g1zZeOjTZddrKmucvH5mlyspIoy+hgNOTiXotW0uoPEvPHyJ/ZpaIxJXnw3fVdggAqxkmyGaU/Nwk3YBxf5am/Jx0QTpk1GhwafR9MBGQn80FdM3m9vcWMCqRpv3zLQiXrif+0yeu1QnyrVVWrprSY2/z/E95aqXKGiwlppO9ljzZER+vpwewtLqZB7Pxz6JQ/joBTXCKJN5gxnHkP0a19UqK8O4xh5hF2XAxHQNoBV4WYhh49nYQp0Z95N5YTuSXrjG7h5AHuklSTiBxImtHD+SN4YXHFkbRp961m9n5nYjcbj3Xe7JKxvj35wTbq4gm5bn//8xZxxYUt6qZ+SNyvbtVdSYULdKMWkTXPHvVR/CKfFw2hvotpgHE5EmY7LhIzmxCkZRaKozMP+OalCSxU5YPzMPgroirVhLEEIsY5sgb0; ADRUM=s=1668169714716&r=https%3A%2F%2Fwww.tesco.com%2Fhelp%2Fen-GB%2Fmanage-cookie-preferences%3F1234808750; cookiePreferences=%7B%22experience%22%3Afalse%2C%22advertising%22%3Afalse%7D; _abck=F8EAC1C0B0B4B84BFF541EAF3A17EEF6~0~YAAQbKcQAmqx7WCEAQAAuNWwZgj/SiONc8V19ToJZ9//VOIn1kPyyP/TmF30ZC2DUKXXf5ENEoznM9LtFAcfLMo5cXg+uvLwW1pUUrAJuQIaHE3Vyuw085vQjdWNaifsrYYcQ+2g6YdVj0+bW0drMhMvHhWD2xhkktI36Zk61ZChi9WrwNIwEIGQprG2TPLVFGzgcLfasUkxecuIYpGu9j1F5m/cAAHy7H7l1ek/s3LzTSjGEhCBo6x+tlHrQreUKTVdh89P1UiI7049Nye31sJiGaJLJ/Iq+IppI83GRPYCgsYnlriKQaPkcroSaFPhYvjm7bOZLKVSJYwqZrewuOpz1iQ6Kxcxdoes6fiNw24oZKXefPBxrC8S3gJUUe+88J4MwQVd00vVt/WdMIgsGYLXcFefhzk=~-1~-1~-1; akavpau_tesco_groceries=1668170477~id=3c60360137a90e3edcb0d2680220cf36; bm_sv=AB15A6646C260BF539A28BB381D95023~YAAQbKcQAt+x7WCEAQAAp9qwZhGVbbrcYwTqdtUHB8p5JgZ/7io3fERNZRK241e+xqPpHgk27SiivUWIK7kliUOagRNS7/LOOVqyWmIoHnrDqe/5xnrecyqD3t8z26I+TJAs+k4DI86RyCL4vQU/aMXkZ9R+bYFDQq4scX9KRqg9rSezeQEKwIFS3hsQeB6qDWlYl00VM1gcQckvsKSPY6V3s9VH0arU1l0DjPmQ4qAS8FlKRP7aHTTTwmwf5o8w~1',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
}

response = requests.get('https://www.tesco.com/groceries/en-GB/shop/frozen-food/all', headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

job_elements = soup.find_all("li", class_="product-list--list-item")

href_pattern = re.compile(r"/groceries/en-GB/products/.*?")
class_pattern = re.compile(r"styled__Anchor.*?")
for element in job_elements:
    href = element.find('a', href=href_pattern, class_=class_pattern)["href"]
    product_url = f'https://tesco.com{href}'
    response = requests.get(product_url, headers=headers)
    soup_product = BeautifulSoup(response.content, "html.parser")
    product_title = soup_product.find('h1', class_='product-details-tile__title').text
    product_info = soup_product.find('div', class_='product-info-block product-info-block--ingredients').find('p', class_='product-info-block__content').text
    product_weight = soup_product.find('div', class_='product-info-block product-info-block--net-contents').find('p', class_='product-info-block__content').text
    print(product_title)
    print(product_info)
    print(product_weight)

# go-to-results-page

