print("stfu")
allBooks = ["نهاية رجل شجاع", "الشيطان و الانسة بريم", "قواعد جارتين", "امواج اكما", "ايكادولي", "جذور القضية الفلسطينية",
"رجال في الشمس", "الحياة كما ينبغي", "17", "عاصفة الاوراق", "ستائر العتمة", "في قلبي انثى عبرية", "عربية الياسمين",
"امارينتا", "ارض زيكولا", "زيكولا", "زمن الخيول البيضاء", "الاجنحة المتكسرة", "اين اختفت الجبنة", "الحياة رقعة شطرنج",
 "مئة عام من العزلة", "الطريق الى الامتياز", "ليل غزة الفسفوري", "الارهاب الغربي", "كيف تكون قائدا ناجحا", 
 "كيف تكسب الاصدقاء", "التعامل مع اناس لا تحتملهم", "مختارات من الشعر","اعمل بذكاء مع القراءة السريعة", "اليوجا",
 "confess", "risk it all for love", "moonfleet", "the lost symbol", "they both die at the end", "they were liars"""]

shelf1 = ["نهاية رجل شجاع", "الشيطان و الانسة بريم", "قواعد جارتين", "امواج اكما", "ايكادولي", "جذور القضية الفلسطينية",
"رجال في الشمس", "الحياة كما ينبغي", "17", "عاصفة الاوراق", "ستائر العتمة", "في قلبي انثى عبرية", "عربية الياسمين",
"امارينتا", "ارض زيكولا", "زيكولا", "زمن الخيول البيضاء", "الاجنحة المتكسرة", "اين اختفت الجبنة", "الحياة رقعة شطرنج",
 "مئة عام من العزلة", "الطريق الى الامتياز", "ليل غزة الفسفوري", "الارهاب الغربي", "كيف تكون قائدا ناجحا", 
 "كيف تكسب الاصدقاء", "التعامل مع اناس لا تحتملهم", "مختارات من الشعر","اعمل بذكاء مع القراءة السريعة", "اليوجا"""]

shelf2 = ["confess", "risk it all for love", "moonfleet", "the lost symbol", "they both die at the end", "they were liars"]

takeaway = "they were liars"

Q1 = input("what are u asking for?")
if Q1 in shelf1:
    print("shelf 1")
elif Q1 in shelf2:
    print("shelf 2")
else:
    print("i dont have it")
if Q1 in allBooks and takeaway:
    print('taken')
