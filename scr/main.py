# 数値の入力
def get_calc_input() -> str:
    """
    ユーザーから計算式を取得する。

    Returns
    -------
    str: get_first_number
        される数
    str: get_operator
        演算子
    str: get_second_number
        する数
    """

    print("==========[簡易電卓で計算を開始します。]===========\n")
    get_first_number = input("初めの数値を指定してください。：")
    get_operator = input("演算子を指定してください。(+ - * /)：")
    get_second_number = input("最後の数値を指定してください。：")
    print("")
    return (
        get_first_number,
        get_operator,
        get_second_number
    )


# 足し算の計算を実施
def addition(get_left: int, get_right: int) -> int:
    return get_left + get_right


# 引き算の計算を実施
def subtraction(get_left: int, get_right: int) -> int:
    return get_left - get_right


# 掛け算の計算を実施
def multiplication(get_left: int, get_right: int) -> int:
    return get_left * get_right


# 割り算の計算を実施
def division(get_left: int, get_right: int) -> int:
    return get_left / get_right


# 変数が値変換できるかのチェック
def is_num(get_data):
    try:
        float(get_data)
    except ValueError:
        return False
    else:
        return True


# ユーザー入力情報の取得
first_number, oeprand, second_number = get_calc_input()

# 数値のチェック
if is_num(first_number) & is_num(second_number):
    num_1 = float(first_number)
    num_2 = float(second_number)

    # 演算子の確認
    if oeprand == "+":
        result = addition(num_1, num_2)
        print(f"{num_1} {oeprand} {num_2} = {result} \n")
    elif oeprand == "-":
        result = subtraction(num_1, num_2)
        print(f"{num_1} {oeprand} {num_2} = {result} \n")
    elif oeprand == "*":
        result = multiplication(num_1, num_2)
        print(f"{num_1} {oeprand} {num_2} = {result} \n")
    elif oeprand == "/":
        result = division(num_1, num_2)
        print(f"{num_1} {oeprand} {num_2} = {result} \n")
    else:
        print("対応していない演算子です。\n")

else:
    print("ユーザーの入力値が誤っているため計算できませんでした。\n")
    print(
        f"入力された、初期値は：{first_number}、演算子は："
        f"{oeprand}、最後の値は：{second_number}、です。\n"
    )

print("==========[簡易電卓を終了します。]===========\n")
