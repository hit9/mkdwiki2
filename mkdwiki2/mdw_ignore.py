import mdw, mdw_report

import os, fnmatch

def ignore_mdw(file_path): # ignore mkdwiki2 file:tpl.html , .fn_ignore amd path_ignore
    if os.path.normpath(file_path) in map(os.path.normpath, mdw.ignore_mdw_files):
        mdw.skip_files[file_path] = 'mkdwiki2 file.'
        return False
    return True

def user_ignore_rules_gen():
    mdw.user_ignore_rules_fn = map(lambda x:x.strip('\n'), open(mdw.fn_ignore_path).readlines()) if os.path.exists(mdw.fn_ignore_path) else []
    mdw.user_ignore_rules_path = map(lambda x:x.strip('\n'), open(mdw.path_ignore_path).readlines()) if os.path.exists(mdw.path_ignore_path) else []

def ignore_user(file_path):
    d = [
        (mdw.user_ignore_rules_fn, os.path.basename, 'ignored by filename'), 
        (mdw.user_ignore_rules_path, lambda x:os.path.relpath(x, mdw.src_dirname), 'ignored by path')
    ]
    
    for i in d:
        for m in i[0]:
            if fnmatch.fnmatch(i[1](file_path), m):
                mdw.skip_files[file_path] = i[2]
                mdw_report.warning('ignore', '\''+file_path+'\'  <->  \''+m+'\'')
                return False
        return True
