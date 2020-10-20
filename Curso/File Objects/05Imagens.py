# Para mexer com imagens deve-se usar o formato de bytes, por isso usa-se rb e não apenas r
with open('test.png', 'rb') as rf:
    with open('test_copy.png', 'wb') as wf:
        for line in rf:
            wf.write(line)
