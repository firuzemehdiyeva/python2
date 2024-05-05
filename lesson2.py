#1) verilmiş listdəki ədədlərin hansılarının hər hansı bir ədədin kvadratı olduğunu define funksiyasında yazıb və listin içərisində ekrana çıxarın. 
# mylist=[-4,-16,0,1,4,5,9,16,25,36,49,64,81,100] -------------

# def kvadrati_olani_tap(mylist):
#     kvadratlar=[]
#     for num in mylist:
#         if num>=0 and (num**0.5) % 1 == 0: 
#             kvadratlar.append(num)
#     return kvadratlar

# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# kvadrati_olanlar=kvadrati_olani_tap(mylist)
# print("listde kvadrati olanlar:")
# print(kvadrati_olanlar)

# --------------------------------------------------------

# 2)Funksiya yazin list qebul etsin ve tekrarlanmayan elementleri bizə qaytarsın: 
#  input:[-1,1,2,2,6,7,7,'say'] ------------

# def tekrarlanan_elementi_tap(input_list):
#     tekrarlanan_element=[]
#     for element in input_list:
#         if input_list.count(element)==1:
#             tekrarlanan_element.append(element)
#     return tekrarlanan_element

# input_list = [-1, 1, 2, 2, 6, 7, 7, 'say']
# tekrarlanmayan=tekrarlanan_elementi_tap(input_list)
# print("Tekrarlanmayan elementler")
# print(tekrarlanmayan)

# ----------------------------------------------------

# 3.Verilmiş inputdakı bütün rəqəmlərin bir birlərinə hasilini icra edən funksiya yazın

# def rəqəmlərin_hasili(h):
#     hasil = 1
#     for rəqəm in h:
#         if rəqəm.isdigit():
#             hasil *= int(rəqəm)
#     return hasil

# inputdakı_sətir = input("Bir sətir daxil edin: ")
# print("Sətirdəki rəqəmlərin bir-birlərinə hasili:", rəqəmlərin_hasili(inputdakı_sətir))

# -----------------------------------------------------------

# 4)verilmiş ədədin bölənlərini list comprehension istifadə edərək yazın

# def bolənlər(ədəd):
#     return [bölən for bölən in range(2, ədəd + 1) if ədəd % bölən == 0]

# ədəd = int(input("Ədədi daxil edin:"))

# print(f"{ədəd} ədədinin bölənləri:", bolənlər(ədəd))

# ------------------------------------------------------------

# 5)Əlininzdə ayların olduğu bir list var siz ay qarşısında uzunluğu olduğu bir dictionary yaradın və bunu comprehension ilə edin və alınan listi print etdirin.

# mylist = ["yanvar", "fevral", "mart", "aprel", "may", "iyun", "iyul", "avqust", "sentyabr", "oktyabr", "noyabr", "dekabr"]
# ay_uzunluqlar = {ay: len(ay) for ay in mylist}

# print("Ay uzunluqları:", ay_uzunluqlar)

# -------------------------------------------------------------------


# 6)names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
#  verilmiş list-dən yalnız adların olduğu və kiçik hərflərlə yazıldığı list düzəldin və bunu conprehension ilə edin (əlavə olaraq funksiya da 
# istifadə edəbilərsiz).
# ['rick', 'morty', 'summer', 'jerry', 'beth']


# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

# lowercase_names = [name.split()[0].lower() for name in names]

# print(lowercase_names)

# ----------------------------

# 7) verilmiş iki listdəki ədədlərin indexlərinə uyğun olaraq ortalamasını tapın.
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# results=[ 2.5, 3.5, 4.5]

# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# results = [(nums1[i] + nums2[i]) / 2 for i in range(len(nums1))]

# print(results)
