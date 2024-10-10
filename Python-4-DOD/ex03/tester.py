from new_student import Student


def main():
    try:
        student = Student(name="Edward", surname="agle")
        print(student)

        student2 = Student(name="Edward", surname="agle", id="toto")
        print(student2)

    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        exit(1)


if __name__ == "__main__":
    main()
