import os
from collections import Counter
import socket

def count_words_in_file(filepath):
    with open(filepath, 'r') as file:
        text = file.read()
    words = text.split()
    return len(words), Counter(words)

def main():
    
    # Ensure output directory exists
    output_dir = '/home/output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    data_dir = '/home/data'
    output_file = '/home/output/result.txt'
    
    # List files in data directory
    files = os.listdir(data_dir)
    print(f"Files in {data_dir}: {files}")
    
    # Count words in each file and total
    total_words = 0
    word_counts = {}
    for filename in files:
        filepath = os.path.join(data_dir, filename)
        word_count, counts = count_words_in_file(filepath)
        word_counts[filename] = counts
        total_words += word_count
    
    # Find top 3 words in IF.txt
    if_word_counts = word_counts.get('IF.txt', {})
    top_3_words = if_word_counts.most_common(3)
    
    # Find IP address (not feasible in a platform-agnostic way without external libraries or complex code)
    # Find the IP address of the machine
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    
    # Write results to file
    with open(output_file, 'w') as file:
        file.write(f"Total words in all files: {total_words}\n")
        file.write(f"Top 3 words in IF.txt: {top_3_words}\n")
        file.write(f"IP Address: {ip_address}\n")
    
    # Print the results for console output
    with open(output_file, 'r') as file:
        print(file.read())

if __name__ == "__main__":
    main()
