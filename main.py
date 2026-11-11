from station_bike import Station, Bicycle
from client import Client
from trips import RentalSystem


def main():
    print("=== ЗАПУСК ДЕМО-СЦЕНАРІЮ ===\n")

    system = RentalSystem()

    st_a = Station("Станція А")
    st_b = Station("Станція Б")

    b1 = Bicycle(1, "електричний")
    b2 = Bicycle(2, "звичайний")
    b3 = Bicycle(3, "звичайний")
    b4 = Bicycle(4, "електричний")

    st_a.add_bike(b1)
    st_a.add_bike(b2)
    st_b.add_bike(b3)
    st_b.add_bike(b4)

    olya = Client("Оля", 100.0)
    ivan = Client("Іван", 50.0)

    bike1 = st_a.remove_bike("електричний")
    if bike1:
        cost1 = 100.0
        olya.deduct_money(cost1)
        st_b.add_bike(bike1)
        system.total_revenue += cost1
        print(f"Поїздка 1 успішна! {olya.name} сплатила {cost1} грн.")


    bike2 = st_b.remove_bike("звичайний")
    if bike2:

        cost2 = 30.0
        ivan.deduct_money(cost2)
        st_a.add_bike(bike2)
        system.total_revenue += cost2
        print(f"Поїздка 2 успішна! {ivan.name} сплатив {cost2} грн.")

    olya.balance += 50.0 
    bike3 = st_a.remove_bike("звичайний")
    if bike3:

        cost3 = 20.0
        olya.deduct_money(cost3)
        st_b.add_bike(bike3)
        system.total_revenue += cost3
        print(f"Поїздка 3 успішна! {olya.name} сплатила {cost3} грн.")

    print("\n--- Спроба взяти електричний велосипед на Станції А ---")
    failed_bike = st_a.remove_bike("електричний")
    if failed_bike is None:
        print("Повідомлення: На Станції А немає доступних електричних велосипедів!")

    assert ivan.balance == 20.0, "Помилка підрахунку балансу Івана"
    assert system.get_total_revenue() == 150.0, "Помилка розрахунку загальної виручки"

    print("\n=== БАЛАНС КЛІЄНТІВ ===")
    print(f"Баланс клієнта {olya.name}: {olya.balance} грн")
    print(f"Баланс клієнта {ivan.name}: {ivan.balance} грн")

    print("\n=== ЗВІТ АДМІНІСТРАТОРА ===")
    print(f"Велосипедів на {st_a.name}: {len(st_a.bikes)} (детально: {st_a.get_bikes_count()})")
    print(f"Велосипедів на {st_b.name}: {len(st_b.bikes)} (детально: {st_b.get_bikes_count()})")
    print(f"Загальна виручка мережі: {system.get_total_revenue()} грн")

if __name__ == "__main__":
    main()
