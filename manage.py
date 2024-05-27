import os
import sys

# Add parent_directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def main():
    from transformers.linkedList import LinkedList
    ll = LinkedList()
    print("LinkedList initialized:", ll)

if __name__ == '__main__':
    main()
