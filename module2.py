# Original code that i tried to run
import pandas
# 'import pyvis'
from pyvis.network import Network
# importing networkx for whatever reason
import networkx as nx
# create vis network
got_net = Network("3000px","3000px")
# load the network graph
# df = pandas.read_csv("C:\\Users\\hqure\\Documents\\School folder\\BROCK U\\YEAR 5\\CHEM 3P20\\Presentation\\edges_final_network.csv", 
    # sep=_NoDefault.no_default, 
    # delimiter=None, header='infer', 
    # names=_NoDefault.no_default, 
    # index_col=None, usecols=None, squeeze=None, 
    # prefix=_NoDefault.no_default, 
    # mangle_dupe_cols=True, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, 
    # skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, verbose=False, 
    # skip_blank_lines=True, parse_dates=None, infer_datetime_format=False, keep_date_col=False, date_parser=None, 
    # dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', 
    # lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, 
    # encoding_errors='strict', dialect=None, error_bad_lines=None, warn_bad_lines=None, on_bad_lines=None, 
    # delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None, storage_options=None
    #                )
H = nx.from_pandas_edgelist(pandas.read_csv(("C:\\Users\\hqure\\Documents\\School folder\\BROCK U\\YEAR 5\\CHEM 3P20\\Presentation\\edges_final_network.csv"),
                            source='Source',
                            target='Target',
                            edge_attr='weight')
got_net.barnes_hut()
got_data = pd.read_csv("C:\\Users\\hqure\\Documents\\School folder\\BROCK U\\YEAR 5\\CHEM 3P20\\Presentation\\edges_final_network.csv")

nt.from_nx(H)
got_net.show("example.html")


