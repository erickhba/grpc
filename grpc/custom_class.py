import requests

class FakeDataAPI():
    def get_comments():
        response = requests.get("https://jsonplaceholder.typicode.com/posts/")
        return response.content
    
if __name__ == "__main__":
    print(FakeDataAPI.get_comments())