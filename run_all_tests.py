#!/usr/bin/env python3
import subprocess
import time
import sys
import os

os.chdir('/Users/abidhasan/Desktop/cse421_lab-3')

def run_test(test_num, server_file, client_inputs):
    """Run a single test"""
    print(f"\n{'='*60}")
    print(f"TEST {test_num}")
    print('='*60)
    
    # Start server
    server_process = subprocess.Popen([sys.executable, server_file], 
                                     stdout=subprocess.PIPE, 
                                     stderr=subprocess.PIPE,
                                     text=True)
    time.sleep(1)
    
    # Run clients
    for i, client_input in enumerate(client_inputs):
        client_file = f'client/client{test_num}.py'
        print(f"\nClient Test {test_num}.{i+1}:")
        print(f"Input: {client_input}")
        print("Output:")
        
        process = subprocess.Popen([sys.executable, client_file],
                                  stdin=subprocess.PIPE,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  text=True)
        stdout, stderr = process.communicate(input=client_input + '\n', timeout=5)
        
        if stdout:
            print(stdout.strip())
        if stderr and 'Connection' not in stderr:
            print(f"Error: {stderr}")
        
        time.sleep(0.5)
    
    # Stop server
    server_process.terminate()
    try:
        server_process.wait(timeout=2)
    except subprocess.TimeoutExpired:
        server_process.kill()

# Test 1: IP and Device Name
print("\n" + "="*60)
print("RUNNING ALL 4 LAB TESTS")
print("="*60)

print("\n" + "="*60)
print("TEST 1: CLIENT SENDS IP & DEVICE NAME")
print("="*60)
server1 = subprocess.Popen([sys.executable, 'server/server1.py'],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          text=True)
time.sleep(1)
result1 = subprocess.run([sys.executable, 'client/client1.py'],
                        capture_output=True, text=True)
server1.terminate()
server1.wait()
print("Server Output:")
print(server1.stdout.read() if server1.stdout else "")

# Test 2: Vowel Counting
print("\n" + "="*60)
print("TEST 2: VOWEL COUNTING")
print("="*60)

test_cases = [
    ("hello world", "Too many vowels (3 vowels: e,o,o)"),
    ("xyz", "Not enough vowels (0 vowels)"),
    ("a", "Enough vowels I guess (1 vowel)")
]

for text, description in test_cases:
    print(f"\nTest: '{text}' - {description}")
    server2 = subprocess.Popen([sys.executable, 'server/server2.py'],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              text=True)
    time.sleep(0.5)
    result = subprocess.run([sys.executable, 'client/client2.py'],
                           input=text,
                           capture_output=True, text=True)
    server2.terminate()
    server2.wait()
    print("Client Response:", result.stdout.strip().split('\n')[-1])

# Test 3: Multi-threaded Vowel Counting
print("\n" + "="*60)
print("TEST 3: MULTI-THREADED VOWEL COUNTING")
print("="*60)

server3 = subprocess.Popen([sys.executable, 'server/server3.py'],
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          text=True)
time.sleep(1)

test_strings = [("aeiou", "Too many vowels"), ("hi", "Enough vowels I guess"), ("bcdfg", "Not enough vowels")]
processes = []

print("\nSending 3 messages simultaneously:")
for text, expected in test_strings:
    p = subprocess.Popen([sys.executable, 'client/client3.py'],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True)
    processes.append((p, text, expected))

for p, text, expected in processes:
    stdout, stderr = p.communicate(input=text)
    print(f"Message: '{text}' → {stdout.strip().split(chr(10))[-1]}")

server3.terminate()
server3.wait()

# Test 4: Salary Calculation
print("\n" + "="*60)
print("TEST 4: SALARY CALCULATION")
print("="*60)

salary_tests = [
    ("40", "8000 (40 × 200)"),
    ("50", "11000 (8000 + 10 × 300)"),
    ("30", "6000 (30 × 200)")
]

for hours, expected in salary_tests:
    print(f"\nHours: {hours} → Expected: {expected}")
    server4 = subprocess.Popen([sys.executable, 'server/server4.py'],
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE,
                              text=True)
    time.sleep(0.5)
    result = subprocess.run([sys.executable, 'client/client4.py'],
                           input=hours,
                           capture_output=True, text=True)
    server4.terminate()
    server4.wait()
    output_lines = result.stdout.strip().split('\n')
    print("Client Response:", output_lines[-1] if output_lines else "No response")

print("\n" + "="*60)
print("ALL TESTS COMPLETED!")
print("="*60)
