from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 



@borg.on(admin_cmd("الاوامر"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("꙳ ¦ قائمه الاوامر\n\n⌔ ¦ م1 -› لعرض اوامر الادمن\n꙳ ¦ م2 -› لعرض اوامر التسليه\n꙳ ¦ م3 -› لعرض اوامر الترحيب\n꙳ ¦ م4 -› لعرض اوامر الردود\n꙳ ¦ م5 -› لعرض اوامر الحماية\n꙳ ¦ م6 -› لعرض اوامر التليـكراف\n꙳ ¦ م7 -› لعرض اوامر حماية المجموعة\n꙳ ¦ م8 -› لعرض اوامر التاك\n꙳ ¦ م9 -› لعرض اوامر الكشف\n꙳ ¦ م10 -› لعرض اوامر التحويل\n꙳ ¦ م11 -› لعرض اوامر الترجمة\n꙳ ¦ م12 -› لعرض اوامر البحث\n꙳ ¦ م13 -› لعرض اوامر الانتحال\n꙳ ¦ م14 -› لعرض اوامر النت\n꙳ ¦ م15 -› لعرض اوامر البوت\n꙳ ¦ م16 -› لعرض اوامر الحساب\n꙳ ¦ م17 -› لعرض اوامر التقليد\n꙳ ¦ م18 -› لعرض اوامر الحساب الوقتي\n꙳ ¦ م19 -› لعرض اوامر القائمه السوداء\n꙳ ¦ م20 -› لعرض اوامر الجانبية\n꙳ ¦ م21 -› لعرض الاوامر الزغرفه والتمبلر \n꙳ ¦ م22 -› لعرض اوامر الملصقات \n꙳ ¦ م23 -› لعرض اوامر التمبلر\n꙳ ¦ م24 -› لعرض اوامر هيروكو\n꙳ ¦ م25 -› لعرض اوامر المتحركات\n-  ꙳ ¦  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @JMthon")

@borg.on(admin_cmd("م1"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر حماية المجموعه \n\nالامر ¦ `.وضع صوره` \nالاستخدام  ¦  بالرد على الصوره  \nالشرح ¦  لوضع صوره بروفايل للمجموعه \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n الامر  ¦   `.رفع مشرف`\nالاستخدام ¦  بالرد على الشخص او كتابة الايدي او معرفه \nالشرح  ¦   لرفع شخص مشرف في المجموعة مع بعض الصلاحيات\n\n ➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦   `.تك`\nالاستخدام  ¦   بالرد على الشخص او كتابة الايدي او معرفه \nالشرح  ¦   يقوم بتنزيل الشخص من رتبة  المشرفين وحذف جميع صلاحيات الاشراف \nملاحظة  ¦   لازم تكون انت الشخص الي رفعه او تكون مالك المجموعه حتى تنزله   \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n الامر  ¦   `.حظر`\n الاستخدام  ¦   بالرد على الشخص او كتابة الايدي او معرفه  ، \nالشرح ¦  يقوم بحظر الشخص من المجموعه \n\n ➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n الامر ¦  `.الغاء حظر`\nالاستخدام  ¦   بالرد على الشخص او كتابة الايدي او معرفه\nالشرح  ¦  يقوم بالغاء حظر الشخص من المجموعه \n\n ➖➖➖➖➖➖➖➖➖➖➖➖\n\n الامر  ¦   `.كتم`   + السبب «السبب مو اجباري»\nالاستخدام  ¦  بالرد على الشخص او كتابة الايدي او معرفه \nالشرح  ¦  يقوم بحذف جميع رسائل الشخص بالمجموعه وكذلك في الخاص يجب ان تمتلك صلاحيات حذف اولا \n\n ➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦   `.الغاء كتم`\nالاستخدام  ¦   بالرد على الشخص او كتابة الايدي او معرفه\nالشرح  ¦  يقوم بالغاء كتم الشخص والسماح له بالتحدث بحرية  \n\n ➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر ¦   `.طرد`   + السبب «السبب مو اجباري»\nالاستخدام  ¦   بالرد على الشخص او كتابة الايدي او معرفه \nالشرح  ¦   يقوم بطرد الشخص من المجموعه \n\n ➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦   `.تثبيت`   + بالاشعار «لعمل اشعار للاعضاء»\nالاستخدام  :  بالرد على النص التريد تثبيته \nالشرح  ¦   يقوم بتثبيت الرسالة في المجموعه او في الخاص\n\n ➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦   `.الغاء التثبيت`   + للكل «لالغاء تثبيت جميع الرسائل»\nالاستخدام  :  بالرد على النص التريد تثبيته \nالشرح  ¦   يقوم بالغاء تثبيت الرسالة في المجموعه او في الخاص\n\n➖➖➖➖➖➖➖➖➖➖➖➖ \n\n الامر  ¦   `.الاحداث`   + عدد اخر رسائل تريد مشاهدتها\nالاستخدام  ¦   فقط ارسل الامر  `.الاحداث` مع رقم ما بين 1-15\nالشرح  ¦   يقوم بعرض الرسائل المحذوفة في المجموعه يجب اختيار مابين رقم 1-15 وسيقوم بعرضها \n\n ➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n قنـاة السـورس ¦  @JMthon")

@borg.on(admin_cmd("م2"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("قائـمه اوامر التسليه :**\n⌁ `.قمر`\n⌁ `.اقمار`\n⌁ `.قمور`\n⌁ `.قلوب`\n⌁ `.قلب `\n⌁ `.جيم`\n⌁ `.افكر`\n⌁ `.افكرر`\n⌁ `.شنوو `\n⌁ `.مح `\n⌁ `.متت `\n⌁ `.النضام الشمسي `\n⌁ `.موسيقى `\n⌁ `.قنبله `\n⌁ `.مكبعات `\n⌁ `.افعى `\n⌁ `.طائره `\n⌁ `.نجمه `\n⌁ `.دائره `\n⌁ `.شرطه `\n⌁ `.فايروس `\n⌁ `.غبي `\n⌁ `.العد التنازلي`\n - `.يد`\n - `.تهكير`\n - `.قرد `\n - `.بشره `\n - `.انيم `\n - `.نيكول `\n - `.مربع`\n - `.قاتل `\n - `.تحميل`\n - `.رجل `\n - `.شنوو `\n - `.ريبي `\n - `.تفريغ `\n - `.حلويات `\n - `.فليم`\n\n -  𝗦𝗼𝘂𝗿𝗰𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 :  @Jmthon") 
        
@borg.on(admin_cmd("م3"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر الترحيب  \n\nالامر  : `.ضع ترحيب` \nالاستخدام  : كتابه الترحيب مع الامر\nمثال : `.ضع ترحيب` - ههـلـو عـمـري ♥َ🦋ِ . \n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  :  `.حذف ترحيب`\nالاستخدام :  فقط اكتب الامر حذف ترحيب\nالشرح  :  لحذف جميع الترحيبات لمجموعه معينة\n\n ➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  :  `.الترحيبات`\nالاستخدام  :  فقط اكتب الامر \nالشرح  :  يقوم بعرض الترحيب المضاف لمجموعة معينة\n\n➖➖➖➖➖➖➖➖➖➖➖ \n\nقنـاة السـورس   : [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)") 
        
@borg.on(admin_cmd("م4"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر الردود \n\nالامر  ¦ `.اضاضف رد\nالاستخدام  ¦ بكتابة الرد مع الكلمه التي تريد ان ترسل \nالشرح ¦ شاهد شرح توضيحي اضغط هنا  \n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦  `.حذف رد`\nالاستخدام ¦  بكتابة الامر مع الرد \nالشرح  ¦  لحذف رد معين من دردشه معينة \n\n ➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦  `.الردود`\nالاستخدام  ¦  فقط اكتب الامر \nالشرح  ¦  يقوم بعرض الردود الي تم اضافتها\n\n➖➖➖➖➖➖➖➖➖➖➖ \n\n\nالامر  ¦  `.حذف الردود`\nالاستخدام  ¦ فقط اكتب الرد \nالشرح  ¦ يقوم بحذف جميع الردود المضافه للدردشة\n\n➖➖➖➖➖➖➖➖➖➖➖\n\nقنـاة السـورس   ¦ [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)") 
        
@borg.on(admin_cmd("م5"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر الحماية\n\nالامر  ¦ `.الحماية` on/off\nالاستخدام  ¦ كتابه الامر مع on لتشغيله و off لتعطيله \nالشرح ¦ يستخدم هذا الامر لتفعيل خاصية حماية الخاص \n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦ `.سماح`   او  `.س`\nالاستخدام ¦  فقط اكتب الامر \nالشرح  ¦  للموافقه على الشخص وجعله يتكلم بحرية في الخاص\n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦  `.رفض`  او  `.ر`\nالاستخدام  ¦  فقط اكتب الامر \nالشرح  ¦  يقوم برفض الشخص من الخاص واذا كرر سيتم حظره تلقائيا\n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦ `.بلوك`\nالاستخدام  ¦ كتابه الامر فقط في الخاص\nالشرح ¦ يستخدم هذا الامر لحظر شخص من الخاص فقط قم بالرد عليه\n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦ `.انبلوك`\nالاستخدام ¦  فقط اكتب الامر مع السبب او بدون \nالشرح  ¦  يستخدم هذا الامر لحظر شخص من الخاص فقط قم بالرد عليه \n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦  `.المسموح لهم`\nالاستخدام  ¦  فقط اكتب الامر \nالشرح  ¦  يقوم بعرض قائمه الاشخاص الذي تم الموافقة عليهم والذي تم رفضهم من الخاص\n\n➖➖➖➖➖➖➖➖➖➖➖\n\nقنـاة السـورس   : [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)") 
        
@borg.on(admin_cmd("م6"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر التلكراف \n\nالامر  :  `.تلكراف نص`  \nالاستخدام :  ليقوم بصنع رابط تلكراف لمقالة او موضوع معين \nالشرح  :  قم بالرد على النص المراد تحويله الى رابط تلكراف\n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  :  `.تلكراف ميديا` \nالاستخدام  :  ليقوم بصنع رابط تلكراف لصورة او فيديو او متحركه\nالشرح  :  قم بالرد على الصورة المراد تحويلها الى رابط تلكراف\n\n➖➖➖➖➖➖➖➖➖➖➖ \n\nقنـاة السـورس   : [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)") 
       
@borg.on(admin_cmd("م7"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر  قفل وفتح الصلاحيات \n\nالامر  ¦ `.قفل` + الاضافة   |  `.فتح`  + الاضافة\nالاستخدام  ¦ تكتب قفل مع الاضافه لقفل شي من المجموعه ولفتحه ارسل  فتح مع الاضافع لفتحه\nمثال ¦  `.قفل الوسائط`  \nملاحظة  ¦ لرؤية الاضافات [اضغط هنا](https://t.me/Jmthon_tools/143) \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nقنـاة السـورس  : [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)") 
        
@borg.on(admin_cmd("م8"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر المنشن   \n\nالامر  ¦ `.تاك` + معرف الشخص  + الرسالة\nالشرح  ¦ لعمل تاك لشخص ووضع التاك داخل الرسالة شاهد المثال وجرب بنفسك\nمثال ¦ `.تاك` @RRRD7  ههلا\n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦  `.للكل`  + الرسالة\nالاستخدام ¦  لعمل تاك للكل مع الرسالة\nمثال  ¦ `.للكل` هههلا\n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦  .ابلاغ\nالاستخدام  ¦  قم بكتابه الامر فقط\nالشرح  ¦  سيقوم بعمل تاك لمشرفين المجموعه\n\n➖➖➖➖➖➖➖➖➖➖➖\n\nقنـاة السـورس   : [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)") 
        
@borg.on(admin_cmd("م9"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر الكشف   \n\nالامر  ¦ `.الايدي` \nالشرح  ¦ لاظهار ايدي الشخص و المجموعه فقط قم بالرد على الشخص \n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦  `.ايدي` \nالاستخدام ¦  بالرد او مع الايدي او بالمعرف \nالشرح  ¦ يقوم باظهار معلومات عن الشخص \n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦  `.رابط الحساب` \nالاستخدام  ¦  بالرد او المعرف او الايدي\nالشرح  ¦  سيقوم بعمل رابط لحساب الشخص \n\n➖➖➖➖➖➖➖➖➖➖➖\n\nقنـاة السـورس   : [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)") 
        
@borg.on(admin_cmd("م10"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر التحويل\n\nالامر  : `.تحويل صورة`\nالاستخدام  : الرد على الملصق لتحويله صورة\nالشرح  :  لتحويل الملصق الى صورة \n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  :  `.تحويل ملصق`\nالاستخدام :  بالرد على الصورة\nالشرح  :  قم بالرد على الصورة وسيتم تحويلها الى ملصق\n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  :  `.تحويل متحركه`\nالاستخدام  : بالرد على الملصق المتحرك\nالشرح  :  يقوم بتحويل الملصق المتحرك الى متحركه \n\n➖➖➖➖➖➖➖➖➖➖➖ \n\nالامر  :  `.تحويل voice`\nالاستخدام  : بالرد على الاغنيه \nالشرح  :  يقوم بتحويل الاغنيه  على شكل مقطع بصمة \n➖➖➖➖➖➖➖➖➖➖➖ \n\nالامر  :  `.تحويل mp3\n`الاستخدام  : بالرد على البصمه او المقطع الصوتي\nالشرح  :  يقوم بتحويل النقطع الصوتي الى اغنية\n\n➖➖➖➖➖➖➖➖➖➖➖ \n\nقنـاة السـورس  :  𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)")
        
@borg.on(admin_cmd("م11"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر  الترجمه \n\nالامر  ¦ `.ترجمه ar`    |  `.ترجمه en \n`الاستخدام  ¦ ترد على النص المراد ترجمته \nالشرح ¦  اذا تريد ترجمه من اب لغة للعربية رد على الرسالة بـ `.ترجمه ar`  \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nقنـاة السـورس  : [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)")
        
@borg.on(admin_cmd("م12"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر البحث  \n\nالامر  ¦ `.بحث` \nالاستخدام  ¦ كتابة اسم الاغنية مع الامر \nالشرح ¦ هذا الامر يقوم بجلب مقطع صوتي للاغنيه  \n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦  `.سكرين `\nالاستخدام ¦  بكتابة اسم الموقع او النص \nالشرح  ¦  يقوم باخذ لقطه شاشه من متصفح كوكل كروم\n\n➖➖➖➖➖➖➖➖➖➖➖ \n\nقنـاة السـورس   ¦ [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)") 
        
@borg.on(admin_cmd("م14"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر  النت \n\nالامر  ¦ `.بنك`  \n`الاستخدام ¦ فقط ارسل الامر \nالشرح ¦   لرؤية سرعة البوت لديك \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n \n\nالامر  ¦ `.سرعة النت`  \n`الاستخدام  ¦  فقط ارسل الامر \nالشرح ¦   لرؤية سرعة الانترنت لدى البوت\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\n قنـاة السـورس  : [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)")
        
@borg.on(admin_cmd("م15"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر  التشغيل \n\nالامر  ¦ `.اعادة تشغيل`  \nالاستخدام  ¦ فقط اكتب الامر \nالشرح ¦  ولذلك لإعادة تغشيل البوت اذا صادف مشاكل \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n \n\nالامر  ¦ `.تحديث`  \nالاستخدام  ¦ فقط اكتب الامر \nالشرح ¦   لتحديث البوت اذا اضاف المطورين تحديثات \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\n قنـاة السـورس  : [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)")
        
        
@borg.on(admin_cmd("م16"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر االبروفايل\n\nالامر ¦ `.وضع بايو`\nالاستخدام  ¦  بكتابة البايو مع الامر \nالشرح ¦  لوضع بايو لبروفايلك الشخصي\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦   `.وضع صورة`\nالاستخدام ¦  بالرد على الصورة\nالشرح  ¦   لوضع صورة لبروفايلك الشخصي\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦   `.وضع اسم`\nالاستخدام  ¦   بكتابة الاسم مع الامر\nالشرح  ¦   لوضع اسم لبروفايلك الشخصي   \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦   `.وضع معرف`\nالاستخدام  ¦   بكتابة المعرف مع الامر\nالشرح ¦  لوضع معرف جديد لبروفايلك الشخصي\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر ¦  `.حذف صورة`\n\nالاستخدام  ¦   فقط اكتب الامر\nالشرح  ¦  يقوم بحذف صورة واحدة من بروفايلك\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦   `.الحساب`  \nالاستخدام  ¦  فقط اكتب الامر\nالشرح  ¦  يقوك باظهار تقسيم مبسط لحسابك من الدردشات والمجموعات جربه بنفسك\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦   `.انشائي`\nالاستخدام  ¦   فقط اكتبالامر\nالشرح  ¦  يقوم بأظهار جميع القنوات والمجموعات التي قمت بأنشائها  \n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\nقنـاة السـورس ¦  [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)")
        
        
@borg.on(admin_cmd("م17"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر التقليد او اللزكة  \n\nالامر  ¦ `.تقليد` \nالاستخدام  ¦ بالرد او المعرف او الايدي\nالشرح ¦ بعد تفعيل الامر يقوم بتكرار جميع رسائل الشخص الذي فعلت عليه الامر  \n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦  `.الغاء التقليد `\nالاستخدام ¦  بالرد او الايدي او المعرف \nالشرح  ¦  لالغاء تقليد الشخص وعدم ارسال رسائله\n\n ➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦  `.المقلدهم`\nالاستخدام  ¦  فقط اكتب الامر \nالشرح  ¦  يقوم بعرض الاشخاص الي تم تقليدهم\n\n➖➖➖➖➖➖➖➖➖➖➖ \n\nقنـاة السـورس   ¦ [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)")
        
@borg.on(admin_cmd("م18"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر الوقتي   \n\nالامر  ¦ `.اسم وقتي ` \nالاستخدام  ¦ اكتب الامر فقطnالشرح ¦ بعد تفعيل الامر يقوم بعرض وقت مع اسمك يتغير كل دقيقه مع تغير الوقت   \n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦  `.البايو الوقتي `\nالاستخدام ¦  فقط اكتب الامر \nالشرح  ¦  لعرض وقت يتغير مع النبذة \n\n ➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦  `.انهاء + الامر`\nالاستخدام  ¦  فقط اكتب الامر \nالشرح  ¦  يقوم بايقاف الامر من قائمه الوقتي فقط \nمثال ¦ .انهاء اسم وقتي \n\n➖➖➖➖➖➖➖➖➖➖➖ \n\nقنـاة السـورس   ¦ [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)")
        
@borg.on(admin_cmd("م19"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر القائمة السوداء   \n\nالامر  : `.منع` \nالاستخدام  : اكتب الامر مع الكلمه المراد منعها \nالشرح : يقوم هذا الامر بمنع كلمه من المجموعه او الخاص ويقوم بحذفها يجب ان تكون لديك صلاحيات حذف   \n\n➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  :  `.الغاء منع `\nالاستخدام :  اكتب الامر مع الكلمة الذي تم منعها  \nالشرح  :  يقوم بالسماح للكلمة وعدم حذفها في الدردشه \n\n ➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  :  `.القائمة السوداء`\nالاستخدام  :  فقط اكتب الامر \nالشرح  :  يقوم بأظهار الكلمات الذب تم منعها من الدردشة  \n\n➖➖➖➖➖➖➖➖➖➖➖ \n\nقنـاة السـورس   : [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)")
        
@borg.on(admin_cmd("م20"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("اوامر الجانبية\n\nالامر ¦ `.تكرار `\nالاستخدام  ¦  بكتابة الامر مع الرقمىومع الكلمة \nالشرح ¦  ليقوم بتكرار النص\nمثال ¦ .تكرار 10 جمثون\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦   `.سبام`\nالاستخدام ¦ بكتابة الكلمة مع الامر \nالشرح  ¦   يقوم بتفصيخ الكلمه حرف حرف \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦   `.تنصيب`\nالاستخدام  ¦   بكتابة الامر بالرد على الملف \nالشرح  ¦   لتنصيب ملف خارجي للبوت  \n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦   `.الغاء التنصيب`\nالاستخدام  ¦   بكتابة الامر مع اسم الملف \nالشرح ¦  يقوم بحذف الملف من البوت لمدة 24 ساعة فقط\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر ¦  `.تنظيف`\n\nالاستخدام  ¦  اكتب الامر بالرد على الرسالة\nالشرح  ¦  يقوم بحذف الرسائل اكتب الامر على رسالة معينة وسيقوم بحذف الرسائل التي تحتها بروفايلك\n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\nالامر  ¦   `.مسح`  \nالاستخدام  ¦  فقط اكتب الامر بالرد \nالشرح  ¦  يقوك بحذف الرسالة \n\n➖➖➖➖➖➖➖➖➖➖➖➖\n\nقنـاة السـورس ¦  [𝗝ََِ𝗠ٓ𝗧َُِْٓ𝗛ُ𝗢َ𝗡ٍَ](t.me/JMTHON)")
        
        
