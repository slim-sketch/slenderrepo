#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt

# 画一个小星星图标
fig, ax = plt.subplots(figsize=(3,3))
# 五角星坐标
import numpy as np
theta = np.linspace(0, 2*np.pi, 6)
r = np.array([1,0.4,1,0.4,1,1])
x = r * np.cos(theta)
y = r * np.sin(theta)
ax.fill(x,y,color='#ffb900')
ax.set_xlim(-1.2,1.2)
ax.set_ylim(-1.2,1.2)
ax.axis('off')
plt.show()


# In[2]:


from IPython.display import display, Markdown
display(Markdown("# 🎉✨💻🐍\n## Python + Jupyter 图标展示\n> 🌟⭐⚡📊📈🔍"))


# In[3]:


import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(3,3))
circle = plt.matplotlib.patches.Circle((0,0), 0.8, color="#4285F4")
ax.add_patch(circle)
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.axis("equal")
ax.axis("off")
plt.show()


# In[4]:


import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2*np.pi, 200)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) -5 * np.cos(2*t) -2*np.cos(3*t)-np.cos(4*t)

plt.figure(figsize=(3,3))
plt.fill(x,y,color='#ff4466')
plt.axis("off")
plt.show()


# In[ ]:




