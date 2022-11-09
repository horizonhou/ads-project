#! /usr/bin/python
# coding: UTF-8
import sys
l11l1ll_opy_ = sys.version_info [0] == 2
l1ll1l1_opy_ = 2048
l11ll1l_opy_ = 7
def l1llll1_opy_ (l111ll1_opy_):
    global l1l11ll11_opy_
    l111l1l_opy_ = ord (l111ll1_opy_ [-1])
    l1l111_opy_ = l111ll1_opy_ [:-1]
    l1ll11_opy_ = l111l1l_opy_ % len (l1l111_opy_)
    l1ll111ll_opy_ = l1l111_opy_ [:l1ll11_opy_] + l1l111_opy_ [l1ll11_opy_:]
    if l11l1ll_opy_:
        l111l1_opy_ = unicode () .join ([unichr (ord (char) - l1ll1l1_opy_ - (l1lll1_opy_ + l111l1l_opy_) % l11ll1l_opy_) for l1lll1_opy_, char in enumerate (l1ll111ll_opy_)])
    else:
        l111l1_opy_ = str () .join ([chr (ord (char) - l1ll1l1_opy_ - (l1lll1_opy_ + l111l1l_opy_) % l11ll1l_opy_) for l1lll1_opy_, char in enumerate (l1ll111ll_opy_)])
    return eval (l111l1_opy_)
import sys
l1l11ll11_opy_ = sys.version_info [0] == 2
l1ll11lll_opy_ = 2048
l1lll1l11_opy_ = 7
def l1ll11l1l_opy_ (l1ll1llll_opy_):
    global l1ll111ll_opy_
    l1l1l1l1l_opy_ = ord (l1ll1llll_opy_ [-1])
    l1lll11l1_opy_ = l1ll1llll_opy_ [:-1]
    l1111lll_opy_ = l1l1l1l1l_opy_ % len (l1lll11l1_opy_)
    l1l1ll1l1_opy_ = l1lll11l1_opy_ [:l1111lll_opy_] + l1lll11l1_opy_ [l1111lll_opy_:]
    if l1l11ll11_opy_:
        l11l11ll_opy_ = unicode () .join ([unichr (ord (char) - l1ll11lll_opy_ - (l1ll11111_opy_ + l1l1l1l1l_opy_) % l1lll1l11_opy_) for l1ll11111_opy_, char in enumerate (l1l1ll1l1_opy_)])
    else:
        l11l11ll_opy_ = str () .join ([chr (ord (char) - l1ll11lll_opy_ - (l1ll11111_opy_ + l1l1l1l1l_opy_) % l1lll1l11_opy_) for l1ll11111_opy_, char in enumerate (l1l1ll1l1_opy_)])
    return eval (l11l11ll_opy_)
import shutil
import codecs
import random
import importlib
import keyword
import errno
import sys
import os
import re
license = (
    l1llll1_opy_ (u"ࠫࠬ࠭ࡃࡰࡲࡼࡶ࡮࡭ࡨࡵࠢ࠵࠴࠶࠺ࠬࠡ࠴࠳࠵࠺࠲ࠠ࠳࠲࠴࠺࠱ࠦ࠲࠱࠳࠺࠰ࠥ࠸࠰࠲࠺ࠣࡎࡦࡩࡱࡶࡧࡶࠤࡩ࡫ࠠࡉࡱࡲ࡫ࡪ࠲ࠠࡈࡇࡄࡘࡊࡉࠠࡦࡰࡪ࡭ࡳ࡫ࡥࡳ࡫ࡱ࡫࠱ࠦࡷࡸࡹ࠱࡫ࡪࡧࡴࡦࡥ࠱ࡧࡴࡳࠊࡍ࡫ࡦࡩࡳࡹࡥࡥࠢࡸࡲࡩ࡫ࡲࠡࡶ࡫ࡩࠥࡇࡰࡢࡥ࡫ࡩࠥࡒࡩࡤࡧࡱࡷࡪ࠲ࠠࡗࡧࡵࡷ࡮ࡵ࡮ࠡ࠴࠱࠴ࠥ࠮ࡴࡩࡧࠣࠦࡑ࡯ࡣࡦࡰࡶࡩࠧ࠯࠻ࠋࡻࡲࡹࠥࡳࡡࡺࠢࡱࡳࡹࠦࡵࡴࡧࠣࡸ࡭࡯ࡳࠡࡨ࡬ࡰࡪࠦࡥࡹࡥࡨࡴࡹࠦࡩ࡯ࠢࡦࡳࡲࡶ࡬ࡪࡣࡱࡧࡪࠦࡷࡪࡶ࡫ࠤࡹ࡮ࡥࠡࡎ࡬ࡧࡪࡴࡳࡦ࠰ࠍ࡝ࡴࡻࠠ࡮ࡣࡼࠤࡴࡨࡴࡢ࡫ࡱࠤࡦࠦࡣࡰࡲࡼࠤࡴ࡬ࠠࡵࡪࡨࠤࡑ࡯ࡣࡦࡰࡶࡩࠥࡧࡴࠋࠢࠣࠤࠥ࡮ࡴࡵࡲ࠽࠳࠴ࡽࡷࡸ࠰ࡤࡴࡦࡩࡨࡦ࠰ࡲࡶ࡬࠵࡬ࡪࡥࡨࡲࡸ࡫ࡳ࠰ࡎࡌࡇࡊࡔࡓࡆ࠯࠵࠲࠵ࠐࡕ࡯࡮ࡨࡷࡸࠦࡲࡦࡳࡸ࡭ࡷ࡫ࡤࠡࡤࡼࠤࡦࡶࡰ࡭࡫ࡦࡥࡧࡲࡥࠡ࡮ࡤࡻࠥࡵࡲࠡࡣࡪࡶࡪ࡫ࡤࠡࡶࡲࠤ࡮ࡴࠠࡸࡴ࡬ࡸ࡮ࡴࡧ࠭ࠢࡶࡳ࡫ࡺࡷࡢࡴࡨࠎࡩ࡯ࡳࡵࡴ࡬ࡦࡺࡺࡥࡥࠢࡸࡲࡩ࡫ࡲࠡࡶ࡫ࡩࠥࡒࡩࡤࡧࡱࡷࡪࠦࡩࡴࠢࡧ࡭ࡸࡺࡲࡪࡤࡸࡸࡪࡪࠠࡰࡰࠣࡥࡳࠦࠢࡂࡕࠣࡍࡘࠨࠠࡃࡃࡖࡍࡘ࠲ࠊࡘࡋࡗࡌࡔ࡛ࡔ࡙ࠡࡄࡖࡗࡇࡎࡕࡋࡈࡗࠥࡕࡒࠡࡅࡒࡒࡉࡏࡔࡊࡑࡑࡗࠥࡕࡆࠡࡃࡑ࡝ࠥࡑࡉࡏࡆ࠯ࠤࡪ࡯ࡴࡩࡧࡵࠤࡪࡾࡰࡳࡧࡶࡷࠥࡵࡲࠡ࡫ࡰࡴࡱ࡯ࡥࡥ࠰ࠍࡗࡪ࡫ࠠࡵࡪࡨࠤࡑ࡯ࡣࡦࡰࡶࡩࠥ࡬࡯ࡳࠢࡷ࡬ࡪࠦࡳࡱࡧࡦ࡭࡫࡯ࡣࠡ࡮ࡤࡲ࡬ࡻࡡࡨࡧࠣ࡫ࡴࡼࡥࡳࡰ࡬ࡲ࡬ࠦࡰࡦࡴࡰ࡭ࡸࡹࡩࡰࡰࡶࠤࡦࡴࡤࠋ࡮࡬ࡱ࡮ࡺࡡࡵ࡫ࡲࡲࡸࠦࡵ࡯ࡦࡨࡶࠥࡺࡨࡦࠢࡏ࡭ࡨ࡫࡮ࡴࡧ࠱ࠫࠬ࠭ࠎ")
)
# =========== l1l1l1l11_opy_ constants
l1l111l11_opy_ = sys.version_info[0] == 2
if l1l111l11_opy_:
    import __builtin__ as l1l1111ll_opy_
