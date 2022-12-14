# Bioinformatika. Lab 3.

## Apibūdinkite fastq formatą. Kokia papildoma informacija pateikiam lyginant su FASTA formatu?

FASTQ yra tekstinis sekoskaitos duomenų failų formatas, kuriame saugomi neapdoroti sekos duomenys ir kokybės balai. FASTQ failai tapo standartiniu formatu, kuriuo saugomi "Illumina" sekoskaitos sistemų NGS duomenys, ir gali būti naudojami kaip įvesties duomenys įvairiems antrinės duomenų analizės sprendimams. Lyginant su FASTA, šis turi sekos identifikacinius numerius bei kokybės balus/įverčius (naudojama ASCII simbolių lentelė).

## Kurią mėnesio dieną Jūs gimėte? Prie dienos pridėkite 33. Koks ASCII simbolis atitinka šį skaičių?

Gimiau 23 dieną. 23 + 33 = 56. ASCII lentelėje atitinka skaitmens '8' simbolį.

## Kodėl pirmi 32 ASCII kodai negali būti naudojami sekos kokybei koduoti?

ASCII pirmieji 32 kodai (skaičiai 0-31 dešimtainiu tikslumu) skirti valdymo ženklams: kodai, kurie iš pradžių buvo skirti ne spausdintinai informacijai išreikšti, o ASCII naudojančių įrenginių (pvz., spausdintuvų) valdymui arba metainformacijai apie duomenų srautus, pvz., saugomus magnetinėje juostoje, pateikti.

## Parašykite, kokią koduotę nustatėte ir kuo remiantis?
Naudojau šį šaltinį: https://en.wikipedia.org/wiki/FASTQ_format#Encoding ir remiausi ten pateiktomis lentelėmis.

Naudojamų simbolių aibė baigiasi ties ASCII lentelės 73 elementu. Iš to išplaukia, kad gali būti naudojamos **Sanger Phred+33** arba **Illumina 1.8+ Phred+33** koduotės.

Patikrinau ar yra simbolių, kurie nepatenka į tinkamą aibę, 'J' simbolis yre galimas Illumina koduotėje, tačiau Sanger koduotėje jo nėra. Paieškojus, 'J' simbolio nėra, tad koduotė - **Sanger Phred+33**.

## Pateikite grafiką, kurio y ašyje būtų read’ų skaičius, x ašyje - C/G nukletidų dalis read’o sekoje. Parašykite, koks „stambių“ pikų skaičius yra gautame grafike?

<img width="746" alt="image" src="https://user-images.githubusercontent.com/56769782/207632649-3a95ad5a-c69f-4d61-9766-18882645326f.png">

Matomi 3 pikai, kai (C/G nucleotides) X ašis yra ties 0.35, 0.55 ir 0.7.

## Pateikite lentelę, kurioje būtų read’o id ir rasto mikroorganizmo rūšis

<img width="1147" alt="image" src="https://user-images.githubusercontent.com/56769782/207632804-587be3e1-4688-4f0e-ae60-e84208ca2a13.png">

## Kokių rūšių bakterijų buvo mėginyje?
  - Staphylococcus aureus
  - Escherichia coli
  - Thermus thermophilus
