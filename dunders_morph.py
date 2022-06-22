class Morph:
    def __init__(self, *args):
        self.args = args

    def add_word(self, word):
        list(self.args).append(word)

    def get_words(self):
        return self.args

    def __eq__(self, other):
        if isinstance(other, str):
            return other.lower() in self.args


dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                    'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                    'векторами', 'векторах'
                    ),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                    'эффектами', 'эффектах'
                    ), Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях'
                             )]

text = input().strip(".,?!").split()
count = 0
for w in text:
    for el in dict_words:
        if w == el:
            count += 1

print(count)
