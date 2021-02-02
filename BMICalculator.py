name = 'Pranav';
height_m = 1.5240030480060962;
weight_kg = 37.2;
bmi = weight_kg / (height_m ** 2);
ot = 'Sorry you overweight, do some squats once in a while'
ut = 'UNDERWEIGHT, EAT SOME PROTEIN';

print("bmi:");
print(bmi);

if bmi > 18.5 and bmi < 25:
    print(name);
    print('YEAH YOU NOT OVERWEIGHT');
else:
    if bmi > 25:
        print(name);
        print(ot);
    elif bmi < 18.5:
        print(ut);

# Pranav Raja 