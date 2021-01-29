import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm, rcParams
import seaborn as sns

str_title="孙耀然能力值"
# labels=np.array([u"力量","敏捷",u"智力",u"耐力",u"财富",u"幸运"])
# stats=[99, 1, 1, 1, 1, 1]
labels=np.array([u"力量","力量",u"力量",u"力量",u"力量",u"力量"])
stats=[99, 99, 99, 99, 99, 99]
# 画图数据准备，角度、状态值

angles_ori=np.linspace(0, 2*np.pi, len(labels), endpoint=False)
stats=np.concatenate((stats,[stats[0]]))
angles=np.concatenate((angles_ori,[angles_ori[0]]))
# 用Matplotlib画蜘蛛图
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)   
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, alpha=0.25)

# 设置中文字体
font = fm.FontProperties(fname=r"C:/Program Files (x86)/Microsoft Office/root/VFS/Fonts/private/MSYH.TTC", size=14)  
ax.set_thetagrids(angles_ori * 180/np.pi, labels, FontProperties=font)
ax.set_title(str_title,fontproperties=font,size=25)
plt.show()