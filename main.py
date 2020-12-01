from commandline import Commandline
from renderer import Renderer


def main():
    renderer = Renderer()
    app = Commandline("addresses.csv")
    page = app.start()
    print(renderer.render(page))

    while True:
        user_input = str(input())
        page = app.execute(user_input)
        print(renderer.render(page))


if __name__ == "__main__":
    main()
