with open('translated_transcripts/transcript_results/mc1.mp3.txt.txt', 'r') as infile:
    text = infile.read()
    un = text.decode()
    print(un)