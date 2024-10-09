import os

def generate_files(num_files, file_size_mb):
    file_size_bytes = file_size_mb * 1024 * 1024  # Convert MB to bytes
    data = "A" * 1024  # 1 KB of data

    for i in range(num_files):
        file_name = f"file_{i+1}.txt"
        with open(file_name, 'w') as f:
            for _ in range(file_size_bytes // 1024):
                f.write(data)
        print(f"{file_name} generated.")

if __name__ == "__main__":
    generate_files(20, 100)