import os

# LOCAL
from ElasConnect import ElasConnect
from ElasModules import ElasModules
from ElasIndex import ElasIndex
from ElasCompare import ElasCompare
from ElasPut import PutDoc


def check_directory(_directory):
    if not os.path.exists(_directory):
        os.mkdir(_directory)
    else:
        print(f"{directory} - Dir already exist!")


api_used = ["cmhl", "mit", "zait", "ccn", "oway", "auderbox"]

for name in api_used:
    connector = ElasConnect(name).elas_connect()
    elas_index_data = connector.cat.indices(index="*", format="json")
    modules = ElasModules(name).elas_modules()
    filtered_index_data = ElasIndex(elas_index_data, modules).get_index_data()

    directory = f"../logs/{name}"

    check_directory(_directory=directory)
    dps = ElasCompare(filtered_index_data, directory=directory).compare_index()
    PutDoc(name, connector).put_doc()
