from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("22463709",))
        self.API_HASH = getenv("25c1f59ab1e6bba7b0c31778834de784")
        
        MUST_JOIN_ID = int(getenv("MUST_JOIN_ID", "-100253743252"))
        MUST_JOIN_LINK = getenv("MUST_JOIN_LINK", "t.me/odistupa")


        self.BOT_TOKEN = getenv("8494242239:AAERNwMO_pLZ9onAZfCATFzjN9tbUhAIPT8")
        self.MONGO_URL = getenv("mongodb+srv://yuzimusicbot:i8RaqHtZFvvlP4GZ@cluster0.2ukrc.mongodb.net/?retryWrites=true&w=majority")

        self.LOGGER_ID = int(getenv("LOGGER_ID", -1003700226600"))
        self.OWNER_ID = int(getenv("OWNER_ID", 8313412433))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("BQFWxN0AU-QEKVptFvxQBIpVgsNpp2Cr2sLpp9aw_3rUCar4pMHjFsuUML3Yu1I83JrD8c19cbCX59MpiaTd8rODb56g4fsp1JZcAl3_TZmuMgyL5SvxWlydwcKoVASPBC4PN9ngI0DX9_Uu2-OfTXY3xKB9Tul5ELX1zyvLX82UKjx0W2yDs4V_XB7-fYHCRPDq8SJ2pUtV_ECAqw4FkJ3cRhe3Qp9qzrtbiqRGiJlOhsi2F7N2SNcT6fOXOw4txTlABElcms8ikI3d04C4V-xCuPduAzTdxSnvqXd04SmuiuIiS4FKQ7EgwQoclJsKMEab9vdBlFGzRPWX-1dfbpeBS4dpHgAAAAHMcJ11AA", None)
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/odistupa")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/odistupaF")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"
    
        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "https://batbin.me/tenacious").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
