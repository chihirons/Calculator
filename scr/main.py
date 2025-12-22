import sys


# 計算に必要な処理
#  ・データを入力するフォームの作成
#  ・入力データの処理
# 四則演算の関数
#  ・データの取得
#  ・計算
#  ・結果の返却
# データ出力


# 数値の入力
def get_calc_line() -> str:
    """
    ユーザーから計算式を取得する。

    Returns
    -------
    str
        ユーザーが入力した計算式
    """
    print("計算を行います。\n 「5 + 8」 のように計算式を入力してください。")
    return input("計算式を入力後、Enterを押下：")


def addition(get_left: int, get_right: int) -> int:
    # 足し算の計算を実施
    pass


def subtraction(get_left: int, get_right: int) -> int:
    # 引き算の計算を実施
    pass


def multiplication(get_left: int, get_right: int) -> int:
    # 掛け算の計算を実施
    pass


def division(get_left: int, get_right: int) -> int:
    # 割り算の計算を実施
    pass


# ユーザー入力文字列を取得し空白区切りでリスト変換
user_input_list = get_calc_line().split()
print(user_input_list)

# 仮で入力チェックを実施
if len(user_input_list) < 3:
    print("入力された式は計算できません。")
    sys.exit(255)
