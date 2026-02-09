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

    def test_income_growth_by_learning(self):
        """
        学習進捗（人的資本への投資）に応じた年収成長のテスト
        初期年収500万, 学習時間1000時間, 成長係数(係数)0.1 の場合
        予測年収 = 500 + (1000 * 0.1) = 600万
        """
        from .logic import predict_income_growth

        current_income = 5000000
        study_hours = 1000
        growth_coeffcient = 100

        predicted_income = predict_income_growth(current_income, study_hours, growth_coeffcient)

        self.assertEqual(predicted_income, 5100000)