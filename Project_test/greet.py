"""簡単なあいさつスクリプト（Claude Code 練習用）"""


def greet(name: str) -> str:
    """名前を受け取り、あいさつ文を返す"""
    name = name.strip() or "ゲスト"
    return f"こんにちは、{name}さん！"


def main() -> None:
    # 標準入力から名前を受け取る
    name = input("名前を入力してください: ")
    message = greet(name)
    # わざと未定義の変数を参照してエラーを出す（デバッグ練習用）
    print(message + bonus)


if __name__ == "__main__":
    main()
