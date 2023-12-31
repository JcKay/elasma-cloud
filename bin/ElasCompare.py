from ElasLogs import ElasLogs


def dps_to_total_dps(dps):
    dps_ft = float(dps[:-2])
    if dps.endswith("gb"):
        return dps_ft * 1024  # Convert MB

    elif dps.endswith("mb"):
        return dps_ft  # Original MB

    else:
        return 0


def calc_dps(_eid_pss, _lid_pss, _eid_ss, _lid_ss):
    _eid_pss_ft = float(_eid_pss[:-2])
    _eid_ss_ft = float(_eid_ss[:-2])
    _lid_pss_ft = float(_lid_pss[:-2])
    _lid_ss_ft = float(_lid_ss[:-2])
    if _eid_pss.endswith('gb') and _lid_pss.endswith("gb"):
        _dps = _eid_pss_ft - _lid_pss_ft
        if _dps < 0:
            _dps = _eid_ss_ft - _lid_ss_ft
            if _dps < 0:
                _dps = _eid_pss_ft
            else:
                _dps = _dps / 2
        _dps = str(round(_dps, 2)) + "gb"
        return _dps

    elif _eid_pss.endswith('gb') and _lid_pss.endswith('mb'):
        _dps = str(round((((_eid_pss_ft * 1024) - _lid_pss_ft) / 1024), 2)) + "gb"
        return _dps

    elif _eid_pss.endswith('mb') and _lid_pss.endswith('gb'):
        _dps = _eid_pss
        return _dps

    else:
        _dps = _eid_pss_ft - _lid_pss_ft
        if _dps < 0:
            _dps = _eid_ss_ft - _lid_ss_ft
            if _dps < 0:
                _dps = _eid_pss_ft
            else:
                _dps = _dps / 2
        _dps = str(round(_dps, 2)) + "mb"
        return _dps


class ElasCompare:
    def __init__(self, elas_index_data, directory):
        self.elas_index_data = elas_index_data
        self.logs = ElasLogs(_directory=directory)
        self.filenames_list = self.logs.file_list
        self.total_dps = 0

    def compare_index(self):
        for string, eid in self.elas_index_data.items():  # loop elas_index_data
            if string in self.filenames_list:  # loop filenames from logs
                lid = self.logs.read_previous_logs(string)  # get data from logs
                if lid is None or "pri_store_size" not in lid:  # check pss and none
                    self.total_dps += dps_to_total_dps(eid['pri_store_size'])
                    self.logs.add_to_logs(filename=string, source=eid, dps=eid['pri_store_size'])

                else:
                    eid_pss = eid["pri_store_size"]
                    lid_pss = lid["pri_store_size"]
                    eid_ss = eid["store_size"]
                    lid_ss = lid["store_size"]
                    dps = calc_dps(eid_pss, lid_pss, eid_ss, lid_ss)
                    self.total_dps += dps_to_total_dps(dps)
                    self.logs.add_to_logs(filename=string, source=eid, dps=dps)

            else:
                self.total_dps += dps_to_total_dps(eid['pri_store_size'])
                self.logs.add_to_logs(filename=string, source=eid, dps=eid['pri_store_size'])
        self.logs.add_to_logs(filename='tdpss-', source="tdpss-", dps=self.total_dps)
