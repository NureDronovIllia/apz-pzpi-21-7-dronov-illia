from auth import authenticate_iot


def main():
    authenticate_iot()

    scenario: int = int(
        input(
            'If you want to start a refuel to critical amount enter "1"\nIf you want to refuel to a specific amount enter "2":'
        )
    )

    if scenario not in [1, 2]:
        print("Only 1 and 2 are allowed")
        return

    if scenario == 1:
        storage_id: int = int(input("Enter fuel storage_id:"))


if __name__ == "__main__":
    main()