else:
    import builtins as l1l1111ll_opy_
l1l1ll1l1_opy_ = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨါၵၸၼာဓࠨࠏ"))
l1l111lll_opy_ = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢိ္ေံဵျွိထࠥࠐ"))
random.seed()
l1l1l1111_opy_ = 2048
l1l1l1l1l_opy_ = l1l1l1111_opy_
l1l111l11_opy_ = 7
print(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုၾႂဧေၘၓေဣ၈ၶၷၪၯၯၸၷၨၫၰၫဨၐၺၳၽၭဦၕၲၩၼၵၩဦၘၼၹၯၸၲဦၗၥၫၼၼၧၧၼၲၷဧၟၩၸၻၬၴၵဩၿႃုဓࠦࠑ")).format(
    l1l1ll1l1_opy_.capitalize(), l1l111lll_opy_))
print(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪ၈ၶၹၽၸၱၪၭၻဩာ၉ေဣ၌ၬၪၸၫၫဣ၊ၵၰၭၴၭၨၷၰၷၫဴဨ၏ၮၪၮၲၹၭွဥ၈ၹၥၩၰၨဥ့္ဴဦၩၷဥဧၱၸၺၸွဴံႀၻၽံၤၵၨၬၬၫံၲၷၮးၰၯၫၨၳၺၮၷဵၔ၌၈၌ၗၗ။ဵဵဳ့ၥၲိဓࠥࠒ")))
def main():
    global l1l1l1lll_opy_
    global l1l1l1l1l_opy_
    global l1l1lll1l_opy_
    global l1l11l11l_opy_
    def l1l1111ll_opy_(l1lll111l_opy_, open=False):
        try:
            os.makedirs(l1lll111l_opy_.rsplit(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာံူဒࠣࠓ")), 1)[0])
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise
        if open:
            return codecs.open(l1lll111l_opy_, encoding=l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦီၾၸၬဵျာဘࠨࠔ")), mode=l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧူၻိဖࠥࠕ")))
    def l1l111ll1_opy_(l1ll1111l_opy_, name):
        return l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨါႁးႀႀးႆၿးႅဪမࠧࠖ")).format(
            l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢိၧၢာရࠨࠗ")) if name.startswith(
                l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုၢၤီဝࠢ࠘"))) else l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪၤီသࠢ࠙")) if name.startswith(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာၦူမࠣࠚ"))) else l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦီၵါရࠤࠛ")),
            bin(l1ll1111l_opy_)[2:] .replace(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧူဴိဝࠥࠜ")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨါၲုဟࠦࠝ"))),
            l1l111lll_opy_
        )
    def l111l1ll_opy_(l11l11ll_opy_):
        global l1l1l1l1l_opy_
        if l1l111l11_opy_:
            l1l1ll1l1_opy_ = unicode() .join([unichr(l1l1l1111_opy_ + ord(char) + (
                l1ll11111_opy_ + l1l1l1l1l_opy_) % l1l111l11_opy_) for l1ll11111_opy_, char in enumerate(l11l11ll_opy_)])
            l1l1lll1l_opy_ = unichr(l1l1l1l1l_opy_)
        else:
            l1l1ll1l1_opy_ = str() .join([chr(l1l1l1111_opy_ + ord(char) + (
                l1ll11111_opy_ + l1l1l1l1l_opy_) % l1l111l11_opy_) for l1ll11111_opy_, char in enumerate(l11l11ll_opy_)])
            l1l1lll1l_opy_ = chr(l1l1l1l1l_opy_)
        l1111lll_opy_ = l1l1l1l1l_opy_ % len(l11l11ll_opy_)
        l1lll11l1_opy_ = l1l1ll1l1_opy_[:-
                                                    l1111lll_opy_] + l1l1ll1l1_opy_[-l1111lll_opy_:]
        l1ll1llll_opy_ = l1lll11l1_opy_ + l1l1lll1l_opy_
        l1l1l1l1l_opy_ += 1
        return l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢိၽဥာဢࠨࠞ")) + l1ll1llll_opy_ + l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုဥာဣࠨࠟ"))
    def l1l111l1l_opy_(l11l11l1_opy_):
        return l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪာီဖဎၯၵၳၴၹၽဤၹႁၶဒထဖဎၯၻၓၾၻၱၳၴ်ၾဵႄဩ၁ဦၻၼၸဵၿၩၸၻၬၴၵၨၭၴၮၲဥၢ္ၡဦ၅၀ဥ္ဖဎၩၰၤၷ၉ၪၷၫႃဳႂဧ၆ဤႁ္ႀဒထၬၬၧၺၐၴၫၾၰၻၻၾဵႄဩ၁ဦႃဵႂနဓထတၬၨၫဧၾၲၙၫၵၦၴၫၰၫႃဳႂဧေၯၫႁၨၩၚၽၶၯၶၪၑၰၽၩၸၩၯီ၁ဖဎဦဨဣဥၮၵၳၨၩၯဥၺၽၶၯၶၪၓၹႄဴႃပဍဥဧဩဤဓဒဣဥဧဩၷၺၺၬၳၮၗၶဦ၅ဣၴၹၭဤီၳၨၾၬၭၗၺၺၬၳၮၕၭၺၭၵၦၳဩၟဳ္ၠီနဓဤဦဨဣၷၶၽၥၺၭၧၘၻၻၭၴၯ၏ၮၻၮၶၧၴဣ၂ဧၴၩၿၭၧၘၻၻၭၴၯ၏ၮၻၮၶၧၴဣၠ၁ံဵၣပဍဥဧဩဤဓဒဣဥဧဩၶၵၼၤၹၰၸၲ၊ၱၶၹၨၷၧၫဨ၀ဥၺၽၶၯၶၪၓၹဩဩဦၴၨၳဧေၶၵၼၤၹၬၭၗၺၺၬၳၮၕၭၺၭၵၦၳဲထတဨဣဥဧၻၩၩၷၧၪၫၜၸၸၱၱၬၓၲၸၫၺၤၱဧ၆ဤၸၷၷၦၻၮၨၙၼၵၮၵၰၐၯၼၨၷၨၵဤၡ၂ၵၴၻၪၸၯၷၱ၉ၰၼၸၧၶၦၪၤဩုဦၺၲၹၨၽၩၪၛၷၷၰၷၫၒၱၷၪၹၪၰဦၣၵၴၻၪၸၯၷၱ၉ၰၼၸၧၶၦၪ၁ၦထတဨဣဥဧဩဤဦဨတဏဧဩဤဦၱၩဥၰၼၔၿၼၫၴၵျၿံႅွဒထဩဤဦဨဣဥဧဩၷၺၺၬၳၮၕၭၺၭၵၦၳဩ၁ဦၽၱၮၪၸၨၫဨါီဧ့ၮၵၱၱဥုၤၹၴၱၦၭၹဩာၵၺၧဥုၬၬၧၺာဥဴဩၧၮၩၵ၇ၨၼၩႁးႀဥဴဩာၩၰၤၷၐၷၨၫႀဣူဧၼၸၸၱၱၬၕၻိဦိဣၨၯၪၶၓၷၧၺၳၾၷႁးႀီဧၯၳၸဨၦၭၨၻ၍ၴၬၨၽဳဩၧၮၩၵဥၰၷဤၫၶၸၲၬၻၥၺၭဣိၹၮၧၵၬၨၩၚၽၶၯၶၪၑၰၽၩၸၩၯီၤဲထတဨဣဥဧၮၰၹၭွဒထဩဤဦဨဣဥဧဩၷၺၺၬၳၮၕၭၺၭၵၦၳဩ၁ဦၻၷၷဧေိဦံၭၴၰၷဤီၣၦၭၹဩာၵၺၧဥုၬၬၧၺာဥဴဩၧၮၩၵ၇ၨၼၩႁးႀဥဴဩာၩၰၤၷၐၷၨၫႀဣူဧၼၸၸၱၱၬၕၻိဦိဣၨၯၪၶၓၷၧၺၳၾၷႁးႀီဧၯၳၸဨၦၭၨၻ၍ၴၬၨၽဳဩၧၮၩၵဥၰၷဤၫၶၸၲၬၻၥၺၭဣိၹၮၧၵၬၨၩၚၽၶၯၶၪၑၰၽၩၸၩၯီၤဲထတဨဣဥဧဩဤဦဨတဏဧဩဤဦၺၨၹၼၻၲဦၭၹၦၳဩာၹၼၵၮၵၰၐၯၼၨၷၨၵိဓဒဣဥဧဩါိုဢࠦࠠ")).format(l1l11lll1_opy_, l1l1l1111_opy_, l1l111l11_opy_)
    def l111lll1_opy_(l1l1111l1_opy_):
        print(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥၷီူါဓဒ၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂နဓၿံႅဣၼၰၵၰဦၷၥၫၼၼၧၧၼၨဥႀၸၹၸဨၨၽၻၮၲၹၱၹၪဳဩၶၫၩၯဥၾၸၶၲၬုဥၴၾၰၺၱဣၲၶၭၹၲၭဣၕႀၽၬၵၶဣၸၶၾၶၩၭဣၨၶၭၩဦၮၲၷဧၯၶၫၭဤဒထ၊ၲၪဨၜၔၜဩၧၮၷၲၸၬဩၴၫၺဣၵၹၸၮၫၫၷဥၾၱၥၺဨၷၴဧၸၦၬၽၶၨၨၽၩဦၩၱၩဧႀၬၧၼဣၳၶၽူဦၪၼဥၬၭၭၺၼၬၳၮဩၸၮၭဣၨၶၷၪၯၯဣၫၰၵၩဴပဍဒထံဤ၈၉၆ၐၜၙဤၟၗၘၗဧ၌ၓ၊၍ဣ၆ၕ၍ဤၜ၉၏ၚ၈။ၐ။ဨ၇၆ၛ၊ဤၚၗဣ၆ၕဩၓ၌၎ူၑၐၗ၉ဦၕ၈၉ၐၞၑဦ၎၌ၗၚၝဤၚၗဣၕၙ၎ၚ။ၖၗဥ၈၌၇၏၌၈ၓၛ၊ၐဦၔၒၘၚဩၓ၌ဨၚၔၙၔဥဧဩတဏၛၱၩၴဨၦၴၷႂဤၺၰၨဥၫၮၪၧၽၯၹဧၬၳၴၮၬၬဧၯၭၲၭဣၹၶဩၸၮၭဣၸၶၾၶၩၭဣၹၶၹဤၪၱၵၪၪၽၳၸႁဣ၁ၻၸၴၪၱၵ၃ဧၪၲၪဨၵၺၵဩၿံႅဣၫၹၸၱဦၼၫၪၹၮဲဓဒ၌ၹဧႀၭၲၴဣၬၬၷၩၸၩၷၪဧၪၲဦၷၥၫၼၼၧၧၼၬၴၵဩၨၯၺၨၨၻၸၶၿဨဿၹၶၹၨၯၺ၁ဴဵ့ဳ၂ၼၲၵၫၲၶ၄ၧၾံႄဖဎဓဒူဥ၈ၽဤၬၱၵၸၻဩၷၵၵၨဥၰၭၩၴၼၬၫၰၮၶၹဨၰၦႀဩၦၫဨၲၧၭၾၷၩၩၷၪၫဩၸၮၩၷဥၺၱၳၻၴၧၳီၽဤၨၭုဥၬ့ၫဴဨၶၴၴၮဤၵၮဣၹၯၸၷၫဨၬၲၷၸၶၺၭၧဥၭၻၳၳဨၨၽၻၮၶၴၩၯဥၴၸၨၻၴၨၸဵဖဎ၇ၬၤၵၻဩၽၵၽၵဥၪၸၲၬၱၪဥၭၲၰၫဨၷၴဧၪၺၵၱၧဥၻၱၭၹဴဣၪဵၰဲဦၪၼဥၨၭၨၯၶၪဥၬႁၸၫၺၱၦၳဩၱၵၬၸၱၬဩၲၧၵၨၸဧၽၬၧၼဣၼၰၵၰဦၪၨဥၹၮၧၻၺၶၮၽၮၰၿဨၶၨၨၷၲၫၬဣၫၶၻဤၯၬၨၳၻၲၪၯၭၵၸဵဖဎၟၷၸဥၴၪၽဦၩၯၸၶဩၩၾၫၯၺၫၮဤၩၭၵၹၨၲၲဦၿၲၷၫၼဤၵၺဣၫၰၵၩၹဨၬၳဧႂၳၻၺဣၵၹၸၮၫၫၷဥၭၻၳၳဨၲၧၭၾၷၩၩၷၮၶၷဤၫႀၳၱၰၬၭၺၴၼဳနဓထတဵဣၘၶၾၶၩၭဣၩၰၻၩၩၼၲၷႀဵဤၵၪၩၺၺၬၥၺၱၲၳဧၭၭၸၭၦၹၶၻၽဦၩၱၩဧၬၳၴၮၬၬဧၯၭၲၭဣၵၨၽၬဦၫၤၳဧၪၰၹၷဣၧၬဩၷၻၸၳၱၰၮၨဦၩၶဥၪၸၱၳၩၱၩဧၵၭၴၭဣၵၨၻၥၳၭၷၪၹၼဲဓဒၗၭၬဩၧၵၶၩၮၮဩၪၯၴၨဥၷၪၸၮဨၶၭၶၾၰၪဨၥၪဧၼၳၳၭၷၭၰၷၫဦၴၬၰၬဩ၇၀့ၦၴၵၯၭၭၧၩၮၳၮၷဵၷၳၾဵၬၲၬဴဣၸၶဩၭၴၫၯၺၫၲၲၭဨၷၭၬဩၪၯၴၨဥၵၪၱၫဨၤၳၫဩၩၾၼၨၳၺၲၳၴံတဏၶၹၽဦၣဿၸၶၾၶၩၭဣၩၰၻၩၩၼၲၷႀ၇ဤၡ၄ၷၦၹၰၩၺဨၧၮၹၮၧၺၷၵၾ၅ဩၟ၂ၫၲၳၭၲၫဦၮၬၱၬဩၴၧၼၫ၃ၤၦၡဓဒတဏဴဩ၇ၵၵၰၪၵၽၷဦၩၱၩဧၼၸၸၱၱၬဧၵၭၺၭၵၦၳၼဤၩၩၱဥၩၮဤၳၩၵၰၬၭဤၧၻဣၵၳၪၭၴဴဣၧႀၹၥၹၻၬၳၮဩၳၨၮၸၸၪၪၸၯၷၱဒထ။ၩဦၻၸၷၬဩၸၵဨၷၦၲၮဤၧဨၯၴၶၴဤၧၼဣၹၯၮဤၩၷၰၲၬၷၸၹဨၬၳဧၽၬၫဨၦၴၵၯၭၭဨၩၮၳၮဤၵၸၼၤၪၸၲၬၱၪဳၻႁၸဦၼၲဥၫၲၷၩၷၹၪၹဩၥၲၴဣၫၬၪၸၻၺၨၸဵဖဎဓဒ၎ၳၶႀၲဦၴၬၲၰၽၥၺၱၲၳၺ၃ထတပဍဲဧ၊ဤၩၷၰၲၬၷၸဦၩၩၹၬၻဤၧဨၶၹၹၲၲၭဨၯၮၻၮၶၧၴဣၸၯၸၹၲၬဣၧၬဩၴၸၭၦၪၫၮၨဦၪၼဥၾၱၭၺၭၶၵၨၬၩဓဒူဥ၈ဩါဦၷၵဥဩဩၭၴၻၬၩၬဩၥဦၻၷၷၰၷၫဦၴၬၹၬၻၥၲဨၶၭၶၾၰၪဨၥၪဧၮၷၩၩၳၪၫဩၻၯၼၫဥၣဩၶၧၼၫၪၹဩၸၮၭၱဥၫၸၹၨၴၨၩနဓေဦၑၩဥၻၱၩဦၸၨၵဿၨၧၵၵၰၪၵၽၷဦၷၳၹၰၸၲဦၱၶဥ၍ၪၰၹၭဣိၻၱၩဦၬၨၫၨၾၰၺေုဥၨဩၿးႅဣၮၵဩၥဦၻၷၷၰၷၫဦၴၬၹၬၻၥၲဨၦၦၵဩၳၴၴၼဥၩၮဤၻၻၨၩဧၪၸဦၼၫၪဧၼၸၧၺၷေဧၼၳဦၽၶၪဧူၴိုၾ့ႄူါၸုဣၷၨၽၬၫၺဣၹၯၪၲဦုၳႀ္ႆၶိပဍဲဧၒၪဦၼၫၪဧၹၩၶ၀ၢၨၶၶၱၫၶၷၸဧၸၴၺၱၲၳဧၲၷဦၻၨၹဧၽၳဦၜၵၺၬဵဤၮၷၺၪၽၮၶဲဨၲၳၳႂဤၧဨဿၧၳၪၲၱ၆ဿၧၳၪၲၱ၆ၾ့ႄ၅ၦၲၩၱၰ၅ဩၧၧၶၱၴၻဩၦၫဨၸၸၬၭဤၯၶဣၹၯၮဤၳၱၧၩၳၮဤၵၺဣၦၻဩၸၮၭဣၪၵၭဤၵၮဣၦဧၼၸၸၱၱၬဧၵၭၺၭၵၦၳဖဎဳဨၒၧၭၾၷၩၩၷၮၶၷဤၵၮဣၸၻၻၭၴၯဣၱၰၽၩၸၩၯၸဧၲၷဦၽၱၸၼၲၸၧၪၯၪဧၯၳၸဨၶၪၵၼၭၺၱၹၪဧၲၲၬၷၵၲၨၽၭၵၶဣၸၰၷၧၫဨၬၹဧၬၥၴဨၥၪဧၽၶၯၾၬၦၳၵၽဦၪၵၴၲၮၲဓဒူဥၕၸဤၸၭၱၦၴၲၲၭဨၥၦၪၴၨၵၷၵဥၺၾၴၶၷၵၹဧၯၳၸဨၰၪၻၱၳၪၻဣၸၻၪၶၺၱၱၬဧႀၭၺၰဣၤၦဩာၴၷၱဲၶၿၩၸၺၬၩၨၫၰၫဨၰၪၻၱၳၪၻုဥၨၵၷၵဨၮၳၶႀၲဦၩၶဥၷၻၭၼၩၷၪဧၶၩၺၰၲၩၺဲထတပဍၑၰၬၩၴၫၨဿနဓၿ္ႅတဏ၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆၁၃၅၀၂၄၆ထတပဍဥဧဩဤဦဨဣဦူါအࠤࠡ")).format(l1l1ll1l1_opy_.capitalize(), l1l1ll1l1_opy_, l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦၹူဧိဣࠥࠢ")), license))
        exit(l1l1111l1_opy_)
    if len(sys.argv) > 1:
        for l1lll111l_opy_ in l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧူ၃ိဤࠥࠣ")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨါဳၰဪဧࠧࠤ")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢိဵူၭၬၵၴိဦࠥࠥ")):
            if l1lll111l_opy_ in sys.argv[1]:
                l111lll1_opy_(0)
        l1l1lll11_opy_ = sys.argv[1] .replace(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုၟၡီါࠢࠦ")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪဴီာࠢࠧ")))
    else:
        l1l1lll11_opy_ = os.getcwd() .replace(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာၣၥါဨࠤࠨ")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦီးါဩࠤࠩ")))
    if len(sys.argv) > 2:
        l1l111ll1_opy_ = sys.argv[2] .replace(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧူၠၢုာࠦࠪ")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨါဵုိࠦࠫ")))
    else:
        l1l111ll1_opy_ = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢိႃဳႂံႄဵႃၧၾ့ႄူါࠣࠬ")).format(
            * (l1l1lll11_opy_.rsplit(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုဲာေࠨ࠭")), 1) + [l1l1ll1l1_opy_]))
    if len(sys.argv) > 3:
        l1l11l11l_opy_ = sys.argv[3] .replace(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪၡၣူိࠣ࠮")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာံူီࠣ࠯")))
    else:
        l1l11l11l_opy_ = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦီႄဴႃ့ၾံႄၨၧၵၶၩၮၮ့ၸၾၼဪဳࠧ࠰")).format(
            l1l1lll11_opy_, l1l1ll1l1_opy_)
    try:
        l1l11lll1_opy_ = open(l1l11l11l_opy_)
    except Exception as exception:
        print(exception)
        l111lll1_opy_(1)
    exec(l1l11lll1_opy_.read(), globals(), locals())
    l1l11lll1_opy_.close()
    l1l11l1l1_opy_ = locals()
    def l1l1l11ll_opy_(l1l11l1ll_opy_, default):
        try:
            return l1l11l1l1_opy_[l1l11l1ll_opy_]
        except:
            return default
    l1ll1l11l_opy_ = l1l1l11ll_opy_(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧူၳၨၮၸၸၪၪၸၫၧၶၹၹၲၲၭၻဪဴࠧ࠱")), False)
    l1l1l1ll1_opy_ = l1l1l11ll_opy_(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨါၧၻၦၮၰၨၷၺၺၬၳၮၼါဲࠤ࠲")), False)
    l1l111lll_opy_ = l1l1l11ll_opy_(
        l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢိၷၥၫၼၼၧၧၼၨၩၦၷၥၳၭၢၹၨၲၰိဴࠥ࠳")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုၢႀႄၨါဴࠤ࠴")).format(l1l1ll1l1_opy_))
    l1l11lll1_opy_ = l1l1l11ll_opy_(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪၵၳၪၭၴၧၰၦၹၴၩၸု့ࠦ࠵")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာၦႄႁၥုးࠦ࠶")).format(l1l1ll1l1_opy_))
    l1l11l1l1_opy_ = l1l1l11ll_opy_(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦီၹၩၶ၀ၢၨၶၶၱၫၶၷၸီြࠢ࠷")), True)
    l1l11ll1l_opy_ = l1l1l11ll_opy_(
        l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧူၷၵၽၵၨၬၨၩၾၼၨၳၺၲၳၴၻဪျࠧ࠸")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨါၶႁဣၵႀႁါ္ࠤ࠹"))) .split()
    l1l1ll11l_opy_ = l1l1l11ll_opy_(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢိၻၮၮၷၨၩၾၼၨၳၺၲၳၴၻဪွࠧ࠺")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုၳၾၪူ်ࠣ࠻"))) .split()
    l1l11ll1l_opy_ = l1l1l11ll_opy_(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪၸၲၲၴၥၸၤၹၯၨၪၸၩၪၲၬၷၸၹုှࠦ࠼")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာီ၂ࠢ࠽"))) .split()
    l1l111lll_opy_ = l1l1l11ll_opy_(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦီၮၼၺၭၵၳၨၵၣၳၷၧၺၳၮၷိဿࠥ࠾")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧူါဿࠤ࠿"))) .split()
    l1l11l1ll_opy_ = l1l1l11ll_opy_(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨါၶၴၤၮၵၨၪၯၴၨၸီ၅ࠢࡀ")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢို၃ࠦࡁ"))) .split()
    l1ll111l1_opy_ = l1l1l11ll_opy_(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုၳၱၨၲၲၥၶၤၲၬၼါ၂ࠤࡂ")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪာ၇ࠨࡃ"))) .split()
    l111llll_opy_ = [
        l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာႂ္ႁဵႃဴႂီ၉ࠢࡄ")).format(directory.replace(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦီၥၠိ၆ࠥࡅ")), l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧူဳိ၇ࠥࡆ"))), fileName)
        for directory, l1l1l1ll_opy_, l1llllll1_opy_ in os.walk(l1l1lll11_opy_)
        for fileName in l1llllll1_opy_
    ]
    def l1l11l11l_opy_(l1l1l1ll1_opy_):
        for l1l11l111_opy_ in l1l11ll1l_opy_:
            if l1l11l111_opy_ in l1l1l1ll1_opy_:
                return True
        return False
    l1ll11ll1_opy_ = [
        l1l1l1ll1_opy_ for l1l1l1ll1_opy_ in l111llll_opy_ if not l1l11l11l_opy_(l1l1l1ll1_opy_)]
    l1l1111l1_opy_ = re.compile(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨၶိၦၾဵႄဪါ၇ࠤࡇ")).format(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢၸုဦာ၌ࠨࡈ"))))
    l1ll11ll1_opy_ = re.compile(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုၦၴၫၲၲၭၣွ၂ၤၥၷူူၞဲၣႀဲၣဳာာ၍ࠨࡉ")))
    l1l11lll1_opy_ = re.compile(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪဳေႄဴႃံိာ၎ࠨࡊ")).format(l1l11lll1_opy_), re.DOTALL)
    def l11l1ll1_opy_(l1l1ll111_opy_):
        comment = l1l1ll111_opy_.group(0)
        if l1l11lll1_opy_.search(comment):
            l1l1lllll_opy_.append(comment.replace(l1l11lll1_opy_, l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာီၐࠢࡋ"))))
            return l1l1lll11_opy_
        else:
            return l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦီူ။ࠣࡌ"))
    def l1l1l1l11_opy_(l1l1ll111_opy_):
        global l1l1lll1l_opy_
        l1l1lll1l_opy_ += 1
        return l1l1lllll_opy_[l1l1lll1l_opy_]
    l1l1l1l1l_opy_ = (
        re.compile(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧၻါႁးႀႀးႆၿးႅေု၆ိါ၍ࠤࡍ")).format(
            l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨၶဨူ၂၁ဨူိဨ၏ࠥࡎ")),
            l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢၸုါ၄၃ဪဦုုၑࠦࡏ")),
            l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣၺဪဥဧာဤိၑࠥࡐ"))
        ), re.MULTILINE)
        if l1l11l1l1_opy_ else
        re.compile(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤၵာႂ္ႁႁ္ႀႀ္ႆဲူ၇ဧာၕࠨࡑ")).format(
            l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥၷဩေ၃၂ဩဪီဩၗࠢࡒ")),
            l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦၹူာ၅၄ဤဧူူၒࠣࡓ")),
            l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧၻါဩုၖࠦࡔ"))
        ), re.MULTILINE)
    )
    l1l1lll11_opy_ = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨါၥႃဳႂၦၬၣိၖࠥࡕ")).format(l1l1ll1l1_opy_)
    l1l11l11l_opy_ = re.compile(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢၸုၾဵႄူၕࠣࡖ")).format(l1l1lll11_opy_))
    l1l11111_opy_ = re.compile(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣၺဪဳေႄဴႃံိာၛࠨࡗ")).format(l1l11lll1_opy_))
    def l1ll11l11_opy_(l1l1ll111_opy_):
        string = l1l1ll111_opy_.group(0)
        if l1ll1l11l_opy_:
            if l1l11111_opy_.search(string):
                l1l11l1ll_opy_.append(string.replace(l1l11lll1_opy_, l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪာၜࠨࡘ"))))
                return l1l1lll11_opy_
            else:
                l1l11l1ll_opy_.append(l111l1ll_opy_(string))
                return l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာၼၷၗၩၺၤၲၩၵၩႁးႀဥုႄဵႃေဪၜ࡙ࠧ")).format(l1l11lll1_opy_, l1l1lll11_opy_)
        else:
            l1l11l1ll_opy_.append(string)
            return l1l1lll11_opy_
    def l1l1llll1_opy_(l1l1ll111_opy_):
        global l1l1l1lll_opy_
        l1l1l1lll_opy_ += 1
        return l1l11l1ll_opy_[l1l1l1lll_opy_]
    l1lllllll_opy_ = re.compile(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦၹူာၡၺၸၢႃၻၹႂၽၵီ၆ောႁးႀီႃေၿ့ႅာႁုႄံႃေၿိႂြႁုေဪၝ࡚ࠧ")).format(
        l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧၻဦိုဪဳေ၈ာ၅၄ဤၠၥၥၠၣၤၟီု၈၀ဧၣၡၡၣၦၠိေဪာီါၚ࡛ࠣ")),
        l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨၶိဪဥဧဵဳ၃ီ၇ဿဦၢၧၠၢၥၟၡူေ၃၂ဩၞၣၣၥၡၢဪာဧဩါါၜࠤ࡜")),
        l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢၸဪဪဳေ၈ာ၅၄ဤၠၥၥၠၣၤၟီီါၜࠣ࡝")),
        l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣၺဪဧဵဳ၃ီ၇ဿဦၢၧၠၢၥၟၡူါါၞࠤ࡞"))
    ), re.MULTILINE | re.DOTALL | re.VERBOSE)
    l1l1lll11_opy_ = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪၤႂ္ႁၥၻၢာၣࠨ࡟")).format(l1l1ll1l1_opy_)
    l1l11llll_opy_ = re.compile(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥၷီႄဴႃုၢࠦࡠ")).format(l1l1lll11_opy_))
    def l1l11llll_opy_(l1l1ll111_opy_):
        l1l1lll1l_opy_ = l1l1ll111_opy_.group(0)
        if l1l1lll1l_opy_:
            global l1l11l11l_opy_
            l111lll1_opy_[l1l11l11l_opy_:l1l11l11l_opy_] = [l1l1lll1l_opy_]
            l1l11l11l_opy_ += 1
        return l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦီူၠࠣࡡ"))
    l11111ll_opy_ = re.compile(
        l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧူၪၸၷၰၡၺဳၣၥၮၸၹၼၻၩၥၧၟၸေၲၱၶၷၵၹၣၼီၢၿီဳေိါၢࠤࡢ")), re.MULTILINE)
    l1lll1111_opy_ = re.compile(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨၶိုဪဒထဩဤဦဨဣဥဧဩၠၨဨဣဥဧဩဤဦဨဍဥဧဩဤဦဨဣဥု၈ဥႁးႀီဧဩဤတဨဣဥဧဩဤဦဨါ၄ဨႄဵႃေဣဥဧဓဤဦဨဣဥဧဩဤၡၦၟၩၣၠၡဦဨဣဏဧဩဤဦဨဣဥဧၥၻူဨဣဥဧဩဤဦဒဣဥဧဩဤဦဨဣိ၆၅ဥၥၧာဥဧဩဎဦဨဣဥဧဩဤဦူ၂၁ဨႄဴႃေဣဥထဩဤဦဨဣဥဧဩာ၅၄ဤႀးႆိဦဨဍဥဧဩဤဦဨဣဥၣၫဤဦဨဣဥဧဩဤတဨဣဥဧူါိၤࠥࡣ")).format(l1l1lll11_opy_, l1l1lll11_opy_), re.VERBOSE)
    l1llll111_opy_ = re.compile(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢၸုၟၧၪၱၶၢၪဪၧࠧࡤ")))
    l1l1l1lll_opy_ = set(keyword.kwlist + [l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုၢၤၰၷၭၺၧၢာၩࠨࡥ"))] + l1ll111l1_opy_)
    l1l1ll1l1_opy_ = [l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪႀ့ႆဳႁ္ႀာၪࠨࡦ")).format(l1l1lll11_opy_, l1l1l11l1_opy_)
                            for l1l1l11l1_opy_ in l1l11l1ll_opy_]
    l1llll111_opy_ = [
        l1l1llll_opy_ for l1l1llll_opy_ in l1l1ll1l1_opy_ if os.path.exists(l1l1llll_opy_)]
    for l1l1llll_opy_ in l1llll111_opy_:
        l1llll111_opy_ = open(l1l1llll_opy_)
        content = l1llll111_opy_.read()
        l1llll111_opy_.close()
        content = l1l1l1l1l_opy_.sub(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာီၬࠢࡧ")), content)
        content = l1lllllll_opy_.sub(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦီူၧࠣࡨ")), content)
        l1l1l1lll_opy_.update(re.findall(l1lll1111_opy_, content))
    class l1l1ll1ll_opy_:
        def __init__(self):
            for l1l11l1l1_opy_ in l1l111lll_opy_:
                l1ll1111l_opy_ = l1l11l1l1_opy_.replace(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧူဲိၪࠥࡩ")), l1l11lll1_opy_)
                try:
                    exec(
                        l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨါိုတဏၰၶၴၵၺၷဥႂ္ႁဦၩၶဥၪၾၶၸၭၱၹၔၸၨၻၴၨဒထဩဤဦဨဣဥဧဩဤဦဨဣဥဧဩဤဦဨဣဥဧဩဤဦုဪာၮࠨࡪ")).format(l1l11l1l1_opy_),
                        globals()
                    )
                    setattr(self, l1ll1111l_opy_, currentModule)
                except Exception as exception:
                    print(exception)
                    setattr(self, l1ll1111l_opy_, None)
                    print(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢိၟၤၷၵၲၲၭ၂ဣၨၶၾၰၪဨၱၴၻဩၭၴၻၳၪၪၽဤၫႀၷၪၹၷၥၲဨၰၴၫၾၰၫဨၾဵႄူၪࠣ࡫")).format(
                        l1l11l1l1_opy_))
    l1l111ll1_opy_ = l1l1ll1ll_opy_()
    l1ll1l111_opy_ = set()
    def l1llll1ll_opy_(l1l11lll1_opy_):
        if l1l11lll1_opy_ in l1ll1l111_opy_:
            return
        else:
            l1ll1l111_opy_.update([l1l11lll1_opy_])
        try:
            l1l1ll11l_opy_ = list(l1l11lll1_opy_.__dict__)
        except:
            l1l1ll11l_opy_ = []
        try:
            if l1l111l11_opy_:
                l1l111l1l_opy_ = list(l1l11lll1_opy_.func_code.co_varnames)
            else:
                l1l111l1l_opy_ = list(l1l11lll1_opy_.__code__.co_varnames)
        except:
            l1l111l1l_opy_ = []
        l1ll111l1_opy_ = [getattr(l1l11lll1_opy_, l1ll1111l_opy_)
                         for l1ll1111l_opy_ in l1l1ll11l_opy_]
        l1llllll1_opy_ = (l1l11lll1_opy_.join(l1l1ll11l_opy_)) .split(
            l1l11lll1_opy_)
        l1l1l1l11_opy_ = set([entry for entry in (l1l111l1l_opy_ + l1llllll1_opy_)
                        if not (entry.startswith(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုၢၤီၱࠢ࡬"))) and entry.endswith(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪၤၦူၬࠣ࡭"))))])
        l1l1l1lll_opy_.update(l1l1l1l11_opy_)
        for l1lll1111_opy_ in l1ll111l1_opy_:
            try:
                l1llll1ll_opy_(l1lll1111_opy_)
            except:
                pass
    l1llll1ll_opy_(l1l1111ll_opy_)
    l1llll1ll_opy_(l1l111ll1_opy_)
    l11l1l11_opy_ = list(l1l1l1lll_opy_)
    l11l1l11_opy_.sort(key=lambda s: s.lower())
    l1l11l111_opy_ = []
    l1l111lll_opy_ = []
    for l1l1l1ll1_opy_ in l1ll11ll1_opy_:
        if l1l1l1ll1_opy_ == l1l11l11l_opy_:
            continue
        l1ll111l1_opy_, l1l11lll_opy_ = l1l1l1ll1_opy_.rsplit(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာံူၭࠣ࡮")), 1)
        l1llll111_opy_, l1l11l111_opy_ = (
            l1l11lll_opy_.rsplit(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦီ့ါၯࠤ࡯")), 1) + [l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧူါၰࠤࡰ"))])[: 2]
        l1l11l11l_opy_ = l1l1l1ll1_opy_[len(l1l1lll11_opy_):]
        if l1l11l111_opy_ in l1l11ll1l_opy_ and not l1l1l1ll1_opy_ in l1llll111_opy_:
            l11l11l1_opy_ = random.randrange(64)
            l11l1ll1_opy_ = codecs.open(l1l1l1ll1_opy_, encoding=l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨါၻၼၩဲဿူၰࠣࡱ")))
            content = l11l1ll1_opy_.read()
            l11l1ll1_opy_.close()
            l1l1lllll_opy_ = []
            l111lll1_opy_ = content.split(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢိၤၱာၶࠨࡲ")), 2)
            l1l11l11l_opy_ = 0
            l1l1l1ll_opy_ = True
            if len(l111lll1_opy_) > 0:
                if l1l1111l1_opy_.search(l111lll1_opy_[0]):
                    l1l11l11l_opy_ += 1
                    if len(l111lll1_opy_) > 1 and l1ll11ll1_opy_.search(l111lll1_opy_[1]):
                        l1l11l11l_opy_ += 1
                        l1l1l1ll_opy_ = False
                elif l1ll11ll1_opy_.search(l111lll1_opy_[0]):
                    l1l11l11l_opy_ += 1
                    l1l1l1ll_opy_ = False
            if l1ll1l11l_opy_ and l1l1l1ll_opy_:
                l111lll1_opy_[l1l11l11l_opy_:l1l11l11l_opy_] = [
                    l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုဦဥၪၸၨၯၶၪဿဧၞၘ၌ဵျာၷࠨࡳ"))]
                l1l11l11l_opy_ += 1
            if l1ll1l11l_opy_:
                l1l1l11l1_opy_ = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪၡၵူၳࠣࡴ")).join(
                    [l1l111l1l_opy_(l11l11l1_opy_)] + l111lll1_opy_[l1l11l11l_opy_:])
            else:
                l1l1l11l1_opy_ = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာၣၷါၵࠤࡵ")).join(l111lll1_opy_[l1l11l11l_opy_:])
            l1l1l11l1_opy_ = l1l1l1l1l_opy_.sub(
                l11l1ll1_opy_, l1l1l11l1_opy_)
            l1l11l1ll_opy_ = []
            l1l1l11l1_opy_ = l1lllllll_opy_.sub(
                l1ll11l11_opy_, l1l1l11l1_opy_)
            l1l1l11l1_opy_ = l11111ll_opy_.sub(l1l11llll_opy_, l1l1l11l1_opy_)
            l111ll1l_opy_ = set(re.findall(
                l1lll1111_opy_, l1l1l11l1_opy_) + [l1llll111_opy_])
            l1l111ll_opy_ = l111ll1l_opy_.difference(l1l11l111_opy_).difference(
                l1l1l1lll_opy_)
            l1l111l1l_opy_ = list(l1l111ll_opy_)
            l1l1l1111_opy_ = [re.compile(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦၹူၠၨႃဳႂၣၫါၶࠤࡶ")).format(
                l1l11llll_opy_)) for l1l11llll_opy_ in l1l111l1l_opy_]
            l1l11l111_opy_ += l1l111l1l_opy_
            l1l111lll_opy_ += l1l1l1111_opy_
            for l1ll1111l_opy_, l1l111l11_opy_ in enumerate(l1l111lll_opy_):
                l1l1l11l1_opy_ = l1l111l11_opy_.sub(
                    l1l111ll1_opy_(l1ll1111l_opy_,
                                      l1l11l111_opy_[l1ll1111l_opy_]),
                    l1l1l11l1_opy_
                )
            l1l1l1lll_opy_ = -1
            l1l1l11l1_opy_ = l1l11llll_opy_.sub(
                l1l1llll1_opy_, l1l1l11l1_opy_)
            l1l1lll1l_opy_ = -1
            l1l1l11l1_opy_ = l1l11l11l_opy_.sub(
                l1l1l1l11_opy_, l1l1l11l1_opy_)
            content = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧူၠၴုၹࠦࡷ")).join(
                l111lll1_opy_[:l1l11l11l_opy_] + [l1l1l11l1_opy_])
            content = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨါၢၶဪၻࠧࡸ")).join([line for line in [line.rstrip()
                                for line in content.split(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢိၤၱာၽࠨࡹ")))] if line])
            try:
                l1l1lll1l_opy_ = l1l111ll1_opy_(
                    l1l11l111_opy_.index(l1llll111_opy_), l1llll111_opy_)
            except:
                l1l1lll1l_opy_ = l1llll111_opy_
            l11111l1_opy_ = l1l11l11l_opy_.split(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုဲာၾࠨࡺ")))
            for index in range(len(l11111l1_opy_)):
                try:
                    l11111l1_opy_[index] = l1l111ll1_opy_(
                        l1l11l111_opy_.index(l11111l1_opy_[index]), l11111l1_opy_[index])
                except:
                    pass
            l1l11l11l_opy_ = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪဴီႀࠢࡻ")).join(l11111l1_opy_)
            l1l1ll111_opy_ = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာႂ္ႁႁ္ႀာႀࠨࡼ")).format(
                l1l111ll1_opy_, l1l11l11l_opy_) .rsplit(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡸࠦီးါၽࠤࡽ")), 1)[0]
            l1ll11111_opy_ = l1l1111ll_opy_(
                l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡹࠧူၿံႅဲႀးႆဲႁ်ႀာႂࠨࡾ")).format(l1l1ll111_opy_, l1l1lll1l_opy_, l1l11l111_opy_), open=True)
            l1ll11111_opy_.write(content)
            l1ll11111_opy_.close()
        elif not l1l11l111_opy_ in l1l1ll11l_opy_:
            l1l1ll111_opy_ = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡺࠨါႁးႀႀးႆါၿࠤࡿ")).format(
                l1l111ll1_opy_, l1l11l11l_opy_) .rsplit(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡻࠢိ့ဪႃࠧࢀ")), 1)[0]
            l111llll_opy_ = l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡵࠣုၾဵႄးၿ့ႅဪႄࠧࢁ")).format(l1l1ll111_opy_,
                                              l1l11lll_opy_)
            l1l1111ll_opy_(l111llll_opy_)
            shutil.copyfile(l1l1l1ll1_opy_, l111llll_opy_)
    print(l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡶࠤဪၔၩၯၹၹၫၤၹၬၭဤၽၷၵၩၺ၃ဤႁးႀာႆࠨࢂ")).format(len(l1l11l111_opy_)))
if __name__ == l1ll11l1l_opy_ (l1llll1_opy_ (u"ࡷࠥာၦၨၱၧၱၱၤၦူႂࠣࢃ")):
    main()