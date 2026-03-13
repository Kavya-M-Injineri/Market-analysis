text = open('analysis_output.txt', encoding='utf-16le').read()
with open('analysis_output_utf8.txt', 'w', encoding='utf-8') as f:
    f.write(text)
