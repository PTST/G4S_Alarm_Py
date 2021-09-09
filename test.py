import g4s

if __name__  == "__main__":
    import os

    USERNAME: str = os.environ["g4s_username"]
    PASSWORD: str = os.environ["g4s_password"]

    alarm = g4s.Alarm(USERNAME, PASSWORD)
    print(alarm)