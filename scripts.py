import random

from datacenter.models import Schoolkid, Commendation, Mark, Chastisement, Lesson

def get_schoolkid_name(schoolkid):

    try:
        return Schoolkid.objects.get(full_name__contains=schoolkid)
    except Schoolkid.DoesNotExist:
        print(f"Ученик '{schoolkid}' не найден!!!")
        return None
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем '{schoolkid}'. Напишите полностью ФИО!!!")
        return None


def fix_marks(schoolkid):

    kid = get_schoolkid_name(schoolkid)
    if not kid:
        return None
    bad_marks = Mark.objects.filter(schoolkid=kid, points__in=[2, 3])
    updated_count = bad_marks.update(points=5)
    return updated_count


def remove_chastisements(schoolkid):

    kid = get_schoolkid_name(schoolkid)
    if not kid:
        return None
    chastisements = Chastisement.objects.filter(schoolkid=kid)
    return chastisements.delete()


def create_commendation(schoolkid, year_of_study, group_letter, subject):
    commendation_list = [
        "Молодец!",
        "Отлично",
        "Хорошо",
        "Гораздо лучше, чем я ожидал!",
        "Ты меня приятно удивил!",
        "Великолепно!",
        "Прекрасно!Ты меня очень обрадовал!",
        "Именно этого я давно ждал от тебя!",
        "Сказано здорово – просто и ясно!",
    ]
    kid = get_schoolkid_name(schoolkid)
    if not kid:
        return None
    lessons = Lesson.objects.filter(year_of_study=year_of_study, group_letter=group_letter, subject__title=subject)
    last_lesson = lessons.order_by("-date").first()
    if not last_lesson:
        print(f"Урок '{subject}' для {year_of_study}{group_letter} не найден!")
        return None
    commendation = Commendation.objects.create(
                                                text=random.choice(commendation_list),
                                                created=last_lesson.date, schoolkid=kid,
                                                subject=last_lesson.subject, teacher=last_lesson.teacher
                                                )
    return commendation


