def calculate_future_assets(initial_asset, interest_rate, inflation_rate, years):
    """
    将来の名目資産と実質資産を計算する
    名目資産 = 初期資産 * (1 + 運用利回り)^年数
    実質資産 = 名目資産 / (1 + インフレ率)^年数
    """
    nominal_asset = initial_asset * (1 + interest_rate) ** years
    real_asset = nominal_asset / (1 + inflation_rate) ** years

    return {
        'nominal': int(nominal_asset),
        'real': int(real_asset)
    }

def predict_income_growth(current_income, study_hours, growth_coefficient):
    """
    学習時間に基づいた予測年収を計算する
    予測年収 = 現在の年収 + (学習時間 * 成長係数)
    """
    predicted_income = current_income + (study_hours * growth_coefficient)
    return predicted_income
            