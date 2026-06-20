import requests
import hashlib
import sys
import time


class Website:
    def __init__(self, url):
        self.old_content = ""
        self.url = url

    def get_old_content(self):
        try:
            with open("old_content.txt", "r") as f:
                self.old_content = f.read()
        except FileNotFoundError:
            pass

    def request_new_content(self):
        response = requests.get(self.url)
        self.new_content = response.text
        if response.status_code != 200:
            print(f"ERROR: HTTP {response.status_code}")
            sys.exit()
        self.encrypt_new_content()

    def encrypt_new_content(self):
        self.new_content = hashlib.md5(self.new_content.encode()).hexdigest()

    def compare_content(self):
        self.get_old_content()
        self.request_new_content()
        if not self.old_content:
            print("FIRST RUN, SAVING THE CONTENT!")
            self.save_new_content()
        elif self.new_content != self.old_content:
            print("WEBPAGE CONTENT CHANGED!!")
            self.save_new_content()
        else:
            print("NO CHANGE!")

    def save_new_content(self):
        with open("old_content.txt", "w") as f:
            f.write(self.new_content)


def main():
    url = input("ENTER URL: ")
    while True:
        try:
            interval = float(
                input("ENTER TIME INTERVAL FOR PERIODICAL CHECK ( in minutes ): "))
        except ValueError:
            print("ENTER REAL NUMBERS ONLY!")
            continue
        break

    interval = interval*60
    web_content = Website(url)
    while True:
        web_content.compare_content()
        time.sleep(interval)


if __name__ == "__main__":
    main()
