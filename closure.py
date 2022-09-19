#Hola -> HolaHolaHola
def make_repeater_of(n):
    def repeater(string):
        assert type(string) == str, "Only character string can be used"
        return string * n
    return repeater

def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("Hola"))

if __name__ == '__main__':
    run()

#Challenge
def make_division_by(n):
    def division(integer):
        assert type(integer)==int, "Only integer number"
        assert n !=0, "You cannot divide by zero"
        return integer/n
    return division
def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    division_by_18 = make_division_by(18)
    print(division_by_18(54))

if __name__=='__main__':
    run()


def run2():
    x,n = int(input("Type the numerator: ")), int(input("type the denominator: "))
    division_by_n=make_division_by(n)
    print(division_by_n(x))

run2()
