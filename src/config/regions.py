REGION_LANG = {
    "ME": "ar",
    "IND": "hi",
    "ID": "id",
    "VN": "vi",
    "TH": "th",
    "BD": "bn",
    "PK": "ur",
    "TW": "zh",
    "EU": "en",
    "CIS": "ru",
    "NA": "en",
    "SAC": "es",
    "BR": "pt"
}

REGION_URLS = {
    "IND": "https://client.ind.freefiremobile.com/",
    "ID": "https://clientbp.ggblueshark.com/",
    "BR": "https://client.us.freefiremobile.com/",
    "ME": "https://clientbp.common.ggbluefox.com/",
    "VN": "https://clientbp.ggblueshark.com/",
    "TH": "https://clientbp.common.ggbluefox.com/",
    "CIS": "https://clientbp.ggblueshark.com/",
    "BD": "https://clientbp.ggblueshark.com/",
    "PK": "https://clientbp.ggblueshark.com/",
    "SG": "https://clientbp.ggblueshark.com/",
    "NA": "https://client.us.freefiremobile.com/",
    "SAC": "https://client.us.freefiremobile.com/",
    "EU": "https://clientbp.ggblueshark.com/",
    "TW": "https://clientbp.ggblueshark.com/"
}

def get_region(language_code: str) -> str:
    """Return language code for a given region"""
    return REGION_LANG.get(language_code)

def get_region_url(region_code: str) -> str:
    """Return URL for a given region code"""
    return REGION_URLS.get(region_code, None)

def LoginUrl(server: str) -> str:
    if server == "IND":
        return "https://ffmconnect.live.gop.garenanow.com/oauth/guest/token/grant"
