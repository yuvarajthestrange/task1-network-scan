# results_analyzer.py
# Simple Nmap scan result analyzer

def analyze_results(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        print("\n===== Open Ports and Hosts Found =====")
        for line in lines:
            if "Nmap scan report for" in line:
                print(f"\n{line.strip()}")
            if "/tcp" in line and "open" in line:
                print(f"  {line.strip()}")

    except FileNotFoundError:
        print("Error: The scan results file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    scan_file = input("Enter the path to your Nmap scan results file (e.g., scan_results.txt): ")
    analyze_results(scan_file)
