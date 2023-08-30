import matplotlib
from attrdef import DmgApfAttr, SingleMultAttr
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

matplotlib.rc('font', family='YouYuan')

'''
1000护穿和250属攻
'''
# Make data
armor_pens = np.arange(0, 3000, 10)
atk_powers = np.arange(1500, 3500, 10)


armor_pen = SingleMultAttr('armor_pen') #净护甲穿透
elem_atk_power = SingleMultAttr('atk_power') #元素攻击

len_x = len(armor_pens)
len_y = len(atk_powers)
Z = np.ndarray(shape=(len_y, len_x))
for i, x in zip(range(len_x), armor_pens):
    for j, y in zip(range(len_y), atk_powers):
        armor_pen.value = -x 
        elem_atk_power.value = y
        Z[j, i] = (armor_pen + 1000) / (elem_atk_power + 250)

armor_pens, atk_powers = np.meshgrid(armor_pens, atk_powers)
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(armor_pens, atk_powers, Z, vmin=0.95, vmax=1.05, cmap=cm.coolwarm)
ax.set_xlabel('当前缺少护穿')
ax.set_ylabel('当前属攻')
ax.set_zlabel('1000护穿/250属攻收益')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()
'''
334元穿和138属攻
'''
elem_pens = np.arange(0, 3000, 10)
atk_powers = np.arange(1500, 3500, 10)

elem_pen = SingleMultAttr('elem_pen')
elem_atk_power = SingleMultAttr('atk_power') #元素攻击
len_x = len(elem_pens)
len_y = len(atk_powers)
Z = np.ndarray(shape=(len_y, len_x))
for i, x in zip(range(len_x), elem_pens):
    for j, y in zip(range(len_y), atk_powers):
        elem_pen.value = -x 
        elem_atk_power.value = y
        Z[j, i] = (elem_pen + 334) / (elem_atk_power + 138)

armor_pens, atk_powers = np.meshgrid(elem_pens, atk_powers)
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(armor_pens, atk_powers, Z, vmin=0.95, vmax=1.05, cmap=cm.coolwarm)
ax.set_xlabel('当前缺少元穿')
ax.set_ylabel('当前属攻')
ax.set_zlabel('334元穿/138属攻收益')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

"""
25.1爆伤与138属攻对比
"""
criticals = np.arange(300, 900, 10)
atk_powers = np.arange(1500, 3500, 10)

critical = SingleMultAttr('full_critical')
elem_atk_power = SingleMultAttr('atk_power') #元素攻击
len_x = len(criticals)
len_y = len(atk_powers)
Z = np.ndarray(shape=(len_y, len_x))
for i, x in zip(range(len_x), criticals):
    for j, y in zip(range(len_y), atk_powers):
        critical.value = x 
        elem_atk_power.value = y
        Z[j, i] = (critical + 25.1) / (elem_atk_power + 138)

armor_pens, atk_powers = np.meshgrid(criticals, atk_powers)
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(armor_pens, atk_powers, Z, vmin=0.95, vmax=1.05, cmap=cm.coolwarm)
ax.set_xlabel('当前爆伤')
ax.set_ylabel('当前属攻')
ax.set_zlabel('25.1爆伤/138属攻收益')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

"""
25.1爆伤与424攻强对比
"""
criticals = np.arange(300, 900, 10)
atk_powers = np.arange(5000, 25000, 100)

critical = SingleMultAttr('full_critical')
elem_atk_power = SingleMultAttr('atk_power') #攻强
len_x = len(criticals)
len_y = len(atk_powers)
Z = np.ndarray(shape=(len_y, len_x))
for i, x in zip(range(len_x), criticals):
    for j, y in zip(range(len_y), atk_powers):
        critical.value = x 
        elem_atk_power.value = y
        Z[j, i] = (critical + 25.1) / (elem_atk_power + 424)

armor_pens, atk_powers = np.meshgrid(criticals, atk_powers)
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(armor_pens, atk_powers, Z, vmin=0.95, vmax=1.05, cmap=cm.coolwarm)
ax.set_xlabel('当前爆伤')
ax.set_ylabel('当前攻强')
ax.set_zlabel('25.1爆伤/424攻强收益')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

"""
424攻强与138属攻对比
"""
atk_powers1 = np.arange(1500, 3500, 10)
atk_powers2 = np.arange(5000, 25000, 100)

elem_atk_power = SingleMultAttr('atk_power') #属攻
atk_power = SingleMultAttr('atk_power') #攻强
len_x = len(atk_powers1)
len_y = len(atk_powers2)
Z = np.ndarray(shape=(len_y, len_x))
for i, x in zip(range(len_x), atk_powers1):
    for j, y in zip(range(len_y), atk_powers2):
        elem_atk_power.value = x 
        atk_power.value = y
        Z[j, i] = (elem_atk_power + 138) / (atk_power + 424)

armor_pens, atk_powers = np.meshgrid(atk_powers1, atk_powers2)
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(armor_pens, atk_powers, Z, vmin=0.95, vmax=1.05, cmap=cm.coolwarm)
ax.set_xlabel('当前属攻')
ax.set_ylabel('当前攻强')
ax.set_zlabel('138属攻/424攻强收益')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

"""
27爆伤与392护穿对比
"""
criticals = np.arange(300, 900, 10)
armor_pens = np.arange(0, 3000, 10)

