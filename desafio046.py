from time import sleep
import emoji
print('AGUARDE A CONTAGEM PARA OS FOGOS')

for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize("Detonação dos fogos :sunny: ", use_aliases=True))
print('FIM')