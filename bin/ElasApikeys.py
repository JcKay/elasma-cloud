class ElasAPIkeys:
    def __init__(self, name):
        self.name = name

    def elas_apikey(self):
        apikey_dict = {
            "cmhl": {
                "apikey_id": "eTsNmIoBK39i9M4oPabh",
                "apikey_secret": "bWVQHBDtQM2L6FIUZa9nrA",
                "apikey_base64": "ZVRzTm1Jb0JLMzlpOU00b1BhYmg6YldWUUhCRHRRTTJMNkZJVVphOW5yQQ=="
            },
            "mit": {
                "apikey_id": "JykHpIoBRAGcV7cPg5HX",
                "apikey_secret": "mLRsPjcqR0Sx3FG070vEvQ",
                "apikey_base64": "SnlrSHBJb0JSQUdjVjdjUGc1SFg6bUxSc1BqY3FSMFN4M0ZHMDcwdkV2UQ=="
            },
            "zait": {
                "apikey_id": "ei4JpIoB8wmDSIYB-ajd",
                "apikey_secret": "EnJwXzH-QHG479xbc6rxqw",
                "apikey_base64": "ZWk0SnBJb0I4d21EU0lZQi1hamQ6RW5Kd1h6SC1RSEc0Nzl4YmM2cnhxdw=="
            },
            "ccn": {
                "apikey_id": "LeGXrIoBGqLwwqXfDCUy",
                "apikey_secret": "7FTvn2vkS8Wdn7phPIvI-Q",
                "apikey_base64": "TGVHWHJJb0JHcUx3d3FYZkRDVXk6N0ZUdm4ydmtTOFdkbjdwaFBJdkktUQ=="
            },
            "oway": {
                "apikey_id": "SsearIoBG1oxNVJEMkJu",
                "apikey_secret": "7otBVkMqSOq8WKfgKlejYg",
                "apikey_base64": "U3NlYXJJb0JHMW94TlZKRU1rSnU6N290QlZrTXFTT3E4V0tmZ0tsZWpZZw=="
            },
            "auderbox": {
                "apikey_id": "Zo2crIoBRI88kg3wjMrh",
                "apikey_secret": "83Kfm07ZR6unbS7XW2HzGw",
                "apikey_base64": "Wm8yY3JJb0JSSTg4a2czd2pNcmg6ODNLZm0wN1pSNnVuYlM3WFcySHpHdw=="
            },
            "dev": {
                "apikey_id": "XPG_A4sBcXnoItZdLA41",
                "apikey_secret": "T55MMqOWRlCkhga-35lLcg",
                "apikey_base64": "WFBHX0E0c0JjWG5vSXRaZExBNDE6VDU1TU1xT1dSbENraGdhLTM1bExjZw=="
            }
        }

        return apikey_dict[self.name]
