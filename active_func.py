from __future__ import annotations
from typing import Dict

class ActiFunc:
    func_dict : Dict [str, Dict[str, function]] = {}
    init_flag = False
    @staticmethod
    def init() -> None:
        if not ActiFunc.init_flag :
            ActiFunc.init_flag = True
            ActiFunc.func_dict = {
                'atk_power' : {
                    'active' : ActiFunc.atk_power_active,
                    'deacti' : ActiFunc.atk_power_deacti
                }, 
                'pct_dmg_inc' : {
                    'active' : ActiFunc.pct_dmg_inc_active,
                    'deacti' : ActiFunc.pct_dmg_inc_deacti
                },
                'armor_pen' : {
                    'active' : ActiFunc.armor_pen_active,
                    'deacti' : ActiFunc.armor_pen_deacti
                },
                'elem_pen': {
                    'active': ActiFunc.elem_pen_active,
                    'deacti': ActiFunc.elem_pen_deacti
                },
                'full_critical': {
                    'active': ActiFunc.full_critical_dmg_active,
                    'deacti': ActiFunc.full_critical_dmg_deacti
                },
                '700crit_dmg': {
                    'active': ActiFunc._700crit_dmg_active,
                    'deacti': ActiFunc._700crit_dmg_deacti
                }
            }

    @staticmethod
    def __getitem__(k: str) -> Dict[str, function]:
        ActiFunc.init()
        return ActiFunc.func_dict[k]

    """
    atk_power : 攻击强度，元素攻击
    """
    @staticmethod
    def atk_power_active(value: float) -> float:
        return value / 700.0 + 1
    @staticmethod
    def atk_power_deacti(apf: float, value: float) -> float:
        return apf * (value / 700.0 + 1) - 1
    """
    pct_dmg_inc:  全伤，技伤，普伤等百分比伤害
    """
    @staticmethod
    def pct_dmg_inc_active(value: float) -> float:
        return value + 1
    @staticmethod
    def pct_dmg_inc_deacti(apf: float, value: float) -> float:
        return apf * (value + 1) - 1

    """
    满暴击爆伤
    """
    @staticmethod
    def full_critical_dmg_active(value: float) -> float:
        return value 

    @staticmethod
    def full_critical_dmg_deacti(apf: float, value: float) -> float:
        return apf

    """
    700爆伤下暴击值
    """
    @staticmethod
    def _700crit_dmg_active(value: float) -> float:
        if value >= 500:
            return 700 * 100
        else :
            return value / 5 * 700 + (100 - value / 5) * 100

    @staticmethod
    def _700crit_dmg_deacti(apf: float, value: float) -> float:
        return apf  
    """
    armor_pen: 净护甲穿透
    """ 
    @staticmethod
    def armor_pen_active(value: float) -> float :
        if value >= 0:
            return 1
        armor = -value
        return 1 - armor / (armor + 1505)

    @staticmethod
    def armor_pen_deacti(apf: float, value: float) -> float :
        k = ActiFunc.armor_pen_active(value) * apf
        if k == 1:  
            return 0
        armor = 1505 * (1 - k) / k
        return -armor

    """
    elem_pen: 净元素穿透
    """
    @staticmethod
    def elem_pen_active(value: float) -> float:
        if value < 0:
            return ActiFunc.armor_pen_active(value)
        return 1 + value / (value + 3992)
    @staticmethod
    def elem_pen_deacti(apf: float, value: float) -> float:
        k = ActiFunc.elem_pen_active(value) * apf 
        if k < 1.0:
            return ActiFunc.armor_pen_deacti(apf, value)
        elif k < 2.0:
            return 3992.0 * (k - 1) / (2 - k)


    """
    dmg_apf: 伤害增幅
    """
    @staticmethod
    def dmg_apf_active(value: float) -> float:
        return value + 1

    @staticmethod
    def dmg_apf_deacti(apf: float, value: float) -> float:
        return apf / (value + 1) - 1