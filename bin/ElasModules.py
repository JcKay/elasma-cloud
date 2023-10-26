class ElasModules:
    def __init__(self, name):
        self.name = name

    def elas_modules(self):
        CMHL = [
            "auditbeat-",
            "winlogbeat-",
            "auditd.log-",
            "logs-endpoint.",
            "logs-system.",
            "logs-windows.",
            "fortinet_fortigate.log-",
        ]

        MIT = [
            "logs-endpoint.",
            "logs-system.",
            "logs-windows.",
            "logs-apache.access-",
            "logs-modsecurity.auditlog-",
            "logs-auditd.log-",
            "logs-o365.audit-",
            "logs-azure.activitylogs-",
            "azure-access-"
        ]

        ZAIT = [
            "logs-endpoint.",
            "logs-system.",
            "logs-elastic_agent.",
            "nginx.access-"
        ]

        CCN = [
            "logs-aws.",
            "logs-system.",
            "logs-windows.",
            "logs-auditd.log-",
            "logs-apache.access-",
        ]

        OWAY = [
            "logs-endpoint.",
            "logs-nginx.",
            "logs-system.",
            "logs-auditd.log-",
        ]

        AUDERBOX = [
            "logs-apache.access-",
            "logs-windows.",
            "logs-system.",
        ]

        lists_dict = {
            "cmhl": CMHL,
            "mit": MIT,
            "zait": ZAIT,
            "ccn": CCN,
            "oway": OWAY,
            "auderbox": AUDERBOX,
        }

        return lists_dict[self.name]
