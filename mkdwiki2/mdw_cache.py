import os, pickle
import mdw, mdw_report, mdw_core

def clean():
    mdw_core.check_cwd()
    write_cache({})
    mdw_report.success('cache clean')

def get_cache():
    if os.path.exists(mdw.cache_fn):
        try:
            d = pickle.load(open(mdw.cache_fn))
        except:
            mdw_report.error('cache pickle error. rm \''+mdw.cache_fn+'\' for a try')
        if type({}) != type(d) :
            mdw_report.error('cache type error. rm \''+mdw.cache_fn+'\' for a try')
    else:
        d = {}
    return d

def write_cache(d):
    pickle.dump(d, open(mdw.cache_fn, 'w'))

def ifilter(cache_dict, file_path):
    # only when file_path in cache_dict and it is not modefied,filter it out from file_list
    for i in cache_dict.iterkeys():
        if os.path.samefile(i, file_path) :
            if os.stat(file_path).st_mtime == cache_dict[i] :
                mdw.skip_files[file_path] = 'cached file'
                return False
    return True