critical = SingleMultAttr('full_critical')
armor_pen = SingleMultAttr('armor_pen') #护穿
len_x = len(criticals)
len_y = len(armor_pens)
Z = np.ndarray(shape=(len_y, len_x))
for i, x in zip(range(len_x), criticals):
    for j, y in zip(range(len_y), armor_pens):
        critical.value = x 
        armor_pen.value = -y
        Z[j, i] = (critical + 27) / (armor_pen + 392)

armor_pens, atk_powers = np.meshgrid(criticals, armor_pens)
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(armor_pens, atk_powers, Z, vmin=0.95, vmax=1.05, cmap=cm.coolwarm)
ax.set_xlabel('当前爆伤')
ax.set_ylabel('当前缺少穿透')
ax.set_zlabel('27爆伤/392穿透收益')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

"""
200暴击值与1000穿透对比
"""
crits = np.arange(0, 500, 10)
armor_pens = np.arange(0, 3000, 10)

crit = SingleMultAttr('700crit_dmg')
armor_pen = SingleMultAttr('armor_pen') #护穿
len_x = len(crits)
len_y = len(armor_pens)
Z = np.ndarray(shape=(len_y, len_x))
for i, x in zip(range(len_x), crits):
    for j, y in zip(range(len_y), armor_pens):
        crit.value = x 
        armor_pen.value = -y
        Z[j, i] = (crit + 200) / (armor_pen + 1000)

armor_pens, atk_powers = np.meshgrid(crits, armor_pens)
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(armor_pens, atk_powers, Z, vmin=0.95, vmax=1.05, cmap=cm.coolwarm)
ax.set_xlabel('当前暴击值')
ax.set_ylabel('当前缺少穿透')
ax.set_zlabel('200暴击值/1000穿透收益')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

"""
25首伤与250属攻对比
"""
head_dmgs = np.arange(50, 300, 1)
atk_powers = np.arange(1500, 3500, 10)

head_dmg = SingleMultAttr('pct_dmg_inc') #首伤
atk_power = SingleMultAttr('atk_power') #护穿
len_x = len(head_dmgs)
len_y = len(atk_powers)
Z = np.ndarray(shape=(len_y, len_x))
for i, x in zip(range(len_x), head_dmgs):
    for j, y in zip(range(len_y), atk_powers):
        head_dmg.value = x 
        atk_power.value = y
        Z[j, i] = (head_dmg + 25) / (atk_power + 250)

armor_pens, atk_powers = np.meshgrid(head_dmgs, atk_powers)
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(armor_pens, atk_powers, Z, vmin=0.95, vmax=1.05, cmap=cm.coolwarm)
ax.set_xlabel('当前首伤')
ax.set_ylabel('当前属攻')
ax.set_zlabel('25首伤/250属攻收益')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

"""
25首伤与45爆伤对比
"""
head_dmgs = np.arange(50, 300, 1)
criticals = np.arange(300, 900, 10)

head_dmg = SingleMultAttr('pct_dmg_inc') #首伤
critical = SingleMultAttr('full_critical') #爆伤
len_x = len(head_dmgs)
len_y = len(criticals)
Z = np.ndarray(shape=(len_y, len_x))
for i, x in zip(range(len_x), head_dmgs):
    for j, y in zip(range(len_y), criticals):
        head_dmg.value = x 
        critical.value = y
        Z[j, i] = (head_dmg + 25) / (critical + 45)

armor_pens, atk_powers = np.meshgrid(head_dmgs, criticals)
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(armor_pens, atk_powers, Z, vmin=0.95, vmax=1.05, cmap=cm.coolwarm)
ax.set_xlabel('当前首伤')
ax.set_ylabel('当前爆伤')
ax.set_zlabel('25首伤/45爆伤收益')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

"""
250属攻与45爆伤对比
"""
atk_powers = np.arange(1500, 3500, 10)
criticals = np.arange(300, 900, 10)

atk_power = SingleMultAttr('atk_power') #属攻
critical = SingleMultAttr('full_critical') #爆伤
len_x = len(atk_powers)
len_y = len(criticals)
Z = np.ndarray(shape=(len_y, len_x))
for i, x in zip(range(len_x), atk_powers):
    for j, y in zip(range(len_y), criticals):
        atk_power.value = x 
        critical.value = y
        Z[j, i] = (atk_power + 250) / (critical + 45)

armor_pens, atk_powers = np.meshgrid(atk_powers, criticals)
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(armor_pens, atk_powers, Z, vmin=0.95, vmax=1.05, cmap=cm.coolwarm)
ax.set_xlabel('当前属攻')
ax.set_ylabel('当前爆伤')
ax.set_zlabel('250属攻/45爆伤收益')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

"""
137属攻与27爆伤对比
"""
atk_powers = np.arange(1500, 3500, 10)
criticals = np.arange(300, 900, 10)

atk_power = SingleMultAttr('atk_power') #属攻
critical = SingleMultAttr('full_critical') #爆伤
len_x = len(atk_powers)
len_y = len(criticals)
Z = np.ndarray(shape=(len_y, len_x))
for i, x in zip(range(len_x), atk_powers):
    for j, y in zip(range(len_y), criticals):
        atk_power.value = x 
        critical.value = y
        Z[j, i] = (atk_power + 137) / (critical + 27)

armor_pens, atk_powers = np.meshgrid(atk_powers, criticals)
# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf = ax.plot_surface(armor_pens, atk_powers, Z, vmin=0.95, vmax=1.05, cmap=cm.coolwarm)
ax.set_xlabel('当前属攻')
ax.set_ylabel('当前爆伤')
ax.set_zlabel('137属攻/27爆伤收益')
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()