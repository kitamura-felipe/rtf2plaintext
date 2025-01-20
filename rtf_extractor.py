# rtf_extractor.py

def extract_plain_text_from_rtf(file_path):
    """
    Extracts plain text from an RTF file by removing RTF control words and unnecessary formatting.

    Args:
        file_path (str): Path to the RTF file.

    Returns:
        str: Extracted plain text.
    """
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    # Simplistic extraction of plain text by removing RTF control words
    import re
    plain_text = re.sub(r'{\\.*?}|\\[a-z]+\d* ?', '', content)  # Remove RTF control words and braces
    plain_text = re.sub(r'\n+', '\n', plain_text)  # Normalize new lines
    
    return plain_text.strip()

# Example usage
if __name__ == "__main__":
    # Replace with the path to your RTF file
    rtf_file_path = "/path/to/your/file.rtf"
    plain_text = extract_plain_text_from_rtf(rtf_file_path)
    print(plain_text)
