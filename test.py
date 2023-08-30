from attrdef import DmgApfAttr, SingleMultAttr

elem_pen = SingleMultAttr('elem_pen')
armor_pen = SingleMultAttr('armor_pen')
elem_pen.value = -80
armor_pen.value = -100

global_dmg = SingleMultAttr('pct_dmg_inc')
global_dmg.value = 1.00

elem_atk = SingleMultAttr('atk_power')
elem_atk.value = 3000

print(elem_pen + 80)
print(armor_pen + 100)
print(global_dmg + 0.35)
print(elem_atk + 96)