from django.test import TestCase

# Create your tests here.
class AssetCaluculationTest(TestCase):
    def test_basic_asset_calculation(self):
        """
        基本の名目資産と実質資産の計算をテスト
        A0=100万, r_inv=5%, r_inf=2%, n=10年 の場合
        名目資産: 100 * (1 + 0.05)^10 ≒ 162.88
        実質資産: 162.88 / (1 + 0.02)^10 ≒ 133.62
        """
        from .logic import calculate_future_assets

        initial_asset = 1000000
        interest_rate = 0.05
        inflation_rate = 0.02
        years = 10

        result = calculate_future_assets(initial_asset, interest_rate, inflation_rate, years)
        
        # 期待される値（名目資産と実質資産）
        # 誤差を考慮して assertAlmostEqual を使います
        self.assertAlmostEqual(result['nominal'], 1628894)
        self.assertAlmostEqual(result['real'], 1336260, delta=1)