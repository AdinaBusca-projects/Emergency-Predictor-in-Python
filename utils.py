def ask_severity_symptom(symptom):
    while True:
        try:
            val = int(input(f"On a scale of 0 (none) to 5 (severe),, how bad is your {symptom}? : "))
            if 0 <= val <= 5:
                return val
        except ValueError:
            pass
        print("Plase eneter a number between 0 and 5.")