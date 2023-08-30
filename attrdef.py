from __future__ import annotations
from typing import Dict, Tuple
from active_func import ActiFunc

class SingleMultAttr:
    """
    单输入单输出类型属性
    """
    def __init__(self, key: str, value: float = 0.0) -> None:
        """
        key list :
            atk_power : 攻击强度，元素攻击
            pct_dmg_inc:  全伤，技伤，普伤等百分比伤害
            armor_pen: 护甲穿透
            elem_pen: 元素穿透
            full_critical: 满暴击下的爆伤
            700crit_dmg: 700爆伤下暴击值
        """
        self.key         : str = key
        self.value       : float = value
        self.active_func : function = ActiFunc.__getitem__(key)['active']
        self.deacti_func : function = ActiFunc.__getitem__(key)['deacti']

    def __add__(self, o: float) -> float:
        return self.delta_apf(o)

    def __rsub__(self, o: float) -> float:
        return self.getgap_apf(o)

    def active(self) -> float:
        return self.active_func(self.value)
            

    def delta_apf(self, delta: float) -> float :
        return self.active_func(self.value + delta) / self.active_func(self.value)

    def deacti_apf(self, apf: float) -> float:
        return self.deacti_func(apf, self.value)

    def getgap_apf(self, apf: float) -> float:
        return self.deacti_apf(apf) - self.value

#伤害增幅
class DmgApfAttr:
    def __init__(self, value: float = 0) -> None:
        self.value: float = value
        self.active_func : function = ActiFunc.dmg_apf_active
        self.deacti_func : function = ActiFunc.dmg_apf_deacti

    def __add__(self, o: float) -> float:
        return self.delta_apf(o)

    def __rsub__(self, o: float) -> float:
        return self.getgap_apf(o)

    def active(self) -> float:
        return self.active_func(self.value)

    def delta_apf(self, delta: float) -> float:
        return delta 
    
    def deacti_apf(self, apf: float) -> float:
        return apf

    def getgap_apf(self, apf: float) -> float:
        return apf / (self.value + 1) - 1