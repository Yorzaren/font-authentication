import font_generator.cjk as cjk
import font_generator.zh as zh


class TestInputTexts:
    def test_protect_zh(self):
        # Make sure there isn't stray additions or deletions from the set.
        assert len(zh.ZH_ALL) == 9900
        assert len(zh.HSK) == 2663

    def test_protect_cjk(self):
        assert len(cjk.CJK) == 20989
        assert len(cjk.CJK_A) == 6592
        assert len(cjk.CJK_B) == 42720
        assert len(cjk.CJK_C) == 4154
        assert len(cjk.CJK_D) == 222
        assert len(cjk.CJK_ALL) == 74677
