# Python Threading: Producer-Consumer Demo

This project is a simple Python script that demonstrates advanced, low-level threading synchronization using `threading.Condition`.

It solves the classic **"Producer-Consumer"** problem:

1.  **5 Consumer Threads** (`waiter`) start first. They want to get a password from a shared list, but the list is empty. They go to sleep and `wait()` for a signal.
2.  **1 Producer Thread** (the main thread) then asks the user for a password (it "produces" data).
3.  After getting a password, it adds it to the shared list and sends a `notify()` signal.
4.  This signal wakes up **one** of the sleeping threads, which can now safely "consume" the password from the list before going back to sleep.

---

### Skills Demonstrated

This script is a technical demonstration of advanced computer science concepts:

* **Multithreading:** Running multiple threads of execution concurrently.
* **Synchronization:** Using a `threading.Condition` object to prevent a "race condition" (where multiple threads might try to access the empty list at the same time).
* **Signaling:** Using `cond.wait()` to pause threads and `cond.notify()` to wake them up efficiently, ensuring the program doesn't waste CPU cycles.
* **Resource Locking:** The `cond.acquire()` and `cond.release()` (which are part of the `Condition` object) ensure that only one thread can modify the shared list at any given moment.

---

### How to Run

1.  Download the `main.py` file.
2.  Run it using Python 3:

```bash
python3 main.py
```
The program will immediately start 5 "waiter" threads (which will go to sleep) and then prompt you for a password. Each time you enter a password and press Enter, one of the waiting threads will wake up and print it.
