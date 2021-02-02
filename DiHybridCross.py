a = 'Aa'
b = 'Aa'
h = 'heterozygous'
o = 'homozygous dominant'
u = 'homozygous recessive'
c = a[0] + b[0] + ' ' + a[0] + b[1] + ' ' + b[0] + a[0] + ' ' + b[0] + a[1]
Genotype_Table = {
    'A': {
        'a': h,
        'A': o,
    },
    'a': {
        'a': u,
        'A': h,
    },
}

output = ''
for i in c.split():
    output += Genotype_Table[i[0]][i[1]] + ' '
print(f'Genes-> {c}')
print(f"Genotypes-> {output}")

import time


def FOIL(arg): return arg[0] + arg[2] + ' ' + arg[0] + arg[3] + ' ' + arg[1] + arg[2] + ' ' + arg[1] + arg[3]
def FOILL(arg): return [arg[0] + arg[2], arg[0] + arg[3], arg[1] + arg[2], arg[1] + arg[3]]
Dihybrid1 = 'SSYY'
parent1 = FOIL(Dihybrid1)
print('parent 1: ' + parent1)
Dihybrid2 = 'SSYY'
parent2 = FOIL(Dihybrid2)
print('parent 2: ' + parent2)

superlongcross = parent1[0] + parent2[0] + parent1[1] + parent2[1] + ' ' + parent1[0] + parent2[3] + parent1[1] + parent2[4] + ' ' + parent1[0] + parent2[6] + parent1[1] + parent2[7] + ' ' + parent1[0] + parent2[9] + parent1[1] + parent2[10] + ' ' + parent1[3] + parent2[0] + parent1[4] + parent2[1] + ' ' + parent1[3] + parent2[3] + parent1[4] + parent2[4] + ' ' + parent1[3] + parent2[6] + parent1[4] + parent2[7] + ' ' + parent1[3] + parent2[9] + parent1[4] + parent2[10] + \
    ' ' + parent1[6] + parent2[0] + parent1[7] + parent2[1] + ' ' + parent1[6] + parent2[3] + parent1[7] + parent2[4] + ' ' + parent1[6] + parent2[6] + parent1[7] + parent2[7] + ' ' + parent1[6] + parent2[9] + parent1[7] + parent2[10] + \
    ' ' + parent1[9] + parent2[0] + parent1[10] + parent2[1] + ' ' + parent1[9] + parent2[3] + parent1[10] + parent2[4] + \
    ' ' + parent1[9] + parent2[6] + parent1[10] + parent2[7] + \
    ' ' + parent1[9] + parent2[9] + parent1[10] + parent2[10]
print(superlongcross)

#0.0010006427764892578
def foil(arg): return arg[0] + arg[2] + arg[0] + \
    arg[3] + arg[1] + arg[2] + arg[1] + arg[3]
p1 = 'SSYY'
p2 = 'SSYY'
p3 = foil(p1)
p4 = foil(p2)
print(p3)
print(p4)


second = ''
p11 = FOILL(p1)
p22 = FOILL(p2)
t1 = time.time()
for i in p11:
    for ii in p22:
        second += (i[0]+ii[0]+i[1]+ii[1]) + ' '

print(second)

t2 = time.time() - t1

print(t2)
