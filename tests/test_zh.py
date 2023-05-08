import font_generator.zh as zh


class TestZh:
    def test_protect_zh(self):
        # Make sure there isn't stray additions or deletions from the set.
        assert len(zh.ZH_ALL) == 9900
        assert len(zh.HSK) == 2663
