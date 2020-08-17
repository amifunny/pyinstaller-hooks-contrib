import os
import sys
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.compat import is_win


hiddenimports = [
    "pyproj.datadir"
]

datas = collect_data_files('pyproj')

if hasattr(sys, 'real_prefix'):  # check if in a virtual environment
    root_path = sys.real_prefix
else:
    root_path = sys.prefix

# - conda-specific
if is_win:
    tgt_proj_data = os.path.join('Library', 'share', 'proj')
    src_proj_data = os.path.join(root_path, 'Library', 'share', 'proj')

else:  # both linux and darwin
    tgt_proj_data = os.path.join('share', 'proj')
    src_proj_data = os.path.join(root_path, 'share', 'proj')

if os.path.exists(src_proj_data):
    datas.append((src_proj_data, tgt_proj_data))
    # a real-time hook takes case to define the path for `PROJ_LIB`