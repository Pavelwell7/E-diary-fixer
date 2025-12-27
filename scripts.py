import random

from datacenter.models import Schoolkid, Commendation, Mark, Chastisement, Lesson


def fix_marks(schoolkid):

    try:
        kid = Schoolkid.objects.get(full_name__contains=schoolkid)
        bad_marks = Mark.objects.filter(schoolkid=kid, points__in=[2, 3])
        updated_count = bad_marks.update(points=5)
        return updated_count
    except Schoolkid.DoesNotExist:
        print(f"Ученик '{schoolkid}' не найден!!!")
        return None
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid}'. Напишите полностью ФИО!!!")
        return None


def remove_chastisements(schoolkid):

    try:
        kid = Schoolkid.objects.get(full_name__contains=schoolkid)
        chastisements = Chastisement.objects.filter(schoolkid=kid)
        return chastisements.delete()
    except Schoolkid.DoesNotExist:
        print(f"Ученик '{schoolkid}' не найден!!!")
        return None
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid}'. Напишите полностью ФИО!!!")
        return None


def create_commendation(schoolkid):

    try:
        commendation_list = ["Молодец!",
                             "Отлично",
                             "Хорошо",
                             "Гораздо лучше, чем я ожидал!",
                             "Ты меня приятно удивил!",
                             "Великолепно!",
                             "Прекрасно!Ты меня очень обрадовал!",
                             "Именно этого я давно ждал от тебя!",
                             "Сказано здорово – просто и ясно!",
                             ]
        kid = Schoolkid.objects.get(full_name__contains = schoolkid)
        lesson_math = Lesson.objects.filter(year_of_study=6, group_letter='А', subject__title="Музыка")
        last_math_lesson = lesson_math.order_by("-date").first()
        commendation = Commendation.objects.create(text=random.choice(commendation_list),
                                               created=last_math_lesson.date, schoolkid=kid,
                                               subject=last_math_lesson.subject, teacher=last_math_lesson.teacher)
        return commendation
    except Schoolkid.DoesNotExist:
        print(f"Ученик '{schoolkid}' не найден!!!")
        return None
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid}'. Напишите полностью ФИО!!!")
        return None


