n1, n2, n3, n4 = map(float, input().split())
nota = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10
print(f'Media: {nota:.1f}')
if nota >= 7:
    print('Aluno aprovado.')
elif nota < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')
    nota = (nota + nota_exame) / 2
    if nota >= 5:
        print('Aluno aprovado.')
    else:
        print('aluno reprovado.')
    print(f'Media final: {nota:.1f}')