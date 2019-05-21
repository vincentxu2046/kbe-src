"""
使用说明
实时修改module，调用cluster_controller runscript reload
可以在不重启服务器的情况下reload module模块
"""


import pydevd_reload as r
module = ""
r.xreload(module)