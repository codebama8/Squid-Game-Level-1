import time
import random
import threading
import sys

print(" WELCOME TO RED LIGHT, GREEN LIGHT")
print(" Rule: Press Enter only when the light is GREEN!")
print(" If you press Enter during RED light, you're eliminated!")
print(" You have 60 seconds to reach step 10.\n")
input("Press Enter to start...")

position = 0
start_time = time.time()
user_input = None

def get_input():
    global user_input
    input()  # enter key
    user_input = True

while position < 10:
    elapsed = time.time() - start_time
    if elapsed > 60:
        print(" Time's up! You’re eliminated!")
        sys.exit()

    green = random.choice([True, True, True, False])  # احتمال قرمز کمتر

    if green:
        print(f"\n🟢 GREEN LIGHT – Press Enter to move (Step {position + 1})")
        user_input = None
        t = threading.Thread(target=get_input)
        t.start()
        t.join(timeout=3)

        if user_input:
            position += 1
            print(f"✅ You moved to step {position}")
        else:
            print("❌ You didn’t move in time. Eliminated!")
            sys.exit()

    else:
        print("\n🔴 RED LIGHT – Do NOT press Enter! (Wait...)")
        user_input = None
        t = threading.Thread(target=get_input)
        t.start()
        t.join(timeout=3)

        if user_input:
            print("💀 You moved on RED light! You are eliminated!")
            sys.exit()
        else:
            print(" You waited safely.")

    print("-" * 40)
    time.sleep(1.2)

# success
print("\n Congratulations! You crossed the finish line safely!")
print(" You survived the first game of Squid Game.")
