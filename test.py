import g4s

if __name__  == "__main__":
    import os

    USERNAME = os.environ.get("g4s_username")
    PASSWORD = os.environ.get("g4s_password")

    alarm = g4s.Alarm(USERNAME, PASSWORD)
    print(alarm)