import requests


def test_upload():
    r = requests.post('http://127.0.0.1:8000/upload', data={'content': '这是复制内容'})
    print(r.text)


if __name__ == '__main__':
    test_upload()
